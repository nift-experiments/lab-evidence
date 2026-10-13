# Cross-benchmark subsystem signals — diagnostic draft

| Subsystem | Benchmarks | Evidence | Direction | Confidence |
|---|---|---|---|---|
| Call-argument staging / runtime dispatch | scripting | Paired same-node calls +145.76% large, +65.63% small; allocation slope9→17 per loop iteration; new evaluate_call_operand/form_call_arguments stacks; identical syscall counts | regression | Strong specimen-level result; root-cause commit not bisected |
| Collection sorting | scripting | Paired same-node large sort/index −30.71%;10/10 pairs faster, ranges nonoverlap | improvement | Strong tested-case result; do not generalize all sorting |
| BFS value/allocation paths | scripting | Paired large BFS +18.35%; allocations2,748,737→3,842,094 | suspected allocation contribution | Separate path investigation needed; not automatically same cause as calls |
| Frequency counting | scripting | Paired large +19.89%; allocation counts nearly identical | slower descriptive median | Allocation churn alone does not explain it |
| Template fresh-process RSS | template-engines | Idle supervisor allocation control adds64MiB to child'sreportedpeak | measurement boundary caveat | Confirmed floor; raw retained, floored memory unranked |
| Async/task retention | concurrency | Official audit complete; targeted same-node follow-up pending | unresolved | No release causal claim yet |

Other suites still collecting. No cross-benchmark shared root cause is inferred from similarly named operations. All practitioner findings are drafts and Labs stays unchanged.

| Website fresh-build path/filesystem probes | website-generator | Same-node freshfull+38.29%, syscallcount+73,389; profilesretained | regression | Confirmed testedboundary; rootcauseunproven |
| Prepared template loops | template-engines | Same-node10k fresh−54.91%, source-render−71.82% | improvement | Three-pair diagnostic, rangeswidelyseparated |
| Async queue | concurrency | Same-node100k4→4queue−67.04%;1kschedule change noisy | improvement inqueue | Three-pair diagnostic; no genericscheduler claim |
