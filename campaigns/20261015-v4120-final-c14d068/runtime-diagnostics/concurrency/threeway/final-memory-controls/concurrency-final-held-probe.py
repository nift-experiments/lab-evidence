import sys,subprocess,threading,time,json,hashlib,signal,os
sys.path.insert(0,'scripts');import run
c=next(x for x in json.load(open('docs/SCENARIOS.json')) if x['name']=='waiting-memory-10000')
p=subprocess.Popen(run.command('nift'),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True);reader=run.Reader(p);stop=threading.Event();peak=[0];aborted=[]
def monitor():
 while not stop.wait(.01):
  m=run.tree(p.pid)[0];peak[0]=max(peak[0],m)
  if m>6144:
   aborted.append('RSS guard >6144MiB');os.killpg(p.pid,signal.SIGKILL);break
t=threading.Thread(target=monitor,daemon=True);t.start();receipt={'case':c['name'],'candidate':'c14d06835bca515a5281e41da0e40219c2d60ef0','scope':'untimed bounded cloud capability diagnostic after official timing','rss_guard_mib':6144,'timeout_seconds':90}
try:
 assert reader.line(10)==b'BOOT';p.stdin.write(b'memory|10000|4|0|10\n');p.stdin.flush();line=reader.line(45)
 if line==b'READY':
  receipt['held_tree_rss_mib']=run.tree(p.pid)[0];p.stdin.write(b'GO\n');p.stdin.flush();line=reader.line(45)
 rows=json.loads(line);rows.sort(key=lambda x:x[0]);assert rows==run.expected(c);receipt.update(pass_=True,rows=len(rows),result_sha256=hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest());p.stdin.close();p.wait(timeout=5)
except Exception as e:
 receipt.update(pass_=False,error=str(e),guard=aborted)
 if p.poll() is None:os.killpg(p.pid,signal.SIGKILL);p.wait()
finally:stop.set();t.join();receipt['peak_sampled_tree_rss_mib']=peak[0]
open('work/final-held-10000-capability-6gib.json','w').write(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
