import json,sys,statistics,hashlib
from pathlib import Path
p=Path(sys.argv[1]);d=json.loads((p/'raw.json').read_text());s=json.loads((p/'summary.json').read_text());obs=d['observations'];assert d['complete'] and d['all_correct'] and len(obs)==72
assert sum(not x['warmup'] for x in obs)==60;assert d['machine']['cpu_affinity']==[0]
for a,b in zip(obs[::2],obs[1::2]):assert (a['round'],a['case'])==(b['round'],b['case']) and {a['version'],b['version']}=={'old','new'}
assert all(x['correct'] and x['exit_code']==0 and not x['timeout'] for x in obs)
rows=[]
for row in s['rows']:
 c=row['case'];nums={}
 for k in ('old','new'):
  a=[x for x in obs if x['case']==c and x['version']==k];assert len(a)==12 and {x['round'] for x in a}==set(range(12));assert sum(x['warmup'] for x in a)==2;a=[x for x in a if not x['warmup']];n=sorted(x['wall_ms'] for x in a);nums[k]=n
  r={'samples':10,'median_ms':statistics.median(n),'min_ms':min(n),'max_ms':max(n),'median_peak_rss_kib':statistics.median(x['peak_rss_kib'] for x in a)}
  for q in (.9,.95,.99):
   idx=9*q;lo=int(idx);r[f'p{int(q*100)}_ms']=n[lo]+(n[min(lo+1,9)]-n[lo])*(idx-lo)
  assert r==row[k]
 first=[x for x in obs[::2] if x['case']==c and not x['warmup']];assert sum(x['version']=='old' for x in first)==5
 assert row['delta_ms']==statistics.median(nums['new'])-statistics.median(nums['old'])
 row['ranges_disjoint']=max(nums['old'])<min(nums['new']) or max(nums['new'])<min(nums['old']);row['paired_new_slower']=sum(next(x['wall_ms'] for x in obs if x['case']==c and x['version']=='new' and x['round']==t)>next(x['wall_ms'] for x in obs if x['case']==c and x['version']=='old' and x['round']==t) for t in range(2,12));rows.append(row)
r={'pass':True,'observations':72,'measured':60,'warmups':12,'raw_sha256':hashlib.sha256((p/'raw.json').read_bytes()).hexdigest(),'checks':['adjacent pairs','5/5 first ordering','complete counts/correctness','all statistics independently recomputed'],'rows':rows};(p/'independent-audit.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
