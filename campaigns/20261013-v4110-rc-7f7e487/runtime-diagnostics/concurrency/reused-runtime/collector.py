from pathlib import Path
import os,sys,json,subprocess,hashlib,threading,signal,time
base=Path('/opt/concurrency');sys.path.insert(0,str(base/'scripts'));import run
commands={e:run.command(e) for e in run.ENGINES};commands['nift']=[commands['nift'][0],str(base/'adapters/nift.f')];commands['python'][1]=str(base/'adapters/python.py');commands['node'][1]=str(base/'adapters/js.mjs');commands['bun'][1]=str(base/'adapters/js.mjs');commands['prior-nift']=['/opt/concurrency-prior-nift/nift',str(base/'adapters/nift.f')]
out=base/'work/diagnostic-reuse';out.mkdir(exist_ok=False);suite=out/'suite';(suite/'work').mkdir(parents=True);(suite/'adapters').symlink_to(base/'adapters');(suite/'work/fixtures').symlink_to(base/'work/fixtures');run.R=suite;run.command=lambda e:commands[e];os.chdir(suite)
c=next(x for x in json.loads((base/'docs/SCENARIOS.json').read_text()) if x['name']=='schedule-1000');rows=[];failures=[];guard_mib=6144
meta={'scope':'Separate ten-request retained-runtime diagnostic; not pooled with official isolated timings','case':c,'candidate_sha':'7f7e487c47a87e871dfef53345e2b71288008bff','prior_sha':'445f4d3545cf031bcce4bf77a2b4a61ffb3b4c4f','requests_per_runtime':10,'engines':list(commands),'timeout_per_request_seconds':60,'rss_guard_mib':guard_mib,'sampler':'same frozen helper5ms sampled process-tree RSS, plus watchdog','binary_sha256':{e:hashlib.sha256(Path(v[0]).read_bytes()).hexdigest() for e,v in commands.items()}};(out/'launch.json').write_text(json.dumps(meta,indent=2)+'\n')
for engine in commands:
 p,reader,err=run.persistent(engine);stop=threading.Event();censored=[]
 def watch():
  while not stop.wait(.01):
   mib=run.tree(p.pid)[0]
   if mib>guard_mib:
    censored.append({'reason':'RSS watchdog','sampled_tree_rss_mib':mib});os.killpg(p.pid,signal.SIGKILL);break
 t=threading.Thread(target=watch,daemon=True);t.start()
 try:
  for request in range(10):
   row=run.trial(engine,c,(p,reader),timeout=60);fields={x.split(':')[0]:x.split(':')[1].strip() for x in Path(f'/proc/{p.pid}/status').read_text().splitlines() if x.startswith(('VmRSS:','VmHWM:'))};row.update(engine=engine,request=request,case=c['name'],accepted_timing=False,post_response_proc=fields);rows.append(row)
   with (out/'observations.jsonl').open('a') as f:f.write(json.dumps(row,separators=(',',':'))+'\n')
   print(engine,request,row['wall_ms'],flush=True)
 except Exception as error:
  failure={'engine':engine,'error':str(error),'censored':censored};failures.append(failure);(out/'failures.json').write_text(json.dumps(failures,indent=2)+'\n');print('DIAGNOSTIC FAILURE',json.dumps(failure),flush=True)
 finally:
  stop.set();t.join()
  if p.poll() is None:
   p.stdin.close()
   try:p.wait(timeout=10)
   except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait()
  err.close()
summary=[]
for engine in commands:
 group=[x for x in rows if x['engine']==engine];summary.append({'engine':engine,'completed_requests':len(group),'first_ms':group[0]['wall_ms'] if group else None,'last_ms':group[-1]['wall_ms'] if group else None,'trajectory_ms':[x['wall_ms'] for x in group],'proc_rss_trajectory':[x['post_response_proc'] for x in group]})
(out/'summary.json').write_text(json.dumps({'pass':not failures and len(rows)==60,'scope':'descriptive retained-runtime trajectories; not official medians, no statistical significance claim','rows':summary,'failures':failures},indent=2)+'\n');print('REUSED RUNTIME DIAGNOSTIC COMPLETE',flush=True)
