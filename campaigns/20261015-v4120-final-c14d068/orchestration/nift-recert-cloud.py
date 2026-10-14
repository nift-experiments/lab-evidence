import shutil,os,re,shlex,subprocess,json,tempfile,secrets,sys,time,urllib.request,urllib.error,concurrent.futures,threading
from pathlib import Path
STATE=Path('/tmp/nift-recert-c14d068-state.json'); OUT=Path('/home/nick/Repositories/nift/nift-benchmarks/lab-evidence/campaigns/20261015-v4120-final-c14d068');SHA='c14d06835bca515a5281e41da0e40219c2d60ef0'
with open('/home/nick/.bashrc','rb') as f:
 f.seek(0,2);f.seek(max(0,f.tell()-16384));tail=f.read().decode()
matches=re.findall(r'(?m)^\s*(?:export\s+)?LINODE_CLI_TOKEN\s*=\s*(.+)$',tail)
m=matches[-1] if matches else None
if not m:raise SystemExit('Authorized token assignment unavailable in bashrc tail')
token=shlex.split(m)[0];del tail,m,matches
lock=threading.Lock()
def save():
 with lock:STATE.write_text(json.dumps(state));STATE.chmod(0o600)
def cli(args):
 p=subprocess.run(['linode-cli',*args,'--json'],env=dict(os.environ,LINODE_CLI_TOKEN=token,XDG_CONFIG_HOME=state['private'],LINODE_CLI_CONFIG=state['private']+'/cli-config'),capture_output=True,text=True)
 if p.returncode:raise RuntimeError('Linode CLI failed '+str(p.returncode)+': '+'[redacted CLI error; inspect sanitized diagnostics]' )
 return json.loads(p.stdout) if p.stdout.strip() else None
def request(path):return json.load(urllib.request.urlopen(urllib.request.Request('https://api.linode.com/v4/'+path,headers={'Authorization':'Bearer '+token}),timeout=30))
def opts():return ['-i',state['private']+'/key','-o','BatchMode=yes','-o','StrictHostKeyChecking=accept-new','-o','UserKnownHostsFile='+state['private']+'/known_hosts','-o','ConnectTimeout=15']
names=['build-systems','concurrency','filesystem-automation','scripting-benchmark','shell-benchmark','task-runners','template-engines','website-generator-benchmark']
cmd=sys.argv[1]
if STATE.exists():state=json.loads(STATE.read_text())
elif cmd=='create':
 gate=json.loads((OUT/'preflight-gate.json').read_text())
 assert gate['candidate_sha']==SHA and gate['all_eight_suites_passed'] is True
 private=Path(tempfile.mkdtemp(prefix='nift-recert-private-',dir='/tmp'));private.chmod(0o700);subprocess.run(['ssh-keygen','-q','-t','ed25519','-N','','-f',str(private/'key')],check=True)
 state={'private':str(private),'nodes':{},'candidate':SHA};save()
else:raise SystemExit('Refresh state does not exist')
if cmd=='create':
 gate=json.loads((OUT/'preflight-gate.json').read_text())
 assert gate['candidate_sha']==SHA and gate['all_eight_suites_passed'] is True
 plan=request('linode/types/g6-standard-4');assert plan['price']['hourly']<=0.08 and plan['memory']==8192 and plan['vcpus']==4
 (OUT/'cloud-plan.json').write_text(json.dumps({k:plan[k] for k in ['id','memory','vcpus','disk','price']},indent=2)+'\n')
 key=Path(state['private']+'/key.pub').read_text().strip()
 def create(name):
  if name in state['nodes']:return state['nodes'][name]
  label='nift-recert-'+name.replace('-benchmark','')+'-20261015-c14'
  # Existing matching labels are recovered after an ambiguous create, never duplicated.
  existing=[x for x in cli(['linodes','list']) if x['label']==label]
  if existing:x=existing[0]
  else:
   password=secrets.token_urlsafe(40)+'Aa1!'
   x=cli(['linodes','create','--label',label,'--type','g6-standard-4','--region','us-east','--image','linode/ubuntu24.04','--root_pass',password,'--authorized_keys',key,'--booted','true']);x=x[0] if isinstance(x,list) else x;del password
  row={k:x.get(k) for k in ['id','label','created','status','type','region']};row['ip']=x['ipv4'][0];state['nodes'][name]=row;save();return dict(benchmark=name,**{k:v for k,v in row.items() if k!='ip'})
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
  for x in pool.map(create,names):print(json.dumps(x),flush=True)
 (OUT/'hosts.json').write_text(json.dumps({n:{k:v for k,v in r.items() if k!='ip'} for n,r in state['nodes'].items()},indent=2)+'\n')
