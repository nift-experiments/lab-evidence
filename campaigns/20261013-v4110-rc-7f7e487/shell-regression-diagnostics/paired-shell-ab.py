import sys,json,tempfile,subprocess,hashlib
from pathlib import Path
S=Path('/opt/campaign/shell-benchmark');sys.path.insert(0,str(S/'scripts'))
from workload_campaign import prepare,verify
from campaign_measure import measure,isolated_env,summary,identity,metadata
from suite import invocation
R=Path('/opt/campaign/evidence/shell-ab-diagnostic');R.mkdir(exist_ok=True)
keys=['function-calls','string-transform','traverse-100000']
primary=Path('/opt/campaign/evidence/official-refresh/shell-workloads.json');d=json.loads(primary.read_text());jobs=[next(j for j in d['jobs'] if j['id']==k+'/nift') for k in keys]
def call(*x):return subprocess.check_output(x,text=True).strip()
versions={'old':{'root':'/opt/shell-ab-old','sha':'2eaec7d70e9ce2e698d0ba23a605fb9cf85317ff','binary':'e7cb28d6150c797acbb52a618faff3cf981281b9ea4e91a8c478062242f0c3a2'},'new':{'root':'/opt/nift','sha':'7f7e487c47a87e871dfef53345e2b71288008bff','binary':'671e182ea31f3a23af92dadd738aba43edcb427670e7cf2f0d06b6362d28a606'}}
for v in versions.values():
 assert call('git','-C',v['root'],'rev-parse','HEAD')==v['sha'];assert not call('git','-C',v['root'],'status','--porcelain');v['executable']=v['root']+'/nift';v['identity']=identity(v['executable'],['--version']);assert v['identity']['sha256']==v['binary']
assert call('git','-C',str(S),'rev-parse','HEAD')=='aec1349fd0ba986108d9c851944e41e5ed330b6f';assert not call('git','-C',str(S),'status','--porcelain')
record={'kind':'targeted same-node diagnostic, separate from official','versions':versions,'suite_sha':call('git','-C',str(S),'rev-parse','HEAD'),'machine':metadata(S),'compiler':call('g++','--version').splitlines()[0],'flags':'Native Make defaults -O2 no architecture flags','sample_plan':{'measured_per_case_version':10,'warmups_per_case_version':2,'observations':72},'ordering':'Adjacent pairs; reversed first version by round + original case index; rotated case order','jobs':jobs,'official_raw_sha256':hashlib.sha256(primary.read_bytes()).hexdigest(),'observations':[],'complete':False,'all_correct':False}
assert record['machine']['cpu_affinity']==[0]
def save():(R/'raw.json').write_text(json.dumps(record,indent=2)+'\n')
for turn in range(12):
 for index in [(turn+i)%3 for i in range(3)]:
  j=jobs[index];case=j['case'];c=j['definition']
  for key in (('old','new') if (turn+index)%2==0 else ('new','old')):
   with tempfile.TemporaryDirectory(prefix='shell-ab-') as td:
    root=Path(td);fixture=prepare(root,c);env=isolated_env(root/'home');command=invocation(versions[key]['executable'],'nift','bare',code=j['source']);r,out,err=measure(command,root,env,180);r.update(round=turn,warmup=turn<2,case=case,version=key,correct=False)
    r['stdout_text']=out.decode(errors='replace');r['stderr_text']=err.decode(errors='replace')
    try:assert r['exit_code']==0 and not r['timeout'];r['validation']=verify(root,c,fixture,out);r['correct']=True
    except Exception as e:r['rejection']=str(e)
    record['observations'].append(r);save();print(turn,key,case,r['correct'],r['wall_ms'],flush=True)
record['complete']=len(record['observations'])==72;record['all_correct']=all(x['correct'] for x in record['observations']);save();rows=[]
for c in keys:
 row={'case':c}
 for k in versions:row[k]=summary([x for x in record['observations'] if x['case']==c and x['version']==k and not x['warmup']])
 row['delta_ms']=row['new']['median_ms']-row['old']['median_ms'];row['percent_change']=100*(row['new']['median_ms']/row['old']['median_ms']-1);rows.append(row)
(R/'summary.json').write_text(json.dumps({'rows':rows},indent=2)+'\n')
assert hashlib.sha256(primary.read_bytes()).hexdigest()==record['official_raw_sha256']
for v in versions.values():assert hashlib.sha256(Path(v['executable']).read_bytes()).hexdigest()==v['binary']
if record['complete'] and record['all_correct']:(R/'PASS').write_text('SHELL_AB_PASS\n')
print('COMPLETE',record['complete'],record['all_correct'],flush=True)
