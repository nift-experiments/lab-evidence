import sys,subprocess,json,tempfile,hashlib
from pathlib import Path
sys.path.insert(0,'/opt/supplement/current/scripts')
from campaign import legacy,validate
from campaign_measure import isolated_env
R=Path('/opt/supplement/evidence-v3');assert (R/'TIMING_PASS').exists();P=R/'profiles';P.mkdir(exist_ok=True);rows=[]
for engine in ('Nift','Hugo'):
 for mode in ('fresh','warm-full'):
  for tool in ('strace','perf'):
   with tempfile.TemporaryDirectory(prefix='website-supp-profile-') as td:
    base=Path(td);exe='/opt/nift/nift' if engine=='Nift' else '/opt/supplement/tools/hugo';cwd,cmd,outputs=legacy.nift_fixture(base,10000,exe) if engine=='Nift' else legacy.hugo_fixture(base,10000,exe);env=isolated_env(base/'home');env.update(CI='1');env.pop('GOMAXPROCS',None)
    if engine=='Nift':
     p=cwd/'.nift/config.json';d=json.loads(p.read_text());d['config']['build-threads']=-1;p.write_text(json.dumps(d));cmd=[exe,'build','--all']
    else:
     p=cwd/'hugo.toml';p.write_text(p.read_text().replace('["taxonomy"','["home", "taxonomy"')+'\n[markup.goldmark.renderer]\nunsafe = true\n')
    if mode=='warm-full':b=subprocess.run(cmd,cwd=cwd,env=env,capture_output=True,timeout=180);assert b.returncode==0;validate(engine,cwd,10000);legacy.clean_outputs(cwd,outputs)
    dest=P/f'{engine}-{mode}-{tool}';wrapped=['strace','-f','-c','-o',str(dest)+'.txt',*cmd] if tool=='strace' else ['perf','record','-e','cpu-clock','-F','99','--call-graph','dwarf','-o',str(dest)+'.data','--',*cmd]
    p=subprocess.run(wrapped,cwd=cwd,env=env,capture_output=True,timeout=180);Path(str(dest)+'.stdout').write_bytes(p.stdout);Path(str(dest)+'.stderr').write_bytes(p.stderr);r={'engine':engine,'mode':mode,'tool':tool,'command':wrapped,'exit_code':p.returncode,'correct':False,'affinity':[0,1,2,3],'binary_sha256':hashlib.sha256(Path(exe).read_bytes()).hexdigest()}
    if p.returncode==0:r['validation']=validate(engine,cwd,10000);r['correct']=True
    else:r['unavailable_or_failed']=p.stderr.decode(errors='replace')[-2000:]
    if tool=='perf' and p.returncode==0:
     with Path(str(dest)+'.report').open('w') as f:subprocess.run(['perf','report','--stdio','--no-children','-i',str(dest)+'.data'],stdout=f,stderr=subprocess.STDOUT,check=True)
    rows.append(r);(P/'receipt.json').write_text(json.dumps({'kind':'post-timing bounded software CPU/syscall profiles, not timings','rows':rows},indent=2)+'\n');print(engine,mode,tool,r['correct'],flush=True)
(P/'COMPLETE').write_text('PROFILE_ATTEMPTS_COMPLETE\n')
