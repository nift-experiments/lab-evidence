import concurrent.futures,multiprocessing,os,time,asyncio,json

def job(i):time.sleep(.02);return os.getpid()
async def cancellation():
 t=asyncio.create_task(asyncio.sleep(1));await asyncio.sleep(0);t.cancel()
 try:await t
 except asyncio.CancelledError:print(json.dumps({'cancel':'CancelledError'}))
if __name__=='__main__':
 for w in [1,2,4]:
  with concurrent.futures.ProcessPoolExecutor(max_workers=w,mp_context=multiprocessing.get_context('spawn')) as pool:pids=set(pool.map(job,range(16)))
  assert 1<=len(pids)<=w;print(json.dumps({'workers':w,'distinct_worker_processes':len(pids)}))
 asyncio.run(cancellation())
