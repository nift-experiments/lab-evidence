import json,hashlib,sys
from pathlib import Path
base=Path('/home/nick/Repositories/nift/nift-experiments/task-runners');sys.path.insert(0,str(base/'generators'));from workflow import graph
root=Path(sys.argv[1]);rows=[json.loads(x) for x in (root/'observations.jsonl').read_text().splitlines()];dest=root/'output-hashes';dest.mkdir();index={}
for row in rows:
 name="manifest-"+row["proof"]["output_manifest_sha256"]+".json";path=dest/name
 if path.exists():hashes=json.loads(path.read_text())
 else:
  tasks=graph(row['size'])['tasks']
  if row['tiny']:tasks=[{'id':f'tiny-{i:05}','prerequisites':[]} for i in range(row['size'])]
  by={t['id']:t for t in tasks};changed=set(row['mutation']['names']);memo={};hashes={}
  def output(n):
   if n in memo:return memo[n]
   v={'value':row['mutation']['value'] if n in changed else 1,'records':list(range(32))};own=(json.dumps(v,**({} if n in changed else {'indent':2}))+'\n').encode()
   if row['tiny']:
    h=14695981039346656037
    for b in own:h=((h^b)*1099511628211)%2**64
    result=(str(h)+'\n').encode()
   else:result=(json.dumps({'task':n,'digest':hashlib.sha256(b'\n'.join([own,*[output(p) for p in by[n]['prerequisites']]])).hexdigest()},sort_keys=True)+'\n').encode()
   memo[n]=result;hashes[n]=hashlib.sha256(result).hexdigest();return result
  for n in row['scope'] if row['scope'] is not None else by:output(n)
  path.write_text(json.dumps(hashes,sort_keys=True,indent=2)+'\n')
 assert hashlib.sha256(json.dumps(hashes,sort_keys=True).encode()).hexdigest()==row['proof']['output_manifest_sha256']
 index[row['id']]={'map':name,'observed_manifest_sha256':row['proof']['output_manifest_sha256']}
(dest/'index.json').write_text(json.dumps({'policy':'Per-output SHA maps independently reconstructed from frozen graph/mutations; each map cryptographically agrees with the original observed output-map digest. Identical cross-runner maps stored once.','observations':index},indent=2)+'\n')
print('Retained output maps:',len(list(dest.glob('manifest-*.json'))),'for',len(rows),'observations')
