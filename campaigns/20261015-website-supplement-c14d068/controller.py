import json,sys,subprocess,os,hashlib,time,statistics
from pathlib import Path
host=sys.argv[1];R=Path('/opt/supplement/evidence');R.mkdir(exist_ok=True)
def run(*a):return subprocess.check_output(a,text=True,stderr=subprocess.STDOUT).strip()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def telemetry():
 data={}
 for label,cmd in {'date':['date','-u','+%FT%TZ'],'uname':['uname','-a'],'cpu':['lscpu'],'mount':['findmnt','-J'],'disk':['lsblk','-J','-o','NAME,TYPE,SIZE,ROTA,MODEL'],'filesystem':['df','-T'],'frequency':['bash','-c','cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_* 2>/dev/null || true'],'virtualization':['systemd-detect-virt'],'hugo_build':['/opt/supplement/tools/hugo','version'],'hugo_help':['/opt/supplement/tools/hugo','help'],'hugo_env':['/opt/supplement/tools/hugo','env'],'packages':['dpkg-query','-W']}.items():
  try:data[label]=run(*cmd)
  except subprocess.CalledProcessError as e:data[label]={'unavailable':e.output}
 for f in ('stat','meminfo','loadavg','diskstats','pressure/cpu','pressure/io'):data[f]=Path('/proc/'+f).read_text()
 return data
assert sha('/opt/nift/nift')=='7dd42dcee5ca4a6965f0823c0ae59198282da1eb77e0fcd4cae93a537870a6fb';assert sha('/opt/supplement/tools/hugo')=='8f6ddd98ff4a21a27b86530eb2e40d305673c26f72b1d57734ef68505cd28f89'
assert run('git','-C','/opt/nift','rev-parse','HEAD')=='c14d06835bca515a5281e41da0e40219c2d60ef0'
for name,rev in [('current','a2890bc504cf7c55b77cd4fddae17403b7caf8ae'),('historical','4947b42c863782ba6be0fdbbd2003d60d6d0d3d4')]:assert run('git','-C','/opt/supplement/'+name,'rev-parse','HEAD')==rev
suitehashes={name:{f:sha(Path('/opt/supplement')/name/'scripts'/f) for f in ('benchmark.py','campaign.py','campaign_measure.py','measure.c')} for name in ('current','historical')};assert suitehashes['current']==suitehashes['historical']
phases=[]
def job(phase,engine,workers,mode,harness='current',observer='none',affinity=[0,1,2,3]):return dict(phase=phase,engine=engine,workers=workers,mode=mode,harness=harness,observer=observer,affinity=affinity,job_id='-'.join(map(str,[phase,engine,workers,mode,harness,observer])))
if host=='a':
 phases.append(('scaling',[job('scaling',e,w,m) for e in ('Nift','Hugo') for w in (1,2,4,'default') for m in ('fresh','warm-full')]))
 phases.append(('replay',[job('replay',e,1,m,harness=h,affinity=[0]) for h in ('historical','current') for e in ('Nift','Hugo') for m in ('fresh','warm-full')]))
 phases.append(('observer-controls',[job('observer-controls',e,w,m,observer=o) for e in ('Nift','Hugo') for w in (1,4) for m in ('fresh','warm-full') for o in ('none','GNU-time-only','proc50ms+GNU-time')]))
else:phases.append(('replication',[job('replication',e,w,'fresh') for e in ('Nift','Hugo') for w in (1,2,4,'default')]))
record={'host':host,'suite_hashes':suitehashes,'worker_default_source':'Nift ProjectInfo.cpp hardware_concurrency multiplier; fixture default -1. Hugo unset GOMAXPROCS, actual Go defaults not equated to sampled thread count.','metadata':telemetry(),'jobs':[j for _,jobs in phases for j in jobs],'observations':[],'phase_telemetry':{},'complete':False,'all_correct':False}
(R/'provenance.json').write_text(json.dumps({k:v for k,v in record.items() if k!='observations'},indent=2)+'\n')
def save():(R/'raw.json').write_text(json.dumps(record,indent=2)+'\n')
for phase,jobs in phases:
 record['phase_telemetry'][phase]={'before':telemetry()}
 for turn in range(6):
  ordered=jobs[turn%len(jobs):]+jobs[:turn%len(jobs)]
  for j in ordered:
   spec=dict(j,round=turn,warmup=turn==0,id=j['job_id']+'-r'+str(turn));cmd=['taskset','-c',','.join(map(str,j['affinity'])),'python3','/opt/run-one.py',json.dumps(spec)]
   p=subprocess.run(cmd,capture_output=True,text=True,timeout=600);log=R/(spec['id']+'.log');log.write_text(p.stdout+'\nSTDERR\n'+p.stderr)
   if p.returncode==0:
    row=json.loads(p.stdout.strip().splitlines()[-1]);record['observations'].append(row);save();print(phase,turn,j['engine'],j['workers'],j['mode'],j['observer'],row['correct'],row.get('wall_ms'),flush=True)
    if not row['correct']:raise RuntimeError('correctness rejected; raw preserved')
   else:
    record['failure']={'spec':spec,'exit_code':p.returncode,'log':str(log)};save();raise RuntimeError('worker failed; raw retained')
 record['phase_telemetry'][phase]['after']=telemetry();save()
record['complete']=len(record['observations'])==len(record['jobs'])*6;record['all_correct']=all(x['correct'] for x in record['observations']);save();rows=[]
for j in record['jobs']:
 obs=[o for o in record['observations'] if o['spec']['job_id']==j['job_id'] and not o['spec']['warmup']];vals=[o['wall_ms'] for o in obs];rows.append({**j,'samples':len(obs),'median_ms':statistics.median(vals),'min_ms':min(vals),'max_ms':max(vals),'median_cpu_ms':statistics.median(o['cpu_ms'] for o in obs),'median_peak_rss_kib':statistics.median(o['peak_rss_kib'] for o in obs)})
(R/'summary.json').write_text(json.dumps({'rows':rows},indent=2)+'\n')
if record['complete'] and record['all_correct']:(R/'TIMING_PASS').write_text('SUPPLEMENT_TIMING_PASS\n')
print('SUPPLEMENT_TIMING_COMPLETE',len(record['observations']),flush=True)
