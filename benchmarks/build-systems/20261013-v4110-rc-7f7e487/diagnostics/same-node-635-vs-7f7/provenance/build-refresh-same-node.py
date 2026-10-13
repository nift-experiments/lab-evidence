#!/usr/bin/env python3
"""Targeted same-node old/candidate diagnostics, separate from accepted peers."""
import os,sys,json,subprocess,shutil,hashlib,statistics
from pathlib import Path
ROOT=Path('/opt/suite');sys.path.insert(0,str(ROOT/'scripts'));sys.path.insert(0,str(ROOT/'generators'))
from campaign import verify,preconditions,store
from certify import mutate,dependency_audit
from native import generate
from tiny import generate as generate_tiny
out=Path('/opt/results/build-systems-same-node-635-vs-7f7');assert not out.exists();out.mkdir(parents=True)
os.sched_setaffinity(0,{0,1,2,3})
plan=[{'kind':'native','size':1000,'profile':'heavy','jobs':1,'cases':[{'name':'noop','samples':30,'warmups':2}]},{'kind':'tiny','size':10000,'profile':'light','jobs':4,'cases':[{'name':'noop','samples':20,'warmups':2},{'name':'full','samples':5,'warmups':1}]}]
binaries={'old':'/opt/nift-build-prior/nift','candidate':'/opt/nift/nift'}
identity=json.loads(Path('/root/build-same-node-artifact-identity.json').read_text());identity.update(plan=plan,suite_sha='e95bfe88ac9e1eaf67cfeb8f67020fc3373ab81e',affinity=[0,1,2,3],boundary='unchanged C CLOCK_MONOTONIC fork/exec through wait4; reset and correctness outside clock',purpose='screen33.39%tiny10kfull wall/93.34%memory increase and53.47%native1kheavyj1noop improvement',measure_sha256=hashlib.sha256((ROOT/'work/tools/measure').read_bytes()).hexdigest())
(out/'identity.json').write_text(json.dumps(identity,indent=2)+'\n');(out/'plan.json').write_text(json.dumps(plan,indent=2)+'\n')
rows=[];compare={};index=0
for gi,g in enumerate(plan):
 work=ROOT/'work'/f'diagnostic-ab-{g["kind"]}-{g["size"]}';assert not work.exists();work.mkdir()
 canonical=work/'canonical';(generate_tiny(canonical,g['size'],g['jobs']) if g['kind']=='tiny' else generate(canonical,g['size'],g['profile'],g['jobs']))
 manifest=json.loads((canonical/'manifest.json').read_text());manifest['input_sha256']={str(p.relative_to(canonical)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (canonical/'inputs').rglob('*') if p.is_file()};store(out,'manifests',manifest)
 baseline={}
 for label,binary in binaries.items():
  base=work/(label+'-baseline');shutil.copytree(canonical,base);env=dict(os.environ,BUILD_TRACE=str(base/'initial.trace'),LC_ALL='C',TZ='UTC')
  p=subprocess.run([binary,'build'],cwd=base,env=env,capture_output=True,text=True,timeout=3600);(out/f'bootstrap-{gi}-{label}.stdout').write_text(p.stdout);(out/f'bootstrap-{gi}-{label}.stderr').write_text(p.stderr);assert p.returncode==0,p.stderr
  assert sorted((base/'initial.trace').read_text().splitlines())==sorted(a['id'] for a in manifest['actions']);hashes=verify(base,manifest,None,0);dependency_audit(base,'nift',manifest)
  if baseline:assert hashes==verify(next(iter(baseline.values())),manifest,None,0)
  baseline[label]=base
 for ci,c in enumerate(g['cases']):
  for ri in range(c['samples']+c['warmups']):
   order=['old','candidate'];offset=(gi+ci+ri)%2;order=order[offset:]+order[:offset]
   for label in order:
    fixture=work/'current';shutil.rmtree(fixture,ignore_errors=True);shutil.copytree(baseline[label],fixture);expected,delta,target=mutate(fixture,manifest,c['name']);assert target is None
    prepared=preconditions(fixture,manifest,c['name'],manifest['input_sha256']);trace=fixture/'measured.trace';env=dict(os.environ,BUILD_TRACE=str(trace),LC_ALL='C',TZ='UTC');metric=fixture/'resource.json';cmd=[binaries[label],'build']
    with (out/f'{index:06}.stdout').open('w') as stdout,(out/f'{index:06}.stderr').open('w') as stderr:p=subprocess.run([str(ROOT/'work/tools/measure'),str(metric),*cmd],cwd=fixture,env=env,stdout=stdout,stderr=stderr,timeout=3600)
    metrics=json.loads(metric.read_text());actions=trace.read_text().splitlines() if trace.exists() else [];assert p.returncode==0 and metrics['exit_code']==0;assert len(actions)==len(set(actions)) and sorted(actions)==sorted(expected)
    hashes=verify(fixture,manifest,None,delta);key=(g['kind'],g['size'],g['profile'],g['jobs'],c['name'])
    if key in compare:assert hashes==compare[key]
    else:compare[key]=hashes
    refs={}
    for name,category,data in [('action_trace','action-traces',actions),('expected_actions','action-oracles',sorted(expected)),('output_hashes','output-hashes',hashes)]:refs[name],refs[name+'_sha256']=store(out,category,data)
    row={'index':index,'graph_index':gi,'case_index':ci,**{k:g[k] for k in ['kind','size','profile','jobs']},'scenario':c['name'],'variant':label,'round':ri,'warmup':ri<c['warmups'],'order':order,'command':cmd,'preconditions':prepared,'metrics':metrics,'passed':True,**refs};rows.append(row)
    with (out/'observations.jsonl').open('a') as f:f.write(json.dumps(row,separators=(',',':'))+'\n')
    print(json.dumps({'index':index,'kind':g['kind'],'size':g['size'],'scenario':c['name'],'variant':label,'round':ri,'wall_ms':metrics['wall_ms']}),flush=True);index+=1;shutil.rmtree(fixture)
 shutil.rmtree(work)
summary=[]
for key in sorted({tuple(r[k] for k in ['kind','size','profile','jobs','scenario','variant']) for r in rows}):
 obs=[r for r in rows if tuple(r[k] for k in ['kind','size','profile','jobs','scenario','variant'])==key and not r['warmup']];cell=dict(zip(['kind','size','profile','jobs','scenario','variant'],key));cell['samples']=len(obs)
 for metric in ['wall_ms','cpu_ms','peak_rss_kib']:
  values=sorted(r['metrics'][metric] for r in obs);stats={'median':statistics.median(values),'min':min(values),'max':max(values)}
  if len(values)>=20:
   pos=(len(values)-1)*.95;lo=int(pos);hi=min(lo+1,len(values)-1);stats['p95']=values[lo]+(values[hi]-values[lo])*(pos-lo)
  cell[metric]=stats
 summary.append(cell)
(out/'summary.json').write_text(json.dumps({'cohorts':summary,'observations':len(rows),'measured':sum(not r['warmup'] for r in rows),'warmups':sum(r['warmup'] for r in rows),'outliers_removed':0},indent=2)+'\n');(out/'complete.json').write_text(json.dumps({'all_correct':True,'observations':len(rows),'official_current_peer_data_modified':False},indent=2)+'\n');print('BUILD TARGETED SAME-NODE COMPLETE',flush=True)
