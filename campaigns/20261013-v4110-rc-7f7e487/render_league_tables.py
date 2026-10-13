"""Publication-independent league tables from retained audited datasets."""
import json,collections
from pathlib import Path
R=Path(__file__).resolve().parent;D=R/'docs';B=R.parents[1]/'benchmarks';SERIES=R.name
load=lambda p:json.loads(p.read_text())
synth=load(D/'INTERIM-DIAGNOSTIC-SYNTHESIS.json')
reg=[];wins=[]
for x in load(R/'scripting-regression-diagnostics/same-node/scripting-ab-diagnostic/independent-audit.json')['rows']:
 r=dict(benchmark='scripting',scenario=x['scenario'],old_ms=x['old_ms'],candidate_ms=x['new_ms'],change_pct=x['increase_pct'],basis='10 paired measured samples/version',confidence='10/10 pairs and disjoint ranges' if 'function-calls' in x['scenario'] or x['scenario']=='arrays-strings-hash/sort-index/large' else 'descriptive median; significance not established')
 (reg if r['change_pct']>0 else wins).append(r)
for x in load(R/'targeted-same-node-normalized.json'):
 r=dict(benchmark=x['benchmark'],scenario=x['scenario']+' / '+x['boundary'],old_ms=x['old_ms'],candidate_ms=x['candidate_ms'],change_pct=-x['improvement_pct'],basis=x['basis'],confidence='small paired diagnostic; descriptive')
 if 'schedule-1000' in x['scenario'] or (x['benchmark']=='template-engines' and x['scenario']=='article' and x['boundary']=='fresh'):continue
 (reg if r['change_pct']>0 else wins).append(r)
for x in load(R/'runtime-diagnostics/filesystem-automation/paired-ab/summary.json')['cases']:
 wins.append(dict(benchmark='filesystem-automation',scenario=x['case'],old_ms=x['median_ms']['prior'],candidate_ms=x['median_ms']['candidate'],change_pct=-x['candidate_percent_lower'],basis='3 paired measured samples/version;24 observations audited',confidence='large separated change; small diagnostic'))
for x in load(R/'shell-regression-diagnostics/same-node/shell-ab-diagnostic/independent-audit.json')['rows']:
 if x['case']=='traverse-100000':continue
 reg.append(dict(benchmark='shell',scenario=x['case'],old_ms=x['old']['median_ms'],candidate_ms=x['new']['median_ms'],change_pct=x['percent_change'],basis='10 paired measured samples/version',confidence='10/10 slower pairs; disjoint ranges'))
reg.sort(key=lambda x:x['change_pct'],reverse=True);wins.sort(key=lambda x:x['change_pct'])
now=load(R/'all-audited-current-wall.json');old=load(R/'all-audited-prior-wall.json')
for n in ('primary','filter'):
 now+=load(R/'runtime-readiness'/f'filesystem-{n}-normalized-wall.json');old+=load(R/'runtime-readiness'/f'filesystem-{n}-normalized-prior-wall.json')
key=lambda x:tuple(x[k] for k in ('benchmark','scenario','boundary','metric','unit','contract_sha256','cohort'))
groups=collections.defaultdict(list);og=collections.defaultdict(list)
for x in now:groups[key(x)].append(x)
for x in old:og[key(x)].append(x)
gaps=[];trends=[]
for k,xs in groups.items():
 ns=[x for x in xs if x['engine']=='nift'];ps=[x for x in xs if x['engine']!='nift']
 if not ns:continue
 n=ns[0];on=[x for x in og[k] if x['engine']=='nift'];op=[x for x in og[k] if x['engine']!='nift']
 if on:trends.append(dict(benchmark=n['benchmark'],scenario=n['scenario'],boundary=n['boundary'],unit=n['unit'],old=on[0]['value'],candidate=n['value'],change_pct=100*(n['value']/on[0]['value']-1),basis='cross-node trend only'))
 if ps:
  p=min(ps,key=lambda x:x['value']);gaps.append(dict(benchmark=n['benchmark'],scenario=n['scenario'],boundary=n['boundary'],unit=n['unit'],nift=n['value'],peer=p['engine'],peer_value=p['value'],deficit=n['value']/p['value'],previous_deficit=on[0]['value']/min(x['value'] for x in op) if on and op else None))
