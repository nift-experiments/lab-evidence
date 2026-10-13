#!/usr/bin/env python3
"""Additive, read-only refresh audit: sequence, rotation and retained summaries."""
import argparse,json,math,statistics,hashlib
from collections import defaultdict
from pathlib import Path

p=argparse.ArgumentParser();p.add_argument('directory',type=Path);p.add_argument('--local',action='store_true');args=p.parse_args();root=args.directory
plan=json.loads((root/'plan.json').read_text());rows=[json.loads(x) for x in (root/'observations.jsonl').read_text().splitlines()];summary=json.loads((root/'summary.json').read_text());identity=json.loads((root/'identity.json').read_text())
if not args.local:
 frozen=Path(__file__).with_name('task-frozen-plan.json');assert hashlib.sha256(frozen.read_bytes()).hexdigest()=='e3b10edf2ed2636a9035cc919027101e70edc5509d76185fa70ac577ecaa04ed'
 assert plan==json.loads(frozen.read_text())
 assert identity['candidate_sha']=='7f7e487c47a87e871dfef53345e2b71288008bff'
 assert identity['nift_binary_sha256']=='671e182ea31f3a23af92dadd738aba43edcb427670e7cf2f0d06b6362d28a606'
 assert identity['suite_sha']=='f37b63bd13cf71256607ba4652bcc911e270f94e' and not identity['suite_dirty']
 assert identity['affinity']==[0,1,2,3]
 assert len(plan)==31 and len(rows)==1527
 assert sum(c['samples'] for c in plan)*3==1434
expected=[]
for ci,c in enumerate(plan):
 for ri in range(c['samples']+1):
  order=['nift','turbo','nx'];offset=(ci+ri)%3;order=order[offset:]+order[:offset]
  for runner in order:expected.append((ci,c,ri,order,runner))
assert len(rows)==len(expected)
groups=defaultdict(list)
for index,(row,(ci,c,ri,order,runner)) in enumerate(zip(rows,expected),1):
 assert row['id']==f'{index:06}'
 assert row['cell_index']==ci and row['round']==ri and row['warmup']==(ri==0)
 assert row['runner']==runner and row['order']==order
 for field in ['tiny','size','jobs','case','samples']:assert row[field]==c[field]
 for field in ['wall_ms','cpu_ms','peak_rss_kib']:assert math.isfinite(row['metrics'][field]) and row['metrics'][field]>=0
 assert row['metrics']['wall_ms']>0 and row['metrics']['exit_code']==0
 if not row['warmup']:groups[tuple(row[k] for k in ['tiny','size','jobs','case','runner'])].append(row)
assert len(groups)==len(plan)*3==summary['cells']
assert summary['observations']==len(rows) and summary['measured']==sum(not r['warmup'] for r in rows) and summary['all_correct']
def percentile(values):
 values=sorted(values);pos=(len(values)-1)*.95;lo=int(pos);hi=min(lo+1,len(values)-1);return values[lo]+(values[hi]-values[lo])*(pos-lo)
seen=set()
for cell in summary['summary']:
 key=tuple(cell[k] for k in ['tiny','size','jobs','case','runner']);assert key not in seen;seen.add(key);observations=groups[key];assert cell['samples']==len(observations)
 for metric in ['wall_ms','cpu_ms','peak_rss_kib']:
  values=[row['metrics'][metric] for row in observations];wanted={'median':statistics.median(values),'min':min(values),'max':max(values),'p95':percentile(values) if len(values)>=20 else None}
  assert set(cell[metric])==set(wanted)
  for field,value in wanted.items():
   if value is None:assert cell[metric][field] is None
   else:assert math.isclose(cell[metric][field],value,rel_tol=1e-12,abs_tol=1e-9),(key,metric,field)
assert seen==set(groups)
print(json.dumps({'all_passed':True,'scope':'additional sequence/rotation/distribution audit; independent task/output/concurrency audit required separately','observations':len(rows),'measured':summary['measured'],'warmups':len(rows)-summary['measured'],'runner_cells':len(groups),'rotated_order_verified':True,'identity_verified':not args.local,'summary_metrics_recomputed':True,'no_outliers_removed':True},indent=2))
