from pathlib import Path
import json,subprocess,os,tempfile,hashlib,statistics,time,sys
r=Path('/opt/template-engines');sys.path.insert(0,str(r/'scripts'));from certify import expected
out=r/'work/diagnostic-threeway';out.mkdir(exist_ok=False);cases=[c for c in json.loads((r/'corpus/manifest.json').read_text()) if c['name'] in ['loop-10000','article']];bins={v:str(r/'work'/('threeway-'+v+'-adapter')) for v in ['prior','checkpoint','candidate']};sources={'prior':'c8d9c266518d115e4f289c5c6a2b94ddd7ee9968','checkpoint':'7f7e487c47a87e871dfef53345e2b71288008bff','candidate':'c14d06835bca515a5281e41da0e40219c2d60ef0'};cpu=min(os.sched_getaffinity(0));env=dict(os.environ);env.pop('BENCH_GATE',None);raw=[]
meta={'scope':'Separate targeted same-node diagnostic, official data unchanged','suite_sha':'3c0dcdd1aad3cbb0a0c638c9041233b1e329dc6f','prior_sha':sources['prior'],'candidate_sha':sources['candidate'],'binaries':{v:{'source_sha':sources[v],'sha256':hashlib.sha256(Path(p).read_bytes()).hexdigest()} for v,p in bins.items()},'library_sha256':{v:hashlib.sha256(Path('/opt/recert-threeway/'+v+'/libnift_c.a').read_bytes()).hexdigest() for v in bins},'compiler':subprocess.check_output(['g++','--version'],text=True).strip(),'build_flags':'normal Makefile embed; adapter -std=c++17 -O2 -pthread, no instrumentation','cpu':cpu,'cases':[c['name'] for c in cases],'boundaries':['fresh full invocation','source-render per operation'],'measured_pairs':3,'order':'three-version rotation by pair, three measured pairs each','persistent_warmups_per_worker':2,'fresh_warmups_per_version_case':1,'timeout_seconds':120};(out/'launch.json').write_text(json.dumps(meta,indent=2)+'\n')
for c in cases:
 for mode in ['fresh','render']:
  for phase,rounds in ([('warmup',1),('measured',3)] if mode=='fresh' else [('measured',3)]):
   for pair in range(rounds):
    versions=list(bins);shift=pair%3;order=versions[shift:]+versions[:shift]
    for version in order:
     cmd=['taskset','-c',str(cpu),bins[version],str(r/'corpus'/c['name']),mode,'1','1',str(c['renders']),str(c['distinct'])];start=time.perf_counter_ns();p=subprocess.run(cmd,env=env,capture_output=True,timeout=120);elapsed=(time.perf_counter_ns()-start)/1e6;assert p.returncode==0,(c['name'],mode,version,p.stderr)
     if mode=='fresh':
      assert p.stdout==expected(c);rows=[{'wall_ms':elapsed,'phase':phase,'output_sha256':hashlib.sha256(p.stdout).hexdigest()}]
     else:
      rows=[json.loads(x) for x in p.stdout.splitlines()];assert [x['sample'] for x in rows]==[-2,-1,0]
      for x in rows:x.update(wall_ms=x['ns']/x['operations']/1e6,phase='warmup' if x['sample']<0 else 'measured',outputs_exactly_checked=True)
     for row in rows:
      row.update(case=c['name'],boundary='fresh' if mode=='fresh' else 'source-render',version=version,pair=pair,order=order,correct=True);raw.append(row)
      with (out/'observations.jsonl').open('a') as f:f.write(json.dumps(row,separators=(',',':'))+'\n')
     print(c['name'],mode,pair,version,rows[-1]['wall_ms'],flush=True)
summary=[]
for c in cases:
 for boundary in ['fresh','source-render']:
  values={v:[x['wall_ms'] for x in raw if x['case']==c['name'] and x['boundary']==boundary and x['version']==v and x['phase']=='measured'] for v in bins};assert all(len(a)==3 for a in values.values());med={v:statistics.median(a) for v,a in values.items()};summary.append({'case':c['name'],'boundary':boundary,'median_ms':med,'candidate_change_percent':(med['prior']-med['candidate'])/med['prior']*100,'samples_per_version':3,'values_ms':values})
(out/'summary.json').write_text(json.dumps({'pass':all(x['correct'] for x in raw),'rows':summary,'scope':'small descriptive paired control; no statistical-significance claim'},indent=2)+'\n');print('PAIRED TEMPLATE DIAGNOSTIC COMPLETE',flush=True)
