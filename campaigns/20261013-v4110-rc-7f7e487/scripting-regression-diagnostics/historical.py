import json, statistics
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE=ROOT/'benchmarks/scripting'
old=json.loads((BASE/'20261010-v4100/scripting.json').read_text())
new=json.loads((BASE/'20261013-v4110-rc-7f7e487/official-refresh/scripting.json').read_text())
a={j['id']:j for j in old['jobs']};b={j['id']:j for j in new['jobs']}
def median(j): return statistics.median(s['wall_ms'] for s in j['samples'] if not s['warmup'])
def group(s):
 if 'noop' in s or 'output' in s or 'cold-start' in s: return 'startup-sensitive'
 if 'function-calls' in s: return 'function/call overhead'
 if s.startswith('structured-data/'): return 'JSON/data processing'
 if s.startswith('filesystem/'): return 'filesystem traversal'
 if s.startswith('arrays-strings-hash/'): return 'collection/sort'
 return 'scalar compute / algorithm (inspect workload)'
rows=[]
for key,j in a.items():
 if not key.endswith('/nift') or key not in b: continue
 assert j['source_sha256']==b[key]['source_sha256'] and j['oracle_sha256']==b[key]['oracle_sha256']
 scenario=key.rsplit('/',1)[0];ratio=median(b[key])/median(j);peers=[]
 for pk,pj in a.items():
  if pk.rsplit('/',1)[0]!=scenario or pk.endswith('/nift') or pk not in b:continue
  if pj['source_sha256']!=b[pk]['source_sha256'] or pj['oracle_sha256']!=b[pk]['oracle_sha256']:continue
  pr=median(b[pk])/median(pj)
  peers.append({'engine':pk.rsplit('/',1)[1],'old_ms':median(pj),'new_ms':median(b[pk]),'ratio':pr,'increase_pct':100*(pr-1),'nift_ratio_over_peer_ratio':ratio/pr,'binary_hash_equal':old['tools'][pk.rsplit('/',1)[1]].get('sha256')==new['tools'][pk.rsplit('/',1)[1]].get('sha256')})
 rows.append({'scenario':scenario,'category':group(scenario),'old_ms':median(j),'new_ms':median(b[key]),'increase_pct':100*(ratio-1),'delta_ms':median(b[key])-median(j),'ratio':ratio,'peers':peers,'nift_ratio_over_median_peer_ratio':ratio/statistics.median(p['ratio'] for p in peers) if peers else None})
rows.sort(key=lambda x:x['increase_pct'],reverse=True)
assert len(rows)==30
(HERE/'historical-peer-movement.json').write_text(json.dumps({'scope':'Cross-node diagnostic, not causal attribution or official normalized metric; peer ratios are scenario-specific descriptive controls, not corrections. Binary/version and host differences remain confounders.','rows':rows},indent=2)+'\n')
lines=['# Historical scripting regression diagnostic','','All 30 matched Nift medians increased. These are cross-node comparisons; peer-normalized ratios are descriptive diagnostics, not corrected benchmark results. Same-node A/B is pending.','','| Scenario | Category | Old ms | New ms | Increase | Nift ratio / median peer ratio |','|---|---|---:|---:|---:|---:|']
for r in rows:lines.append(f"| {r['scenario']} | {r['category']} | {r['old_ms']:.3f} | {r['new_ms']:.3f} | {r['increase_pct']:.2f}% | {r['nift_ratio_over_median_peer_ratio']:.3f} |")
(HERE/'HISTORICAL.md').write_text('\n'.join(lines)+'\n')
for r in rows[:10]:print(r['scenario'],round(r['increase_pct'],2),round(r['nift_ratio_over_median_peer_ratio'],3))
