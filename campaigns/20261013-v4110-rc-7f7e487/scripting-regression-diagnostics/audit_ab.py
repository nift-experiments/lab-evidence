"""Independent audit of the separate paired diagnostic, not official evidence."""
import argparse,collections,hashlib,json,statistics
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('directory',type=Path);args=p.parse_args();root=args.directory
raw=json.loads((root/'raw.json').read_text());summary=json.loads((root/'summary.json').read_text())
assert raw['complete'] and raw['all_correct'] and summary['complete'] and summary['all_correct']
assert raw['candidate_sha']=='7f7e487c47a87e871dfef53345e2b71288008bff'
assert raw['prior_sha']=='2eaec7d70e9ce2e698d0ba23a605fb9cf85317ff'
assert raw['machine']['cpu_affinity']==[0]
obs=raw['observations'];assert len(obs)==720
cases={x['case'] for x in obs};assert len(cases)==30
assert len(raw['launch_order'])==720
for i,(a,b) in enumerate(zip(obs,raw['launch_order'])):
 assert (a['case'],a['version'],a['round'])==(b['case'],b['version'],b['round']) and b['sequence']==i
 assert a['correct'] and a['exit_code']==0 and not a['timeout']
 assert a['warmup']==(a['round']<2)
for i in range(0,720,2):
 a,b=obs[i:i+2];assert a['case']==b['case'] and a['round']==b['round'] and {a['version'],b['version']}=={'old','new'}
rows=[];reported={x['case']:x for x in summary['rows']};assert set(reported)==cases
for case in sorted(cases):
 result={'scenario':case.removesuffix('/nift')}
 for version in ('old','new'):
  cells=[x for x in obs if x['case']==case and x['version']==version];assert len(cells)==12 and {x['round'] for x in cells}==set(range(12))
  measured=[x for x in cells if not x['warmup']];assert len(measured)==10
  assert len({x['source_sha256'] for x in cells})==len({x['oracle_sha256'] for x in cells})==1
  med=statistics.median(x['wall_ms'] for x in measured);assert abs(reported[case][version]['median_ms']-med)<1e-9
  result[version+'_ms']=med
 first=[obs[i]['version'] for i in range(0,720,2) if obs[i]['case']==case and not obs[i]['warmup']];assert collections.Counter(first)=={'old':5,'new':5}
 result['delta_ms']=result['new_ms']-result['old_ms'];result['increase_pct']=100*(result['new_ms']/result['old_ms']-1)
 assert abs(reported[case]['percent_change']-result['increase_pct'])<1e-9
 rows.append(result)
rows.sort(key=lambda x:x['increase_pct'],reverse=True)
receipt={'kind':'independent diagnostic A/B audit','passed':True,'observations':720,'measured':600,'warmups':120,'cases':30,'balanced_first_order':True,'raw_sha256':hashlib.sha256((root/'raw.json').read_bytes()).hexdigest(),'rows':rows,'interpretation':'Separate same-node diagnostic; descriptive medians, no significance claim or universal noise cutoff. Review paired samples and tails before calling near-flat values regressions.'}
(root/'independent-audit.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'pass':True,'cases':30,'worst10':rows[:10]},indent=2))
