"""Instrument unchanged accepted lifecycle harnesses in disposable pinned exports."""
from pathlib import Path
import os,subprocess,runpy,json,time,re,hashlib,psutil,platform,shutil
ROOT=Path(__file__).resolve().parents[4]
BASE=ROOT/'nift-experiments';WORK=BASE/'ai-sdk-baseline/incremental-memory-work';EVIDENCE=Path(__file__).resolve().parent
NODE=BASE/'ai-sdk-baseline/toolchain/node-v24.21.0-linux-x64/bin/node';NIFT=BASE/'ai-sdk-baseline/toolchain/nift-v4.8.0/nift'
PINS={'ai-sdk':'7bb3b9f1713aed61291e73136ab100c2a6f5457c','ai-sdk-agent':'dd568e4ec671dd6ddde38f06f7e24836840f3cb4'}
original_run=subprocess.run
if not WORK.exists():
 WORK.mkdir(parents=True)
 for project,pin in PINS.items():
  target=WORK/project;target.mkdir()
  archive=original_run(['git','archive',pin],cwd=BASE/project,capture_output=True,check=True).stdout
  original_run(['tar','-x','-C',str(target)],input=archive,check=True)
  (target/'node_modules').symlink_to(BASE/project/'node_modules',target_is_directory=True)
  for folder in ['generated','public','runtime','.nift/public']:
   src=BASE/project/folder;dst=target/folder
   if dst.exists():shutil.rmtree(dst)
   if src.exists():shutil.copytree(src,dst)
 env={'platform':platform.platform(),'python':platform.python_version(),'logical_cpus':os.cpu_count(),'affinity':len(os.sched_getaffinity(0)),'ram_bytes':psutil.virtual_memory().total,'cpu':next(x.split(':',1)[1].strip() for x in Path('/proc/cpuinfo').read_text().splitlines() if x.startswith('model name')),'active_desktop':True,'source_revisions':PINS,'upstream_revision':'3ebefff610f96892c50be48cf1838c453e2349f7','nift_version':'4.8.0','nift_sha256':hashlib.sha256(NIFT.read_bytes()).hexdigest(),'node_version':original_run([str(NODE),'--version'],capture_output=True,text=True,check=True).stdout.strip(),'sample_policy':'Single observation per changed-input case, matching accepted lifecycle protocol; supplementary timings do not replace accepted timings.','cache_state':'Disposable export receives unmeasured forced warm prime to replace relocated cache products, then unmeasured normal baseline per original harness; force equality after every case; sources and outputs restored. Dependencies reused outside timing; OS cache uncontrolled.','worker_cap':4,'metric':'GNU maximum individual process/phase RSS, KiB / 1024 = MiB; sampled 50ms descendant resident-page sum bytes / 1048576 = MiB, not PSS, shared pages double-counted and short peaks may be missed.'}
 assert env['nift_sha256']=='a77deda5ef4124886a6ad344cd0fe0a43a5fa02d793cdf7e7eef2ed19645d8c4'
 (EVIDENCE/'environment.json').write_text(json.dumps(env,indent=2)+'\n')
os.environ.update({'PATH':str(NIFT.parent)+':'+str(NODE.parent)+':'+os.environ['PATH'],'AI_SDK_NODE':str(NODE),'NODE_ENV':'production','PYTHONDONTWRITEBYTECODE':'1'})
for k in ['AI_GATEWAY_API_KEY','MXBAI_API_KEY','MXBAI_STORE_ID','GEISTDOCS_CHAT_PROXY_URL','GEISTDOCS_CHAT_PROXY_TOKEN','GEISTDOCS_CHAT_SECRET']:os.environ.pop(k,None)
records=[]
def measured(command,**kw):
 if not (isinstance(command,list) and len(command)>1 and command[1]=='scripts/build-content.py'):return original_run(command,**kw)
 project=Path(kw['cwd']).name;case=Path(kw['stdout'].name).stem.removeprefix(project+'-');suite=os.environ['AI_SDK_MEMORY_SUITE'];folder=EVIDENCE/project/suite/case;folder.mkdir(parents=True,exist_ok=True)
 env=kw.get('env',{}).copy();env['AI_SDK_PHASE_MEASUREMENTS']=str(folder/'phases');kw['env']=env;kw.pop('check',None)
 start=time.perf_counter();p=subprocess.Popen(['/usr/bin/time','-v','-o',str(folder/'whole.time'),*command],**kw);peak=0;samples=0
 while p.poll() is None:
  try:members=psutil.Process(p.pid).children(recursive=True)
  except psutil.Error:members=[]
  total=0
  for member in members:
   try:total+=member.memory_info().rss
   except psutil.Error:pass
  peak=max(peak,total);samples+=1;time.sleep(.05)
 rss=int(re.search(r'Maximum resident set size \(kbytes\): (\d+)',(folder/'whole.time').read_text()).group(1));row={'project':project,'suite':suite,'case':case,'command':command,'source_revision':PINS[project],'supplemental_elapsed_s':time.perf_counter()-start,'maximum_process_phase_rss_kib':rss,'sampled_peak_sum_rss_bytes':peak,'memory_samples':samples,'exit_code':p.returncode}
 records.append(row);(EVIDENCE/'samples.json').write_text(json.dumps(records,indent=2)+'\n');print(json.dumps({'memory_observation':row}),flush=True)
 if p.returncode:raise subprocess.CalledProcessError(p.returncode,command)
 return subprocess.CompletedProcess(command,p.returncode)
subprocess.run=measured
for project in PINS:
 root=WORK/project
 with (EVIDENCE/(project+'-warm-prime.log')).open('w') as log:
  original_run(['python3','scripts/build-content.py','--force'],cwd=root,env=os.environ.copy(),stdout=log,stderr=subprocess.STDOUT,check=True)
 for suite in (['body','routes'] if project=='ai-sdk' else ['body','routes','coordinated']):
  root=WORK/project;out=EVIDENCE/project/suite;out.mkdir(parents=True,exist_ok=True);os.environ['AI_SDK_VERIFICATION_OUTPUT']=str(out);os.environ['AI_SDK_MEMORY_SUITE']=suite
  script=root/f'scripts/verify-lifecycle-{suite}.py';(out/'harness-sha256.txt').write_text(hashlib.sha256(script.read_bytes()).hexdigest()+'\n')
  runpy.run_path(str(script),run_name='__main__')
print('All original lifecycle and restoration gates passed.',flush=True)
