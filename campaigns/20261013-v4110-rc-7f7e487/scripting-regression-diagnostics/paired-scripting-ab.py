import json,hashlib,subprocess,tempfile,time,sys
from pathlib import Path
S=Path('/opt/campaign/scripting-benchmark');sys.path.insert(0,str(S/'scripts'))
from campaign_measure import measure,isolated_env,metadata,identity,summary
from campaign import equivalent
R=Path('/opt/campaign/evidence/scripting-ab-diagnostic');R.mkdir(exist_ok=True)
versions={'old':{'sha':'2eaec7d70e9ce2e698d0ba23a605fb9cf85317ff','root':Path('/opt/nift-ab-old')},'new':{'sha':'7f7e487c47a87e871dfef53345e2b71288008bff','root':Path('/opt/nift')}}
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def cmd(*args):return subprocess.check_output(args,text=True).strip()
assert cmd('git','-C',str(S),'rev-parse','HEAD')=='f889fff4af94658259932f611d4b0ad681c1eebf';assert not cmd('git','-C',str(S),'status','--porcelain')
for key,v in versions.items():
 assert cmd('git','-C',str(v['root']),'rev-parse','HEAD')==v['sha'];assert not cmd('git','-C',str(v['root']),'status','--porcelain');v['executable']=str(v['root']/'nift');v['identity']=identity(v['executable'],['--version']);v['root']=str(v['root'])
assert versions['new']['identity']['sha256']=='671e182ea31f3a23af92dadd738aba43edcb427670e7cf2f0d06b6362d28a606'
assert versions['old']['identity']['sha256']=='e7cb28d6150c797acbb52a618faff3cf981281b9ea4e91a8c478062242f0c3a2'
accepted=json.loads(Path('/opt/campaign/evidence/official-refresh/scripting.json').read_text());jobs=[j for j in accepted['jobs'] if j['id'].endswith('/nift')];assert len(jobs)==30
sources={}
case_positions={j['id']:i for i,j in enumerate(jobs)}
for j in jobs:
 cat,bench,size,lang=j['id'].split('/');source=S/'benchmarks/sources'/cat/bench/(size+'.f');gold=S/'benchmarks/golden'/f'{cat}__{bench}__{size}.txt';assert digest(source)==j['source_sha256'] and digest(gold)==j['oracle_sha256'];sources[j['id']]={'source':source,'gold':gold}
record={'kind':'separate-same-node-paired-version-diagnostic-not-official-campaign','accepted_raw_sha256':digest('/opt/campaign/evidence/official-refresh/scripting.json'),'candidate_sha':versions['new']['sha'],'prior_sha':versions['old']['sha'],'suite_sha':cmd('git','-C',str(S),'rev-parse','HEAD'),'machine':metadata(S),'versions':versions,'compiler':cmd('g++','--version').splitlines()[0],'compiler_sha256':digest('/usr/bin/g++'),'build_command':'make -C ROOT -j2 nift, Native Make defaults, C++17/C99 -O2 no arch flags','sample_plan':{'measured_per_case_version':10,'warmups_per_case_version':2,'cases':30,'planned_measured':600,'planned_warmups':120,'affinity':[0],'timeout_seconds':180},'ordering':'Rotate case order by round; each case runs old/new adjacent. Reverse first version by round+original case index parity (balanced5/5 first during measured rounds). Frozen supervisor/clock/env/oracle code imported without modifying suite.','harness_files':{n:digest(S/'scripts'/n) for n in ('campaign_measure.py','campaign.py','measure.c')},'start_utc':cmd('date','-u','+%FT%TZ'),'complete':False,'all_correct':False,'observations':[],'launch_order':[],'round_machine_states':[]}
assert record['machine']['cpu_affinity']==[0] and not record['machine']['dirty']
libraries={}
for key,v in versions.items():
 text=cmd('ldd',v['executable']);paths=[Path(t) for t in text.split() if t.startswith('/') and Path(t).is_file()]
 libraries[key]={'runtime':{str(p.resolve()):digest(p) for p in paths},'build_archives':{str(p.relative_to(Path(v['root']))):digest(p) for p in Path(v['root']).rglob('libffi.a')}}
record['library_sha256']=libraries
(R/'provenance.json').write_text(json.dumps({k:v for k,v in record.items() if k not in ('observations','launch_order','round_machine_states')},indent=2)+'\n')
subprocess.run(['dpkg-query','-W'],stdout=(R/'dpkg-versions.tsv').open('w'),check=True)
(R/'libraries.txt').write_text(cmd('ldd',versions['old']['executable'])+'\nNEW\n'+cmd('ldd',versions['new']['executable'])+'\n')
def save(): (R/'raw.json').write_text(json.dumps(record,indent=2)+'\n')
with tempfile.TemporaryDirectory(prefix='scripting-ab-home-') as td:
 env=isolated_env(td)
 for turn in range(12):
  order=jobs[turn%len(jobs):]+jobs[:turn%len(jobs)]
  record['round_machine_states'].append({'round':turn,'proc_stat':Path('/proc/stat').read_text(),'loadavg':Path('/proc/loadavg').read_text(),'meminfo':Path('/proc/meminfo').read_text()})
  for pos,j in enumerate(order):
   keys=('old','new') if (turn+case_positions[j['id']])%2==0 else ('new','old')
   for key in keys:
    source=sources[j['id']]['source'];gold=sources[j['id']]['gold'];command=[versions[key]['executable'],str(source)];record['launch_order'].append({'round':turn,'case':j['id'],'version':key,'sequence':len(record['launch_order'])})
    row,out,err=measure(command,S,env,180);row.update(case=j['id'],version=key,command=command,round=turn,warmup=turn<2,correct=row['exit_code']==0 and not row['timeout'] and equivalent(out,gold.read_bytes()),source_sha256=j['source_sha256'],oracle_sha256=j['oracle_sha256'],stdout_text=out.decode(errors='replace'),stderr_text=err.decode(errors='replace'))
    record['observations'].append(row);save()
    if not row['correct']:print('REJECTED',key,j['id'],row['exit_code'],flush=True)
  print('PAIRED_ROUND',turn+1,'/12 observations',len(record['observations']),flush=True)
record['complete']=len(record['observations'])==720;record['all_correct']=all(x['correct'] for x in record['observations']);record['end_utc']=cmd('date','-u','+%FT%TZ');save()
for v in versions.values():assert not cmd('git','-C',v['root'],'status','--porcelain');assert digest(v['executable'])==v['identity']['sha256']
assert not cmd('git','-C',str(S),'status','--porcelain');assert digest('/opt/campaign/evidence/official-refresh/scripting.json')==record['accepted_raw_sha256']
summaryrows=[]
for j in jobs:
 by={key:[x for x in record['observations'] if x['case']==j['id'] and x['version']==key and not x['warmup']] for key in versions};correct=all(len(x)==10 and all(r['correct'] for r in x) for x in by.values());entry={'case':j['id'],'both_correct':correct}
 if correct:
  for key,rows in by.items():entry[key]=summary(rows)
  entry['new_over_old']=entry['new']['median_ms']/entry['old']['median_ms'];entry['percent_change']=100*(entry['new_over_old']-1)
 summaryrows.append(entry)
(R/'summary.json').write_text(json.dumps({'kind':record['kind'],'complete':record['complete'],'all_correct':record['all_correct'],'rows':summaryrows},indent=2)+'\n')
if record['complete'] and record['all_correct']:(R/'PASS').write_text('PAIRED_AB_PASS\n')
print('PAIRED_AB_COMPLETE',record['complete'],record['all_correct'],flush=True)
