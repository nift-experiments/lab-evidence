import json,sys,tempfile,subprocess
from pathlib import Path
sys.path.insert(0,'/opt/campaign/shell-benchmark/scripts')
from workload_campaign import prepare,verify
from campaign_measure import isolated_env
from suite import invocation
R=Path('/opt/campaign/evidence/shell-ab-diagnostic/profiles');R.mkdir(exist_ok=True)
d=json.loads((R.parent/'raw.json').read_text());assert d['complete'] and d['all_correct'];j=d['jobs'][0];rows=[]
for key,v in d['versions'].items():
 for tool in ('strace','perf'):
  with tempfile.TemporaryDirectory(prefix='shell-call-profile-') as td:
   root=Path(td);fixture=prepare(root,j['definition']);env=isolated_env(root/'home');cmd=invocation(v['executable'],'nift','bare',code=j['source']);dest=R/f'{key}.{tool}'
   command=['strace','-f','-c','-o',str(dest)+'.txt',*cmd] if tool=='strace' else ['perf','record','-e','cpu-clock','-F','999','--call-graph','dwarf','-o',str(dest)+'.data','--',*cmd]
   p=subprocess.run(command,cwd=root,env=env,capture_output=True,timeout=180);Path(str(dest)+'.stdout').write_bytes(p.stdout);Path(str(dest)+'.stderr').write_bytes(p.stderr);r={'version':key,'tool':tool,'exit_code':p.returncode,'correct':False,'command':command}
   if p.returncode==0:r['validation']=verify(root,j['definition'],fixture,p.stdout);r['correct']=True
   if tool=='perf' and p.returncode==0:
    with Path(str(dest)+'.report').open('w') as f:subprocess.run(['perf','report','--stdio','--no-children','-i',str(dest)+'.data'],stdout=f,stderr=subprocess.STDOUT,check=True)
   rows.append(r);print(key,tool,p.returncode,r['correct'],flush=True)
(R/'receipt.json').write_text(json.dumps({'kind':'post-timing function-call diagnostic profiles, not benchmark samples','rows':rows},indent=2)+'\n')
