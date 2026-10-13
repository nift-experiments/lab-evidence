import json,hashlib,subprocess,tempfile,sys,shutil
from pathlib import Path
S=Path('/opt/campaign/website-generator-benchmark');sys.path.insert(0,str(S/'scripts'))
from campaign_measure import measure,isolated_env,metadata,identity,summary
from campaign import validate,snapshot,legacy
R=Path('/opt/campaign/evidence/website-ab-diagnostic');R.mkdir(exist_ok=True)
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def call(*x):return subprocess.check_output(x,text=True).strip()
versions={'old':{'source_sha':'495012966756c9d2910a714c453359c8ff60bab1','root':'/opt/website-ab-old','historical_binary_sha256':'a1654dbf879bf0517141612fbcdb55f441e5e60009a5954faaa274bfa6868bf2'},'new':{'source_sha':'7f7e487c47a87e871dfef53345e2b71288008bff','root':'/opt/nift'}}
for key,v in versions.items():
 assert call('git','-C',v['root'],'rev-parse','HEAD')==v['source_sha'];assert not call('git','-C',v['root'],'status','--porcelain');v['executable']=v['root']+'/nift';v['identity']=identity(v['executable'],['--version'])
assert versions['new']['identity']['sha256']=='671e182ea31f3a23af92dadd738aba43edcb427670e7cf2f0d06b6362d28a606'
for v in versions.values():
 text=call('ldd',v['executable']);paths=[Path(t) for t in text.split() if t.startswith('/') and Path(t).is_file()];v['runtime_library_sha256']={str(p.resolve()):digest(p) for p in paths}
versions['old']['historical_binary_reproduced']=versions['old']['identity']['sha256']==versions['old']['historical_binary_sha256']
assert versions['old']['identity']['version']=='Nift v4.7.2'
assert call('git','-C',str(S),'rev-parse','HEAD')=='a2890bc504cf7c55b77cd4fddae17403b7caf8ae' and not call('git','-C',str(S),'status','--porcelain')
cases=['application-cold','warm-full','incremental/no-op','incremental/one-page'];sourcepos={c:i for i,c in enumerate(cases)}
record={'kind':'targeted same-node version diagnostic, not official campaign','pages':10000,'cases':cases,'versions':versions,'suite_sha':call('git','-C',str(S),'rev-parse','HEAD'),'machine':metadata(S),'compiler':call('g++','--version').splitlines()[0],'flags':'Native Make default C++17/C99 -O2 no arch flags','sample_plan':{'samples':5,'warmups':1,'planned_observations':48,'affinity':[0]},'ordering':'Adjacent version pairs, firstversion reversed by round+originalcaseindex; caseorderrotated perround. Five measuredrounds yield3/2 first-order split percase.','boundary':'Frozen C supervisor; unchanged10k fixture recipe,fullcontent/routes validation andincremental fullrebuild parity. Fresh fixture each observation; unmeasured baseline primeswarm/incremental cases. OS cache uncontrolled.','harness_sha256':{f:digest(S/'scripts'/f) for f in ('campaign_measure.py','campaign.py','benchmark.py','measure.c')},'official_raw_sha256':{f:digest(Path('/opt/campaign/evidence/official-refresh')/f) for f in ('website-100.json','website-1000.json','website-10000.json','targeted-builds.json')},'start_utc':call('date','-u','+%FT%TZ'),'complete':False,'all_correct':False,'observations':[],'launch_order':[]}
assert record['machine']['cpu_affinity']==[0] and not record['machine']['dirty']
(R/'provenance.json').write_text(json.dumps({k:v for k,v in record.items() if k not in ('observations','launch_order')},indent=2)+'\n');subprocess.run(['dpkg-query','-W'],stdout=(R/'dpkg-versions.tsv').open('w'),check=True)
def save(): (R/'raw.json').write_text(json.dumps(record,indent=2)+'\n')
def untimed(command,cwd,env):
 p=subprocess.run(command,cwd=cwd,env=env,capture_output=True,timeout=180);assert p.returncode==0,p.stderr.decode(errors='replace')[-1000:]
