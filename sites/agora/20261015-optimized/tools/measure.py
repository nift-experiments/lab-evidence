#!/usr/bin/env python3
"""Serialized Linux publication measurement. Observer is outside sampled workload RSS."""
import argparse,json,os,subprocess,time,threading,re,signal
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--cwd',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--label',required=True);p.add_argument('--interval',type=float,default=.02);p.add_argument('command',nargs=argparse.REMAINDER);a=p.parse_args();cmd=a.command[1:] if a.command and a.command[0]=='--' else a.command
assert cmd;a.output=a.output.resolve();a.cwd=a.cwd.resolve();a.output.mkdir(parents=True,exist_ok=True);stem=a.output/a.label;env=os.environ.copy();env['PATH']='/home/nick/.bun/bin:'+env['PATH']
for key in list(env):
 if key.startswith(('VITE_','TSS_','FUMADOCS_','ALGOLIA_','AWS_')) or key in ('DOCS_DEV_SCOPE','SITE_URL','PUBLIC_SITE_URL','NODE_OPTIONS'):
  env.pop(key,None)
start=time.perf_counter();proc=subprocess.Popen(['/usr/bin/time','-v','-o',str(stem.with_suffix('.time')),*cmd],cwd=a.cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,start_new_session=True)
def stop_owned_workload(signum, frame):
 try:
  os.killpg(proc.pid, signal.SIGTERM)
  try:proc.wait(timeout=5)
  except subprocess.TimeoutExpired:
   os.killpg(proc.pid, signal.SIGKILL);proc.wait()
 except ProcessLookupError:pass
 raise KeyboardInterrupt
signal.signal(signal.SIGINT,stop_owned_workload);signal.signal(signal.SIGTERM,stop_owned_workload)
phase={'name':'startup'};events=[];milestones=[];completion={}
def log_output():
 with stem.with_suffix('.log').open('wb') as out:
  for line in iter(proc.stdout.readline,b''):
   out.write(line);out.flush();text=line.decode(errors='replace')
   plain=re.sub(r'\x1b\[[0-9;]*[A-Za-z]', '', text).strip()
   if any(marker in plain for marker in ('building client', 'building ssr', 'building server', 'modules transformed', 'rendering chunks', 'built in', '[static-payload] generated', '[static-seo] generated', '[prerender] Prerendering', '[prerender] Concurrency', '[MDX] generated')):
    milestones.append({'elapsedSeconds':time.perf_counter()-start,'phase':phase['name'],'line':plain})
   if plain.startswith('[nift-pipeline-start] '):
    name=plain.split('] ',1)[1];phase['name']=name;events.append({'elapsedSeconds':time.perf_counter()-start,'phase':name,'line':plain})
   if text.startswith('$ '):
    if 'sync-openapi' in text:name='openapi-sync'
    elif 'generate-docs-last-updated' in text:name='last-updated'
    elif 'generate-static-docs-payload' in text:name='static-payload'
    elif 'generate-static-route-html' in text:name='route-html'
    elif 'vite build' in text:name='application-build-and-prerender'
    elif 'legacy-redirect' in text:name='legacy-redirect-check'
    else:continue
    phase['name']=name;events.append({'elapsedSeconds':time.perf_counter()-start,'phase':name,'line':text.strip()})
def watch_completion():
 proc.wait();completion['end']=time.perf_counter()
watcher=threading.Thread(target=watch_completion);watcher.start()
thread=threading.Thread(target=log_output);thread.start();peak={'treeRssKiB':0};samples=0;pageKiB=os.sysconf('SC_PAGE_SIZE')/1024
with stem.with_suffix('.jsonl').open('w') as trace:
 while proc.poll() is None:
  rows={}
  for path in Path('/proc').iterdir():
   if not path.name.isdigit():continue
   try:
    stat=(path/'stat').read_text();tail=stat.rsplit(')',1)[1].split();rows[int(path.name)]={'pid':int(path.name),'name':stat.split('(',1)[1].rsplit(')',1)[0],'ppid':int(tail[1]),'pgrp':int(tail[2]),'rssKiB':int(tail[21])*pageKiB}
   except (OSError,ValueError,IndexError):continue
  ids={pid for pid,r in rows.items() if r['pgrp']==proc.pid};ids.add(proc.pid)
  while True:
   more={pid for pid,r in rows.items() if r['ppid'] in ids};new=more-ids
   if not new:break
   ids.update(new)
  processes=[rows[pid] for pid in sorted(ids) if pid in rows and pid!=proc.pid]
  row={'elapsedSeconds':time.perf_counter()-start,'phase':phase['name'],'treeRssKiB':sum(r['rssKiB'] for r in processes),'processes':processes};trace.write(json.dumps(row,separators=(',',':'))+'\n');samples+=1
  if row['treeRssKiB']>peak['treeRssKiB']:peak=row
  time.sleep(a.interval)
code=proc.wait();thread.join();watcher.join();end=completion['end'];t=stem.with_suffix('.time').read_text();m=re.search(r'Maximum resident set size \(kbytes\): (\d+)',t)
report={'label':a.label,'command':cmd,'exitCode':code,'wallSeconds':end-start,'sampledPeakTreeRssMiB':peak['treeRssKiB']/1024,'maxIndividualProcessRssMiB':int(m[1])/1024 if m else None,'peak':peak,'phaseEvents':events,'milestones':milestones,'samples':samples,'requestedSamplingSleepSeconds':a.interval,'memoryDefinition':'Summed RSS of simultaneously observed workload process group plus descendants. Excludes Python observer and GNU time wrapper. Shared pages may be counted more than once; short-lived peaks can be missed. Not PSS or exact physical memory.','osCaches':'uncontrolled'}
timestamps=[json.loads(line)['elapsedSeconds'] for line in stem.with_suffix('.jsonl').read_text().splitlines()]
if len(timestamps)>1:
 import statistics
 gaps=[b-a for a,b in zip(timestamps,timestamps[1:])];report['observedSamplingGapSeconds']={'median':statistics.median(gaps),'min':min(gaps),'max':max(gaps)}
report['phaseAttribution']='Approximate; inferred from buffered command log lines. Verify against phaseEvents and build log.'
stem.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ['phaseEvents','milestones','memoryDefinition','peak']},indent=2),flush=True);raise SystemExit(code)
