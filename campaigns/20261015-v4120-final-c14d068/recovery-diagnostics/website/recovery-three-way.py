#!/usr/bin/env python3
"""Post-official diagnostics only; frozen suite helpers and correctness oracles."""
import argparse,json,sys,tempfile,subprocess,hashlib,itertools,statistics
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('suite',choices=['scripting','shell','website']);ap.add_argument('--output',required=True);a=ap.parse_args()
role={'scripting':'scripting-benchmark','shell':'shell-benchmark','website':'website-generator-benchmark'}[a.suite];S=Path('/opt/campaign')/role;sys.path.insert(0,str(S/'scripts'))
from campaign_measure import measure,isolated_env,identity,metadata,summary
V={'release':('/opt/recovery-release','c8d9c266518d115e4f289c5c6a2b94ddd7ee9968'),'original':('/opt/recovery-original','7f7e487c47a87e871dfef53345e2b71288008bff'),'final':('/opt/nift','c14d06835bca515a5281e41da0e40219c2d60ef0')}
def cmd(*xs):return subprocess.check_output(xs,text=True).strip()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
versions={}
for k,(root,rev) in V.items():
 assert cmd('git','-C',root,'rev-parse','HEAD')==rev and not cmd('git','-C',root,'status','--porcelain');exe=root+'/nift';versions[k]={'source_sha':rev,'executable':exe,'identity':identity(exe,['--version']),'runtime_library_sha256':{str(Path(t).resolve()):sha(Path(t).resolve()) for t in cmd('ldd',exe).split() if t.startswith('/') and Path(t).is_file()}}
assert not cmd('git','-C',str(S),'status','--porcelain')
if a.suite=='scripting':
 from campaign import equivalent
 cases=['sanity/function-calls/small','sanity/function-calls/large'];samples,warmups=10,2
elif a.suite=='shell':
 from workload_campaign import prepare,verify
 from suite import invocation
 official=json.loads(Path('/opt/campaign/evidence/official-refresh/shell-workloads.json').read_text());jobs={j['case']:j for j in official['jobs'] if j['shell']=='nift'};cases=['function-calls','string-transform'];samples,warmups=10,2
else:
 from campaign import legacy,validate
 cases=['10000/application-cold'];samples,warmups=5,1
assert Path('/opt/campaign/evidence/official-refresh/PASS').is_file(), 'Official run must finish before diagnostic timing'
P=Path(a.output);P.mkdir(parents=True,exist_ok=False);perms=list(itertools.permutations(versions));official_hash={p.name:sha(p) for p in Path('/opt/campaign/evidence/official-refresh').glob('*.json')}
r={'kind':'three-way same-node recovery diagnostic; separate from official','suite':a.suite,'versions':versions,'suite_sha':cmd('git','-C',str(S),'rev-parse','HEAD'),'machine':metadata(S),'compiler':cmd('g++','--version').splitlines()[0],'flags':'Native Make defaults -std=c++17 -O2 -Wall -Wextra -pedantic -pthread; no architecture flags','cases':cases,'samples':samples,'warmups':warmups,'ordering':'Adjacent three-version blocks, six permutations cycled, rotated case order; unequal permutation counts documented when measured rounds not divisible by six','harness_sha256':{p.name:sha(p) for p in (S/'scripts').glob('*.py')},'official_raw_sha256':official_hash,'observations':[],'complete':False,'all_correct':False}
assert r['machine']['cpu_affinity']==[0]
def save():(P/'raw.json').write_text(json.dumps(r,indent=2)+'\n')
for turn in range(samples+warmups):
 for index in [(turn+i)%len(cases) for i in range(len(cases))]:
  c=cases[index];permutation=perms[((turn-warmups if turn>=warmups else turn)+index)%6]
  for k in permutation:
   exe=versions[k]['executable']
   with tempfile.TemporaryDirectory(prefix='recovery-three-way-') as td:
    root=Path(td);env=isolated_env(root/'home');validation=None
    if a.suite=='scripting':
     family,size=c.rsplit('/',1);cat,bench=family.split('/');src=S/'benchmarks/sources'/cat/bench/(size+'.f');gold=S/'benchmarks/golden'/f'{cat}__{bench}__{size}.txt';cwd=S;command=[exe,str(src)]
    elif a.suite=='shell':
     j=jobs[c];fixture=prepare(root,j['definition']);cwd=root;command=invocation(exe,'nift','bare',code=j['source'])
    else:
     cwd,_,outputs=legacy.nift_fixture(root/'fixture',10000,exe);config=cwd/'.nift/config.json';d=json.loads(config.read_text());d['config']['build-threads']=1;config.write_text(json.dumps(d));command=[exe,'build','--all'];env.update(GOMAXPROCS='1',CI='1')
    row,out,err=measure(command,cwd,env,180);row.update(round=turn,case=c,version=k,warmup=turn<warmups,correct=False,command=command,stdout_text=out.decode(errors='replace'),stderr_text=err.decode(errors='replace'))
    try:
     assert row['exit_code']==0 and not row['timeout']
     if a.suite=='scripting':assert equivalent(out,gold.read_bytes());row.update(source_sha256=sha(src),oracle_sha256=sha(gold))
     elif a.suite=='shell':row['validation']=verify(root,j['definition'],fixture,out);row['source_sha256']=j['source_sha256']
     else:row['validation']=validate('Nift',cwd,10000)
     row['correct']=True
    except Exception as e:row['rejection']=str(e)
    r['observations'].append(row);save();print(turn,c,k,row['correct'],row['wall_ms'],flush=True)
r['complete']=len(r['observations'])==len(cases)*3*(samples+warmups);r['all_correct']=all(x['correct'] for x in r['observations']);save();rows=[]
for c in cases:
 row={'case':c}
 for k in versions:row[k]=summary([o for o in r['observations'] if o['case']==c and o['version']==k and not o['warmup']])
 row['final_vs_release_percent']=100*(row['final']['median_ms']/row['release']['median_ms']-1);row['final_vs_original_percent']=100*(row['final']['median_ms']/row['original']['median_ms']-1);rows.append(row)
(P/'summary.json').write_text(json.dumps({'rows':rows},indent=2)+'\n')
for k,v in versions.items():assert sha(v['executable'])==v['identity']['sha256']
for name,h in official_hash.items():assert sha(Path('/opt/campaign/evidence/official-refresh')/name)==h
if r['complete'] and r['all_correct']:(P/'PASS').write_text('RECOVERY_THREE_WAY_PASS\n')
