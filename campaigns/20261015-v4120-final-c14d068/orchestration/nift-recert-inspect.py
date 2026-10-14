import json,os,re,shlex,subprocess,tempfile,urllib.request
from pathlib import Path
p=Path.home()/'.bashrc'
with p.open('rb') as f:
 f.seek(max(0,p.stat().st_size-16384));tail=f.read().decode()
assignments=re.findall(r'(?m)^\s*(?:export\s+)?LINODE_CLI_TOKEN\s*=\s*(.+)$',tail);assert assignments,'Token assignment not found in permitted tail';token=shlex.split(assignments[-1])[0];del tail,assignments
with tempfile.TemporaryDirectory(prefix='nift-recert-inspect-') as td:
 env=dict(os.environ,LINODE_CLI_TOKEN=token,XDG_CONFIG_HOME=td,LINODE_CLI_CONFIG=td+'/cli-config')
 result=subprocess.run(['linode-cli','linodes','list','--json'],env=env,capture_output=True,text=True,timeout=60)
 if result.returncode:raise SystemExit('CLI inventory failed; sensitive diagnostic suppressed')
 nodes=json.loads(result.stdout)
 response=json.load(urllib.request.urlopen(urllib.request.Request('https://api.linode.com/v4/linode/instances',headers={'Authorization':'Bearer '+token}),timeout=30))
 selected=[{k:n.get(k) for k in ('id','label','status','type','region','created')} for n in nodes if any(s in n.get('label','').lower() for s in ('nift','bench','recert'))]
 receipt={'CLI_total_instances':len(nodes),'API_total_instances':response['results'],'campaign_like_instances':selected,'addresses_credentials_private_state_omitted':True}
 out=Path('/home/nick/Repositories/nift/nift-benchmarks/lab-evidence/campaigns/20261015-v4120-final-c14d068/ci/cloud-inventory-before-provisioning.json');out.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