for x in load(D/'SHELL-COMPETITIVE-GAPS.json'):gaps.append(dict(benchmark='shell',scenario=x['scenario'],boundary=x['boundary'],unit='ms',nift=x['nift_ms'],peer=x['peer'],peer_value=x['peer_ms'],deficit=x['deficit'],previous_deficit=None))
web=B/'website-generator'/SERIES/'official-refresh'
for size in (100,1000,10000):
 summary=load(web/f'website-{size}-summary.json');wg=collections.defaultdict(list)
 for name,x in summary.items():engine,scenario=name.split('/',1);wg[scenario].append((engine,x))
 for scenario,xs in wg.items():
  ns=[x for e,x in xs if e=='Nift'];ps=[(e,x) for e,x in xs if e!='Nift']
  if not ns or not ps:continue
  peer,p=min(ps,key=lambda ex:ex[1]['median_ms']);n=ns[0];gaps.append(dict(benchmark='website-generator',scenario=f'{size}pages/{scenario}',boundary='official fresh fixture or reused warm fixture as defined',unit='ms',nift=n['median_ms'],peer=peer,peer_value=p['median_ms'],deficit=n['median_ms']/p['median_ms'],previous_deficit=None))
gaps.sort(key=lambda x:x['deficit'],reverse=True)
text=['# Diagnostic league tables — seven closed suites','','All rows derive from retained audited evidence. Build is audited/collected but its diagnostic closeout is pending; it will be incorporated when ready. Same-node measured direction does not imply a population significance test. Weak/near-flat controls are separately noted, not promoted to established changes.','','## Confirmed regressions — worst first','','Same-node version observations, with confidence stated per row. Cross-node trends are excluded.','','| Rank | Benchmark / scenario | Old ms | Candidate ms | Regression | Basis / confidence |','|---:|---|---:|---:|---:|---|']
for i,x in enumerate(reg,1):text.append(f"| {i} | {x['benchmark']} / {x['scenario']} | {x['old_ms']:.3f} | {x['candidate_ms']:.3f} | +{x['change_pct']:.2f}% | {x['basis']}; {x['confidence']} |")
text+=['','## Confirmed improvements — best first','','Same-node measured improvements; small/overlapping changes retain descriptive qualifications.','','| Rank | Benchmark / scenario | Old ms | Candidate ms | Improvement | Basis / confidence |','|---:|---|---:|---:|---:|---|']
for i,x in enumerate(wins,1):text.append(f"| {i} | {x['benchmark']} / {x['scenario']} | {x['old_ms']:.3f} | {x['candidate_ms']:.3f} | {-x['change_pct']:.2f}% | {x['basis']}; {x['confidence']} |")
text+=['','## Largest remaining competitive deficits — worst first','','Official current-candidate vs fastest valid same-node peer. Different workload/clock/implementation boundaries remain visible; no global language score. Shell external-baseline is separately retained and excluded here. Values below1 are included so strong categories are not hidden.','','| Rank | Benchmark / scenario | Boundary | Nift | Peer | Peer value | Multiple | Previous multiple |','|---:|---|---|---:|---|---:|---:|---:|']
for i,x in enumerate(gaps,1):
 prev=f"{x['previous_deficit']:.2f}× cross-node" if x['previous_deficit'] else 'not normalized'
 text.append(f"| {i} | {x['benchmark']} / {x['scenario']} | {x['boundary']} | {x['nift']:.3f} {x['unit']} | {x['peer']} | {x['peer_value']:.3f} | {x['deficit']:.2f}× | {prev} |")