with tempfile.TemporaryDirectory(prefix='website-ab-') as td:
 base=Path(td);env=isolated_env(base/'home');env.update(GOMAXPROCS='1',CI='1')
 for turn in range(6):
  ordered=cases[turn%4:]+cases[:turn%4]
  for case in ordered:
   keys=('old','new') if (turn+sourcepos[case])%2==0 else ('new','old')
   for key in keys:
    exe=versions[key]['executable'];cwd,_,outputs=legacy.nift_fixture(base/f'{turn}-{sourcepos[case]}-{key}',10000,exe);p=cwd/'.nift/config.json';config=json.loads(p.read_text());config['config']['build-threads']=1;p.write_text(json.dumps(config));full=[exe,'build','--all'];command=full if case in ('application-cold','warm-full') else [exe,'build'];leaf=None
    if case!='application-cold':untimed(full,cwd,env);validate('Nift',cwd,10000)
    if case=='warm-full':legacy.clean_outputs(cwd,outputs)
    if case=='incremental/one-page':
     leaf=f'leaf-{turn}';p=cwd/'content/page-1.html';p.write_text(f'<h1>Page 1</h1><p>Equivalent benchmark content.</p><!--{leaf}-->');legacy.force_mtime_change(p,turn)
    before=snapshot(cwd) if case=='incremental/no-op' else None
    record['launch_order'].append({'sequence':len(record['launch_order']),'round':turn,'case':case,'version':key})
    row,out,err=measure(command,cwd,env,180);row.update(round=turn,case=case,version=key,warmup=turn<1,command=command,correct=False,stderr_text=err.decode(errors='replace')[-2000:])
    try:
     assert row['exit_code']==0 and not row['timeout'];row['validation']=validate('Nift',cwd,10000,leaf_marker=leaf)
     if case.startswith('incremental/'):
      after=snapshot(cwd)
      if before is not None:assert before==after
      untimed(full,cwd,env);assert snapshot(cwd)==after;row['full_rebuild_parity']=True
     row['correct']=True
    except Exception as e:row['rejection']=str(e)
    record['observations'].append(row);save();shutil.rmtree(cwd.parent);print(turn,key,case,row['correct'],round(row['wall_ms'] or 0,3),flush=True)
record['complete']=len(record['observations'])==48;record['all_correct']=all(x['correct'] for x in record['observations']);record['end_utc']=call('date','-u','+%FT%TZ');save();rows=[]
for c in cases:
 entry={'case':c};by={k:[x for x in record['observations'] if x['case']==c and x['version']==k and not x['warmup']] for k in versions}
 if all(len(x)==5 and all(r['correct'] for r in x) for x in by.values()):
  for key,obs in by.items():entry[key]=summary(obs)
  entry['new_over_old']=entry['new']['median_ms']/entry['old']['median_ms'];entry['percent_change']=100*(entry['new_over_old']-1);entry['delta_ms']=entry['new']['median_ms']-entry['old']['median_ms']
 rows.append(entry)
(R/'summary.json').write_text(json.dumps({'kind':record['kind'],'complete':record['complete'],'all_correct':record['all_correct'],'rows':rows},indent=2)+'\n')
for key,v in versions.items():assert digest(v['executable'])==v['identity']['sha256'] and not call('git','-C',v['root'],'status','--porcelain')
for f,sha in record['official_raw_sha256'].items():assert digest(Path('/opt/campaign/evidence/official-refresh')/f)==sha
assert not call('git','-C',str(S),'status','--porcelain')
if record['complete'] and record['all_correct']:(R/'PASS').write_text('TARGETED_WEBSITE_AB_PASS\n')
print('TARGETED_WEBSITE_AB_COMPLETE',record['complete'],record['all_correct'],flush=True)
