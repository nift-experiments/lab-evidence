import sys,json,subprocess,tempfile,hashlib
from pathlib import Path
sys.path.insert(0,'/opt/campaign/website-generator-benchmark/scripts')
from campaign import legacy,validate
from campaign_measure import isolated_env
R=Path('/opt/campaign/evidence/website-ab-diagnostic/profiles');R.mkdir(exist_ok=True)
rows=[]
for key,exe in [('old','/opt/website-ab-old/nift'),('new','/opt/nift/nift')]:
 for tool in ('strace','perf'):
  with tempfile.TemporaryDirectory(prefix='website-profile-') as td:
   base=Path(td);cwd,_,outputs=legacy.nift_fixture(base/'fixture',10000,exe);p=cwd/'.nift/config.json';d=json.loads(p.read_text());d['config']['build-threads']=1;p.write_text(json.dumps(d));env=isolated_env(base/'home')
   dest=R/f'{key}.{tool}'
   command=['strace','-f','-c','-o',str(dest)+'.txt',exe,'build','--all'] if tool=='strace' else ['perf','record','-e','cpu-clock','-F','99','--call-graph','dwarf','-o',str(dest)+'.data','--',exe,'build','--all']
   p=subprocess.run(command,cwd=cwd,env=env,capture_output=True,timeout=180);Path(str(dest)+'.stdout').write_bytes(p.stdout);Path(str(dest)+'.stderr').write_bytes(p.stderr)
   row={'version':key,'tool':tool,'command':command,'exit_code':p.returncode,'correct':False,'binary_sha256':hashlib.sha256(Path(exe).read_bytes()).hexdigest()}
   if p.returncode==0:row['validation']=validate('Nift',cwd,10000);row['correct']=True
   if tool=='perf' and p.returncode==0:
    with Path(str(dest)+'.report').open('w') as f:subprocess.run(['perf','report','--stdio','--no-children','-i',str(dest)+'.data'],stdout=f,stderr=subprocess.STDOUT,check=True)
   rows.append(row);print(key,tool,p.returncode,row['correct'],flush=True)
(R/'receipt.json').write_text(json.dumps({'kind':'post-timing profiles, never benchmark samples','rows':rows},indent=2)+'\n')
