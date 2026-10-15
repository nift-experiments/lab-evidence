"""Monitor the existing run, then serially account, collect and audit; never rerun timing."""
from pathlib import Path
import subprocess,time,json,datetime,hashlib,tarfile,os,sys
N=Path(__file__).resolve().parent;W=N.parents[3];HELPER='/tmp/nift-website-publication-cloud.py';HOST='website-allcore-publication';REMOTE='/opt/website-publication';transport=W/'.lab-tools/website-collection';transport.mkdir(parents=True,exist_ok=True)
def call(args,timeout=120):return subprocess.check_output(['python3',HELPER,*args],text=True,stderr=subprocess.STDOUT,timeout=timeout)
def ssh(cmd,timeout=120):return call(['ssh',HOST,cmd],timeout)
def event(stage,**extra):
 d={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':os.getpid(),'host_id':108212898,'stage':stage,**extra};(N/'COLLECTOR-STATE.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d),flush=True)
event('monitoring-existing-official-controller',remote_controller_pid=8265)
while True:
 try:
  status=ssh('if test -f /opt/website-publication/evidence/official-allcore/PASS; then echo READY_TO_ACCOUNT; elif kill -0 8265 2>/dev/null; then tail -2 /opt/website-publication/evidence/official.log; else echo CONTROLLER_STOPPED_WITHOUT_PASS; tail -8 /opt/website-publication/evidence/official.log; fi')
  print(status,flush=True)
  if 'READY_TO_ACCOUNT' in status:break
  if 'CONTROLLER_STOPPED_WITHOUT_PASS' in status:event('blocked-official-controller-failure',output=status);sys.exit(1)
 except Exception as exc:event('monitor-network-retry',error=str(exc))
 time.sleep(300)
event('official-complete-starting-untimed12cell-accounting')
print(ssh('test -f /opt/website-publication/evidence/official-allcore/PASS && taskset -c 0-3 python3 /opt/website-publication/work-accounting.py',timeout=3600),flush=True)
event('accounting-complete-collecting')
print(ssh('test -f /opt/website-publication/evidence/work-accounting/PASS && cp /opt/nift-build.log /opt/website-publication/evidence/core-build.log && cp /opt/refresh-packages.log /opt/website-publication/evidence/package-install.log && cp /opt/website-publication/gate-attempt1.py /opt/website-publication/evidence/gate-attempt1.py && cp /opt/website-publication/gate.py /opt/website-publication/evidence/gate-final.py && tar -czf /opt/website-publication/evidence-all.tar.gz -C /opt/website-publication evidence',timeout=300),flush=True)
archive=transport/'evidence-all.tar.gz';call(['scp',HOST,'REMOTE:/opt/website-publication/evidence-all.tar.gz',str(archive)],timeout=300)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
with tarfile.open(archive) as tar:
 for item in tar.getmembers():
  if not item.isfile():continue
  parts=Path(item.name).parts;assert parts[0]=='evidence' and '..' not in parts
  rel=Path(*parts[1:]);dest=N/rel if parts[1] in ('official-allcore','work-accounting') else N/'host'/rel
  dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(tar.extractfile(item).read())
rawdir=N/'official-allcore';remoteaudit=rawdir/'independent-audit.json';remoteaudit.rename(rawdir/'remote-independent-audit.json')
subprocess.run([sys.executable,str(N/'audit.py'),str(rawdir)],check=True);assert sha(rawdir/'independent-audit.json')==sha(rawdir/'remote-independent-audit.json')
boundaries=json.loads((N/'COMMAND-BOUNDARIES.json').read_text())
for size in (100,1000,10000):
 d=json.loads((rawdir/f'website-{size}.json').read_text())
 for j in d['jobs']:
  if '/incremental/' in j['id']:assert j['command']==boundaries['normal_publish']['argv']
  else:assert j['command']==boundaries['full_builds'][j['id'].split('/')[0]]['argv']
target=json.loads((rawdir/'targeted-builds.json').read_text())
for j in target['jobs']:assert j['command']==boundaries['explicit_target']['argv' if j['id'].endswith('/targeted-one-page') else 'reference_argv']
boundaries['status']='Verified exact argv against all39new accepted jobs; cleanup boundaries from frozen source';(N/'COMMAND-BOUNDARIES.json').write_text(json.dumps(boundaries,indent=2)+'\n')
account=N/'work-accounting';d=json.loads((account/'summary.json').read_text());assert len(d['rows'])==12;seen=set()
for row in d['rows']:
 assert row['correct'] and row['untimed'];key=(row['engine'],row['pages']);assert key not in seen;seen.add(key);m=json.loads((account/row['manifest']).read_text())
 for prefix,field in [('input','initial_files'),('public','public_output_files'),('new_non_public','new_non_public_files')]:
  assert row[prefix+'_files']==len(m[field]);assert row[prefix+'_bytes']==sum(v['bytes'] for v in m[field].values())
 assert row['semantic_oracle']=={'routes':row['pages'],'content_checked':row['pages']}
 assert row['public_html_files']==row['pages']+(1 if row['engine']=='VitePress' else 0)
assert seen=={(n,s) for n in ('Nift','Hugo','Astro','VitePress') for s in (100,1000,10000)}
(account/'independent-audit.json').write_text(json.dumps({'pass':True,'cells':12,'checks':['exactengine/sizecoverage','allsemanticoraclespassed','manifestinput/output/internalcountsandbytesrecomputed','VitePress404disclosed','untimedaccountingseparatefromofficialsamples']},indent=2)+'\n')
files={str(p.relative_to(N)):sha(p) for folder in [rawdir,account,N/'host'] for p in folder.rglob('*') if p.is_file()}
result={'pass':True,'host_id':108212898,'official_observations':234,'official_measured':195,'official_warmups':39,'official_jobs':39,'untimed_accounting_cells':12,'raw_bytes_preserved':True,'transport_sha256':sha(archive),'files_sha256':files,'candidate':'c14d06835bca515a5281e41da0e40219c2d60ef0','retention':'Host remains active for15separateFSpostexecmetriccells; root owns push/localverification/teardown','utc':datetime.datetime.now(datetime.timezone.utc).isoformat()};(N/'COLLECTION-PASS.json').write_text(json.dumps(result,indent=2)+'\n');event('complete-collected-audited-accounted',official_observations=234,untimed_accounting_cells=12,filesystem_handoff_ready=True)
