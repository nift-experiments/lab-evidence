#!/usr/bin/env python3
"""Independent diagnostic audit of plan/order/action/output and all statistics."""
import argparse,json,hashlib,statistics,math
from pathlib import Path
from collections import defaultdict
p=argparse.ArgumentParser();p.add_argument('directory',type=Path);a=p.parse_args();root=a.directory
identity=json.loads((root/'identity.json').read_text());assert identity['old_sha']=='635996b7ff5c725c81ac8ef57b1d146f7ceda642' and identity['candidate_sha']=='7f7e487c47a87e871dfef53345e2b71288008bff';assert identity['binaries']['candidate']['sha256']=='671e182ea31f3a23af92dadd738aba43edcb427670e7cf2f0d06b6362d28a606';assert identity['affinity']==[0,1,2,3];assert not any(v['status'] for v in identity['binaries'].values())
plan=json.loads((root/'plan.json').read_text());assert plan==identity['plan'];expected=[]
for gi,g in enumerate(plan):
 for ci,c in enumerate(g['cases']):
  for ri in range(c['samples']+c['warmups']):
   order=['old','candidate'];offset=(gi+ci+ri)%2;order=order[offset:]+order[:offset]
   for variant in order:expected.append((gi,ci,g,c,ri,order,variant))
rows=[json.loads(x) for x in (root/'observations.jsonl').read_text().splitlines()];assert len(rows)==len(expected)==120
manifests={}
for f in (root/'manifests').glob('*.json'):
 assert hashlib.sha256(f.read_bytes()).hexdigest()==f.stem
 v=json.loads(f.read_text());key=('tiny' if v.get('kind')=='tiny-action-microbenchmark' else 'native',v['size'],v.get('profile','light'),v['jobs']);assert key not in manifests;manifests[key]=v
 if key[0]=='tiny':
  for i in range(v['size']):assert v['input_sha256'][f'inputs/a{i:06}.txt']==hashlib.sha256(f'deterministic-{i}\n'.encode()).hexdigest()
groups=defaultdict(list);parity={};tiny_expected={}
for row,(gi,ci,g,c,ri,order,variant) in zip(rows,expected):
 assert row['graph_index']==gi and row['case_index']==ci and row['round']==ri and row['warmup']==(ri<c['warmups']);assert row['order']==order and row['variant']==variant and row['scenario']==c['name'] and row['passed']
 for k in ['kind','size','profile','jobs']:assert row[k]==g[k]
 assert row['command']==[('/opt/nift-build-prior/nift' if variant=='old' else '/opt/nift/nift'),'build']
 metric=row['metrics'];assert metric['exit_code']==0 and all(math.isfinite(metric[k]) and metric[k]>=0 for k in ['wall_ms','cpu_ms','peak_rss_kib']) and metric['wall_ms']>0
 graphkey=tuple(row[k] for k in ['kind','size','profile','jobs']);m=manifests[graphkey];data={}
 for field in ['action_trace','expected_actions','output_hashes']:
  f=root/row[field];assert f.resolve().is_relative_to(root.resolve());assert hashlib.sha256(f.read_bytes()).hexdigest()==row[field+'_sha256'];data[field]=json.loads(f.read_text())
 wanted=[] if c['name']=='noop' else sorted(x['id'] for x in m['actions']);assert sorted(data['action_trace'])==wanted and len(data['action_trace'])==len(set(data['action_trace'])) and data['expected_actions']==wanted
 assert set(data['output_hashes'])=={x['id'] for x in m['actions']};assert row['preconditions']['content_mutations_verified'] and row['preconditions']['timestamp_preconditions_verified'] and row['preconditions']['changed_inputs']==[]
 if row['kind']=='tiny':
  if graphkey not in tiny_expected:
   hashes={}
   for i in range(row['size']):
    value=1469598103934665603
    for b in f'deterministic-{i}\n'.encode():value=((value^b)*1099511628211)&((1<<64)-1)
    hashes[f'action/a{i:06}']=hashlib.sha256(f'{value:016x}\n'.encode()).hexdigest()
   tiny_expected[graphkey]=hashes
  assert data['output_hashes']==tiny_expected[graphkey]
 if graphkey in parity:assert parity[graphkey]==data['output_hashes']
 else:parity[graphkey]=data['output_hashes']
 if not row['warmup']:groups[tuple(row[k] for k in ['kind','size','profile','jobs','scenario','variant'])].append(row)
for i,row in enumerate(rows):assert row['index']==i
summary=json.loads((root/'summary.json').read_text());assert summary['observations']==120 and summary['measured']==110 and summary['warmups']==10 and summary['outliers_removed']==0 and len(summary['cohorts'])==6
for cell in summary['cohorts']:
 obs=groups[tuple(cell[k] for k in ['kind','size','profile','jobs','scenario','variant'])];assert len(obs)==cell['samples']
 for metric in ['wall_ms','cpu_ms','peak_rss_kib']:
  values=sorted(x['metrics'][metric] for x in obs);wanted={'median':statistics.median(values),'min':min(values),'max':max(values)}
  if len(values)>=20:
   pos=(len(values)-1)*.95;lo=int(pos);hi=math.ceil(pos);wanted['p95']=values[lo]+(values[hi]-values[lo])*(pos-lo)
  assert set(cell[metric])==set(wanted)
  for k,value in wanted.items():assert math.isclose(cell[metric][k],value,rel_tol=1e-12,abs_tol=1e-9)
print(json.dumps({'all_passed':True,'observations':120,'measured':110,'warmups':10,'variant_cells':6,'source_binary_identity_verified':True,'rotation_counts_verified':True,'actions_output_hashes_verified':True,'tiny_checksums_independently_reconstructed':True,'all_distributions_recomputed':True,'official_primary_modified':False},indent=2))
