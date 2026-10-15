# Website ratio reconciliation

The official final10k fresh comparison is Nift3015.980494ms / Hugo2623.337268ms =1.149673×. The2951.495366ms Nift result belongs to a separate exact-source Nift-only version diagnostic; no Hugo was measured in that diagnostic. Mixing its numerator into the official peer denominator would create a cross-phase ratio.

## Historical versus final official evidence

All times are median milliseconds; ratio=Nift/Hugo. Missing Hugo rows were not measured and cannot be treated as zero or equivalent operations.

| Scenario | Historical Nift | Historical Hugo | Old ratio | Final Nift | Current Hugo | Current ratio |
|---|---:|---:|---:|---:|---:|---:|
| Fresh full | 3853.309 | 5005.257 | 0.770 | 3015.980 | 2623.337 | 1.150 |
| Warm full | 6516.465 | 6455.239 | 1.009 | 2613.877 | 2723.813 | 0.960 |
| Unchanged/no-op | 1287.937 | Not measured | Not measured | 842.446 | Not measured | Not measured |
| One-page incremental | 1255.111 | Not measured | Not measured | 858.452 | Not measured | Not measured |
| Targeted changed leaf (separate supplemental cohort) | 188.069 | Not measured | Not measured | 151.855 | Not measured | Not measured |

## Identity and comparability

Historical Nift4.7.2 core495012966756c9d2910a714c453359c8ff60bab1, CLIa1654dbf879bf0517141612fbcdb55f441e5e60009a5954faaa274bfa6868bf2; final exactc14d068, CLI7dd42dcee5ca4a6965f0823c0ae59198282da1eb77e0fcd4cae93a537870a6fb. Hugo0.167.0 and binary8f6ddd98ff4a21a27b86530eb2e40d305673c26f72b1d57734ef68505cd28f89 are identical across historical/original/final.

Primary historical node EPYC7601; current EPYC7642. Targeted historical supplement used a separate EPYC7542 node and cannot be pooled with the historical primary corpus series. Current supplemental target series is a separate serial cohort on the current host. Same Ubuntu24.04 family, schema5, five measured plus one warmup, CPU0, Nift buildthreads1, HugoGOMAXPROCS1. Primary campaign.py, benchmark.py and campaign_measure.py have no source changes between frozen historical/current suite revisions; no identified primary corpus/timer definition change. This does not make different hosts a controlled version experiment.

Fresh means a new generated minimal-page fixture, with prepared shared dependencies/cache; not dropped OS page caches. Warm full removes output while retaining internal build state. No-op and changed-leaf incremental scan the Nift project. Targeted invokes the explicit changed leaf, validates full output and untouched pages. Hugo incremental/target equivalents are absent in this accepted matrix. Do not compare Nift targeted to Hugo full and label it like-for-like.

## What changed and what we can conclude

Historical10k Nift3853.309/Hugo5005.257 means Nift/Hugo0.769853: Hugo took1.29895× Nift time, not2×. Historical1000 fresh had Hugo/Nift1.5734× and100 had3.8709×. These canonical files do not identify the remembered2× series; it must not be invented.

Cross-node historical→final fresh Nift improved21.73%, while Hugo improved47.59%. Both got faster; Hugo improved more, reversing the observed ratio. Hugo did not change version or binary. Host/environment sensitivity is plausible, but the precise causal split cannot be established from cross-node measurements.

The controlled current-node Nift-only diagnostic is release2871.544599→original3278.509241→final2951.495366ms. Final is9.97% faster than original and2.78% slower than release, with overlapping release/final ranges. This supports near-release recovery, not a halving of Nift performance.

Current official10k fresh: Hugo2623.337ms versus Nift3015.980ms, Nift14.97% more time. Current10k warm full: Nift2613.877ms versus Hugo2723.813ms, Nift4.04% less time. At100pages Nift wins both fresh and warm; at1000 it loses fresh by8.32% and wins warm by11.51%. No universal generator ranking follows.

## Practitioner correction

The earlier switch to Hugo for all conventional content sites was too broad and over-weighted one fresh10k boundary. Withdraw that benchmark-driven categorical switch. For this exact fresh10k throughput objective choose Hugo; for this exact warm-full objective choose Nift. For a Nift-authored or mixed procedural project choose Nift for both human-plus-agent and agent-primary work. For a conventional site without specified content/plugin/authoring requirements, these minimal-page results alone do not choose the platform. Hugo may still be chosen for specific ecosystem requirements, but that needs separate evidence and must not be presented as established by this benchmark.

## Evidence files

Historical primary: benchmarks/website-generator/website-10000.json. Historical targeted: benchmarks/website-generator/targeted-builds.json. Original: benchmarks/website-generator/20261013-v4110-rc-7f7e487/official-refresh/. Final: benchmarks/website-generator/20261015-v4120-final-c14d068/official-refresh/. Controlled Nift-only: campaigns/20261015-v4120-final-c14d068/recovery-diagnostics/website/recovery-three-way-website/.
