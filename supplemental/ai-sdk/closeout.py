"""Accept the supplemental campaign only after all original gates complete."""
from pathlib import Path
import json,hashlib,subprocess,tarfile,io,datetime
E=Path(__file__).resolve().parent;ROOT=E.parents[3];BASE=ROOT/'nift-experiments';WORK=BASE/'ai-sdk-baseline/incremental-memory-work'
log=(E/'campaign.log').read_text();assert 'All original lifecycle and restoration gates passed.' in log
records=json.loads((E/'samples.json').read_text());assert all(x['exit_code']==0 for x in records)
selected=[];allproofs=[];fingerprints=[]
for project,pin in [('ai-sdk','7bb3b9f1713aed61291e73136ab100c2a6f5457c'),('ai-sdk-agent','dd568e4ec671dd6ddde38f06f7e24836840f3cb4')]:
 for suite in (['body','routes'] if project=='ai-sdk' else ['body','routes','coordinated']):
  proofs=json.loads((E/project/suite/(project+'-'+suite+'-proof.json')).read_text());allproofs+=proofs
  assert all(x['incremental_forced_equal'] for x in proofs)
  for x in proofs:
   if project=='ai-sdk-agent' and x['case'] in ['metadata-update-remove','historical-version','provider-reference']:continue
   record=next(y for y in records if y['project']==project and y['suite']==suite and y['case']==x['case']);selected.append({**record,'incremental_forced_equal':True,'changed_files':x['changed_files'],'retired_files':x['retired_files']})
 archive=subprocess.check_output(['git','archive',pin],cwd=BASE/project)
 with tarfile.open(fileobj=io.BytesIO(archive)) as t:
  for member in t:
   if not member.isfile() or member.name.startswith(('generated/','public/','runtime/','.nift/public/')):continue
   actual=WORK/project/member.name;expected=t.extractfile(member).read();assert actual.read_bytes()==expected,(project,member.name)
   fingerprints.append({'project':project,'path':member.name,'sha256':hashlib.sha256(expected).hexdigest()})
assert len(selected)==26 and len(allproofs)==29
(E/'selected-memory.json').write_text(json.dumps(selected,indent=2)+'\n')
(E/'restored-source-hashes.json').write_text(json.dumps(fingerprints,indent=2)+'\n')
(E/'completion.json').write_text(json.dumps({'published_cases':26,'original_harness_checks':29,'all_forced_equal':True,'restoration_passed':True,'maintained_source_files_verified':len(fingerprints),'completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope_exclusion':'Three original rendered HTML-only/uncoordinated metadata/history/provider probes are retained raw but not substituted for the published coordinated workloads.','rejected_attempt_excluded':True,'cloud_instances_created':0,'cloud_instances_deleted':0},indent=2)+'\n')
manifest={str(p.relative_to(E)):hashlib.sha256(p.read_bytes()).hexdigest() for p in E.rglob('*') if p.is_file() and p.name!='SHA256SUMS.json'}
(E/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2)+'\n');print('PASS: 26 published cases, 29 original forced gates, all source/output restoration, checksum manifest.')
