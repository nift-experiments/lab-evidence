import sys,json,statistics,hashlib,itertools
from pathlib import Path
p=Path(sys.argv[1]);d=json.loads((p/'raw.json').read_text());s=json.loads((p/'summary.json').read_text());obs=d['observations'];assert d['complete'] and d['all_correct'];n=d['samples'];w=d['warmups'];assert len(obs)==len(d['cases'])*3*(n+w)
assert d['machine']['cpu_affinity']==[0];assert all(o['correct'] and o['exit_code']==0 and not o['timeout'] for o in obs)
for i in range(0,len(obs),3):
 block=obs[i:i+3];assert len({(o['case'],o['round']) for o in block})==1 and {o['version'] for o in block}==set(d['versions'])
for row in s['rows']:
 for k in d['versions']:
  allrows=[o for o in obs if o['case']==row['case'] and o['version']==k];assert len(allrows)==n+w and {o['round'] for o in allrows}==set(range(n+w));assert sum(o['warmup'] for o in allrows)==w
  rows=[o for o in allrows if not o['warmup']];a=sorted(o['wall_ms'] for o in rows);r={'samples':n,'median_ms':statistics.median(a),'min_ms':min(a),'max_ms':max(a),'median_peak_rss_kib':statistics.median(o['peak_rss_kib'] for o in rows)}
  for q in (.9,.95,.99):
   idx=(n-1)*q;lo=int(idx);r[f'p{int(q*100)}_ms']=a[lo]+(a[min(lo+1,n-1)]-a[lo])*(idx-lo)
  assert row[k]==r
 for against in ('release','original'):assert row[f'final_vs_{against}_percent']==100*(row['final']['median_ms']/row[against]['median_ms']-1)
perms=list(itertools.permutations(d['versions']))
for i in range(0,len(obs),3):
 block=obs[i:i+3];o=block[0];index=d['cases'].index(o['case']);turn=o['round'];expected=perms[((turn-w if turn>=w else turn)+index)%6];assert tuple(x['version'] for x in block)==expected
result={'pass':True,'observations':len(obs),'measured':sum(not o['warmup'] for o in obs),'warmups':sum(o['warmup'] for o in obs),'raw_sha256':hashlib.sha256((p/'raw.json').read_bytes()).hexdigest(),'checks':['complete sets/counts','three-version adjacent blocks','exact six-permutation schedule','correctness','all distributions and recovery ratios independently recomputed']};(p/'independent-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
