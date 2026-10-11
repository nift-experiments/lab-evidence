import json,sys
from pathlib import Path
root=Path(sys.argv[1]);files=list((root/'definitions').glob('*.json'));assert files
for p in files:
 g=json.loads(p.read_text());assert set(g)=={'schema','tasks'} and g['schema']==1
 names=[t['id'] for t in g['tasks']];assert len(names)==len(set(names));seen=set()
 for t in g['tasks']:
  assert set(t)<= {'id','prerequisites','kind','input','output','receipt'} and {'id','prerequisites','kind','input','output'}<=set(t)
  assert t['kind'] in ['json','transform','check','compile','archive','tiny']
  assert isinstance(t['input'],str) and (t['output'] is None or isinstance(t['output'],str))
  assert len(t['prerequisites'])==len(set(t['prerequisites'])) and set(t['prerequisites'])<=seen
  seen.add(t['id'])
(root/'schema-validation.json').write_text(json.dumps({'all_passed':True,'definitions':len(files),'unique_task_identity':True,'topological_prerequisite_closure':True,'field_and_body_kind_validation':True},indent=2)+'\n')
print('Canonical graph definitions validated:',len(files))
