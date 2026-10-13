import sys,json,subprocess,hashlib,tempfile
from pathlib import Path
S=Path('/opt/campaign/scripting-benchmark');sys.path.insert(0,str(S/'scripts'))
from campaign_measure import isolated_env
from campaign import equivalent
R=Path('/opt/campaign/evidence/diagnostics');R.mkdir(exist_ok=True)
version=subprocess.run(['perf','--version'],capture_output=True,text=True);records=[]
with tempfile.TemporaryDirectory(prefix='scripting-diag-home-') as td:
 for family in ('sanity/function-calls','sanity/loops','structured-data/json-parse'):
  cat,bench=family.split('/');source=S/'benchmarks/sources'/cat/bench/'large.f';gold=S/'benchmarks/golden'/f'{cat}__{bench}__large.txt';stem=bench+'-large';cmd=['perf','record','-e','cpu-clock','-F','99','--call-graph','dwarf','-o',str(R/(stem+'.perf.data')),'--','/opt/nift/nift',str(source)]
  p=subprocess.run(cmd,cwd=S,env=isolated_env(td),capture_output=True,timeout=180);(R/(stem+'.stdout')).write_bytes(p.stdout);(R/(stem+'.stderr')).write_bytes(p.stderr)
  record={'family':family,'size':'large','command':cmd,'exit_code':p.returncode,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'expected_sha256':hashlib.sha256(gold.read_bytes()).hexdigest(),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'correct':p.returncode==0 and equivalent(p.stdout,gold.read_bytes()),'profile_supported':p.returncode==0}
  if p.returncode==0:
   for label,extra in [('self',['--no-children']),('cumulative',[])]:
    report=subprocess.run(['perf','report','--stdio','-i',str(R/(stem+'.perf.data')),'--sort','dso,symbol','--percent-limit','1',*extra],cwd=S,capture_output=True,timeout=120);(R/(stem+'-'+label+'.txt')).write_bytes(report.stdout+report.stderr);record[label+'_report_exit']=report.returncode
  records.append(record)
(R/'diagnostic-identity.json').write_text(json.dumps({'kind':'postofficial-one-invocation-softwareCPUprofiles-not-timing-samples','candidate_sha':'7f7e487c47a87e871dfef53345e2b71288008bff','perf_version':(version.stdout+version.stderr).decode() if isinstance(version.stdout,bytes) else version.stdout+version.stderr,'perf_event_paranoid':Path('/proc/sys/kernel/perf_event_paranoid').read_text().strip(),'settings_changed':False,'records':records},indent=2)+'\n')
print(json.dumps({'profiles':len(records),'supported':sum(x['profile_supported'] for x in records),'all_supported_outputs_correct':all(x['correct'] for x in records if x['profile_supported'])}))
