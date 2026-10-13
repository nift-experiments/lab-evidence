import sys,json,subprocess,hashlib,tempfile,os,signal,re
from pathlib import Path
S=Path('/opt/campaign/scripting-benchmark');sys.path.insert(0,str(S/'scripts'))
from campaign_measure import isolated_env
from campaign import equivalent
BASE=Path('/opt/campaign/evidence/scripting-ab-diagnostic');assert (BASE/'PASS').exists();raw=json.loads((BASE/'raw.json').read_text());rawsha=hashlib.sha256((BASE/'raw.json').read_bytes()).hexdigest()
R=BASE/'instrumentation';R.mkdir(exist_ok=True);rows=[]
def run(command,env,limit=600):
 p=subprocess.Popen(command,cwd=S,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True)
 try:out,err=p.communicate(timeout=limit);return p.returncode,out,err,False
 except subprocess.TimeoutExpired:
  os.killpg(p.pid,signal.SIGKILL);out,err=p.communicate();return p.returncode,out,err,True
versions={k:v['executable'] for k,v in raw['versions'].items()}
cases=['sanity/function-calls/large','sanity/function-calls/small','graphs-trees-search/bfs/large','arrays-strings-hash/frequency-count/large']
with tempfile.TemporaryDirectory(prefix='scripting-ab-instrument-home-') as td:
 env=isolated_env(td)
 for family in cases:
  cat,bench,size=family.split('/');source=S/'benchmarks/sources'/cat/bench/(size+'.f');gold=S/'benchmarks/golden'/f'{cat}__{bench}__{size}.txt';expected=gold.read_bytes();stem=cat+'-'+bench+'-'+size
  for version,exe in versions.items():
   prefix=R/(version+'-'+stem);command=[exe,str(source)]
   # Direct target invocation in every instrument; no additional target shell/wrapper.
   commands={'heaptrack':['heaptrack','--record-only','-o',str(prefix)+'.heaptrack',*command], 'strace':['strace','-f','-c','-o',str(prefix)+'.strace.txt',*command], 'perf':['perf','record','-e','cpu-clock','-F','99','--call-graph','dwarf','-o',str(prefix)+'.perf.data','--',*command]}
   for tool,cmd in commands.items():
    code,out,err,timeout=run(cmd,env);Path(str(prefix)+'.'+tool+'.stdout').write_bytes(out);Path(str(prefix)+'.'+tool+'.stderr').write_bytes(err)
    # heaptrack's launcher adds informational text to stdout; preserve it in full,
    # and verify the exact expected adjacent target-output block occurs once.
    target_lines=expected.strip().splitlines();out_lines=[x.strip() for x in out.splitlines()];target_blocks=sum(out_lines[i:i+len(target_lines)]==target_lines for i in range(len(out_lines)))
    correct=code==0 and not timeout and (equivalent(out,expected) if tool!='heaptrack' else target_blocks==1)
    row={'family':family,'version':version,'tool':tool,'command':cmd,'exit_code':code,'timeout':timeout,'correct':correct,'stdout_scope':'launcher+target; expected target block occurs once' if tool=='heaptrack' else 'target only','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'oracle_sha256':hashlib.sha256(expected).hexdigest()}
    if tool=='heaptrack' and code==0:
     traces=[p for p in R.glob(prefix.name+'.heaptrack*') if p.is_file() and p.suffix in ('.gz','.zst')]
     row['trace_files']=[p.name for p in traces]
     if len(traces)==1:
      pc,po,pe,pt=run(['heaptrack_print','-f',str(traces[0])],env,600);Path(str(prefix)+'.heaptrack-report.txt').write_bytes(po+pe);row.update(report_exit=pc,report_timeout=pt)
      text=(po+pe).decode(errors='replace');m=re.search(r'([\d,]+)\s+allocations?\b',text)
      row['allocation_summary_lines']=[line.strip() for line in text.splitlines() if any(x in line.lower() for x in ('allocation calls:','calls to allocation functions:','temporary allocations:','peak heap memory consumption:','total memory leaked:'))]
    if tool=='perf' and code==0:
     pc,po,pe,pt=run(['perf','report','--stdio','-i',str(prefix)+'.perf.data','--sort','dso,symbol','--percent-limit','1','--no-children'],env,120);Path(str(prefix)+'.perf-self.txt').write_bytes(po+pe);row.update(report_exit=pc,report_timeout=pt)
    rows.append(row);(R/'instrumentation.json').write_text(json.dumps({'kind':'postpaired-instrumentation-not-timing-observations','versions':raw['versions'],'raw_timing_sha256':rawsha,'policy':'same tools/commands and full source sizes for old/new; only executable changes; direct target process; no kernel changes','records':rows},indent=2)+'\n');print(version,family,tool,'correct',correct,'exit',code,flush=True)
assert hashlib.sha256((BASE/'raw.json').read_bytes()).hexdigest()==rawsha
(R/'COMPLETE').write_text('POSTPAIR_INSTRUMENTATION_COMPLETE\n');print('POSTPAIR_INSTRUMENTATION_COMPLETE',flush=True)
