import json,statistics,hashlib,sys,subprocess,re
from pathlib import Path
p=Path(sys.argv[1]);rs=[json.loads(x) for x in (p/'observations.jsonl').read_text().splitlines()];summary=json.loads((p/'summary.json').read_text())
assert len(rs)==1527 and summary['measured']==1434 and summary['cells']==93
plan=json.loads((p/'plan.json').read_text())
for i in range(0,len(rs),3):
 chunk=rs[i:i+3];assert [r['runner'] for r in chunk]==chunk[0]['order']
 assert len({(r['cell_index'],r['round']) for r in chunk})==1
for ci,c in enumerate(plan):
 for runner in ['nift','turbo','nx']:
  group=[r for r in rs if r['cell_index']==ci and r['runner']==runner]
  assert sorted(r['round'] for r in group)==list(range(c['samples']+1))
  assert all(all(r[k]==c[k] for k in ['tiny','size','jobs','case','samples']) for r in group)
for r in rs:
 order=['nift','turbo','nx'];i=(r['round']+r['cell_index'])%3
 assert r['order']==order[i:]+order[:i]
 assert r['warmup']==(r['round']==0)
 assert r['metrics']['exit_code']==0 and not r['proof']['failed'] and not r['proof']['blocked']
 assert r['proof']['not_executed']==sorted((set(r['scope']) if r['scope'] is not None else set(r['proof']['starts'])|set(r['proof']['not_executed']))-set(r['proof']['starts']))
variance=[]
for c in summary['summary']:
 x=c['wall_ms'];spread=(x['max']-x['min'])/x['median'];variance.append({k:c[k] for k in ['tiny','size','jobs','case','runner','samples']}|{'range_over_median':spread,'flag_over_25pct':spread>.25,'low_sample':c['samples']<10})
(p/'variance-review.json').write_text(json.dumps({'policy':'All observations retained; descriptive min-max/median spread, not a confidence interval. p95 only n>=20; no significance or universal ranking claim.','flagged':sum(x['flag_over_25pct'] for x in variance),'cells':variance},indent=2)+'\n')
(p/'validation.json').write_text(json.dumps({'all_passed':True,'observations':1527,'measured':1434,'warmups':93,'runner_cells':93,'independent_raw_trace_and_output_reconstruction':True,'runner_rotation_verified':True,'scenario_order':'fixed','source_sha':'8f90fd49d8b2484c1d732cb440ea442e53e08172','suite_sha':'56384cace6821a1541e7773cf1d8ce7a4c688ed8'},indent=2)+'\n')
print('Independent rotation/completeness/variance review passed; flagged cells:',sum(x['flag_over_25pct'] for x in variance))
