import json,statistics,hashlib
from pathlib import Path
p=Path(__file__).parent
if not (p/'raw.json').exists():
 import sys;p=Path(sys.argv[1])
d=json.loads((p/'raw.json').read_text());s=json.loads((p/'summary.json').read_text());obs=d['observations']
assert d['complete'] and d['all_correct'] and len(obs)==48
assert sum(not x['warmup'] for x in obs)==40
assert d['versions']['old']['historical_binary_reproduced']
assert d['versions']['new']['source_sha']=='7f7e487c47a87e871dfef53345e2b71288008bff'
assert d['machine']['cpu_affinity']==[0]
for a,b in zip(obs[::2],obs[1::2]):assert (a['round'],a['case'])==(b['round'],b['case']) and {a['version'],b['version']}=={'old','new'}
for i,o in enumerate(obs):
 assert o['correct'] and o['exit_code']==0 and not o['timeout']
 assert o['validation']=={'routes':10000,'content_checked':10000}
 assert d['launch_order'][i]=={'sequence':i,'round':o['round'],'case':o['case'],'version':o['version']}
 if o['case'].startswith('incremental/'):assert o['full_rebuild_parity']
rows=[]
for c in d['cases']:
 r=next(x for x in s['rows'] if x['case']==c);v={}
 for k in ('old','new'):
  a=[x for x in obs if x['case']==c and x['version']==k];assert len(a)==6 and {x['round'] for x in a}==set(range(6));a=[x for x in a if not x['warmup']];assert len(a)==5
  nums=sorted(x['wall_ms'] for x in a);v[k]=nums
  expected={'samples':5,'median_ms':statistics.median(nums),'min_ms':min(nums),'max_ms':max(nums),'median_peak_rss_kib':statistics.median(x['peak_rss_kib'] for x in a)}
  for q in (.9,.95,.99):
   idx=4*q;lo=int(idx);expected[f'p{int(q*100)}_ms']=nums[lo]+(nums[min(lo+1,4)]-nums[lo])*(idx-lo)
  assert r[k]==expected,(r[k],expected)
 first=[x['version'] for x in obs[::2] if x['case']==c and not x['warmup']];assert sorted(first.count(k) for k in ('old','new'))==[2,3]
 delta=statistics.median(v['new'])-statistics.median(v['old']);assert r['delta_ms']==delta
 rows.append({'case':c,'delta_ms':delta,'percent_change':r['percent_change'],'ranges_disjoint':max(v['old'])<min(v['new']) or max(v['new'])<min(v['old'])})
result={'pass':True,'observations':48,'measured':40,'warmups':8,'checks':['all correctness/routes/content/parity','adjacent version pairs','3/2 first-order split','all statistics independently recomputed'],'raw_sha256':hashlib.sha256((p/'raw.json').read_bytes()).hexdigest(),'rows':rows}
(p/'independent-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
