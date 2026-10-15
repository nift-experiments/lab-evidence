import json,sys,tempfile,subprocess,hashlib,os,time,threading
from pathlib import Path
spec=json.loads(sys.argv[1]);suite=Path('/opt/supplement')/spec['harness'];sys.path.insert(0,str(suite/'scripts'))
from campaign import legacy,validate
from campaign_measure import measure,isolated_env
R=Path('/opt/supplement/evidence');art=R/'artifacts'/spec['id'];art.mkdir(parents=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def snapshot(root):
 rows=[]
 for p in sorted(root.rglob('*')):
  if p.is_file():rows.append({'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':sha(p)})
 return {'files':len(rows),'bytes':sum(x['bytes'] for x in rows),'tree_sha256':hashlib.sha256(json.dumps(rows,sort_keys=True).encode()).hexdigest(),'entries':rows}
def proctree(pid):
 found=[];todo=[pid]
 while todo:
  x=todo.pop()
  try:
   stat=Path(f'/proc/{x}/status').read_text();d={s.split(':',1)[0]:s.split(':',1)[1].strip() for s in stat.splitlines() if ':' in s};found.append({'pid':x,'name':d['Name'],'threads':int(d['Threads']),'rss_kib':int(d.get('VmRSS','0 kB').split()[0])});todo.extend(map(int,Path(f'/proc/{x}/task/{x}/children').read_text().split()))
  except (FileNotFoundError,ProcessLookupError,PermissionError):pass
 return found
def telemetry():
 return {name:Path('/proc/'+name).read_text() for name in ('stat','meminfo','loadavg','diskstats','pressure/cpu','pressure/io','pressure/memory') if Path('/proc/'+name).exists()}
before=telemetry()
with tempfile.TemporaryDirectory(prefix='website-supp-') as td:
 base=Path('/opt/supplement/work')/spec['job_id'] if spec['mode']=='warm-full' else Path(td);base.mkdir(parents=True,exist_ok=True);exe='/opt/nift/nift' if spec['engine']=='Nift' else '/opt/supplement/tools/hugo';existing=(base/('nift' if spec['engine']=='Nift' else 'hugo')).exists()
 if existing:
  cwd=base/('nift' if spec['engine']=='Nift' else 'hugo');command=[exe,'build','--all'] if spec['engine']=='Nift' else [exe,'--quiet','--destination','public'];outputs=['public'] if spec['engine']=='Nift' else ['public','resources']
 else:cwd,command,outputs=legacy.nift_fixture(base,10000,exe) if spec['engine']=='Nift' else legacy.hugo_fixture(base,10000,exe)
 env=isolated_env(base/'home');env['CI']='1'
 if spec['engine']=='Nift':
  config=cwd/'.nift/config.json';d=json.loads(config.read_text());d['config']['build-threads']=-1 if spec['workers']=='default' else spec['workers'];
  if not existing:config.write_text(json.dumps(d))
  command=[exe,'build','--all']
 else:
  conf=cwd/'hugo.toml';s=conf.read_text();s=s.replace('["taxonomy"','["home", "taxonomy"')+'\n[markup.goldmark.renderer]\nunsafe = true\n';
  if not existing:conf.write_text(s)
 if spec['engine']=='Hugo' and spec['workers']!='default':env['GOMAXPROCS']=str(spec['workers'])
 else:env.pop('GOMAXPROCS',None)
 legacy.clean_outputs(cwd,outputs)
 inputs=snapshot(cwd);(art/'input-manifest.json').write_text(json.dumps(inputs)+'\n')
 result={'spec':spec,'warm_policy':'persistent fixture; remove only outputs before each observation, first round warmup initially unbuilt, retain internal state thereafter','command':command,'env_controls':{k:env.get(k) for k in ('GOMAXPROCS','CI')},'binary_sha256':sha(exe),'suite_sha':subprocess.check_output(['git','rev-parse','HEAD'],cwd=suite,text=True).strip(),'harness_sha256':{n:sha(suite/'scripts'/n) for n in ('campaign.py','benchmark.py','campaign_measure.py','measure.c')},'input':{k:v for k,v in inputs.items() if k!='entries'},'correct':False}
 if spec['observer']=='none':rec,out,err=measure(command,cwd,env,180)
 else:
  ticks=[];tfile=art/'gnu-time.txt';wrapped=['/usr/bin/time','-v','-o',str(tfile),*command];start=time.perf_counter()
  with (art/'stdout.txt').open('wb') as of,(art/'stderr.txt').open('wb') as ef:
   p=subprocess.Popen(wrapped,cwd=cwd,env=env,stdout=of,stderr=ef,start_new_session=True)
   if spec['observer']=='proc50ms+GNU-time':
    while p.poll() is None:ticks.append({'elapsed':time.perf_counter()-start,'processes':proctree(p.pid)});time.sleep(.05)
   try:code=p.wait(timeout=180)
   except subprocess.TimeoutExpired:os.killpg(p.pid,9);code=p.wait()
  elapsed=(time.perf_counter()-start)*1000;out=(art/'stdout.txt').read_bytes();err=(art/'stderr.txt').read_bytes();txt=tfile.read_text();fields={line.strip().split(': ',1)[0]:line.strip().split(': ',1)[1] for line in txt.splitlines() if ': ' in line};user=float(fields['User time (seconds)']);system=float(fields['System time (seconds)']);rec={'wall_ms':elapsed,'cpu_ms':1000*(user+system),'user_ms':1000*user,'system_ms':1000*system,'peak_rss_kib':int(fields['Maximum resident set size (kbytes)']),'exit_code':code,'timeout':code==137,'cpu_wall_ratio':(user+system)/(elapsed/1000)};(art/'proc-samples.json').write_text(json.dumps(ticks)+'\n');rec['proc_sample_count']=len(ticks);rec['max_sampled_threads']=max((sum(p['threads'] for p in x['processes']) for x in ticks),default=None);rec['observer_wall_includes_final_sampling_delay']=spec['observer']=='proc50ms+GNU-time'
 result.update(rec);(art/'stdout.txt').write_bytes(out);(art/'stderr.txt').write_bytes(err)
 if result['exit_code']==0 and not result.get('timeout',False):
  result['validation']=validate(spec['engine'],cwd,10000);result['correct']=True
  outdir=cwd/'public';om=snapshot(outdir);(art/'output-manifest.json').write_text(json.dumps(om)+'\n');result['output']={k:v for k,v in om.items() if k!='entries'}
  for name in ('index.html','page-1.html','page-9999.html'):(art/name).write_bytes((outdir/name).read_bytes())
 result['telemetry_before']=before;result['telemetry_after']=telemetry();(art/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