elif cmd=='status':
 for name,row in state['nodes'].items():
  if row.get('deleted'):print(json.dumps({'benchmark':name,'id':row['id'],'status':'deleted_verified'}));continue
  x=cli(['linodes','view',str(row['id'])]);x=x[0] if isinstance(x,list) else x;print(json.dumps({'benchmark':name,**{k:x.get(k) for k in ['id','status','type','region']}}),flush=True)
elif cmd=='ssh':
 row=state['nodes'][sys.argv[2]];raise SystemExit(subprocess.run(['ssh',*opts(),'root@'+row['ip'],sys.argv[3]]).returncode)
elif cmd=='scp':
 row=state['nodes'][sys.argv[2]];src,dest=sys.argv[3:5];src=src.replace('REMOTE:','root@'+row['ip']+':');dest=dest.replace('REMOTE:','root@'+row['ip']+':');raise SystemExit(subprocess.run(['scp',*opts(),src,dest]).returncode)
elif cmd=='delete':
 name=sys.argv[2];row=state['nodes'][name];gate=json.loads((OUT/'lifecycle'/name/'ready.json').read_text())
 assert gate['linode_id']==row['id'] and gate['candidate_sha']==SHA
 assert all(gate[k] is True for k in ('measurements_complete','independent_audit_pass','evidence_collected','evidence_pushed','required_diagnostics_complete'))
 repo=OUT.parents[1]
 head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip()
 remote=subprocess.check_output(['git','ls-remote','origin','refs/heads/main'],cwd=repo,text=True).split()[0]
 assert head==remote and gate['evidence_commit']==head
 receipt={'benchmark':name,'linode_id':row['id'],'candidate_sha':SHA,'evidence_commit':head,'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
 target=OUT/'lifecycle'/name/'teardown.json'
 target.write_text(json.dumps(receipt,indent=2)+'\n')
 before=cli(['linodes','list'])
 if any(x['id']==row['id'] for x in before):cli(['linodes','delete',str(row['id'])])
 listed=cli(['linodes','list']);assert not any(x['id']==row['id'] for x in listed)
 code=None
 try:request('linode/instances/'+str(row['id']))
 except urllib.error.HTTPError as e:code=e.code
 assert code==404
 subprocess.run(['ssh-keygen','-R',row['ip'],'-f',state['private']+'/known_hosts'],capture_output=True,check=True)
 backup=Path(state['private']+'/known_hosts.old')
 if backup.exists():backup.unlink()
 row['deleted']=True;row.pop('ip',None);save()
 receipt.update(cli_absent=True,api_status=404,temporary_per_host_known_hosts_removed=True,shared_access_retained_for_other_hosts=True,completed_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
 target.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
elif cmd=='verify-cleanup':
 assert len(state['nodes'])==8 and all(x.get('deleted') for x in state['nodes'].values())
 ids=[x['id'] for x in state['nodes'].values()];listed=cli(['linodes','list']);assert not any(x['id'] in ids for x in listed)
 statuses={}
 for node in ids:
  code=None
  try:request('linode/instances/'+str(node))
  except urllib.error.HTTPError as e:code=e.code
  assert code==404;statuses[str(node)]=code
 private=Path(state['private']);assert private.parent==Path('/tmp') and private.name.startswith('nift-recert-private-')
 shutil.rmtree(private);STATE.unlink()
 receipt={'all_eight_cli_absent':True,'api_status_by_id':statuses,'shared_temporary_ssh_key_known_hosts_and_cli_configuration_removed':not private.exists(),'temporary_cloud_state_removed':not STATE.exists(),'credential_source_unchanged':True,'completed_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
 (OUT/'lifecycle'/'final-access-cleanup.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
else:raise SystemExit('Unsupported command')
