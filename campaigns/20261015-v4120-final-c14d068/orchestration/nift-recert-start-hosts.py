import subprocess,concurrent.futures,json,time
from pathlib import Path
s=json.loads(Path('/tmp/nift-recert-c14d068-state.json').read_text())
def start(name):
 for attempt in range(12):
  p=subprocess.run(['python3','/tmp/nift-recert-cloud.py','scp',name,'/tmp/nift-recert-host-prepare.sh','REMOTE:/root/nift-recert-host-prepare.sh'],capture_output=True,text=True)
  if p.returncode==0:break
  time.sleep(5)
 else:return {'benchmark':name,'started':False,'error':'SSH not ready'}
 p=subprocess.run(['python3','/tmp/nift-recert-cloud.py','ssh',name,'nohup bash /root/nift-recert-host-prepare.sh > /root/refresh-prepare.log 2>&1 < /dev/null & echo $!'],capture_output=True,text=True)
 return {'benchmark':name,'started':p.returncode==0,'pid':p.stdout.strip() if p.returncode==0 else None}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:r=list(pool.map(start,s['nodes']))
Path('/home/nick/Repositories/nift/nift-benchmarks/lab-evidence/campaigns/20261015-v4120-final-c14d068/cloud-start.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
