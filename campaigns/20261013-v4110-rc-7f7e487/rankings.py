"""Rank audited normalized suite exports; never merge raw measurements across hosts.
Input rows: benchmark, scenario, boundary, metric, unit, contract_sha256,
series, engine, value, audit_pass, evidence, cohort. Previous rows use same schema.
metric = wall_time|memory|throughput. cohort distinguishes diagnostics/distributions.
"""
from pathlib import Path
import json,sys,collections,math
ROOT=Path(__file__).resolve().parent

def load(path):
 rows=json.loads(Path(path).read_text());assert isinstance(rows,list)
 for r in rows:
  assert r['audit_pass'] is True and r['evidence']
  assert r['metric'] in ['wall_time','memory','throughput'] and len(r['contract_sha256'])==64
  assert isinstance(r['value'],(int,float)) and math.isfinite(r['value']) and r['value']>0
  assert r['cohort'] and r['unit'] and r['boundary']
 return rows

def key(r):return tuple(r[x] for x in ['benchmark','scenario','boundary','metric','unit','contract_sha256','cohort'])
def render(title,data,value):
 text='# '+title+'\n\nAudited suite exports only. Time, memory and throughput are ranked separately. Historical changes are cross-node trends, not controlled same-machine A/B. Percentages are descriptive. Capability gaps and product priorities require separate explicit assessments.\n'
 for metric in ['wall_time','memory','throughput']:
  text+='\n## '+metric.replace('_',' ').title()+'\n\n| Rank | Benchmark / scenario / boundary | '+value+' | Evidence |\n|---:|---|---:|---|\n'
  for i,r in enumerate(data[metric],1):text+=f'| {i} | {r["benchmark"]} / {r["scenario"]} / {r["boundary"]} | {r["rank_value"]:.2f} | [source]({r["evidence"]}) |\n'
 return text

def main(current,previous):
 now=load(current);old=load(previous);prior={key(r):r for r in old if r['engine']=='nift'};groups=collections.defaultdict(list)
 for r in now:groups[key(r)].append(r)
 improvements={m:[] for m in ['wall_time','memory','throughput']};regressions={m:[] for m in improvements};gaps={m:[] for m in improvements}
 for k,rows in groups.items():
  n=[r for r in rows if r['engine']=='nift'];assert len(n)<=1,'Duplicate Nift normalized identity'
  if not n:continue
  n=n[0];metric=n['metric'];higher=metric=='throughput';peers=[r for r in rows if r['engine']!='nift']
  if peers:
   best=(max if higher else min)(peers,key=lambda r:r['value']);multiple=best['value']/n['value'] if higher else n['value']/best['value']
   severity='severe' if multiple>10 else 'significant' if multiple>=3 else 'moderate' if multiple>=1.5 else 'competitive'
   gaps[metric].append(dict(n,peer=best['engine'],peer_value=best['value'],rank_value=multiple,severity=severity,statistical_significance_claim=False))
  if k in prior:
   p=prior[k];pct=(n['value']-p['value'])/p['value']*100 if higher else (p['value']-n['value'])/p['value']*100
   r=dict(n,previous_value=p['value'],previous_evidence=p['evidence'],rank_value=abs(pct),improvement_percent=pct,comparison='cross-node trend, not a controlled same-machine A/B')
   if pct>0:improvements[metric].append(r)
   elif pct<0:regressions[metric].append(r)
 for data in [improvements,regressions,gaps]:
  for m in data:data[m].sort(key=lambda r:r['rank_value'],reverse=True)
 doc=ROOT/'docs';doc.mkdir(exist_ok=True)
 (doc/'CROSS-BENCHMARK-IMPROVEMENTS.json').write_text(json.dumps({'status':'accepted exports ranked','formula_lower':'(old-new)/old*100','formula_throughput':'(new-old)/old*100','improvements':improvements,'regressions':regressions},indent=2)+'\n')
 (doc/'CROSS-BENCHMARK-IMPROVEMENTS.md').write_text(render('Nift old-to-new improvements',improvements,'Improvement %')+'\n'+render('Regressions',regressions,'Degradation %'))
 (doc/'CROSS-BENCHMARK-GAPS.json').write_text(json.dumps({'status':'accepted exports ranked','formula_lower':'Nift/best valid peer','formula_throughput':'best valid peer/Nift','rankings':gaps,'product_priority':'pending separately reasoned ranking','capabilities':'pending separately ordered practical-impact assessment'},indent=2)+'\n')
 (doc/'CROSS-BENCHMARK-GAPS.md').write_text(render('Current competitive gaps',gaps,'Deficit multiple'))
if __name__=='__main__':main(*sys.argv[1:])
