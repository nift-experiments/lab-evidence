import os,subprocess,json,hashlib
from pathlib import Path
base=Path('/tmp/graph-recert-c14d068'); receipts=base/'receipts';receipts.mkdir(exist_ok=True)
env=dict(os.environ,NIFT='/tmp/nift-recert-c14d068/nift',NIFT_SOURCE_SHA='c14d06835bca515a5281e41da0e40219c2d60ef0',NINJA='/tmp/refresh-ninja-1.13.2/ninja')
subprocess.run(['cc','-O2','scripts/measure.c','-o','work/measure'],cwd=base/'task-runners',check=True)
subprocess.run(['cc','-O2','scripts/tiny-body.c','-o','work/tiny-body'],cwd=base/'task-runners',check=True)
commands=[]
for kind,profile,jobs in [('native',p,j) for p in ['light','heavy'] for j in [1,2,4]]+[('tiny','light',j) for j in [1,2,4]]:
 name=f'build-{kind}-{profile}-j{jobs}'
 args=['python3','scripts/certify.py','--kind',kind,'--size','100','--profile',profile,'--jobs',str(jobs),'--results',str(receipts/name)]
 if kind=='tiny':args+=['--scenarios','noop','leaf','batch10','batch10pct','full']
 commands.append(('build-systems',name,args,{}))
commands += [('task-runners','task-semantic',['python3','scripts/probe.py'],{'TASK_RUNNER_PROBE_OUTPUT':str(receipts/'task-semantic.json')}),('task-runners','task-smoke',['python3','scripts/campaign-refresh.py','--smoke','--output',str(receipts/'task-smoke')],{})]
for suite,name,args,extra in commands:
 print(name,flush=True)
 with (receipts/(name+'.log')).open('w') as out:
  subprocess.run(args,cwd=base/suite,env=dict(env,**extra),stdout=out,stderr=subprocess.STDOUT,check=True)
(receipts/'commands.json').write_text(json.dumps(commands,indent=2)+'\n')
