from pathlib import Path
import os,sys,time,json,subprocess,hashlib,select,signal,threading,statistics,argparse,resource
R=Path(__file__).resolve().parents[1];os.chdir(R)
ENGINES=['nift','python','node','bun','go']
AFFINITY=sorted(os.sched_getaffinity(0))[:4]
def pin():os.sched_setaffinity(0,AFFINITY)
def command(e):
 if e=='nift':return [str(R/'work/nift-source/nift'),'adapters/nift.f']
 if e=='python':return [str(next((R/'work/tools/python').glob('*/bin/python3'))),'adapters/python.py']
 if e=='node':return [str(R/'work/tools/node-v24.21.0-linux-x64/bin/node'),'adapters/js.mjs']
 if e=='bun':return [str(R/'work/tools/bun-linux-x64/bun'),'adapters/js.mjs']
 return [str(R/'work/go-adapter')]
def unsupported(e,c):
 if e=='nift' and c['kind']=='memory' and c['n']==10000:return 'Outside practical 8GiB host range: local held checkpoint used 13700MiB; no official timing accepted'
 if e=='python' and c['kind']=='atomic':return 'No comparable public shared-memory atomic integer in ordinary CPython'
 if e in ['node','bun'] and c['kind']=='mutex':return 'No standard native mutex/protected-value primitive; no custom lock substituted'
 return None

def kernel(i,n):
 x=i+1
 for _ in range(n):x=x*48271%2147483647
 return x

def expected(c):
 k=c['kind'];n=c['n'];it=c['iterations'];e=c['extra']
 if k in ['atomic','mutex']:return [[0,n*(it if k=='mutex' else 1)]]
 out=[]
 for i in range(n*it if k=='nested' else n):
  if k in ['wait','stagger','mixed-wait','memory']:v=i
  elif k=='files':
   v=0
   for j in range(128):v=(v*31+(i*7+j*13)%128)%1000000007
  elif k=='queue':v=i*17+3
  elif k.startswith('process') or k=='mixed':v={'value':i*17+3+(kernel(i,it) if k=='mixed' else 0),'exit':7 if k=='process-fail' and i<e else 0}
  elif k=='failure' and i<e:v={'error':'task.failure'}
  else:v=kernel(i,8 if k=='nested' else it)
  out.append([i,v])
 return out

def proc_stats(pid):
 try:
  s=Path(f'/proc/{pid}/stat').read_text().rsplit(')',1)[1].split();rss=int(s[21])*os.sysconf('SC_PAGE_SIZE');cpu=sum(int(s[i]) for i in [11,12,13,14])/os.sysconf('SC_CLK_TCK');threads=int(s[17]);children=[]
  for task in Path(f'/proc/{pid}/task').iterdir():
   try:children+= (task/'children').read_text().split()
   except OSError:pass
  return rss,cpu,threads,[int(x) for x in children]
 except (OSError,ValueError,IndexError):return 0,0,0,[]
def tree(pid):
 seen=set();todo=[pid];rss=0;count=0;threads=0
 while todo:
  p=todo.pop()
  if p in seen:continue
  seen.add(p);r,c,t,kids=proc_stats(p);rss+=r;count+=bool(r);threads+=t;todo+=kids
 return rss/1048576,count,threads
class Reader:
 def __init__(self,p):self.p=p;self.buf=b''
 def line(self,timeout):
  end=time.monotonic()+timeout
  while b'\n' not in self.buf:
   if not select.select([self.p.stdout],[],[],max(0,end-time.monotonic()))[0]:raise TimeoutError('response watchdog')
   data=os.read(self.p.stdout.fileno(),65536)
   if not data:raise RuntimeError('participant exited before complete response')
   self.buf+=data
   if len(self.buf)>64*1024*1024:raise RuntimeError('response exceeds bounded 64MiB')
  line,self.buf=self.buf.split(b'\n',1);return line

