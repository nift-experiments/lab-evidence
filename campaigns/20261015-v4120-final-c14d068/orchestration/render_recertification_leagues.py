from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
x=json.loads((root/'docs/INTERIM-RECERTIFICATION.json').read_text())
s='# Interim final-candidate recertification\n\nAudited official suites: '+', '.join(x['audited_official_suites'])+'. Exact-source three-way version diagnostics remain separate from current official peer results and historical cross-node trends. No publication or release is authorized.\n\n'
s+='## Best same-node wall improvements versus release — complete\n\n| Rank | Suite / scenario | Release | Original | Final | Unit | Improvement vs release | Recovery vs original | Samples/version |\n|---:|---|---:|---:|---:|---|---:|---:|---:|\n'
for i,a in enumerate(sorted(x['same_node_version_improvements'],key=lambda a:a['improvement_percent'],reverse=True),1):
 s+=f"| {i} | {a['suite']} / {a['scenario']} | {a['release']:.6f} | {a['original']:.6f} | {a['final']:.6f} | {a['unit']} | {a['improvement_percent']:.2f}% | {-a['final_vs_original_percent']:+.2f}% | {a['samples_each']} |\n"
s+='\n## Every measured positive same-node wall change — complete\n\n| Rank | Suite / scenario | Baseline | Baseline value | Final | Increase | Classification |\n|---:|---|---|---:|---:|---:|---|\n'
for i,a in enumerate(sorted(x['same_node_version_regressions'],key=lambda a:a['change_percent'],reverse=True),1):
 s+=f"| {i} | {a['suite']} / {a['scenario']} | {a['baseline']} | {a[a['baseline']]:.6f} | {a['final']:.6f} | {a['change_percent']:.2f}% | {a['classification']} |\n"
s+='\nEvery comparison above uses the same node, exact versions and frozen diagnostic boundaries. Template diagnostics have three measured observations/version and remain descriptive. Scripting has ten; final/release ranges overlap, and large calls are slower in eight of ten paired blocks. Overlapping ranges do not prove equality or eliminate a small regression. Major original call regressions have disjoint ranges and all ten final blocks faster. Near-flat changes are retained. Original/checkpoint and release baselines are explicitly distinguished.\n\n'
s+='## Current same-node peer wall deficits — complete\n\n| Rank | Suite / scenario / boundary | Nift | Best peer | Peer | Unit | Nift / peer |\n|---:|---|---:|---|---:|---|---:|\n'
for i,a in enumerate(sorted(x['current_same_node_wall_deficits'],key=lambda a:a['deficit'],reverse=True),1):
 nv=a.get('nift_value',a.get('nift_ms'));pv=a.get('best_peer_value',a.get('best_peer_ms'));s+=f"| {i} | {a['suite']} / {a['scenario']} | {nv:.4f} | {a['best_peer']} | {pv:.4f} | {a.get('unit','ms/invocation')} | {a['deficit']:.2f}× |\n"
s+='\n## Large gains but still behind\n\n| Scenario | Improvement vs release | Derived old deficit | Current official deficit | Verdict |\n|---|---:|---:|---:|---|\n'
for a in x['same_node_version_improvements']:
 for b in x['current_same_node_wall_deficits']:
  if a['suite']==b['suite'] and a['scenario']==b['scenario'] and a['improvement_percent']>=20:
   peer=b.get('best_peer_value',b.get('best_peer_ms'));s+=f"| {a['suite']} / {a['scenario']} | {a['improvement_percent']:.2f}% | {a['release']/peer:.2f}× | {b['deficit']:.2f}× | Still behind {b['best_peer']} |\n"
s+='\nDerived old deficits divide controlled old Nift diagnostic medians by the current official peer median on the same host and matching boundary. These are cross-phase diagnostics, not a simultaneously interleaved old-Nift/peer benchmark. Current deficits use official Nift/peer medians from the same cohort. No cross-node peer denominator is substituted.\n\n'
s+='## Memory and capabilities remain separate\n\n'+x.get('template_memory_control','Memory controls pending.')+'\n\nRaw scripting call peak-memory diagnostics are retained separately; small quantized differences do not establish a leak or superiority. Nift public parse-only/prepared-AST template modes remain unsupported in this frozen public-API matrix. Nift has lower medians than the best other template engine in 30 of 43 supported matching fresh/source-render cells; this is not an overall engine ranking. Practitioner judgments and the release recommendation remain pending the wider sweep.\n'
(root/'docs/INTERIM-RECERTIFICATION.md').write_text(s)
print(json.dumps({'improvements':len(x['same_node_version_improvements']),'positive_changes':len(x['same_node_version_regressions']),'peer_deficits':len(x['current_same_node_wall_deficits'])}))
