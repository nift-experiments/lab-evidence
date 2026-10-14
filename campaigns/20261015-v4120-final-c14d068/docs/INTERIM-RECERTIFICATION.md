# Interim final-candidate recertification

Scripting full evidence is independently audited: 1,880 measured and 376 warmups, all 188 participating jobs correct. Current same-node peer deficits are valid; version-recovery conclusions remain pending the exact release/original/final diagnostic. Historical cross-node movements are not treated as controlled version effects.

## Same-node version improvements and regressions

No completed three-way version diagnostic yet. No rows are invented.

## Complete current same-node scripting wall deficit league

| Rank | Scenario | Nift ms | Best peer | Peer ms | Nift / peer |
|---:|---|---:|---|---:|---:|
| 1 | arrays-strings-hash/frequency-count/large | 416.542 | luajit | 3.022 | 137.83× |
| 2 | sanity/function-calls/large | 193.726 | luajit | 1.419 | 136.53× |
| 3 | arrays-strings-hash/sliding-window/large | 250.116 | luajit | 2.404 | 104.04× |
| 4 | arrays-strings-hash/map-set/large | 212.697 | luajit | 2.633 | 80.77× |
| 5 | dynamic-programming/fibonacci/large | 141.525 | luajit | 2.060 | 68.72× |
| 6 | arrays-strings-hash/scan/large | 82.874 | luajit | 1.374 | 60.32× |
| 7 | sanity/loops/large | 72.592 | luajit | 1.419 | 51.15× |
| 8 | graphs-trees-search/bfs/large | 799.359 | luajit | 16.932 | 47.21× |
| 9 | arrays-strings-hash/sort-index/large | 511.631 | python | 23.052 | 22.19× |
| 10 | structured-data/json-transform/large | 462.853 | node | 74.546 | 6.21× |
| 11 | graphs-trees-search/bfs/small | 11.405 | lua54 | 1.868 | 6.11× |
| 12 | structured-data/json-traverse/large | 370.415 | node | 68.608 | 5.40× |
| 13 | arrays-strings-hash/frequency-count/small | 7.068 | luajit | 1.312 | 5.39× |
| 14 | arrays-strings-hash/sort-index/small | 6.847 | luajit | 1.508 | 4.54× |
| 15 | arrays-strings-hash/sliding-window/small | 5.287 | luajit | 1.339 | 3.95× |
| 16 | sanity/function-calls/small | 4.650 | luajit | 1.301 | 3.57× |
| 17 | arrays-strings-hash/map-set/small | 4.701 | luajit | 1.395 | 3.37× |
| 18 | filesystem/traverse/large | 25.005 | luajit | 7.641 | 3.27× |
| 19 | arrays-strings-hash/scan/small | 3.556 | luajit | 1.291 | 2.76× |
| 20 | structured-data/json-parse/large | 182.077 | node | 66.988 | 2.72× |
| 21 | sanity/loops/small | 3.346 | luajit | 1.281 | 2.61× |
| 22 | dynamic-programming/fibonacci/small | 2.817 | luajit | 1.263 | 2.23× |
| 23 | sanity/output/small | 2.521 | luajit | 1.217 | 2.07× |
| 24 | sanity/noop/large | 2.389 | luajit | 1.184 | 2.02× |
| 25 | sanity/noop/small | 2.463 | luajit | 1.228 | 2.01× |
| 26 | sanity/output/large | 2.465 | luajit | 1.229 | 2.00× |
| 27 | filesystem/traverse/small | 3.104 | luajit | 4.614 | 0.67× |
| 28 | structured-data/json-transform/small | 7.186 | python | 24.470 | 0.29× |
| 29 | structured-data/json-traverse/small | 6.235 | python | 23.981 | 0.26× |
| 30 | structured-data/json-parse/small | 4.269 | python | 23.702 | 0.18× |

All rows are median fresh-process latency from 10 measured samples. Boundaries include invocation overhead; this is not an overall language ranking. Memory and capabilities remain separate. Practitioner choices are reevaluated after more audited evidence; no release or publication is authorized.