def trial(e,c,persistent=None,timeout=120):
 new=persistent is None
 errpath=R/'work/adapter-stderr.log';err=errpath.open('ab') if new else None
 before_cpu=0;peak=[0,0,0];stop=threading.Event()
 if not new:before_cpu=proc_stats(persistent[0].pid)[1]
 start=time.perf_counter_ns()
 p,reader=persistent if not new else (subprocess.Popen(command(e),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err,start_new_session=True,preexec_fn=pin),None)
 reader=reader or Reader(p)
 def sample():
  while not stop.is_set():
   r,n,t=tree(p.pid);peak[0]=max(peak[0],r);peak[1]=max(peak[1],n);peak[2]=max(peak[2],t);stop.wait(.005)
 sampler=threading.Thread(target=sample,daemon=True);sampler.start()
 held=None
 try:
  request='|'.join(str(c[k]) for k in ['kind','n','workers','iterations','extra'])+'\n';p.stdin.write(request.encode());p.stdin.flush()
  line=reader.line(timeout)
  if line==b'BOOT':line=reader.line(timeout)
  if line==b'READY':held=tree(p.pid);p.stdin.write(b'GO\n');p.stdin.flush();line=reader.line(timeout)
  cpu=proc_stats(p.pid)[1]-before_cpu
  child_max=None
  if new:
   p.stdin.close();_,status,usage=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status)
   if p.returncode:raise RuntimeError('participant exit '+str(p.returncode))
   cpu=usage.ru_utime+usage.ru_stime;child_max=usage.ru_maxrss/1024
  wall=(time.perf_counter_ns()-start)/1e6
  rows=json.loads(line);rows.sort(key=lambda x:x[0]);want=expected(c);assert rows==want,{'case':c['name'],'engine':e,'first_mismatch':next(((a,b) for a,b in zip(rows,want) if a!=b),None),'actual_count':len(rows),'expected_count':len(want)}
  normalized=json.dumps(rows,separators=(',',':'),sort_keys=True).encode()
  if c['kind'] in ['failure','process-fail','nested']:
   trace=R/'work/selected-traces'/f"{e}-{c['name']}-{'fresh' if new else 'persistent'}.json"
   trace.parent.mkdir(parents=True,exist_ok=True)
   if not trace.exists():trace.write_bytes(normalized+b'\n')
  return {'wall_ms':wall,'cpu_ms':cpu*1000,'sampled_tree_rss_mib':peak[0],'sampled_process_count':peak[1],'sampled_thread_count':peak[2],'max_child_rss_mib':child_max,'held_tree_rss_mib':held[0] if held else None,'held_process_count':held[1] if held else None,'held_thread_count':held[2] if held else None,'count':len(rows),'result_sha256':hashlib.sha256(normalized).hexdigest(),'correct':True}
 except BaseException:
  try:os.killpg(p.pid,signal.SIGKILL)
  except ProcessLookupError:pass
  try:p.wait(timeout=3)
  except subprocess.TimeoutExpired:pass
  raise
 finally:
  stop.set();sampler.join();
  if err:err.close()

def persistent(e):
 err=(R/'work/adapter-stderr.log').open('ab');p=subprocess.Popen(command(e),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err,start_new_session=True,preexec_fn=pin);reader=Reader(p);assert reader.line(30)==b'BOOT';return p,reader,err

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--certify',action='store_true');ap.add_argument('--pilot',action='store_true');ap.add_argument('--select');ap.add_argument('--output',default='work/official');args=ap.parse_args()
 cs=json.loads((R/'docs/SCENARIOS.json').read_text());
 if args.select:cs=[c for c in cs if c['name'] in args.select.split(',')]
 dest=R/args.output;dest.mkdir(parents=True,exist_ok=True);unsupported_rows=[];results=[]
 with (dest/'observations.jsonl').open('w') as f:
  for ci,c in enumerate(cs):
   for mode in ['fresh','persistent']:
    workers={};count=1 if args.certify or args.pilot else c['samples']+c['warmups']
    try:
     for round in range(count):
      order=ENGINES[(ci+round)%5:]+ENGINES[:(ci+round)%5]
      for e in order:
       reason=unsupported(e,c)
       if reason:
        if round==0:unsupported_rows.append({'case':c['name'],'mode':mode,'engine':e,'reason':reason})
        continue
       if mode=='persistent' and e not in workers:workers[e]=persistent(e)
       row=trial(e,c,workers[e][:2] if mode=='persistent' else None,timeout=60 if args.certify or args.pilot else 120)
       row.update(case=c['name'],engine=e,mode=mode,round=round,warmup=not(args.certify or args.pilot) and round<c['warmups'],workers=c['workers'],n=c['n'],iterations=c['iterations'],extra=c['extra'])
       f.write(json.dumps(row,separators=(',',':'))+'\n');f.flush();results.append(row)
       if mode=='persistent':
        p,reader,err=workers.pop(e);p.stdin.close();p.wait(timeout=10);err.close()
    finally:
     for p,reader,err in workers.values():
      if p.poll() is None:p.stdin.close();p.wait(timeout=10)
      err.close()
    print(c['name'],mode,'PASS',flush=True)
 (dest/'unsupported.json').write_text(json.dumps(unsupported_rows,indent=2)+'\n');(dest/'acceptance.json').write_text(json.dumps({'pass':True,'observations':len(results),'unsupported_cells':len(unsupported_rows),'certification':args.certify,'pilot':args.pilot},indent=2)+'\n')
if __name__=='__main__':main()
