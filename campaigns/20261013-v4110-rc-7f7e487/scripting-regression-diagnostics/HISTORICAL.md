# Historical scripting regression diagnostic

All 30 matched Nift medians increased. These are cross-node comparisons; peer-normalized ratios are descriptive diagnostics, not corrected benchmark results. Same-node A/B is pending.

| Scenario | Category | Old ms | New ms | Increase | Nift ratio / median peer ratio |
|---|---|---:|---:|---:|---:|
| sanity/function-calls/large | function/call overhead | 185.103 | 546.056 | 195.00% | 2.380 |
| sanity/function-calls/small | function/call overhead | 4.987 | 10.027 | 101.08% | 1.559 |
| structured-data/json-parse/large | JSON/data processing | 192.276 | 295.195 | 53.53% | 1.120 |
| graphs-trees-search/bfs/large | scalar compute / algorithm (inspect workload) | 654.593 | 1002.530 | 53.15% | 1.156 |
| arrays-strings-hash/frequency-count/large | collection/sort | 385.547 | 589.370 | 52.87% | 1.226 |
| structured-data/json-transform/large | JSON/data processing | 464.025 | 669.316 | 44.24% | 1.109 |
| sanity/output/large | startup-sensitive | 2.709 | 3.814 | 40.77% | 1.083 |
| graphs-trees-search/bfs/small | scalar compute / algorithm (inspect workload) | 10.358 | 14.471 | 39.70% | 1.145 |
| arrays-strings-hash/frequency-count/small | collection/sort | 7.112 | 9.813 | 37.98% | 1.089 |
| structured-data/json-transform/small | JSON/data processing | 7.439 | 10.185 | 36.91% | 1.058 |
| sanity/loops/small | scalar compute / algorithm (inspect workload) | 3.852 | 5.251 | 36.29% | 1.061 |
| arrays-strings-hash/sliding-window/small | collection/sort | 5.867 | 7.923 | 35.06% | 1.045 |
| dynamic-programming/fibonacci/small | scalar compute / algorithm (inspect workload) | 3.083 | 4.147 | 34.48% | 1.027 |
| arrays-strings-hash/map-set/small | collection/sort | 5.173 | 6.940 | 34.16% | 1.052 |
| structured-data/json-parse/small | JSON/data processing | 4.877 | 6.521 | 33.71% | 0.983 |
| arrays-strings-hash/map-set/large | collection/sort | 215.188 | 284.963 | 32.43% | 1.026 |
| structured-data/json-traverse/large | JSON/data processing | 357.846 | 473.779 | 32.40% | 0.985 |
| filesystem/traverse/large | filesystem traversal | 32.037 | 41.798 | 30.47% | 1.008 |
| sanity/noop/large | startup-sensitive | 2.553 | 3.310 | 29.68% | 1.031 |
| filesystem/traverse/small | filesystem traversal | 3.624 | 4.675 | 29.00% | 0.977 |
| arrays-strings-hash/scan/small | collection/sort | 4.129 | 5.315 | 28.72% | 1.004 |
| structured-data/json-traverse/small | JSON/data processing | 6.380 | 8.186 | 28.31% | 0.923 |
| sanity/noop/small | startup-sensitive | 4.721 | 5.855 | 24.03% | 0.940 |
| sanity/output/small | startup-sensitive | 2.959 | 3.659 | 23.67% | 0.976 |
| arrays-strings-hash/sliding-window/large | collection/sort | 271.359 | 328.926 | 21.21% | 0.934 |
| arrays-strings-hash/scan/large | collection/sort | 88.809 | 103.618 | 16.67% | 0.923 |
| arrays-strings-hash/sort-index/small | collection/sort | 8.230 | 9.541 | 15.93% | 0.885 |
| sanity/loops/large | scalar compute / algorithm (inspect workload) | 74.997 | 82.525 | 10.04% | 0.891 |
| dynamic-programming/fibonacci/large | scalar compute / algorithm (inspect workload) | 152.071 | 164.168 | 7.95% | 0.833 |
| arrays-strings-hash/sort-index/large | collection/sort | 876.868 | 904.664 | 3.17% | 0.834 |
