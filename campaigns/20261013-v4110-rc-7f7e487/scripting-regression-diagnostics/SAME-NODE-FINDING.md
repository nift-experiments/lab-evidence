# Same-node scripting diagnostic finding

Independent audit passed: 30 compatible scenarios, 600 measured observations and 120 warmups; adjacent paired versions with 5/5 balanced first-order per case. Both exact checkouts are clean; old fresh build matches previous accepted binary, candidate hash unchanged. All outputs correct. Official accepted evidence is untouched.

The historical 30/30 slowdown is not reproduced as a broad same-node slowdown: 13 medians increased and 17 decreased. Function calls have a clear large regression; collection frequency counting, BFS and JSON transformation also have higher medians. Near-flat/tiny cases are descriptive and not significance claims. Allocation/profile/syscall comparison remains pending; no release recommendation.

## Ten largest increases

| Scenario | Old ms | Candidate ms | Delta ms | Increase | Historical increase |
|---|---:|---:|---:|---:|---:|
| sanity/function-calls/large | 228.284 | 561.026 | +332.742 | +145.76% | +195.00% |
| sanity/function-calls/small | 6.080 | 10.069 | +3.990 | +65.63% | +101.08% |
| arrays-strings-hash/frequency-count/small | 8.303 | 10.659 | +2.356 | +28.37% | +37.98% |
| graphs-trees-search/bfs/small | 12.723 | 15.270 | +2.547 | +20.02% | +39.70% |
| structured-data/json-transform/large | 586.317 | 703.648 | +117.331 | +20.01% | +44.24% |
| arrays-strings-hash/frequency-count/large | 473.156 | 567.263 | +94.107 | +19.89% | +52.87% |
| graphs-trees-search/bfs/large | 844.177 | 999.076 | +154.899 | +18.35% | +53.15% |
| sanity/noop/small | 3.293 | 3.621 | +0.328 | +9.96% | +24.03% |
| structured-data/json-transform/small | 9.078 | 9.956 | +0.877 | +9.66% | +36.91% |
| structured-data/json-parse/large | 245.533 | 262.571 | +17.038 | +6.94% | +53.53% |

## Ten largest decreases

| Scenario | Old ms | Candidate ms | Delta ms | Change |
|---|---:|---:|---:|---:|
| arrays-strings-hash/sort-index/large | 1088.855 | 754.437 | -334.417 | -30.71% |
| arrays-strings-hash/scan/large | 110.635 | 93.988 | -16.646 | -15.05% |
| structured-data/json-parse/small | 6.812 | 5.979 | -0.833 | -12.23% |
| dynamic-programming/fibonacci/large | 182.107 | 164.111 | -17.995 | -9.88% |
| arrays-strings-hash/sliding-window/large | 339.164 | 307.064 | -32.100 | -9.46% |
| arrays-strings-hash/sort-index/small | 10.823 | 9.843 | -0.981 | -9.06% |
| arrays-strings-hash/scan/small | 4.901 | 4.541 | -0.360 | -7.34% |
| arrays-strings-hash/map-set/large | 295.962 | 278.617 | -17.346 | -5.86% |
| arrays-strings-hash/map-set/small | 7.007 | 6.615 | -0.392 | -5.60% |
| sanity/loops/large | 92.539 | 88.115 | -4.424 | -4.78% |

The large call sample ranges do not overlap (old209.461–239.335ms; candidate524.289–647.215ms). This is difficult to explain by general node drift alone under adjacent alternating execution. The current evaluator call-operand staging is a plausible source hypothesis, not an established root cause. Small call ranges also do not overlap in this run.

Interpretation: mixed subsystem-specific effects plus historical host/environment drift, rather than uniformly slower interpreter execution. The sizeable function-call regression merits investigation before recommending this candidate for release. Other seven suites continue; no candidate changes or benchmark reruns.
