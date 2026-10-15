import json,statistics,hashlib,sys
from pathlib import Path
P=Path(sys.argv[1]);out=[]
def stats(rows):
 nums=sorted(x['wall_ms'] for x in rows);n=len(nums);r={'samples':n,'median_ms':statistics.median(nums),'min_ms':min(nums),'max_ms':max(nums),'median_peak_rss_kib':statistics.median(x['peak_rss_kib'] for x in rows) if all(x['peak_rss_kib'] is not None for x in rows) else None}
 for q in (.9,.95,.99):
  idx=(n-1)*q;lo=int(idx);r[f'p{int(q*100)}_ms']=nums[lo]+(nums[min(lo+1,n-1)]-nums[lo])*(idx-lo)
 return r
for file,counts in [('shell-repeated.json',(76,4900,228)),('shell-application-cold.json',(76,1680,228)),('shell-workloads.json',(141,1275,255))]:
 d=json.loads((P/file).read_text());assert d['publishable'];jobs=d['jobs'];assert len(jobs)==counts[0] and len({j['id'] for j in jobs})==len(jobs)
 measured=warm=0
 assert {j['shell'] for j in jobs}>={'bash','zsh','fish','nu','nift'}
 for j in jobs:
  rows=j['samples'];assert all(r['correct'] and ((r['exit_code']==0 and not r['timeout']) if r['exit_code'] is not None else r.get('metric')=='compiled-forkpty-to-first-prompt' and r['peak_rss_kib'] is None and 'SIGTERM' in r.get('teardown','')) for r in rows)
  a=[r for r in rows if not r['warmup']];b=[r for r in rows if r['warmup']];measured+=len(a);warm+=len(b);assert stats(a)==j['summary']
  assert len({r['round'] for r in rows})==len(rows)
  if file=='shell-workloads.json':
   assert len(a)==j['definition']['samples'] and len(b)==j['definition']['warmups'];assert 'source' not in j or hashlib.sha256(j['source'].encode()).hexdigest()==j['source_sha256']
 assert (len(jobs),measured,warm)==counts
 out.append({'file':file,'jobs':len(jobs),'measured':measured,'warmups':warm,'sha256':hashlib.sha256((P/file).read_bytes()).hexdigest()})
r={'pass':True,'checks':['complete planned counts','unique IDs/rounds','all sample correctness','independently recomputed distribution fields','bash/zsh/fish/nu/nift present','expanded source hashes'],'files':out,'measured':7855,'warmups':711}
(P.parent/'independent-audit.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
