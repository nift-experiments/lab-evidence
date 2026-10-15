import json,sys,statistics,hashlib,tarfile
from pathlib import Path
R=Path(sys.argv[1]);archive=tarfile.open(sys.argv[2]) if len(sys.argv)>2 else (tarfile.open(R.parent/'raw-artifacts.tar.gz') if (R.parent/'raw-artifacts.tar.gz').exists() else None)
manifest_count=0
d=json.loads((R/'raw.json').read_text());s=json.loads((R/'summary.json').read_text());new_obs=d['observations'];linked=d.get('linked_replay_observations',[]);obs=new_obs+linked;expected=120 if d.get('plan_version')==3 else (288 if d['host']=='a' else 48)
if d.get('plan_version')==3:assert len(new_obs)==107 and len(linked)==13
assert d['complete'] and d['all_correct'] and len(obs)==expected and len(d['jobs'])*6==expected
assert len({o['spec']['id'] for o in obs})==expected and d['suite_hashes']['current']==d['suite_hashes']['historical']
for row in s['rows']:
 a=[o for o in obs if o['spec']['job_id']==row['job_id']];assert len(a)==6 and {o['spec']['round'] for o in a}==set(range(6)) and sum(o['spec']['warmup'] for o in a)==1;a=[o for o in a if not o['spec']['warmup']];v=[o['wall_ms'] for o in a]
 assert row['samples']==5 and row['median_ms']==statistics.median(v) and row['min_ms']==min(v) and row['max_ms']==max(v)
 assert row['median_cpu_ms']==statistics.median(o['cpu_ms'] for o in a) and row['median_peak_rss_kib']==statistics.median(o['peak_rss_kib'] for o in a)
for o in obs:
 z=o['spec'];assert o['correct'] and o['exit_code']==0 and not o.get('timeout',False) and o['validation']=={'routes':10000,'content_checked':10000} and o['output']['files']==10000
 assert o['binary_sha256']==('7dd42dcee5ca4a6965f0823c0ae59198282da1eb77e0fcd4cae93a537870a6fb' if z['engine']=='Nift' else '8f6ddd98ff4a21a27b86530eb2e40d305673c26f72b1d57734ef68505cd28f89')
 assert o['suite_sha']==('a2890bc504cf7c55b77cd4fddae17403b7caf8ae' if z['harness']=='current' else '4947b42c863782ba6be0fdbbd2003d60d6d0d3d4')
 assert z['warmup']==(z['round']==0) and z['affinity']==([0] if z['phase']=='replay' else [0,1,2,3])
 if z['engine']=='Hugo':assert o['env_controls']['GOMAXPROCS']==(None if z['workers']=='default' else str(z['workers']))
 for label in ('input','output'):
  prefix='evidence' if o in linked else R.name
  f=R/'artifacts'/z['id']/(label+'-manifest.json')
  if f.exists() or archive is not None:
   m=json.loads(f.read_text()) if f.exists() else json.load(archive.extractfile(prefix+'/artifacts/'+z['id']+'/'+label+'-manifest.json'));manifest_count+=1;a=m['entries'];assert m['files']==len(a) and m['bytes']==sum(x['bytes'] for x in a) and m['tree_sha256']==hashlib.sha256(json.dumps(a,sort_keys=True).encode()).hexdigest();assert all(m[k]==o[label][k] for k in ('files','bytes','tree_sha256'))
for phase in d['phase_telemetry']:
 jobs=[j for j in d['jobs'] if j['phase']==phase]
 for t in range(6):
  skipped={o['spec']['job_id'] for o in linked if o['spec']['round']==t}
  assert [o['spec']['job_id'] for o in new_obs if o['spec']['phase']==phase and o['spec']['round']==t]==[j['job_id'] for j in jobs[t%len(jobs):]+jobs[:t%len(jobs)] if j['job_id'] not in skipped]
r={'pass':True,'host':d['host'],'observations_including_linked_replay':len(obs),'new_observations':len(new_obs),'linked_unchanged_replay':len(linked),'measured':sum(not o['spec']['warmup'] for o in obs),'warmups':sum(o['spec']['warmup'] for o in obs),'raw_sha256':hashlib.sha256((R/'raw.json').read_bytes()).hexdigest(),'artifact_manifests_checked':manifest_count,'checks':['fullcounts/sets','all10000outputcorrectness','fixedbinary/suiteidentity','declaredrotation/affinity/CPUcontrols','summarymedian/min/max/CPU/RSSrecomputed','retainedmanifestscheckedwhenpresent']};(R/'independent-audit.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