text+=['','## Improved substantially but still uncompetitive','','| Scenario | Same-node improvement | Official current deficit | Interpretation |','|---|---:|---:|---|','| Filesystem stat10k | 91.01% | 3.87× Bun | Huge gain; still behind |','| Filesystem walk10k | 85.52% | 6.98× Bun | Huge gain; materially behind |','| Concurrency queue100k4→4 | 67.04% | 208.76× Bun | Massive gain; still severe |','| Template loop10k source-render | 71.82% | 15.35× Handlebars | Major gain; hot rendering still uncompetitive |','','## New regression on top of an old weakness','','| Scenario | Same-node regression | Official peer deficit | Evidence |','|---|---:|---:|---|','| Scripting calls large | 145.76% | 289.09× LuaJIT | Disjoint ranges;10/10 slower |','| Shell calls | 119.68% | see shell official boundary | Independent suite corroborates call-path slowdown |','','Call/source/value staging is an evidence-supported lead; no shared causal commit proved. Website freshfull38.29% is a separate central-product release blocker.','','## Historical cross-node trends — separate ranking','','| Rank | Benchmark / scenario / boundary | Old | Candidate | Change | Unit |','|---:|---|---:|---:|---:|---|']
for i,x in enumerate(sorted(trends,key=lambda x:x['change_pct'],reverse=True),1):text.append(f"| {i} | {x['benchmark']} / {x['scenario']} / {x['boundary']} | {x['old']:.3f} | {x['candidate']:.3f} | {x['change_pct']:+.2f}% | {x['unit']} |")
text+=['','Task gains13.83–33.46% remain here only. No causal version percentage is established from historical cross-node movement.','','## Memory and capabilities — separate','','Held1k tasks:143.625MiB Nift/5.375MiB Go=26.72×; prior143.5MiB, old weakness unchanged. Template/filesystem inherited wait4 supervisor floors are unranked. Task maximum-childRSS leads31/31 configurations; not aggregate-treeRSS. NativeSHA256/statmtime/recursive removal, prepared-template artifacts, public channels/cancellation, outputless tracked nodes/env invalidation/cache restoration/ensure/-j/structured graph remain major separate capability gaps. Exactly-once inlinefilesystem reproducer now passes; do not infer universal bug absence.','','## Core priorities','','Release blockers:1)call regression corroborated by scripting/shell;2)freshwebsite full-build regression. Preserve filesystem metadata/traversal/filter gains, template loops, queue throughput and sorting. Old pathological weaknesses:retained-runtime growth, task creation/retention, blockingwaits, scalarCPU, bulkfilesystem checksum/mirror policy, preparedreuse. Priorities depend on product centrality and changed preferences, not raw percentage alone.','','Near-flat controls excluded from established-change tables:concurrency schedule1k, templatefresharticle, shelltraversal. Persistent reuse degradation is an old weakness, not a confirmed new regression. No new public capability was established beyond the certified exactly-once reproducer behavior. Labs unchanged; no release recommendation.']
(D/'DIAGNOSTIC-LEAGUE-TABLES.md').write_text('\n'.join(text)+'\n')
(D/'DIAGNOSTIC-LEAGUE-TABLES.json').write_text(json.dumps({'scope':'seven closed suites; build diagnostic pending','regressions':reg,'improvements':wins,'wall_deficits':gaps,'cross_node_trends':trends,'memory':'separate validated scopes only; floor metrics unranked','capabilities':'separate from timing rankings'},indent=2)+'\n')
print(json.dumps({'regressions':len(reg),'improvements':len(wins),'official_peer_cells':len(gaps),'cross_node_trends':len(trends)}))

# Make the three complete rankings the top-level synthesis, not scattered excerpts.
main=D/'INTERIM-DIAGNOSTIC-SYNTHESIS.md'
details=D/'INTERIM-DIAGNOSTIC-DETAILS.md'
if not details.exists():details.write_text(main.read_text())
main.write_text((D/'DIAGNOSTIC-LEAGUE-TABLES.md').read_text()+'\n'+(D/'CROSS-BENCHMARK-PREFERENCES.md').read_text()+'\n'+(D/'CROSS-BENCHMARK-PRODUCT-PRIORITIES.md').read_text()+'\nDetailed subsystem discussion is retained in INTERIM-DIAGNOSTIC-DETAILS.md.\n')
synth['league_tables']=load(D/'DIAGNOSTIC-LEAGUE-TABLES.json')
(D/'INTERIM-DIAGNOSTIC-SYNTHESIS.json').write_text(json.dumps(synth,indent=2)+'\n')
