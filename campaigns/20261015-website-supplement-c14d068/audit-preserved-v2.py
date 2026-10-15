import json,sys,hashlib,tarfile
from pathlib import Path
P=Path(sys.argv[1]);archive=tarfile.open(sys.argv[2]);old=json.loads((P/'evidence/raw.json').read_text());boundary=json.loads((P/'evidence/scope-change-boundary.json').read_text());a=old['observations']+boundary['completed_uncheckpointed_observations'];assert len(old['observations'])==120 and len(a)==121 and len({o['spec']['id'] for o in a})==121
assert hashlib.sha256((P/'evidence/raw.json').read_bytes()).hexdigest()=='268a265c05dd2d2c8ade04ce57bdac3486923ca43a7f4b9415040291a91a0756'
checks=0
for o in a:
 assert o['correct'] and o['exit_code']==0 and o['validation']=={'routes':10000,'content_checked':10000}
 for label in ('input','output'):
  m=json.load(archive.extractfile('evidence/artifacts/'+o['spec']['id']+'/'+label+'-manifest.json'));rows=m['entries'];assert m['files']==len(rows) and m['bytes']==sum(x['bytes'] for x in rows) and m['tree_sha256']==hashlib.sha256(json.dumps(rows,sort_keys=True).encode()).hexdigest();assert all(m[k]==o[label][k] for k in ('files','bytes','tree_sha256'));checks+=1
new=json.loads((P/'evidence-v3/raw.json').read_text());ids={o['spec']['id']:o for o in a}
assert all(o==ids[o['spec']['id']] for o in new['linked_replay_observations'])
r={'pass':True,'reason':'user-amended scope, original incomplete plan retained without relabeling it complete','checkpointed':120,'completed_uncheckpointed':1,'unique_retained':121,'measured':sum(not o['spec']['warmup'] for o in a),'warmups':sum(o['spec']['warmup'] for o in a),'manifest_checks':checks,'linked_replay_exact_byte_equivalent_objects':13};(P/'preserved-v2-independent-audit.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
