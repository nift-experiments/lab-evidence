import sys,json,time,asyncio,concurrent.futures,threading,queue,subprocess,pathlib,multiprocessing

def kernel(i,count):
 x=i+1
 for _ in range(count):x=x*48271%2147483647
 return x

def job(kind,i,it,extra):
 if kind=='files':
  h=0
  for b in pathlib.Path(f'work/fixtures/{i}.dat').read_bytes():h=(h*31+b)%1000000007
  return h
 if kind.startswith('process') or kind=='mixed':
  if kind=='mixed':time.sleep(extra/1000)
  ms=i%5 if kind=='process-mixed' else 0; code=7 if kind=='process-fail' and i<extra else 0
  p=subprocess.run(['work/helper',str(i),str(ms),str(code)],capture_output=True,check=False)
  return {'value':int(p.stdout)+(kernel(i,it) if kind=='mixed' else 0),'exit':p.returncode}
 if kind=='failure' and i<extra:raise RuntimeError('task.failure')
 return kernel(i,it)

async def concurrent_tasks(kind,n,it,extra):
 async def one(i):
  try:
   if kind in ('wait','memory','stagger','mixed-wait'):
    ms=extra if kind in ('wait','memory') else (1+i%20 if kind=='stagger' else 20 if i%10==0 else 1)
    await asyncio.sleep(ms/1000);v=i
   elif kind=='nested':v=await asyncio.gather(*(one_inner(i*it+j) for j in range(it)))
   else:v=job(kind,i,it,extra)
   return [i,v]
  except RuntimeError as e:return [i,{'error':str(e)}]
 async def one_inner(i):return kernel(i,8)
 if kind=="memory":
  gate=asyncio.Event()
  async def held(i):
   await gate.wait(); await asyncio.sleep(extra/1000);return [i,i]
  tasks=[asyncio.create_task(held(i)) for i in range(n)]
  await asyncio.sleep(0); print("READY",flush=True); sys.stdin.readline();gate.set();return await asyncio.gather(*tasks)
 rows=await asyncio.gather(*(asyncio.create_task(one(i)) for i in range(n)))
 if kind=='nested':return [[i*it+j,v] for i,vs in rows for j,v in enumerate(vs)]
 return rows

def execute(kind,n,w,it,extra):
 if kind=='mutex':
  lock=threading.Lock();counter=0
  def inc():
   nonlocal counter
   for _ in range(n//w):
    with lock:
     for _ in range(it):counter+=1
  threads=[threading.Thread(target=inc) for _ in range(w)]
  for t in threads:t.start()
  for t in threads:t.join()
  return [[0,counter]]
 if kind=='queue':
  q=queue.Queue(64);rows=[];lock=threading.Lock()
  def producer(p):
   for i in range(p,n,w):q.put(i)
  def consumer():
   local=[]
   while True:
    i=q.get()
    if i is None:break
    local.append([i,i*17+3])
   with lock:rows.extend(local)
  cs=[threading.Thread(target=consumer) for _ in range(extra)];ps=[threading.Thread(target=producer,args=(p,)) for p in range(w)]
  for t in cs+ps:t.start()
  for t in ps:t.join()
  for _ in cs:q.put(None)
  for t in cs:t.join()
  return rows
 if kind in ('cpu','pool','files','process','process-mixed','process-fail','mixed'):
  cls=concurrent.futures.ProcessPoolExecutor if kind in ('cpu','pool') else concurrent.futures.ThreadPoolExecutor
  kw={'mp_context':multiprocessing.get_context('spawn')} if cls is concurrent.futures.ProcessPoolExecutor else {}
  with cls(max_workers=w,**kw) as pool:
   futures=[pool.submit(job,kind,i,it,extra) for i in range(n)]
   return [[i,f.result()] for i,f in enumerate(futures)]
 return asyncio.run(concurrent_tasks(kind,n,it,extra))
if __name__=='__main__':
 print('BOOT',flush=True)
 for line in sys.stdin:
  kind,n,w,it,extra=line.strip().split('|');print(json.dumps(execute(kind,int(n),int(w),int(it),int(extra)),separators=(',',':')),flush=True)
