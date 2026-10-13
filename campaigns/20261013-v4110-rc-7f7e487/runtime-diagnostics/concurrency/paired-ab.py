from pathlib import Path
import os,sys,json,subprocess,hashlib,statistics,time
base=Path('/opt/concurrency');sys.path.insert(0,str(base/'scripts'));import run
out=base/'work/diagnostic-ab';out.mkdir(exist_ok=False);suite=out/'suite';(suite/'work').mkdir(parents=True);(suite/'adapters').symlink_to(base/'adapters');(suite/'work/fixtures').symlink_to(base/'work/fixtures');run.R=suite;os.chdir(suite)
binaries={'prior':'/opt/concurrency-prior-nift/nift','candidate':'/opt/nift/nift'};sources={'prior':'445f4d3545cf031bcce4bf77a2b4a61ffb3b4c4f','candidate':'7f7e487c47a87e871dfef53345e2b71288008bff'};cases=[c for c in json.loads((base/'docs/SCENARIOS.json').read_text()) if c['name'] in ['queue-100000-4-4','schedule-1000']];selected=['candidate'];run.command=lambda e:[binaries[selected[0]],'adapters/nift.f'];raw=[]
identity={k:{'source_sha':sources[k],'binary_sha256':hashlib.sha256(Path(v).read_bytes()).hexdigest()} for k,v in binaries.items()};meta={'scope':'Separate targeted same-node diagnostic, not official series','suite_sha':subprocess.check_output(['git','rev-parse','HEAD'],cwd=base,text=True).strip(),'identity':identity,'cases':cases,'boundary':'persistent readiness-clock, new runtime per request; scalar/problem work and output serialization remain included','warmups_per_version_case':1,'measured_pairs':3,'order':'prior/candidate then candidate/prior alternation','timeout_seconds':120,'compiler':subprocess.check_output(['g++','--version'],text=True).strip(),'build_flags':'normal Makefile -std=c++17 -O2 -pthread, no instrumentation'};(out/'launch.json').write_text(json.dumps(meta,indent=2)+'\n')
for c in cases:
 for phase,rounds in [('warmup',1),('measured',3)]:
  for rnd in range(rounds):
   order=['prior','candidate'] if rnd%2==0 else ['candidate','prior']
   for version in order:
    selected[0]=version;p,reader,err=run.persistent('nift')
    try:row=run.trial('nift',c,(p,reader),timeout=120)
    finally:
     if p.poll() is None:p.stdin.close();p.wait(timeout=10)
     err.close()
    row.update(case=c['name'],version=version,phase=phase,pair=rnd,order=order);raw.append(row)
    with (out/'observations.jsonl').open('a') as f:f.write(json.dumps(row,separators=(',',':'))+'\n')
    print(c['name'],phase,rnd,version,row['wall_ms'],flush=True)
summary=[]
for c in cases:
 values={v:[r['wall_ms'] for r in raw if r['case']==c['name'] and r['version']==v and r['phase']=='measured'] for v in binaries};med={v:statistics.median(a) for v,a in values.items()};summary.append({'case':c['name'],'median_ms':med,'candidate_change_percent':(med['prior']-med['candidate'])/med['prior']*100,'samples_per_version':3,'values_ms':values})
(out/'summary.json').write_text(json.dumps({'pass':all(r['correct'] for r in raw),'rows':summary,'scope':'small descriptive same-node paired control; no statistical significance claim'},indent=2)+'\n');print('PAIRED CONCURRENCY DIAGNOSTIC COMPLETE',flush=True)
