#!/usr/bin/env python3
"""One paired strace/perf capture after all diagnostic timings, not accepted samples."""
import sys,os,subprocess,json,hashlib,shutil
from pathlib import Path
ROOT=Path('/opt/suite');sys.path.insert(0,str(ROOT/'scripts'));sys.path.insert(0,str(ROOT/'generators'))
from tiny import generate
from certify import mutate
from campaign import verify
assert json.loads(Path('/opt/results/build-systems-same-node-635-vs-7f7/complete.json').read_text())['all_correct']
os.sched_setaffinity(0,{0,1,2,3});out=Path('/opt/results/build-systems-profile-635-vs-7f7');assert not out.exists();out.mkdir();records=[];parity=None
for label,binary in [('old','/opt/nift-build-prior/nift'),('candidate','/opt/nift/nift')]:
 work=ROOT/'work'/('profile-tiny10000-'+label);assert not work.exists();generate(work,10000,4);m=json.loads((work/'manifest.json').read_text());env=dict(os.environ,BUILD_TRACE=str(work/'initial.trace'),LC_ALL='C',TZ='UTC')
 p=subprocess.run([binary,'build'],cwd=work,env=env,capture_output=True,text=True,timeout=1800);assert p.returncode==0;baseline=verify(work,m,None,0)
 if parity is None:parity=baseline
 else:assert parity==baseline
 for profiler in ['strace','perf']:
  expected,delta,target=mutate(work,m,'full');trace=work/(profiler+'.trace');env['BUILD_TRACE']=str(trace)
  argv=['strace','-f','-c','-o',str(out/(label+'.strace')),binary,'build'] if profiler=='strace' else ['perf','record','-e','cpu-clock','-F','99','--call-graph','dwarf','-o',str(out/(label+'.perf.data')),'--',binary,'build']
  with (out/(label+'-'+profiler+'.stdout')).open('w') as stdout,(out/(label+'-'+profiler+'.stderr')).open('w') as stderr:p=subprocess.run(argv,cwd=work,env=env,stdout=stdout,stderr=stderr,timeout=1800)
  actions=trace.read_text().splitlines() if trace.exists() else [];passed=p.returncode==0 and len(actions)==len(set(actions)) and sorted(actions)==sorted(expected)
  if passed:assert verify(work,m,None,0)==parity
  records.append({'variant':label,'profiler':profiler,'command':argv,'exit_code':p.returncode,'correctness_pass':passed,'executed_actions':len(actions),'timing_scope':'instrumented diagnostic only; excluded from accepted timing distributions','binary_sha256':hashlib.sha256(Path(binary).read_bytes()).hexdigest()})
  if profiler=='perf' and passed:
   with (out/(label+'.perf-self.txt')).open('w') as f:subprocess.run(['perf','report','--stdio','--no-children','-i',str(out/(label+'.perf.data'))],stdout=f,stderr=subprocess.STDOUT,check=True)
  (out/'profile-receipts.json').write_text(json.dumps(records,indent=2)+'\n');print(label,profiler,p.returncode,passed,flush=True)
 shutil.rmtree(work)
(out/'complete.json').write_text(json.dumps({'complete':True,'records':len(records),'instrumented_correctness':all(x['correctness_pass'] for x in records),'unavailable_profiles_preserved':True,'official_raw_changed':False},indent=2)+'\n')
