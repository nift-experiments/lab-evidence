# Diagnostic league tables — eight audited suites; build diagnostics pending

All rows derive from retained audited evidence. Build official peer data is included; its same-node diagnostic closeout is pending. Same-node measured direction does not imply a population significance test. Weak/near-flat controls are separately noted, not promoted to established changes.

## Confirmed regressions — worst first

Same-node version observations, with confidence stated per row. Cross-node trends are excluded.

| Rank | Benchmark / scenario | Old ms | Candidate ms | Regression | Basis / confidence |
|---:|---|---:|---:|---:|---|
| 1 | scripting / sanity/function-calls/large | 228.284 | 561.026 | +145.76% | 10 paired measured samples/version; 10/10 pairs and disjoint ranges |
| 2 | shell / function-calls | 22.086 | 48.519 | +119.68% | 10 paired measured samples/version; 10/10 slower pairs; disjoint ranges |
| 3 | scripting / sanity/function-calls/small | 6.080 | 10.069 | +65.63% | 10 paired measured samples/version; 10/10 pairs and disjoint ranges |
| 4 | website-generator / application-cold / 10000pages targeted adjacent paired versions | 2561.445 | 3542.237 | +38.29% | independently audited same-node targeted diagnostic; all observed ranges disjoint; small paired diagnostic; descriptive |
| 5 | scripting / arrays-strings-hash/frequency-count/small | 8.303 | 10.659 | +28.37% | 10 paired measured samples/version; descriptive median; significance not established |
| 6 | scripting / graphs-trees-search/bfs/small | 12.723 | 15.270 | +20.02% | 10 paired measured samples/version; descriptive median; significance not established |
| 7 | scripting / structured-data/json-transform/large | 586.317 | 703.648 | +20.01% | 10 paired measured samples/version; descriptive median; significance not established |
| 8 | scripting / arrays-strings-hash/frequency-count/large | 473.156 | 567.263 | +19.89% | 10 paired measured samples/version; descriptive median; significance not established |
| 9 | scripting / graphs-trees-search/bfs/large | 844.177 | 999.076 | +18.35% | 10 paired measured samples/version; descriptive median; significance not established |
| 10 | shell / string-transform | 60.516 | 69.788 | +15.32% | 10 paired measured samples/version; 10/10 slower pairs; disjoint ranges |
| 11 | scripting / sanity/noop/small | 3.293 | 3.621 | +9.96% | 10 paired measured samples/version; descriptive median; significance not established |
| 12 | scripting / structured-data/json-transform/small | 9.078 | 9.956 | +9.66% | 10 paired measured samples/version; descriptive median; significance not established |
| 13 | scripting / structured-data/json-parse/large | 245.533 | 262.571 | +6.94% | 10 paired measured samples/version; descriptive median; significance not established |
| 14 | scripting / dynamic-programming/fibonacci/small | 3.786 | 3.908 | +3.24% | 10 paired measured samples/version; descriptive median; significance not established |
| 15 | scripting / filesystem/traverse/large | 38.742 | 39.603 | +2.22% | 10 paired measured samples/version; descriptive median; significance not established |
| 16 | scripting / filesystem/traverse/small | 4.989 | 5.072 | +1.66% | 10 paired measured samples/version; descriptive median; significance not established |

## Confirmed improvements — best first

Same-node measured improvements; small/overlapping changes retain descriptive qualifications.

| Rank | Benchmark / scenario | Old ms | Candidate ms | Improvement | Basis / confidence |
|---:|---|---:|---:|---:|---|
| 1 | filesystem-automation / stat-10000 | 3049.752 | 274.114 | 91.01% | 3 paired measured samples/version;24 observations audited; large separated change; small diagnostic |
| 2 | filesystem-automation / filter-size-10000 | 2353.088 | 335.618 | 85.74% | 3 paired measured samples/version;24 observations audited; large separated change; small diagnostic |
| 3 | filesystem-automation / walk-10000 | 1295.283 | 187.531 | 85.52% | 3 paired measured samples/version;24 observations audited; large separated change; small diagnostic |
| 4 | template-engines / loop-10000 / source-render | 119.508 | 33.683 | 71.82% | independently audited same-node targeted diagnostic; descriptive three-pair control; small paired diagnostic; descriptive |
| 5 | concurrency / queue-100000-4-4 / fresh runtime/readiness request | 36066.073 | 11887.314 | 67.04% | independently audited same-node targeted diagnostic; descriptive three-pair control; small paired diagnostic; descriptive |
| 6 | template-engines / loop-10000 / fresh | 168.238 | 75.854 | 54.91% | independently audited same-node targeted diagnostic; descriptive three-pair control; small paired diagnostic; descriptive |
| 7 | template-engines / article / source-render | 0.430 | 0.266 | 38.05% | independently audited same-node targeted diagnostic; descriptive three-pair control; small paired diagnostic; descriptive |
| 8 | scripting / arrays-strings-hash/sort-index/large | 1088.855 | 754.437 | 30.71% | 10 paired measured samples/version; 10/10 pairs and disjoint ranges |
| 9 | scripting / arrays-strings-hash/scan/large | 110.635 | 93.988 | 15.05% | 10 paired measured samples/version; descriptive median; significance not established |
| 10 | website-generator / incremental/no-op / 10000pages targeted adjacent paired versions | 932.931 | 813.536 | 12.80% | independently audited same-node targeted diagnostic; all observed ranges disjoint; small paired diagnostic; descriptive |
| 11 | website-generator / warm-full / 10000pages targeted adjacent paired versions | 3176.786 | 2776.981 | 12.59% | independently audited same-node targeted diagnostic; all observed ranges disjoint; small paired diagnostic; descriptive |
| 12 | scripting / structured-data/json-parse/small | 6.812 | 5.979 | 12.23% | 10 paired measured samples/version; descriptive median; significance not established |
| 13 | website-generator / incremental/one-page / 10000pages targeted adjacent paired versions | 920.908 | 821.310 | 10.82% | independently audited same-node targeted diagnostic; all observed ranges disjoint; small paired diagnostic; descriptive |
| 14 | scripting / dynamic-programming/fibonacci/large | 182.107 | 164.111 | 9.88% | 10 paired measured samples/version; descriptive median; significance not established |
| 15 | scripting / arrays-strings-hash/sliding-window/large | 339.164 | 307.064 | 9.46% | 10 paired measured samples/version; descriptive median; significance not established |
| 16 | scripting / arrays-strings-hash/sort-index/small | 10.823 | 9.843 | 9.06% | 10 paired measured samples/version; descriptive median; significance not established |
| 17 | scripting / arrays-strings-hash/scan/small | 4.901 | 4.541 | 7.34% | 10 paired measured samples/version; descriptive median; significance not established |
| 18 | scripting / arrays-strings-hash/map-set/large | 295.962 | 278.617 | 5.86% | 10 paired measured samples/version; descriptive median; significance not established |
| 19 | scripting / arrays-strings-hash/map-set/small | 7.007 | 6.615 | 5.60% | 10 paired measured samples/version; descriptive median; significance not established |
| 20 | scripting / sanity/loops/large | 92.539 | 88.115 | 4.78% | 10 paired measured samples/version; descriptive median; significance not established |
| 21 | scripting / sanity/output/small | 3.720 | 3.562 | 4.25% | 10 paired measured samples/version; descriptive median; significance not established |
| 22 | scripting / sanity/loops/small | 4.945 | 4.780 | 3.35% | 10 paired measured samples/version; descriptive median; significance not established |
| 23 | scripting / arrays-strings-hash/sliding-window/small | 7.381 | 7.157 | 3.02% | 10 paired measured samples/version; descriptive median; significance not established |
| 24 | scripting / structured-data/json-traverse/small | 8.969 | 8.772 | 2.19% | 10 paired measured samples/version; descriptive median; significance not established |
| 25 | scripting / sanity/noop/large | 3.426 | 3.359 | 1.96% | 10 paired measured samples/version; descriptive median; significance not established |
| 26 | scripting / sanity/output/large | 3.778 | 3.707 | 1.88% | 10 paired measured samples/version; descriptive median; significance not established |
| 27 | scripting / structured-data/json-traverse/large | 491.211 | 489.025 | 0.45% | 10 paired measured samples/version; descriptive median; significance not established |

## Largest remaining competitive deficits — worst first

Official current-candidate vs fastest valid same-node peer. Different workload/clock/implementation boundaries remain visible; no global language score. Shell external-baseline is separately retained and excluded here. Values below1 are included so strong categories are not hidden.

| Rank | Benchmark / scenario | Boundary | Nift | Peer | Peer value | Multiple | Previous multiple |
|---:|---|---|---:|---|---:|---:|---:|
| 1 | concurrency / schedule-10000 | persistent | 20311.090 ms | go | 14.752 | 1376.88× | 1591.35× cross-node |
| 2 | concurrency / tiny-10000 | persistent | 19978.451 ms | go | 16.164 | 1235.97× | 1296.25× cross-node |
| 3 | concurrency / schedule-10000 | fresh | 19493.458 ms | go | 18.540 | 1051.42× | 1108.88× cross-node |
| 4 | concurrency / tiny-10000 | fresh | 17297.852 ms | go | 21.370 | 809.45× | 1037.23× cross-node |
| 5 | scripting / sanity/function-calls/large | fresh-process-repeated | 546.056 ms | luajit | 1.889 | 289.09× | not normalized |
| 6 | concurrency / mutex-8-2 | persistent | 257.462 ms | go | 0.895 | 287.64× | 578.08× cross-node |
| 7 | concurrency / mutex-8-1 | persistent | 227.523 ms | go | 0.851 | 267.31× | 661.88× cross-node |
| 8 | concurrency / mutex-8-4 | persistent | 264.153 ms | go | 0.991 | 266.64× | 749.25× cross-node |
| 9 | concurrency / mutex-1-2 | persistent | 209.273 ms | go | 0.868 | 240.97× | 510.06× cross-node |
| 10 | concurrency / mutex-1-4 | persistent | 220.942 ms | go | 0.935 | 236.22× | 742.13× cross-node |
| 11 | concurrency / queue-100000-4-4 | persistent | 11745.837 ms | bun | 56.266 | 208.76× | 607.04× cross-node |
| 12 | concurrency / cpu-1 | persistent | 10807.809 ms | go | 52.767 | 204.82× | 282.99× cross-node |
| 13 | concurrency / cpu-2 | persistent | 5482.127 ms | go | 26.945 | 203.46× | 247.79× cross-node |
| 14 | concurrency / mutex-1-1 | persistent | 187.105 ms | go | 0.954 | 196.17× | 519.93× cross-node |
| 15 | concurrency / cpu-1 | fresh | 10791.349 ms | go | 57.828 | 186.61× | 235.40× cross-node |
| 16 | concurrency / cpu-4 | persistent | 2850.945 ms | go | 15.286 | 186.51× | 248.11× cross-node |
| 17 | concurrency / queue-100000-4-1 | persistent | 11976.754 ms | bun | 65.372 | 183.21× | 640.18× cross-node |
| 18 | concurrency / wait-1000 | persistent | 2576.345 ms | go | 14.484 | 177.88× | 169.86× cross-node |
| 19 | concurrency / waiting-memory-1000 | persistent | 2772.812 ms | go | 15.600 | 177.74× | 169.17× cross-node |
| 20 | concurrency / queue-100000-1-1 | persistent | 10616.424 ms | bun | 60.019 | 176.88× | 578.14× cross-node |
| 21 | concurrency / queue-100000-1-4 | persistent | 11648.111 ms | bun | 67.150 | 173.46× | 666.30× cross-node |
| 22 | concurrency / cpu-2 | fresh | 5410.661 ms | go | 31.683 | 170.78× | 198.22× cross-node |
| 23 | concurrency / atomic-1 | persistent | 130.693 ms | go | 0.847 | 154.29× | 407.73× cross-node |
| 24 | scripting / arrays-strings-hash/frequency-count/large | fresh-process-repeated | 589.370 ms | luajit | 3.957 | 148.96× | not normalized |
| 25 | concurrency / queue-100000-4-4 | fresh | 12116.366 ms | bun | 85.354 | 141.95× | 384.86× cross-node |
| 26 | concurrency / cpu-4 | fresh | 2876.454 ms | go | 20.507 | 140.27× | 172.07× cross-node |
| 27 | concurrency / wait-1000 | fresh | 2594.638 ms | go | 19.028 | 136.36× | 124.23× cross-node |
| 28 | concurrency / pool-heavy-1 | persistent | 289.215 ms | go | 2.170 | 133.27× | 141.24× cross-node |
| 29 | concurrency / waiting-memory-1000 | fresh | 2798.030 ms | go | 21.405 | 130.72× | 111.99× cross-node |
| 30 | concurrency / queue-100000-4-1 | fresh | 11642.459 ms | bun | 90.086 | 129.24× | 442.29× cross-node |
| 31 | concurrency / queue-100000-1-1 | fresh | 10692.397 ms | bun | 84.193 | 127.00× | 376.02× cross-node |
| 32 | concurrency / queue-100000-1-4 | fresh | 11587.311 ms | bun | 91.422 | 126.74× | 442.57× cross-node |
| 33 | concurrency / queue-10000-4-4 | persistent | 1214.875 ms | go | 11.884 | 102.22× | 352.49× cross-node |
| 34 | concurrency / queue-10000-4-1 | persistent | 1176.023 ms | go | 11.927 | 98.60× | 365.47× cross-node |
| 35 | concurrency / queue-10000-1-4 | persistent | 1179.031 ms | go | 11.967 | 98.52× | 392.66× cross-node |
| 36 | concurrency / tiny-1000 | persistent | 261.055 ms | go | 2.672 | 97.70× | 83.46× cross-node |
| 37 | concurrency / queue-10000-1-1 | persistent | 1039.407 ms | go | 11.084 | 93.78× | 310.21× cross-node |
| 38 | concurrency / schedule-1000 | persistent | 233.856 ms | go | 2.498 | 93.62× | 80.12× cross-node |
| 39 | concurrency / fan-1000 | persistent | 229.789 ms | go | 2.605 | 88.20× | 85.63× cross-node |
| 40 | scripting / arrays-strings-hash/sliding-window/large | fresh-process-repeated | 328.926 ms | luajit | 3.776 | 87.11× | not normalized |
| 41 | concurrency / pool-heavy-2 | persistent | 150.951 ms | go | 1.874 | 80.56× | 95.84× cross-node |
| 42 | concurrency / queue-10000-4-4 | fresh | 1247.884 ms | go | 16.257 | 76.76× | 230.96× cross-node |
| 43 | scripting / arrays-strings-hash/map-set/large | fresh-process-repeated | 284.963 ms | luajit | 3.770 | 75.59× | not normalized |
| 44 | concurrency / queue-10000-1-4 | fresh | 1131.556 ms | go | 15.929 | 71.04× | 243.01× cross-node |
| 45 | concurrency / queue-10000-4-1 | fresh | 1152.334 ms | go | 16.399 | 70.27× | 251.30× cross-node |
| 46 | concurrency / atomic-2 | persistent | 66.909 ms | go | 0.961 | 69.62× | 197.15× cross-node |
| 47 | concurrency / queue-10000-1-1 | fresh | 1070.626 ms | go | 16.619 | 64.42× | 199.62× cross-node |
| 48 | scripting / dynamic-programming/fibonacci/large | fresh-process-repeated | 164.168 ms | luajit | 2.549 | 64.39× | not normalized |
| 49 | concurrency / queue-1000-1-4 | persistent | 115.802 ms | go | 1.824 | 63.50× | 224.83× cross-node |
| 50 | concurrency / queue-1000-4-1 | persistent | 119.052 ms | go | 1.882 | 63.27× | 203.99× cross-node |
| 51 | concurrency / queue-1000-4-4 | persistent | 125.297 ms | go | 2.007 | 62.43× | 172.29× cross-node |
| 52 | concurrency / queue-1000-1-1 | persistent | 102.209 ms | go | 1.804 | 56.65× | 180.43× cross-node |
| 53 | scripting / arrays-strings-hash/scan/large | fresh-process-repeated | 103.618 ms | luajit | 1.885 | 54.97× | not normalized |
| 54 | filesystem-automation / detect-hash-3-10000 | booted | 19772.223 ms | go | 365.594 | 54.08× | 64.18× cross-node |
| 55 | filesystem-automation / detect-hash-1-10000 | booted | 19561.214 ms | go | 364.110 | 53.72× | 65.47× cross-node |
| 56 | filesystem-automation / detect-hash-2-10000 | fresh | 20016.924 ms | go | 375.576 | 53.30× | 64.58× cross-node |
| 57 | filesystem-automation / detect-hash-2-10000 | booted | 19874.134 ms | go | 378.782 | 52.47× | 64.92× cross-node |
| 58 | filesystem-automation / detect-hash-3-10000 | fresh | 19756.367 ms | go | 380.049 | 51.98× | 63.37× cross-node |
| 59 | filesystem-automation / detect-hash-1-10000 | fresh | 19703.429 ms | go | 381.185 | 51.69× | 64.35× cross-node |
| 60 | concurrency / pool-heavy-4 | persistent | 77.766 ms | go | 1.582 | 49.17× | 64.64× cross-node |
| 61 | filesystem-automation / detect-hash-1-1000 | booted | 1992.423 ms | go | 41.225 | 48.33× | 59.92× cross-node |
| 62 | filesystem-automation / read-10000 | booted | 10188.374 ms | go | 212.571 | 47.93× | 65.36× cross-node |
| 63 | filesystem-automation / read-100000 | fresh | 103189.194 ms | go | 2164.440 | 47.67× | 55.77× cross-node |
| 64 | filesystem-automation / read-100000 | booted | 101939.221 ms | go | 2139.967 | 47.64× | 63.40× cross-node |
| 65 | filesystem-automation / clean-10000 | booted | 19821.980 ms | go | 416.678 | 47.57× | 62.70× cross-node |
| 66 | filesystem-automation / detect-hash-3-1000 | booted | 1987.155 ms | go | 41.783 | 47.56× | 59.11× cross-node |
| 67 | filesystem-automation / detect-hash-2-1000 | booted | 2059.295 ms | go | 43.786 | 47.03× | 60.27× cross-node |
| 68 | filesystem-automation / clean-10000 | fresh | 20225.230 ms | go | 434.561 | 46.54× | 59.83× cross-node |
| 69 | filesystem-automation / mirror-0-10000 | booted | 21433.438 ms | go | 461.194 | 46.47× | 56.59× cross-node |
| 70 | scripting / graphs-trees-search/bfs/large | fresh-process-repeated | 1002.530 ms | luajit | 21.869 | 45.84× | not normalized |
| 71 | filesystem-automation / mirror-1-10000 | booted | 22012.325 ms | go | 488.619 | 45.05× | 52.99× cross-node |
| 72 | filesystem-automation / mirror-0-10000 | fresh | 21590.134 ms | go | 479.512 | 45.03× | 57.05× cross-node |
| 73 | filesystem-automation / clean-1000 | booted | 2041.598 ms | go | 45.761 | 44.61× | 55.33× cross-node |
| 74 | filesystem-automation / manifest-10000 | booted | 10788.130 ms | go | 242.676 | 44.45× | 66.05× cross-node |
| 75 | filesystem-automation / mirror-12-10000 | fresh | 21661.765 ms | go | 488.779 | 44.32× | 56.01× cross-node |
| 76 | filesystem-automation / read-10000 | fresh | 10203.037 ms | go | 231.428 | 44.09× | 61.25× cross-node |
| 77 | filesystem-automation / mirror-1-10000 | fresh | 21398.801 ms | go | 486.718 | 43.97× | 52.68× cross-node |
| 78 | concurrency / pool-heavy-1 | fresh | 298.090 ms | go | 6.792 | 43.89× | 43.52× cross-node |
| 79 | filesystem-automation / manifest-1000 | booted | 1052.834 ms | go | 24.089 | 43.71× | 61.48× cross-node |
| 80 | filesystem-automation / mirror-12-10000 | booted | 21206.362 ms | go | 486.214 | 43.62× | 56.52× cross-node |
| 81 | filesystem-automation / read-1000 | booted | 1011.877 ms | go | 23.242 | 43.54× | 61.59× cross-node |
| 82 | concurrency / fan-1000 | fresh | 339.842 ms | go | 7.880 | 43.13× | 30.07× cross-node |
| 83 | concurrency / atomic-4 | persistent | 43.423 ms | go | 1.013 | 42.87× | 114.39× cross-node |
| 84 | filesystem-automation / mirror-12-1000 | booted | 2226.552 ms | go | 52.293 | 42.58× | 55.07× cross-node |
| 85 | filesystem-automation / mirror-0-1000 | booted | 2178.396 ms | go | 51.264 | 42.49× | 53.15× cross-node |
| 86 | scripting / sanity/loops/large | fresh-process-repeated | 82.525 ms | luajit | 1.945 | 42.44× | not normalized |
| 87 | filesystem-automation / detect-hash-1-1000 | fresh | 1988.065 ms | go | 48.390 | 41.08× | 51.83× cross-node |
| 88 | filesystem-automation / mirror-1-1000 | booted | 2177.040 ms | go | 53.188 | 40.93× | 53.44× cross-node |
| 89 | filesystem-automation / manifest-10000 | fresh | 10860.767 ms | go | 267.706 | 40.57× | 63.00× cross-node |
| 90 | filesystem-automation / detect-hash-2-1000 | fresh | 2019.836 ms | go | 50.976 | 39.62× | 52.72× cross-node |
| 91 | filesystem-automation / detect-hash-3-1000 | fresh | 1996.309 ms | go | 51.115 | 39.06× | 52.98× cross-node |
| 92 | concurrency / mutex-8-2 | fresh | 265.976 ms | go | 6.842 | 38.87× | 76.05× cross-node |
| 93 | filesystem-automation / mirror-11-10000 | booted | 21725.430 ms | go | 559.056 | 38.86× | 49.40× cross-node |
| 94 | filesystem-automation / mirror-10-10000 | booted | 21612.024 ms | go | 559.901 | 38.60× | 47.42× cross-node |
| 95 | concurrency / tiny-1000 | fresh | 256.266 ms | go | 6.706 | 38.21× | 29.38× cross-node |
| 96 | filesystem-automation / mirror-10-10000 | fresh | 21964.886 ms | go | 574.838 | 38.21× | 46.35× cross-node |
| 97 | filesystem-automation / clean-1000 | fresh | 2044.397 ms | go | 54.118 | 37.78× | 48.47× cross-node |
| 98 | filesystem-automation / mirror-11-10000 | fresh | 21518.444 ms | go | 578.993 | 37.17× | 46.51× cross-node |
| 99 | filesystem-automation / mirror-12-1000 | fresh | 2154.643 ms | go | 58.244 | 36.99× | 48.48× cross-node |
| 100 | filesystem-automation / mirror-0-1000 | fresh | 2201.077 ms | go | 59.802 | 36.81× | 48.64× cross-node |
| 101 | concurrency / schedule-1000 | fresh | 229.708 ms | go | 6.409 | 35.84× | 32.07× cross-node |
| 102 | concurrency / mutex-8-1 | fresh | 232.701 ms | go | 6.536 | 35.60× | 79.14× cross-node |
| 103 | filesystem-automation / mirror-11-1000 | booted | 2173.383 ms | go | 61.721 | 35.21× | 46.03× cross-node |
| 104 | concurrency / mutex-1-4 | fresh | 237.836 ms | go | 6.856 | 34.69× | 92.42× cross-node |
| 105 | concurrency / mutex-8-4 | fresh | 273.036 ms | go | 7.874 | 34.68× | 95.95× cross-node |
| 106 | concurrency / pool-medium-1 | persistent | 33.129 ms | go | 0.958 | 34.58× | 26.98× cross-node |
| 107 | filesystem-automation / mirror-1-1000 | fresh | 2179.618 ms | go | 63.089 | 34.55× | 46.69× cross-node |
| 108 | filesystem-automation / read-1000 | fresh | 1008.808 ms | go | 29.464 | 34.24× | 48.99× cross-node |
| 109 | concurrency / nested-100 | persistent | 56.421 ms | go | 1.658 | 34.02× | 30.13× cross-node |
| 110 | filesystem-automation / manifest-1000 | fresh | 1059.782 ms | go | 31.983 | 33.14× | 48.79× cross-node |
| 111 | filesystem-automation / mirror-10-1000 | booted | 2213.279 ms | go | 66.944 | 33.06× | 47.38× cross-node |
| 112 | concurrency / mutex-1-2 | fresh | 218.317 ms | go | 6.665 | 32.75× | 70.58× cross-node |
| 113 | filesystem-automation / mirror-11-1000 | fresh | 2212.627 ms | go | 71.461 | 30.96× | 41.84× cross-node |
| 114 | filesystem-automation / mirror-10-1000 | fresh | 2221.436 ms | go | 73.645 | 30.16× | 40.61× cross-node |
| 115 | scripting / arrays-strings-hash/sort-index/large | fresh-process-repeated | 904.664 ms | python | 30.633 | 29.53× | not normalized |
| 116 | concurrency / mutex-1-1 | fresh | 189.138 ms | go | 6.888 | 27.46× | 70.32× cross-node |
| 117 | concurrency / pool-light-1 | persistent | 22.541 ms | go | 0.872 | 25.84× | 15.38× cross-node |
| 118 | concurrency / files-10000 | persistent | 1589.358 ms | go | 62.994 | 25.23× | 20.75× cross-node |
| 119 | concurrency / files-10000 | fresh | 1608.951 ms | go | 66.757 | 24.10× | 17.15× cross-node |
| 120 | filesystem-automation / mixed-10000 | booted | 6036.915 ms | go | 254.491 | 23.72× | 28.44× cross-node |
| 121 | filesystem-automation / mixed-10000 | fresh | 6028.387 ms | go | 266.693 | 22.60× | 28.08× cross-node |
| 122 | concurrency / waiting-memory-100 | persistent | 262.937 ms | go | 11.790 | 22.30× | 20.12× cross-node |
| 123 | concurrency / wait-100 | persistent | 258.189 ms | go | 11.781 | 21.92× | 20.67× cross-node |
| 124 | filesystem-automation / mixed-1000 | booted | 617.213 ms | go | 29.223 | 21.12× | 29.77× cross-node |
| 125 | concurrency / pool-heavy-2 | fresh | 159.824 ms | go | 7.694 | 20.77× | 23.89× cross-node |
| 126 | concurrency / files-1000 | persistent | 161.134 ms | go | 7.978 | 20.20× | 18.66× cross-node |
| 127 | filesystem-automation / generate-10000 | booted | 13529.468 ms | go | 675.544 | 20.03× | 26.21× cross-node |
| 128 | concurrency / queue-1000-4-4 | fresh | 128.907 ms | go | 6.486 | 19.87× | 54.40× cross-node |
| 129 | concurrency / atomic-1 | fresh | 139.685 ms | go | 7.172 | 19.48× | 50.16× cross-node |
| 130 | concurrency / queue-1000-1-4 | fresh | 127.162 ms | go | 6.604 | 19.26× | 61.39× cross-node |
| 131 | concurrency / queue-1000-4-1 | fresh | 131.717 ms | go | 6.906 | 19.07× | 56.00× cross-node |
| 132 | filesystem-automation / generate-10000 | fresh | 13466.959 ms | go | 728.011 | 18.50× | 26.67× cross-node |
| 133 | concurrency / pool-medium-2 | persistent | 17.893 ms | go | 0.976 | 18.33× | 14.73× cross-node |
| 134 | filesystem-automation / generate-1000 | booted | 1360.202 ms | go | 74.719 | 18.20× | 25.78× cross-node |
| 135 | filesystem-automation / mixed-1000 | fresh | 622.891 ms | go | 36.088 | 17.26× | 25.43× cross-node |
| 136 | concurrency / queue-1000-1-1 | fresh | 111.971 ms | go | 6.582 | 17.01× | 37.87× cross-node |
| 137 | concurrency / wait-100 | fresh | 264.840 ms | go | 15.635 | 16.94× | 16.00× cross-node |
| 138 | filesystem-automation / generate-1000 | fresh | 1372.182 ms | go | 86.002 | 15.96× | 23.13× cross-node |
| 139 | concurrency / waiting-memory-100 | fresh | 270.362 ms | go | 17.576 | 15.38× | 13.01× cross-node |
| 140 | template-engines / loop-10000 | source-render | 34.408 ms/render | handlebars | 2.241 | 15.35× | 53.19× cross-node |
| 141 | concurrency / pool-light-2 | persistent | 12.648 ms | go | 0.915 | 13.82× | 8.72× cross-node |
| 142 | concurrency / pool-heavy-4 | fresh | 84.975 ms | go | 6.153 | 13.81× | 13.70× cross-node |
| 143 | concurrency / files-1000 | fresh | 168.950 ms | go | 12.734 | 13.27× | 10.88× cross-node |
| 144 | concurrency / schedule-100 | persistent | 13.619 ms | go | 1.068 | 12.76× | 11.70× cross-node |
| 145 | concurrency / files-100 | persistent | 19.850 ms | go | 1.560 | 12.72× | 9.01× cross-node |
| 146 | concurrency / fan-100 | persistent | 14.262 ms | go | 1.126 | 12.66× | 11.31× cross-node |
| 147 | concurrency / stagger-100 | persistent | 279.584 ms | go | 22.200 | 12.59× | 12.76× cross-node |
| 148 | concurrency / tiny-100 | persistent | 14.888 ms | go | 1.208 | 12.32× | 10.43× cross-node |
| 149 | concurrency / atomic-2 | fresh | 74.700 ms | go | 6.625 | 11.28× | 27.45× cross-node |
| 150 | filesystem-automation / filter-50-100000 | booted | 6693.413 ms | bun | 603.004 | 11.10× | 55.46× cross-node |
| 151 | concurrency / stagger-100 | fresh | 285.665 ms | go | 26.011 | 10.98× | 10.35× cross-node |
| 152 | build-systems / native-1000-heavy-j1/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 179.197 ms | ninja | 16.839 | 10.64× | 20.32× cross-node |
| 153 | filesystem-automation / filter-50-100000 | fresh | 6438.018 ms | bun | 627.027 | 10.27× | 49.51× cross-node |
| 154 | concurrency / pool-medium-4 | persistent | 10.734 ms | go | 1.066 | 10.07× | 9.09× cross-node |
| 155 | filesystem-automation / large-read-100x1048576 | booted | 186.806 ms | python | 18.758 | 9.96× | 11.50× cross-node |
| 156 | filesystem-automation / filter-10-100000 | booted | 5790.287 ms | go | 590.464 | 9.81× | 44.55× cross-node |
| 157 | filesystem-automation / filter-10-10000 | booted | 573.921 ms | go | 58.827 | 9.76× | 43.69× cross-node |
| 158 | filesystem-automation / walk-100000 | fresh | 2336.417 ms | bun | 241.886 | 9.66× | 60.51× cross-node |
| 159 | filesystem-automation / filter-50-10000 | booted | 656.690 ms | go | 67.999 | 9.66× | 49.50× cross-node |
| 160 | filesystem-automation / filter-1-100000 | booted | 5475.102 ms | go | 568.206 | 9.64× | 45.75× cross-node |
| 161 | filesystem-automation / filter-10-100000 | fresh | 5748.250 ms | bun | 616.903 | 9.32× | 44.04× cross-node |
| 162 | filesystem-automation / filter-1-100000 | fresh | 5528.397 ms | go | 594.847 | 9.29× | 42.30× cross-node |
| 163 | filesystem-automation / overwrite-10000 | booted | 3651.606 ms | bun | 393.308 | 9.28× | 16.73× cross-node |
| 164 | filesystem-automation / filter-1-10000 | booted | 536.867 ms | go | 58.057 | 9.25× | 43.26× cross-node |
| 165 | filesystem-automation / walk-100000 | booted | 1824.631 ms | bun | 203.549 | 8.96× | 71.02× cross-node |
| 166 | concurrency / nested-100 | fresh | 63.798 ms | go | 7.402 | 8.62× | 6.90× cross-node |
| 167 | filesystem-automation / filter-50-1000 | booted | 65.896 ms | go | 7.689 | 8.57× | 45.03× cross-node |
| 168 | filesystem-automation / filter-50-10000 | fresh | 655.821 ms | go | 76.582 | 8.56× | 45.24× cross-node |
| 169 | filesystem-automation / filter-1-1000 | booted | 57.310 ms | go | 6.729 | 8.52× | 39.15× cross-node |
| 170 | filesystem-automation / filter-1-10000 | fresh | 553.636 ms | go | 65.236 | 8.49× | 38.65× cross-node |
| 171 | concurrency / atomic-4 | fresh | 60.134 ms | go | 7.088 | 8.48× | 16.11× cross-node |
| 172 | filesystem-automation / filter-10-1000 | booted | 59.689 ms | go | 7.101 | 8.41× | 40.24× cross-node |
| 173 | build-systems / tiny-100-light-j1/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 17.587 ms | make | 2.096 | 8.39× | 10.96× cross-node |
| 174 | filesystem-automation / filter-10-10000 | fresh | 574.897 ms | go | 68.545 | 8.39× | 38.76× cross-node |
| 175 | filesystem-automation / overwrite-10000 | fresh | 3782.107 ms | bun | 461.123 | 8.20× | 15.57× cross-node |
| 176 | concurrency / nested-10 | persistent | 7.742 ms | go | 0.948 | 8.17× | 6.88× cross-node |
| 177 | concurrency / pool-light-4 | persistent | 8.004 ms | go | 1.032 | 7.76× | 6.01× cross-node |
| 178 | concurrency / pool-medium-1 | fresh | 37.919 ms | go | 5.057 | 7.50× | 5.95× cross-node |
| 179 | template-engines / collection | source-render | 7.263 ms/render | handlebars | 0.974 | 7.45× | 30.87× cross-node |
| 180 | filesystem-automation / overwrite-1000 | booted | 354.394 ms | bun | 47.667 | 7.43× | 14.37× cross-node |
| 181 | scripting / structured-data/json-transform/large | fresh-process-repeated | 669.316 ms | python | 95.607 | 7.00× | not normalized |
| 182 | filesystem-automation / walk-10000 | booted | 184.959 ms | bun | 26.515 | 6.98× | 52.25× cross-node |
| 183 | build-systems / native-100-heavy-j1/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 24.861 ms | ninja | 3.723 | 6.68× | 9.60× cross-node |
| 184 | build-systems / native-1000-heavy-j2/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 112.423 ms | ninja | 16.937 | 6.64× | 11.47× cross-node |
| 185 | build-systems / tiny-1000-light-j4/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 65.392 ms | make | 9.897 | 6.61× | 7.85× cross-node |
| 186 | filesystem-automation / filter-extension-100000 | booted | 3628.238 ms | bun | 555.903 | 6.53× | 38.02× cross-node |
| 187 | build-systems / tiny-1000-light-j4/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 61.847 ms | make | 9.524 | 6.49× | 8.15× cross-node |
| 188 | filesystem-automation / large-read-10x10485760 | booted | 263.652 ms | go | 41.071 | 6.42× | 6.57× cross-node |
| 189 | filesystem-automation / filter-extension-100000 | fresh | 3648.602 ms | bun | 579.317 | 6.30× | 36.72× cross-node |
| 190 | filesystem-automation / filter-prefix-100000 | booted | 3371.324 ms | bun | 543.281 | 6.21× | 36.68× cross-node |
| 191 | build-systems / native-100-light-j1/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 24.778 ms | ninja | 4.010 | 6.18× | 9.92× cross-node |
| 192 | build-systems / tiny-10000-light-j4/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 544.418 ms | make | 88.881 | 6.13× | 7.63× cross-node |
| 193 | filesystem-automation / filter-size-100000 | booted | 3334.847 ms | bun | 558.048 | 5.98× | 44.63× cross-node |
| 194 | build-systems / tiny-10000-light-j4/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 542.542 ms | make | 91.066 | 5.96× | 7.59× cross-node |
| 195 | filesystem-automation / filter-prefix-100000 | fresh | 3514.817 ms | go | 592.580 | 5.93× | 35.25× cross-node |
| 196 | filesystem-automation / filter-extension-10000 | booted | 367.552 ms | go | 62.101 | 5.92× | 34.01× cross-node |
| 197 | build-systems / tiny-100-light-j2/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 12.890 ms | make | 2.209 | 5.83× | 6.97× cross-node |
| 198 | build-systems / tiny-10000-light-j4/batch10 | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 543.637 ms | make | 93.532 | 5.81× | 6.61× cross-node |
| 199 | filesystem-automation / filter-prefix-10000 | booted | 340.228 ms | go | 59.388 | 5.73× | 32.49× cross-node |
| 200 | scripting / graphs-trees-search/bfs/small | fresh-process-repeated | 14.471 ms | lua54 | 2.529 | 5.72× | not normalized |
| 201 | filesystem-automation / write-10000 | booted | 3064.102 ms | go | 537.041 | 5.71× | 11.53× cross-node |
| 202 | scripting / sanity/function-calls/small | fresh-process-repeated | 10.027 ms | luajit | 1.764 | 5.68× | not normalized |
| 203 | filesystem-automation / filter-size-100000 | fresh | 3317.358 ms | bun | 584.837 | 5.67× | 41.56× cross-node |
| 204 | build-systems / tiny-100-light-j1/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 21.517 ms | make | 3.807 | 5.65× | 7.20× cross-node |
| 205 | concurrency / pool-light-1 | fresh | 27.460 ms | go | 4.893 | 5.61× | 3.66× cross-node |
| 206 | filesystem-automation / relocate-10000 | booted | 430.593 ms | bun | 78.305 | 5.50× | 43.45× cross-node |
| 207 | filesystem-automation / filter-10-1000 | fresh | 65.169 ms | go | 11.985 | 5.44× | 23.19× cross-node |
| 208 | scripting / arrays-strings-hash/frequency-count/small | fresh-process-repeated | 9.813 ms | luajit | 1.829 | 5.37× | not normalized |
| 209 | filesystem-automation / filter-extension-1000 | booted | 38.398 ms | go | 7.174 | 5.35× | 30.68× cross-node |
| 210 | filesystem-automation / filter-50-1000 | fresh | 73.573 ms | go | 13.801 | 5.33× | 27.01× cross-node |
| 211 | filesystem-automation / filter-1-1000 | fresh | 63.949 ms | go | 12.017 | 5.32× | 23.16× cross-node |
| 212 | filesystem-automation / filter-extension-10000 | fresh | 377.594 ms | go | 71.111 | 5.31× | 30.94× cross-node |
| 213 | filesystem-automation / write-1000 | booted | 303.492 ms | go | 58.217 | 5.21× | 10.89× cross-node |
| 214 | filesystem-automation / filter-size-10000 | booted | 326.770 ms | bun | 62.698 | 5.21× | 38.41× cross-node |
| 215 | filesystem-automation / filter-prefix-10000 | fresh | 351.924 ms | go | 67.785 | 5.19× | 28.04× cross-node |
| 216 | filesystem-automation / large-read-100x1048576 | fresh | 202.330 ms | go | 39.068 | 5.18× | 6.30× cross-node |
| 217 | filesystem-automation / copy-100000 | booted | 26655.207 ms | go | 5168.404 | 5.16× | 10.22× cross-node |
| 218 | filesystem-automation / filter-prefix-1000 | booted | 36.646 ms | go | 7.111 | 5.15× | 29.22× cross-node |
| 219 | filesystem-automation / write-10000 | fresh | 3074.272 ms | go | 608.209 | 5.05× | 11.62× cross-node |
| 220 | build-systems / tiny-1000-light-j4/batch10 | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 74.449 ms | make | 14.783 | 5.04× | 5.94× cross-node |
| 221 | scripting / structured-data/json-traverse/large | fresh-process-repeated | 473.779 ms | node | 94.393 | 5.02× | not normalized |
| 222 | filesystem-automation / copy-100000 | fresh | 26527.248 ms | go | 5296.284 | 5.01× | 9.83× cross-node |
| 223 | filesystem-automation / copy-10000 | booted | 2626.688 ms | go | 526.224 | 4.99× | 10.79× cross-node |
| 224 | filesystem-automation / overwrite-1000 | fresh | 372.370 ms | bun | 74.785 | 4.98× | 9.57× cross-node |
| 225 | filesystem-automation / relocate-10000 | fresh | 451.027 ms | go | 90.851 | 4.96× | 35.21× cross-node |
| 226 | build-systems / tiny-100-light-j2/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 16.099 ms | make | 3.264 | 4.93× | 5.55× cross-node |
| 227 | filesystem-automation / relocate-1000 | booted | 45.976 ms | go | 9.327 | 4.93× | 35.45× cross-node |
| 228 | filesystem-automation / stat-100000 | booted | 2954.971 ms | bun | 614.755 | 4.81× | 52.66× cross-node |
| 229 | scripting / arrays-strings-hash/sort-index/small | fresh-process-repeated | 9.541 ms | luajit | 1.986 | 4.80× | not normalized |
| 230 | filesystem-automation / copy-10000 | fresh | 2723.460 ms | go | 568.762 | 4.79× | 10.74× cross-node |
| 231 | build-systems / tiny-100-light-j4/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 10.629 ms | make | 2.227 | 4.77× | 5.37× cross-node |
| 232 | filesystem-automation / copy-1000 | booted | 259.715 ms | go | 54.665 | 4.75× | 10.31× cross-node |
| 233 | filesystem-automation / write-1000 | fresh | 313.204 ms | go | 66.027 | 4.74× | 9.86× cross-node |
| 234 | filesystem-automation / large-read-10x10485760 | fresh | 275.122 ms | go | 58.207 | 4.73× | 4.64× cross-node |
| 235 | build-systems / native-1000-light-j4/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 76.235 ms | ninja | 16.288 | 4.68× | 6.98× cross-node |
| 236 | filesystem-automation / filter-size-1000 | booted | 35.159 ms | go | 7.521 | 4.67× | 34.12× cross-node |
| 237 | filesystem-automation / filter-size-10000 | fresh | 340.600 ms | go | 73.001 | 4.67× | 34.25× cross-node |
| 238 | build-systems / native-1000-heavy-j4/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 77.313 ms | ninja | 16.761 | 4.61× | 6.79× cross-node |
| 239 | shell / string-transform | shell-workloads.json | 68.691 ms | zsh | 14.949 | 4.60× | not normalized |
| 240 | build-systems / native-100-heavy-j2/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 17.883 ms | ninja | 3.933 | 4.55× | 6.39× cross-node |
| 241 | template-engines / loop-1000 | source-render | 3.385 ms/render | handlebars | 0.749 | 4.52× | 18.04× cross-node |
| 242 | filesystem-automation / stat-100000 | fresh | 2794.862 ms | bun | 621.325 | 4.50× | 46.62× cross-node |
| 243 | build-systems / native-5000-light-j4/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 349.748 ms | ninja | 77.977 | 4.49× | 7.07× cross-node |
| 244 | build-systems / native-100-light-j2/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 17.412 ms | ninja | 3.893 | 4.47× | 6.34× cross-node |
| 245 | build-systems / native-10000-light-j4/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 692.382 ms | ninja | 161.857 | 4.28× | 7.11× cross-node |
| 246 | shell / traverse-100000 | shell-workloads.json | 1111.613 ms | nu | 261.104 | 4.26× | not normalized |
| 247 | concurrency / fan-100 | fresh | 24.618 ms | go | 5.850 | 4.21× | 3.19× cross-node |
| 248 | concurrency / files-100 | fresh | 25.392 ms | go | 6.038 | 4.21× | 3.28× cross-node |
| 249 | filesystem-automation / copy-1000 | fresh | 270.720 ms | go | 64.808 | 4.18× | 9.50× cross-node |
| 250 | scripting / arrays-strings-hash/sliding-window/small | fresh-process-repeated | 7.923 ms | lua54 | 1.904 | 4.16× | not normalized |
| 251 | filesystem-automation / walk-1000 | booted | 21.696 ms | go | 5.236 | 4.14× | 30.23× cross-node |
| 252 | concurrency / mixed-wait-100 | persistent | 89.072 ms | go | 21.562 | 4.13× | 4.13× cross-node |
| 253 | concurrency / pool-medium-2 | fresh | 23.692 ms | go | 5.786 | 4.09× | 3.44× cross-node |
| 254 | build-systems / tiny-100-light-j4/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 13.346 ms | make | 3.320 | 4.02× | 4.36× cross-node |
| 255 | template-engines / literal | source-render | 0.015 ms/render | liquid | 0.004 | 3.98× | 4.36× cross-node |
| 256 | scripting / filesystem/traverse/large | fresh-process-repeated | 41.798 ms | luajit | 10.608 | 3.94× | not normalized |
| 257 | concurrency / schedule-100 | fresh | 18.692 ms | go | 4.788 | 3.90× | 3.57× cross-node |
| 258 | filesystem-automation / stat-10000 | booted | 269.615 ms | bun | 69.629 | 3.87× | 44.77× cross-node |
| 259 | filesystem-automation / walk-10000 | fresh | 195.374 ms | bun | 51.601 | 3.79× | 28.95× cross-node |
| 260 | build-systems / tiny-10000-light-j4/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 17762.305 ms | make | 4711.695 | 3.77× | 2.64× cross-node |
| 261 | concurrency / tiny-100 | fresh | 18.625 ms | go | 4.971 | 3.75× | 3.47× cross-node |
| 262 | concurrency / mixed-wait-100 | fresh | 95.620 ms | go | 25.792 | 3.71× | 3.52× cross-node |
| 263 | concurrency / tiny-10 | persistent | 3.006 ms | go | 0.830 | 3.62× | 3.08× cross-node |
| 264 | build-systems / native-100-heavy-j4/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 13.842 ms | ninja | 3.835 | 3.61× | 4.42× cross-node |
| 265 | concurrency / fan-10 | persistent | 3.265 ms | go | 0.906 | 3.60× | 2.99× cross-node |
| 266 | scripting / arrays-strings-hash/map-set/small | fresh-process-repeated | 6.940 ms | luajit | 1.952 | 3.56× | not normalized |
| 267 | build-systems / native-100-light-j4/noop | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 13.355 ms | ninja | 3.831 | 3.49× | 4.30× cross-node |
| 268 | concurrency / failures | persistent | 3.188 ms | go | 0.924 | 3.45× | 3.53× cross-node |
| 269 | filesystem-automation / filter-extension-1000 | fresh | 44.846 ms | go | 13.076 | 3.43× | 17.95× cross-node |
| 270 | filesystem-automation / stat-10000 | fresh | 284.683 ms | go | 83.773 | 3.40× | 37.55× cross-node |
| 271 | concurrency / schedule-10 | persistent | 3.013 ms | go | 0.890 | 3.39× | 3.07× cross-node |
| 272 | concurrency / pool-light-2 | fresh | 18.198 ms | go | 5.416 | 3.36× | 2.58× cross-node |
| 273 | filesystem-automation / filter-prefix-1000 | fresh | 42.674 ms | go | 12.867 | 3.32× | 17.41× cross-node |
| 274 | filesystem-automation / stat-1000 | booted | 30.091 ms | go | 9.173 | 3.28× | 38.78× cross-node |
| 275 | filesystem-automation / relocate-1000 | fresh | 55.802 ms | go | 17.389 | 3.21× | 21.68× cross-node |
| 276 | filesystem-automation / delete-10000 | booted | 772.377 ms | bun | 245.903 | 3.14× | 14.67× cross-node |
| 277 | filesystem-automation / rename-10000 | booted | 757.302 ms | bun | 241.590 | 3.13× | 15.36× cross-node |
| 278 | scripting / structured-data/json-parse/large | fresh-process-repeated | 295.195 ms | node | 98.649 | 2.99× | not normalized |
| 279 | concurrency / pool-medium-4 | fresh | 17.269 ms | go | 5.870 | 2.94× | 2.45× cross-node |
| 280 | scripting / arrays-strings-hash/scan/small | fresh-process-repeated | 5.315 ms | luajit | 1.811 | 2.93× | not normalized |
| 281 | filesystem-automation / delete-10000 | fresh | 783.569 ms | go | 267.146 | 2.93× | 13.46× cross-node |
| 282 | filesystem-automation / delete-1000 | booted | 78.226 ms | go | 26.678 | 2.93× | 13.88× cross-node |
| 283 | concurrency / process-1000 | fresh | 886.230 ms | go | 302.553 | 2.93× | 2.74× cross-node |
| 284 | scripting / sanity/loops/small | fresh-process-repeated | 5.251 ms | lua54 | 1.802 | 2.91× | not normalized |
| 285 | build-systems / tiny-100-light-j2/batch10 | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 26.735 ms | make | 9.191 | 2.91× | 2.88× cross-node |
| 286 | concurrency / process-1000 | persistent | 835.100 ms | go | 288.374 | 2.90× | 2.67× cross-node |
| 287 | filesystem-automation / filter-size-1000 | fresh | 43.983 ms | go | 15.209 | 2.89× | 20.11× cross-node |
| 288 | filesystem-automation / rename-1000 | booted | 79.327 ms | python | 27.888 | 2.84× | 13.44× cross-node |
| 289 | build-systems / tiny-100-light-j4/batch10 | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 19.537 ms | make | 6.873 | 2.84× | 2.86× cross-node |
| 290 | filesystem-automation / rename-10000 | fresh | 782.918 ms | bun | 279.188 | 2.80× | 13.82× cross-node |
| 291 | shell / metadata-10000 | shell-workloads.json | 124.597 ms | fish | 44.917 | 2.77× | not normalized |
| 292 | filesystem-automation / large-write-10x10485760 | booted | 367.268 ms | python | 133.394 | 2.75× | 2.92× cross-node |
| 293 | build-systems / tiny-100-light-j1/batch10 | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 40.557 ms | make | 15.034 | 2.70× | 3.08× cross-node |
| 294 | concurrency / process-100 | persistent | 88.028 ms | go | 32.722 | 2.69× | 2.41× cross-node |
| 295 | concurrency / process-one-failure | persistent | 88.492 ms | go | 32.902 | 2.69× | 2.35× cross-node |
| 296 | scripting / sanity/noop/small | fresh-process-repeated | 5.855 ms | luajit | 2.180 | 2.69× | not normalized |
| 297 | concurrency / process-100 | fresh | 98.413 ms | go | 37.260 | 2.64× | 2.18× cross-node |
| 298 | filesystem-automation / delete-1000 | fresh | 86.429 ms | go | 32.889 | 2.63× | 11.72× cross-node |
| 299 | concurrency / process-many-failures | persistent | 78.885 ms | go | 30.687 | 2.57× | 2.26× cross-node |
| 300 | filesystem-automation / large-write-100x1048576 | booted | 315.721 ms | python | 124.529 | 2.54× | 2.83× cross-node |
| 301 | filesystem-automation / large-write-10x10485760 | fresh | 387.565 ms | go | 154.285 | 2.51× | 2.56× cross-node |
| 302 | concurrency / pool-light-4 | fresh | 14.070 ms | go | 5.636 | 2.50× | 1.95× cross-node |
| 303 | concurrency / process-many-failures | fresh | 95.028 ms | go | 38.399 | 2.47× | 2.30× cross-node |
| 304 | concurrency / process-one-failure | fresh | 102.732 ms | go | 41.588 | 2.47× | 2.05× cross-node |
| 305 | filesystem-automation / walk-1000 | fresh | 29.888 ms | go | 12.264 | 2.44× | 15.53× cross-node |
| 306 | filesystem-automation / stat-1000 | fresh | 38.179 ms | go | 15.789 | 2.42× | 24.49× cross-node |
| 307 | concurrency / process-10 | persistent | 10.717 ms | go | 4.461 | 2.40× | 1.65× cross-node |
| 308 | build-systems / tiny-1000-light-j4/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1112.796 ms | make | 475.502 | 2.34× | 2.32× cross-node |
| 309 | shell / create-small-100000 | shell-workloads.json | 12170.698 ms | bash | 5210.103 | 2.34× | not normalized |
| 310 | filesystem-automation / rename-1000 | fresh | 87.532 ms | go | 37.894 | 2.31× | 10.91× cross-node |
| 311 | shell / concat-small-10000 | shell-workloads.json | 258.043 ms | fish | 112.276 | 2.30× | not normalized |
| 312 | filesystem-automation / large-write-100x1048576 | fresh | 325.942 ms | go | 142.356 | 2.29× | 2.60× cross-node |
| 313 | template-engines / nested-loops | source-render | 1.089 ms/render | nunjucks | 0.483 | 2.26× | 5.98× cross-node |
| 314 | scripting / dynamic-programming/fibonacci/small | fresh-process-repeated | 4.147 ms | luajit | 1.871 | 2.22× | not normalized |
| 315 | scripting / sanity/output/large | fresh-process-repeated | 3.814 ms | luajit | 1.765 | 2.16× | not normalized |
| 316 | concurrency / nested-10 | fresh | 14.887 ms | go | 6.957 | 2.14× | 1.86× cross-node |
| 317 | build-systems / tiny-100-light-j4/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 96.936 ms | make | 46.477 | 2.09× | 2.40× cross-node |
| 318 | scripting / sanity/output/small | fresh-process-repeated | 3.659 ms | luajit | 1.762 | 2.08× | not normalized |
| 319 | template-engines / many-templates-1000 | source-render | 0.021 ms/render | liquid | 0.010 | 2.04× | 2.17× cross-node |
| 320 | scripting / sanity/noop/large | fresh-process-repeated | 3.310 ms | luajit | 1.634 | 2.03× | not normalized |
| 321 | template-engines / many-templates-10 | source-render | 0.021 ms/render | liquid | 0.011 | 1.97× | 2.03× cross-node |
| 322 | template-engines / many-templates-100 | source-render | 0.021 ms/render | liquid | 0.011 | 1.96× | 2.09× cross-node |
| 323 | concurrency / schedule-10 | fresh | 8.312 ms | go | 4.356 | 1.91× | 1.73× cross-node |
| 324 | build-systems / tiny-100-light-j1/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 242.790 ms | make | 132.183 | 1.84× | 2.06× cross-node |
| 325 | build-systems / tiny-100-light-j2/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 134.747 ms | make | 73.685 | 1.83× | 1.98× cross-node |
| 326 | concurrency / fan-10 | fresh | 8.891 ms | go | 4.874 | 1.82× | 1.59× cross-node |
| 327 | concurrency / tiny-10 | fresh | 8.611 ms | go | 4.789 | 1.80× | 1.64× cross-node |
| 328 | concurrency / process-10 | fresh | 19.188 ms | go | 10.709 | 1.79× | 1.65× cross-node |
| 329 | build-systems / native-1000-heavy-j1/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 383.017 ms | ninja | 213.952 | 1.79× | 2.54× cross-node |
| 330 | build-systems / native-1000-light-j4/target | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 96.046 ms | ninja | 56.506 | 1.70× | 2.03× cross-node |
| 331 | shell / rename-selected-10000 | shell-workloads.json | 591.367 ms | bash | 352.973 | 1.68× | not normalized |
| 332 | shell / copy-small-10000 | shell-workloads.json | 893.480 ms | zsh | 565.223 | 1.58× | not normalized |
| 333 | concurrency / mixed-64 | persistent | 86.083 ms | go | 54.877 | 1.57× | 1.53× cross-node |
| 334 | concurrency / mixed-64 | fresh | 90.836 ms | go | 60.018 | 1.51× | 1.44× cross-node |
| 335 | concurrency / failures | fresh | 9.954 ms | go | 6.590 | 1.51× | 1.57× cross-node |
| 336 | build-systems / native-1000-light-j4/relink | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 196.341 ms | ninja | 130.909 | 1.50× | 1.79× cross-node |
| 337 | build-systems / native-100-light-j1/relink | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 68.942 ms | make | 47.391 | 1.45× | 1.92× cross-node |
| 338 | template-engines / loop-100 | source-render | 0.360 ms/render | nunjucks | 0.253 | 1.42× | 4.71× cross-node |
| 339 | template-engines / many-renders-1000 | source-render | 0.022 ms/render | liquid | 0.015 | 1.41× | 1.46× cross-node |
| 340 | build-systems / native-10000-light-j4/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1986.184 ms | ninja | 1411.246 | 1.41× | 1.78× cross-node |
| 341 | build-systems / native-1000-heavy-j2/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 310.577 ms | ninja | 220.991 | 1.41× | 1.92× cross-node |
| 342 | build-systems / native-5000-light-j4/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1043.840 ms | ninja | 743.613 | 1.40× | 1.73× cross-node |
| 343 | concurrency / process-mixed | persistent | 105.262 ms | go | 75.021 | 1.40× | 1.36× cross-node |
| 344 | concurrency / process-mixed | fresh | 113.424 ms | go | 81.269 | 1.40× | 1.39× cross-node |
| 345 | build-systems / native-100-light-j4/target | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 36.544 ms | make | 26.926 | 1.36× | 1.41× cross-node |
| 346 | shell / selected-cleanup | shell-workloads.json | 48.621 ms | bash | 35.839 | 1.36× | not normalized |
| 347 | build-systems / native-100-light-j1/private | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 96.945 ms | make | 71.542 | 1.36× | 1.61× cross-node |
| 348 | shell / bare/immediate-exit | shell-repeated.json | 2.647 ms | bash | 1.955 | 1.35× | not normalized |
| 349 | shell / bare/trivial-command | shell-application-cold.json | 2.398 ms | bash | 1.779 | 1.35× | not normalized |
| 350 | template-engines / many-renders-100 | source-render | 0.021 ms/render | liquid | 0.016 | 1.34× | 1.41× cross-node |
| 351 | build-systems / native-100-light-j1/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 97.995 ms | make | 73.198 | 1.34× | 1.67× cross-node |
| 352 | build-systems / native-1000-light-j4/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 243.262 ms | ninja | 181.964 | 1.34× | 1.54× cross-node |
| 353 | shell / bare/trivial-command | shell-repeated.json | 2.381 ms | bash | 1.790 | 1.33× | not normalized |
| 354 | template-engines / includes-8 | source-render | 0.159 ms/render | nunjucks | 0.119 | 1.33× | 1.32× cross-node |
| 355 | shell / bare/immediate-exit | shell-application-cold.json | 2.638 ms | bash | 1.985 | 1.33× | not normalized |
| 356 | shell / processes-1 | shell-workloads.json | 4.149 ms | bash | 3.126 | 1.33× | not normalized |
| 357 | shell / processes-1000 | shell-workloads.json | 1015.337 ms | fish | 770.403 | 1.32× | not normalized |
| 358 | build-systems / native-1000-light-j4/private | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 244.627 ms | ninja | 186.416 | 1.31× | 1.60× cross-node |
| 359 | build-systems / native-100-light-j2/target | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 35.274 ms | make | 26.952 | 1.31× | 1.28× cross-node |
| 360 | build-systems / native-100-light-j1/target | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 36.125 ms | make | 27.734 | 1.30× | 1.41× cross-node |
| 361 | build-systems / native-1000-light-j4/batch10 | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 352.375 ms | ninja | 270.869 | 1.30× | 1.31× cross-node |
| 362 | shell / bare/file-roundtrip | shell-repeated.json | 5.482 ms | bash | 4.256 | 1.29× | not normalized |
| 363 | shell / bare/function-string | shell-application-cold.json | 2.492 ms | bash | 1.941 | 1.28× | not normalized |
| 364 | build-systems / native-100-light-j2/relink | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 62.000 ms | ninja | 48.332 | 1.28× | 1.54× cross-node |
| 365 | shell / bare/function-string | shell-repeated.json | 2.502 ms | bash | 1.951 | 1.28× | not normalized |
| 366 | shell / bare/file-roundtrip | shell-application-cold.json | 5.482 ms | bash | 4.287 | 1.28× | not normalized |
| 367 | build-systems / native-100-light-j2/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 87.978 ms | make | 69.024 | 1.27× | 1.32× cross-node |
| 368 | shell / processes-100 | shell-workloads.json | 103.799 ms | fish | 81.445 | 1.27× | not normalized |
| 369 | website-generator / 10000pages/application-cold | official fresh fixture or reused warm fixture as defined | 3739.039 ms | Hugo | 2942.571 | 1.27× | not normalized |
| 370 | build-systems / native-1000-heavy-j4/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 282.094 ms | ninja | 222.516 | 1.27× | 1.52× cross-node |
| 371 | shell / bare/external-100 | shell-repeated.json | 105.603 ms | fish | 83.721 | 1.26× | not normalized |
| 372 | shell / bare/external-100 | shell-application-cold.json | 103.474 ms | fish | 82.411 | 1.26× | not normalized |
| 373 | build-systems / native-100-light-j4/relink | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 57.825 ms | ninja | 46.323 | 1.25× | 1.40× cross-node |
| 374 | build-systems / native-100-light-j4/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 82.751 ms | make | 66.299 | 1.25× | 1.25× cross-node |
| 375 | build-systems / native-100-light-j2/private | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 87.155 ms | make | 70.173 | 1.24× | 1.46× cross-node |
| 376 | shell / delete-tree-100000 | shell-workloads.json | 3027.960 ms | bash | 2455.690 | 1.23× | not normalized |
| 377 | build-systems / native-100-heavy-j1/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 124.852 ms | make | 101.564 | 1.23× | 1.40× cross-node |
| 378 | build-systems / native-100-light-j1/batch10pct | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 334.663 ms | make | 274.280 | 1.22× | 1.25× cross-node |
| 379 | build-systems / native-100-light-j2/batch10 | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 204.535 ms | make | 168.726 | 1.21× | 1.29× cross-node |
| 380 | build-systems / native-100-light-j4/private | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 83.087 ms | make | 68.792 | 1.21× | 1.31× cross-node |
| 381 | shell / bare/command-capture | shell-repeated.json | 3.936 ms | bash | 3.281 | 1.20× | not normalized |
| 382 | build-systems / native-10000-light-j4/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 64888.828 ms | make | 54158.282 | 1.20× | 1.09× cross-node |
| 383 | shell / bare/short-pipeline | shell-application-cold.json | 5.449 ms | bash | 4.555 | 1.20× | not normalized |
| 384 | shell / pipeline-8 | shell-workloads.json | 13.416 ms | fish | 11.300 | 1.19× | not normalized |
| 385 | build-systems / native-100-heavy-j2/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 119.593 ms | make | 101.240 | 1.18× | 1.31× cross-node |
| 386 | shell / processes-10 | shell-workloads.json | 13.158 ms | fish | 11.183 | 1.18× | not normalized |
| 387 | shell / delete-selected-10000 | shell-workloads.json | 252.207 ms | zsh | 214.582 | 1.18× | not normalized |
| 388 | shell / bare/short-pipeline | shell-repeated.json | 5.510 ms | bash | 4.693 | 1.17× | not normalized |
| 389 | build-systems / native-100-light-j4/medium | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 132.003 ms | make | 112.474 | 1.17× | 1.19× cross-node |
| 390 | build-systems / native-10000-light-j4/global | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 61391.417 ms | make | 52365.779 | 1.17× | 1.12× cross-node |
| 391 | build-systems / native-100-light-j4/batch10pct | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 130.258 ms | make | 111.239 | 1.17× | 1.22× cross-node |
| 392 | build-systems / native-100-heavy-j4/leaf | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 116.651 ms | make | 100.069 | 1.17× | 1.28× cross-node |
| 393 | build-systems / native-1000-light-j4/batch10pct | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 825.868 ms | make | 709.698 | 1.16× | 1.21× cross-node |
| 394 | build-systems / native-100-light-j2/batch10pct | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 198.321 ms | make | 170.492 | 1.16× | 1.25× cross-node |
| 395 | build-systems / native-100-light-j1/medium | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 273.029 ms | make | 236.031 | 1.16× | 1.24× cross-node |
| 396 | build-systems / native-100-light-j4/batch10 | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 133.209 ms | make | 115.316 | 1.16× | 1.25× cross-node |
| 397 | build-systems / native-1000-light-j4/generated | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 5729.143 ms | make | 4961.730 | 1.15× | 1.17× cross-node |
| 398 | build-systems / native-100-light-j4/generated | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 662.850 ms | make | 574.860 | 1.15× | 1.14× cross-node |
| 399 | shell / pipeline-2 | shell-workloads.json | 5.482 ms | bash | 4.792 | 1.14× | not normalized |
| 400 | build-systems / native-100-light-j1/batch10 | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 318.623 ms | make | 278.868 | 1.14× | 1.24× cross-node |
| 401 | shell / pipeline-4 | shell-workloads.json | 8.095 ms | fish | 7.094 | 1.14× | not normalized |
| 402 | shell / bare/command-capture | shell-application-cold.json | 3.881 ms | bash | 3.412 | 1.14× | not normalized |
| 403 | build-systems / native-100-light-j4/global | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 600.987 ms | make | 531.771 | 1.13× | 1.06× cross-node |
| 404 | shell / delete-selected-100000 | shell-workloads.json | 2847.672 ms | bash | 2529.888 | 1.13× | not normalized |
| 405 | build-systems / native-100-light-j2/medium | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 169.120 ms | make | 150.883 | 1.12× | 1.25× cross-node |
| 406 | build-systems / native-100-light-j1/generated | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 2225.920 ms | make | 1986.189 | 1.12× | 1.13× cross-node |
| 407 | build-systems / native-5000-light-j4/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 29575.271 ms | make | 26434.667 | 1.12× | 1.10× cross-node |
| 408 | build-systems / native-100-light-j2/generated | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1206.581 ms | make | 1078.512 | 1.12× | 1.11× cross-node |
| 409 | build-systems / native-1000-light-j4/global | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 5463.286 ms | make | 4897.444 | 1.12× | 1.08× cross-node |
| 410 | build-systems / native-1000-light-j4/medium | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 764.766 ms | make | 686.846 | 1.11× | 1.27× cross-node |
| 411 | build-systems / native-5000-light-j4/global | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 29109.104 ms | make | 26170.598 | 1.11× | 1.13× cross-node |
| 412 | build-systems / native-100-light-j4/clean-rebuild | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 660.451 ms | make | 598.021 | 1.10× | 1.11× cross-node |
| 413 | shell / create-empty-100000 | shell-workloads.json | 4023.763 ms | bash | 3653.643 | 1.10× | not normalized |
| 414 | build-systems / native-1000-light-j4/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 5631.814 ms | make | 5114.482 | 1.10× | 1.05× cross-node |
| 415 | build-systems / native-100-light-j2/global | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1139.787 ms | make | 1036.590 | 1.10× | 1.08× cross-node |
| 416 | build-systems / native-100-light-j4/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 652.883 ms | make | 594.974 | 1.10× | 1.12× cross-node |
| 417 | build-systems / native-100-light-j1/global | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 2135.681 ms | make | 1962.283 | 1.09× | 1.09× cross-node |
| 418 | shell / create-empty-1000 | shell-workloads.json | 39.869 ms | bash | 36.673 | 1.09× | not normalized |
| 419 | build-systems / native-100-light-j1/clean-rebuild | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 2265.480 ms | make | 2084.700 | 1.09× | 1.10× cross-node |
| 420 | shell / create-empty-10000 | shell-workloads.json | 384.613 ms | bash | 355.444 | 1.08× | not normalized |
| 421 | build-systems / native-100-light-j2/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1224.345 ms | make | 1131.530 | 1.08× | 1.09× cross-node |
| 422 | website-generator / 1000pages/application-cold | official fresh fixture or reused warm fixture as defined | 337.575 ms | Hugo | 314.176 | 1.07× | not normalized |
| 423 | build-systems / native-100-light-j2/clean-rebuild | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1201.926 ms | make | 1125.586 | 1.07× | 1.10× cross-node |
| 424 | build-systems / native-1000-light-j4/clean-rebuild | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 5576.247 ms | make | 5224.529 | 1.07× | 1.09× cross-node |
| 425 | shell / delete-selected-1000 | shell-workloads.json | 27.000 ms | bash | 25.300 | 1.07× | not normalized |
| 426 | build-systems / native-100-light-j1/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 2223.858 ms | make | 2098.049 | 1.06× | 1.09× cross-node |
| 427 | build-systems / native-1000-heavy-j4/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 13794.567 ms | make | 13128.810 | 1.05× | 1.09× cross-node |
| 428 | build-systems / native-100-heavy-j4/global | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1423.202 ms | make | 1359.146 | 1.05× | 1.00× cross-node |
| 429 | build-systems / native-100-heavy-j1/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 5491.177 ms | make | 5257.428 | 1.04× | 1.02× cross-node |
| 430 | build-systems / native-1000-heavy-j2/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 27520.569 ms | make | 26439.180 | 1.04× | 1.08× cross-node |
| 431 | build-systems / native-100-heavy-j2/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 2792.003 ms | make | 2682.665 | 1.04× | 1.03× cross-node |
| 432 | build-systems / native-1000-heavy-j1/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 53716.564 ms | ninja | 51645.612 | 1.04× | 1.03× cross-node |
| 433 | shell / function-calls | shell-workloads.json | 46.722 ms | nu | 45.153 | 1.03× | not normalized |
| 434 | shell / log-filter-group | shell-workloads.json | 51.493 ms | bash | 49.889 | 1.03× | not normalized |
| 435 | build-systems / native-100-heavy-j4/full | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1484.603 ms | make | 1439.659 | 1.03× | 1.04× cross-node |
| 436 | build-systems / native-100-heavy-j1/global | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 5308.101 ms | make | 5151.897 | 1.03× | 1.05× cross-node |
| 437 | shell / source-tree-report | shell-workloads.json | 248.632 ms | bash | 241.409 | 1.03× | not normalized |
| 438 | build-systems / native-100-heavy-j2/global | C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 2774.185 ms | make | 2710.243 | 1.02× | 1.07× cross-node |
| 439 | shell / bare/interactive | shell-application-cold.json | 2.223 ms | bash | 2.296 | 0.97× | not normalized |
| 440 | template-engines / article | source-render | 0.278 ms/render | nunjucks | 0.289 | 0.96× | 1.57× cross-node |
| 441 | shell / bare/interactive | shell-repeated.json | 2.182 ms | bash | 2.265 | 0.96× | not normalized |
| 442 | shell / bare/native-sum | shell-application-cold.json | 3.348 ms | zsh | 3.498 | 0.96× | not normalized |
| 443 | shell / bare/native-sum | shell-repeated.json | 3.341 ms | zsh | 3.528 | 0.95× | not normalized |
| 444 | website-generator / 1000pages/warm-full | official fresh fixture or reused warm fixture as defined | 287.263 ms | Hugo | 303.421 | 0.95× | not normalized |
| 445 | website-generator / 10000pages/warm-full | official fresh fixture or reused warm fixture as defined | 2999.171 ms | Hugo | 3182.135 | 0.94× | not normalized |
| 446 | template-engines / includes-4 | source-render | 0.089 ms/render | nunjucks | 0.101 | 0.88× | 0.95× cross-node |
| 447 | shell / fibonacci-mod | shell-workloads.json | 4.238 ms | zsh | 4.862 | 0.87× | not normalized |
| 448 | template-engines / loop-10000 | fresh | 74.001 ms/invocation | nunjucks | 94.838 | 0.78× | 1.71× cross-node |
| 449 | template-engines / interpolation | source-render | 0.026 ms/render | liquid | 0.034 | 0.77× | 0.84× cross-node |
| 450 | task-runners / mixed-1000-j4/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 13829.675 ms | nx | 18414.227 | 0.75× | 0.65× cross-node |
| 451 | task-runners / mixed-100-j2/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 2602.624 ms | nx | 3514.926 | 0.74× | 0.73× cross-node |
| 452 | task-runners / mixed-100-j1/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 4759.579 ms | nx | 6430.672 | 0.74× | 0.77× cross-node |
| 453 | scripting / filesystem/traverse/small | fresh-process-repeated | 4.675 ms | luajit | 6.719 | 0.70× | not normalized |
| 454 | task-runners / mixed-1000-j4/shared | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 6995.226 ms | nx | 10424.701 | 0.67× | 0.62× cross-node |
| 455 | shell / arithmetic | shell-workloads.json | 17.556 ms | zsh | 26.206 | 0.67× | not normalized |
| 456 | shell / moderate/interactive | shell-application-cold.json | 3.005 ms | bash | 4.488 | 0.67× | not normalized |
| 457 | task-runners / mixed-100-j4/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 1455.905 ms | nx | 2177.828 | 0.67× | 0.61× cross-node |
| 458 | shell / moderate/interactive | shell-repeated.json | 2.954 ms | bash | 4.430 | 0.67× | not normalized |
| 459 | shell / light/interactive | shell-application-cold.json | 2.597 ms | bash | 4.262 | 0.61× | not normalized |
| 460 | shell / light/interactive | shell-repeated.json | 2.542 ms | bash | 4.184 | 0.61× | not normalized |
| 461 | template-engines / condition | source-render | 0.021 ms/render | liquid | 0.039 | 0.55× | 0.59× cross-node |
| 462 | template-engines / includes-1 | source-render | 0.041 ms/render | liquid | 0.073 | 0.55× | 0.51× cross-node |
| 463 | task-runners / mixed-100-j4/shared | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 909.355 ms | nx | 1651.660 | 0.55× | 0.60× cross-node |
| 464 | template-engines / nested-object | source-render | 0.023 ms/render | liquid | 0.042 | 0.55× | 0.54× cross-node |
| 465 | template-engines / transform | source-render | 0.021 ms/render | liquid | 0.038 | 0.54× | 0.61× cross-node |
| 466 | shell / empty/interactive | shell-repeated.json | 2.200 ms | bash | 4.113 | 0.53× | not normalized |
| 467 | shell / empty/interactive | shell-application-cold.json | 2.159 ms | bash | 4.153 | 0.52× | not normalized |
| 468 | template-engines / loop-10 | source-render | 0.061 ms/render | nunjucks | 0.129 | 0.48× | 1.11× cross-node |
| 469 | template-engines / includes-8 | files | 0.289 ms/render | nunjucks | 0.616 | 0.47× | 0.45× cross-node |
| 470 | template-engines / includes-4 | files | 0.166 ms/render | nunjucks | 0.394 | 0.42× | 0.44× cross-node |
| 471 | task-runners / mixed-1000-j4/fanout | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 1506.146 ms | nx | 3642.456 | 0.41× | 0.40× cross-node |
| 472 | task-runners / mixed-20-j4/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 455.552 ms | nx | 1109.375 | 0.41× | 0.40× cross-node |
| 473 | task-runners / mixed-20-j4/uncached-full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 449.246 ms | nx | 1100.772 | 0.41× | 0.40× cross-node |
| 474 | website-generator / 100pages/application-cold | official fresh fixture or reused warm fixture as defined | 38.998 ms | Hugo | 100.079 | 0.39× | not normalized |
| 475 | task-runners / mixed-20-j4/shared | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 405.928 ms | nx | 1109.660 | 0.37× | 0.37× cross-node |
| 476 | template-engines / includes-1 | files | 0.075 ms/render | nunjucks | 0.209 | 0.36× | 0.41× cross-node |
| 477 | task-runners / mixed-20-j4/target-subgraph | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 398.739 ms | nx | 1117.192 | 0.36× | 0.37× cross-node |
| 478 | website-generator / 100pages/warm-full | official fresh fixture or reused warm fixture as defined | 33.040 ms | Hugo | 99.283 | 0.33× | not normalized |
| 479 | scripting / structured-data/json-transform/small | fresh-process-repeated | 10.185 ms | python | 32.257 | 0.32× | not normalized |
| 480 | template-engines / collection | fresh | 17.563 ms/invocation | nunjucks | 60.855 | 0.29× | 0.58× cross-node |
| 481 | task-runners / mixed-1000-j4/noop | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 116.052 ms | turbo | 448.494 | 0.26× | 0.28× cross-node |
| 482 | scripting / structured-data/json-traverse/small | fresh-process-repeated | 8.186 ms | python | 34.804 | 0.24× | not normalized |
| 483 | task-runners / mixed-1000-j4/leaf | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 168.475 ms | turbo | 760.235 | 0.22× | 0.23× cross-node |
| 484 | task-runners / tiny-1000-j4/noop | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 94.904 ms | turbo | 429.131 | 0.22× | 0.24× cross-node |
| 485 | task-runners / mixed-100-j4/noop | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 15.662 ms | turbo | 72.615 | 0.22× | 0.21× cross-node |
| 486 | template-engines / many-templates-1000 | fresh | 33.820 ms/invocation | liquid | 158.811 | 0.21× | 0.21× cross-node |
| 487 | task-runners / tiny-100-j4/noop | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 13.368 ms | turbo | 70.396 | 0.19× | 0.22× cross-node |
| 488 | template-engines / loop-1000 | fresh | 10.476 ms/invocation | nunjucks | 56.397 | 0.19× | 0.35× cross-node |
| 489 | task-runners / mixed-100-j4/fanout | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 164.566 ms | nx | 918.172 | 0.18× | 0.18× cross-node |
| 490 | scripting / structured-data/json-parse/small | fresh-process-repeated | 6.521 ms | python | 38.055 | 0.17× | not normalized |
| 491 | template-engines / many-renders-1000 | fresh | 25.767 ms/invocation | liquid | 167.375 | 0.15× | 0.15× cross-node |
| 492 | task-runners / mixed-100-j4/leaf | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 64.114 ms | turbo | 423.983 | 0.15× | 0.15× cross-node |
| 493 | task-runners / tiny-1000-j4/leaf | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 99.942 ms | turbo | 694.264 | 0.14× | 0.16× cross-node |
| 494 | task-runners / mixed-20-j4/fanout | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 60.539 ms | turbo | 444.168 | 0.14× | 0.14× cross-node |
| 495 | task-runners / tiny-1000-j4/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 1457.303 ms | nx | 10830.442 | 0.13× | 0.11× cross-node |
| 496 | task-runners / mixed-20-j4/leaf | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 55.061 ms | turbo | 415.621 | 0.13× | 0.13× cross-node |
| 497 | task-runners / mixed-20-j4/target-leaf | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 54.437 ms | turbo | 423.341 | 0.13× | 0.13× cross-node |
| 498 | task-runners / mixed-20-j4/multi-target | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 54.831 ms | turbo | 439.947 | 0.12× | 0.13× cross-node |
| 499 | task-runners / mixed-20-j4/noop | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 6.950 ms | turbo | 58.651 | 0.12× | 0.14× cross-node |
| 500 | template-engines / nested-loops | fresh | 5.711 ms/invocation | nunjucks | 52.368 | 0.11× | 0.14× cross-node |
| 501 | task-runners / tiny-1000-j4/fanout | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 240.522 ms | nx | 2550.482 | 0.09× | 0.10× cross-node |
| 502 | template-engines / loop-100 | fresh | 4.673 ms/invocation | nunjucks | 51.498 | 0.09× | 0.11× cross-node |
| 503 | template-engines / many-templates-100 | fresh | 6.953 ms/invocation | liquid | 79.544 | 0.09× | 0.09× cross-node |
| 504 | template-engines / article | fresh | 4.318 ms/invocation | nunjucks | 51.942 | 0.08× | 0.08× cross-node |
| 505 | task-runners / tiny-100-j4/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 116.526 ms | nx | 1404.365 | 0.08× | 0.09× cross-node |
| 506 | template-engines / literal | fresh | 3.917 ms/invocation | nunjucks | 48.173 | 0.08× | 0.08× cross-node |
| 507 | template-engines / transform | fresh | 3.946 ms/invocation | nunjucks | 49.010 | 0.08× | 0.08× cross-node |
| 508 | template-engines / condition | fresh | 4.055 ms/invocation | nunjucks | 50.355 | 0.08× | 0.08× cross-node |
| 509 | template-engines / loop-10 | fresh | 4.087 ms/invocation | nunjucks | 51.372 | 0.08× | 0.08× cross-node |
| 510 | template-engines / many-templates-10 | fresh | 4.124 ms/invocation | nunjucks | 52.388 | 0.08× | 0.07× cross-node |
| 511 | template-engines / nested-object | fresh | 3.927 ms/invocation | nunjucks | 50.023 | 0.08× | 0.08× cross-node |
| 512 | template-engines / includes-1 | fresh | 3.921 ms/invocation | nunjucks | 50.284 | 0.08× | 0.07× cross-node |
| 513 | template-engines / interpolation | fresh | 3.901 ms/invocation | nunjucks | 50.401 | 0.08× | 0.08× cross-node |
| 514 | template-engines / many-renders-100 | fresh | 5.850 ms/invocation | liquid | 75.591 | 0.08× | 0.08× cross-node |
| 515 | template-engines / includes-8 | fresh | 4.061 ms/invocation | nunjucks | 54.251 | 0.07× | 0.08× cross-node |
| 516 | template-engines / includes-4 | fresh | 3.972 ms/invocation | nunjucks | 53.366 | 0.07× | 0.07× cross-node |
| 517 | task-runners / tiny-1000-j4/one-percent | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 112.575 ms | turbo | 1518.250 | 0.07× | 0.08× cross-node |
| 518 | task-runners / tiny-100-j4/one-percent | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 18.067 ms | turbo | 378.943 | 0.05× | 0.05× cross-node |
| 519 | task-runners / tiny-100-j4/leaf | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 17.818 ms | turbo | 386.138 | 0.05× | 0.05× cross-node |
| 520 | task-runners / tiny-100-j4/fanout | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 25.311 ms | nx | 746.596 | 0.03× | 0.03× cross-node |

## Improved substantially but still uncompetitive

| Scenario | Same-node improvement | Official current deficit | Interpretation |
|---|---:|---:|---|
| Filesystem stat10k | 91.01% | 3.87× Bun | Huge gain; still behind |
| Filesystem walk10k | 85.52% | 6.98× Bun | Huge gain; materially behind |
| Concurrency queue100k4→4 | 67.04% | 208.76× Bun | Massive gain; still severe |
| Template loop10k source-render | 71.82% | 15.35× Handlebars | Major gain; hot rendering still uncompetitive |

## New regression on top of an old weakness

| Scenario | Same-node regression | Official peer deficit | Evidence |
|---|---:|---:|---|
| Scripting calls large | 145.76% | 289.09× LuaJIT | Disjoint ranges;10/10 slower |
| Shell calls | 119.68% | see shell official boundary | Independent suite corroborates call-path slowdown |

Call/source/value staging is an evidence-supported lead; no shared causal commit proved. Website freshfull38.29% is a separate central-product release blocker.

## Historical cross-node trends — separate ranking

| Rank | Benchmark / scenario / boundary | Old | Candidate | Change | Unit |
|---:|---|---:|---:|---:|---|
| 1 | scripting / sanity/function-calls/large / fresh-process-repeated | 185.103 | 546.056 | +195.00% | ms |
| 2 | scripting / sanity/function-calls/small / fresh-process-repeated | 4.987 | 10.027 | +101.08% | ms |
| 3 | scripting / structured-data/json-parse/large / fresh-process-repeated | 192.276 | 295.195 | +53.53% | ms |
| 4 | scripting / graphs-trees-search/bfs/large / fresh-process-repeated | 654.593 | 1002.530 | +53.15% | ms |
| 5 | scripting / arrays-strings-hash/frequency-count/large / fresh-process-repeated | 385.547 | 589.370 | +52.87% | ms |
| 6 | scripting / structured-data/json-transform/large / fresh-process-repeated | 464.025 | 669.316 | +44.24% | ms |
| 7 | scripting / sanity/output/large / fresh-process-repeated | 2.709 | 3.814 | +40.77% | ms |
| 8 | scripting / graphs-trees-search/bfs/small / fresh-process-repeated | 10.358 | 14.471 | +39.70% | ms |
| 9 | scripting / arrays-strings-hash/frequency-count/small / fresh-process-repeated | 7.112 | 9.813 | +37.98% | ms |
| 10 | scripting / structured-data/json-transform/small / fresh-process-repeated | 7.439 | 10.185 | +36.91% | ms |
| 11 | concurrency / pool-light-1 / persistent | 16.488 | 22.541 | +36.72% | ms |
| 12 | scripting / sanity/loops/small / fresh-process-repeated | 3.852 | 5.251 | +36.29% | ms |
| 13 | scripting / arrays-strings-hash/sliding-window/small / fresh-process-repeated | 5.867 | 7.923 | +35.06% | ms |
| 14 | scripting / dynamic-programming/fibonacci/small / fresh-process-repeated | 3.083 | 4.147 | +34.48% | ms |
| 15 | scripting / arrays-strings-hash/map-set/small / fresh-process-repeated | 5.173 | 6.940 | +34.16% | ms |
| 16 | scripting / structured-data/json-parse/small / fresh-process-repeated | 4.877 | 6.521 | +33.71% | ms |
| 17 | build-systems / tiny-10000-light-j4/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 13315.922 | 17762.305 | +33.39% | ms |
| 18 | scripting / arrays-strings-hash/map-set/large / fresh-process-repeated | 215.188 | 284.963 | +32.43% | ms |
| 19 | scripting / structured-data/json-traverse/large / fresh-process-repeated | 357.846 | 473.779 | +32.40% | ms |
| 20 | scripting / filesystem/traverse/large / fresh-process-repeated | 32.037 | 41.798 | +30.47% | ms |
| 21 | scripting / sanity/noop/large / fresh-process-repeated | 2.553 | 3.310 | +29.68% | ms |
| 22 | scripting / filesystem/traverse/small / fresh-process-repeated | 3.624 | 4.675 | +29.00% | ms |
| 23 | scripting / arrays-strings-hash/scan/small / fresh-process-repeated | 4.129 | 5.315 | +28.72% | ms |
| 24 | scripting / structured-data/json-traverse/small / fresh-process-repeated | 6.380 | 8.186 | +28.31% | ms |
| 25 | concurrency / fan-1000 / fresh | 271.582 | 339.842 | +25.13% | ms |
| 26 | scripting / sanity/noop/small / fresh-process-repeated | 4.721 | 5.855 | +24.03% | ms |
| 27 | scripting / sanity/output/small / fresh-process-repeated | 2.959 | 3.659 | +23.67% | ms |
| 28 | scripting / arrays-strings-hash/sliding-window/large / fresh-process-repeated | 271.359 | 328.926 | +21.21% | ms |
| 29 | concurrency / pool-light-2 / persistent | 10.645 | 12.648 | +18.82% | ms |
| 30 | template-engines / condition / fresh | 3.457 | 4.055 | +17.27% | ms/invocation |
| 31 | template-engines / many-templates-10 / fresh | 3.517 | 4.124 | +17.24% | ms/invocation |
| 32 | scripting / arrays-strings-hash/scan/large / fresh-process-repeated | 88.809 | 103.618 | +16.67% | ms |
| 33 | concurrency / files-100 / persistent | 17.054 | 19.850 | +16.40% | ms |
| 34 | concurrency / files-10000 / fresh | 1385.434 | 1608.951 | +16.13% | ms |
| 35 | concurrency / pool-light-4 / persistent | 6.902 | 8.004 | +15.97% | ms |
| 36 | scripting / arrays-strings-hash/sort-index/small / fresh-process-repeated | 8.230 | 9.541 | +15.93% | ms |
| 37 | template-engines / literal / fresh | 3.392 | 3.917 | +15.46% | ms/invocation |
| 38 | concurrency / fan-100 / fresh | 21.550 | 24.618 | +14.24% | ms |
| 39 | template-engines / includes-4 / fresh | 3.501 | 3.972 | +13.44% | ms/invocation |
| 40 | template-engines / includes-1 / fresh | 3.474 | 3.921 | +12.85% | ms/invocation |
| 41 | template-engines / interpolation / fresh | 3.466 | 3.901 | +12.54% | ms/invocation |
| 42 | template-engines / transform / fresh | 3.554 | 3.946 | +11.03% | ms/invocation |
| 43 | template-engines / nested-object / fresh | 3.538 | 3.927 | +10.98% | ms/invocation |
| 44 | template-engines / loop-10 / fresh | 3.689 | 4.087 | +10.79% | ms/invocation |
| 45 | scripting / sanity/loops/large / fresh-process-repeated | 74.997 | 82.525 | +10.04% | ms |
| 46 | concurrency / files-10000 / persistent | 1448.103 | 1589.358 | +9.75% | ms |
| 47 | concurrency / pool-light-1 / fresh | 25.187 | 27.460 | +9.02% | ms |
| 48 | template-engines / many-templates-100 / fresh | 6.439 | 6.953 | +7.99% | ms/invocation |
| 49 | scripting / dynamic-programming/fibonacci/large / fresh-process-repeated | 152.071 | 164.168 | +7.95% | ms |
| 50 | template-engines / nested-object / source-render | 0.021 | 0.023 | +7.72% | ms/render |
| 51 | template-engines / many-templates-10 / source-render | 0.020 | 0.021 | +7.56% | ms/render |
| 52 | concurrency / process-one-failure / fresh | 95.537 | 102.732 | +7.53% | ms |
| 53 | concurrency / files-1000 / persistent | 150.382 | 161.134 | +7.15% | ms |
| 54 | concurrency / process-one-failure / persistent | 82.619 | 88.492 | +7.11% | ms |
| 55 | template-engines / includes-8 / fresh | 3.792 | 4.061 | +7.08% | ms/invocation |
| 56 | template-engines / many-templates-1000 / source-render | 0.020 | 0.021 | +6.53% | ms/render |
| 57 | template-engines / many-templates-1000 / fresh | 31.760 | 33.820 | +6.48% | ms/invocation |
| 58 | template-engines / includes-4 / files | 0.156 | 0.166 | +6.40% | ms/render |
| 59 | concurrency / pool-light-2 / fresh | 17.130 | 18.198 | +6.23% | ms |
| 60 | template-engines / interpolation / source-render | 0.025 | 0.026 | +5.87% | ms/render |
| 61 | concurrency / process-100 / fresh | 93.137 | 98.413 | +5.67% | ms |
| 62 | template-engines / many-renders-100 / fresh | 5.540 | 5.850 | +5.59% | ms/invocation |
| 63 | template-engines / includes-8 / files | 0.274 | 0.289 | +5.56% | ms/render |
| 64 | template-engines / transform / source-render | 0.020 | 0.021 | +5.41% | ms/render |
| 65 | template-engines / many-renders-1000 / fresh | 24.484 | 25.767 | +5.24% | ms/invocation |
| 66 | template-engines / many-renders-1000 / source-render | 0.021 | 0.022 | +4.92% | ms/render |
| 67 | concurrency / files-100 / fresh | 24.279 | 25.392 | +4.59% | ms |
| 68 | template-engines / includes-4 / source-render | 0.085 | 0.089 | +4.58% | ms/render |
| 69 | concurrency / files-1000 / fresh | 162.225 | 168.950 | +4.15% | ms |
| 70 | template-engines / many-templates-100 / source-render | 0.020 | 0.021 | +4.12% | ms/render |
| 71 | concurrency / pool-medium-1 / persistent | 31.897 | 33.129 | +3.86% | ms |
| 72 | template-engines / condition / source-render | 0.021 | 0.021 | +3.83% | ms/render |
| 73 | template-engines / literal / source-render | 0.014 | 0.015 | +3.80% | ms/render |
| 74 | concurrency / pool-medium-1 / fresh | 36.690 | 37.919 | +3.35% | ms |
| 75 | scripting / arrays-strings-hash/sort-index/large / fresh-process-repeated | 876.868 | 904.664 | +3.17% | ms |
| 76 | template-engines / article / fresh | 4.201 | 4.318 | +2.77% | ms/invocation |
| 77 | template-engines / many-renders-100 / source-render | 0.021 | 0.021 | +2.29% | ms/render |
| 78 | concurrency / pool-medium-2 / persistent | 17.576 | 17.893 | +1.80% | ms |
| 79 | template-engines / includes-1 / source-render | 0.040 | 0.041 | +1.14% | ms/render |
| 80 | template-engines / includes-8 / source-render | 0.159 | 0.159 | -0.26% | ms/render |
| 81 | template-engines / includes-1 / files | 0.076 | 0.075 | -0.86% | ms/render |
| 82 | concurrency / stagger-100 / persistent | 283.336 | 279.584 | -1.32% | ms |
| 83 | concurrency / process-many-failures / fresh | 96.989 | 95.028 | -2.02% | ms |
| 84 | concurrency / waiting-memory-100 / persistent | 268.515 | 262.937 | -2.08% | ms |
| 85 | concurrency / stagger-100 / fresh | 291.779 | 285.665 | -2.10% | ms |
| 86 | concurrency / wait-100 / persistent | 263.893 | 258.189 | -2.16% | ms |
| 87 | build-systems / tiny-1000-light-j4/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1141.603 | 1112.796 | -2.52% | ms |
| 88 | concurrency / process-1000 / fresh | 909.268 | 886.230 | -2.53% | ms |
| 89 | concurrency / wait-100 / fresh | 271.795 | 264.840 | -2.56% | ms |
| 90 | concurrency / mixed-wait-100 / persistent | 91.741 | 89.072 | -2.91% | ms |
| 91 | concurrency / wait-1000 / persistent | 2659.625 | 2576.345 | -3.13% | ms |
| 92 | concurrency / pool-medium-4 / persistent | 11.092 | 10.734 | -3.23% | ms |
| 93 | concurrency / pool-light-4 / fresh | 14.541 | 14.070 | -3.24% | ms |
| 94 | concurrency / process-100 / persistent | 91.162 | 88.028 | -3.44% | ms |
| 95 | concurrency / waiting-memory-100 / fresh | 280.327 | 270.362 | -3.55% | ms |
| 96 | concurrency / wait-1000 / fresh | 2694.718 | 2594.638 | -3.71% | ms |
| 97 | concurrency / mixed-wait-100 / fresh | 99.553 | 95.620 | -3.95% | ms |
| 98 | concurrency / pool-medium-4 / fresh | 17.988 | 17.269 | -4.00% | ms |
| 99 | concurrency / waiting-memory-1000 / persistent | 2918.812 | 2772.812 | -5.00% | ms |
| 100 | concurrency / process-mixed / persistent | 110.845 | 105.262 | -5.04% | ms |
| 101 | concurrency / waiting-memory-1000 / fresh | 2963.834 | 2798.030 | -5.59% | ms |
| 102 | concurrency / tiny-1000 / persistent | 277.564 | 261.055 | -5.95% | ms |
| 103 | concurrency / process-mixed / fresh | 120.736 | 113.424 | -6.06% | ms |
| 104 | template-engines / loop-100 / fresh | 4.985 | 4.673 | -6.26% | ms/invocation |
| 105 | concurrency / tiny-1000 / fresh | 274.828 | 256.266 | -6.75% | ms |
| 106 | build-systems / native-10000-light-j4/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 69612.512 | 64888.828 | -6.79% | ms |
| 107 | concurrency / process-many-failures / persistent | 84.664 | 78.885 | -6.83% | ms |
| 108 | concurrency / pool-medium-2 / fresh | 25.428 | 23.692 | -6.83% | ms |
| 109 | concurrency / process-10 / fresh | 20.599 | 19.188 | -6.85% | ms |
| 110 | concurrency / fan-100 / persistent | 15.353 | 14.262 | -7.11% | ms |
| 111 | build-systems / native-100-light-j4/global / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 648.401 | 600.987 | -7.31% | ms |
| 112 | concurrency / process-1000 / persistent | 902.037 | 835.100 | -7.42% | ms |
| 113 | concurrency / process-10 / persistent | 11.627 | 10.717 | -7.82% | ms |
| 114 | concurrency / mixed-64 / persistent | 93.551 | 86.083 | -7.98% | ms |
| 115 | concurrency / tiny-100 / persistent | 16.242 | 14.888 | -8.33% | ms |
| 116 | concurrency / nested-100 / persistent | 62.165 | 56.421 | -9.24% | ms |
| 117 | filesystem-automation / large-write-10x10485760 / booted | 407.197 | 367.268 | -9.81% | ms |
| 118 | concurrency / mixed-64 / fresh | 100.812 | 90.836 | -9.90% | ms |
| 119 | build-systems / native-1000-light-j4/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 6255.545 | 5631.814 | -9.97% | ms |
| 120 | build-systems / native-100-heavy-j4/global / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1584.150 | 1423.202 | -10.16% | ms |
| 121 | build-systems / native-100-light-j4/generated / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 739.513 | 662.850 | -10.37% | ms |
| 122 | build-systems / native-1000-heavy-j1/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 59944.312 | 53716.564 | -10.39% | ms |
| 123 | filesystem-automation / large-read-10x10485760 / booted | 295.589 | 263.652 | -10.80% | ms |
| 124 | build-systems / native-5000-light-j4/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 33161.803 | 29575.271 | -10.82% | ms |
| 125 | build-systems / native-1000-light-j4/global / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 6162.679 | 5463.286 | -11.35% | ms |
| 126 | build-systems / native-1000-light-j4/generated / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 6473.937 | 5729.143 | -11.50% | ms |
| 127 | concurrency / fan-10 / persistent | 3.704 | 3.265 | -11.85% | ms |
| 128 | build-systems / native-1000-light-j4/clean-rebuild / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 6343.013 | 5576.247 | -12.09% | ms |
| 129 | build-systems / native-100-heavy-j2/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 3176.197 | 2792.003 | -12.10% | ms |
| 130 | concurrency / nested-10 / persistent | 8.821 | 7.742 | -12.23% | ms |
| 131 | build-systems / native-100-light-j2/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1396.189 | 1224.345 | -12.31% | ms |
| 132 | concurrency / schedule-1000 / persistent | 267.316 | 233.856 | -12.52% | ms |
| 133 | build-systems / native-100-heavy-j1/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 6286.044 | 5491.177 | -12.64% | ms |
| 134 | build-systems / native-100-light-j4/medium / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 151.312 | 132.003 | -12.76% | ms |
| 135 | concurrency / fan-10 / fresh | 10.220 | 8.891 | -13.00% | ms |
| 136 | filesystem-automation / large-write-10x10485760 / fresh | 446.184 | 387.565 | -13.14% | ms |
| 137 | concurrency / schedule-1000 / fresh | 264.495 | 229.708 | -13.15% | ms |
| 138 | build-systems / native-5000-light-j4/global / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 33519.083 | 29109.104 | -13.16% | ms |
| 139 | filesystem-automation / large-read-10x10485760 / fresh | 317.567 | 275.122 | -13.37% | ms |
| 140 | build-systems / native-1000-heavy-j2/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 31782.891 | 27520.569 | -13.41% | ms |
| 141 | build-systems / native-100-heavy-j1/global / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 6134.809 | 5308.101 | -13.48% | ms |
| 142 | build-systems / native-100-heavy-j2/global / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 3209.242 | 2774.185 | -13.56% | ms |
| 143 | concurrency / fan-1000 / persistent | 266.203 | 229.789 | -13.68% | ms |
| 144 | filesystem-automation / detect-hash-2-1000 / booted | 2387.647 | 2059.295 | -13.75% | ms |
| 145 | task-runners / mixed-1000-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 134.678 | 116.052 | -13.83% | ms |
| 146 | concurrency / schedule-10 / persistent | 3.502 | 3.013 | -13.95% | ms |
| 147 | build-systems / native-100-heavy-j4/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1726.037 | 1484.603 | -13.99% | ms |
| 148 | build-systems / native-100-light-j2/generated / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1404.547 | 1206.581 | -14.09% | ms |
| 149 | build-systems / native-100-light-j4/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 760.339 | 652.883 | -14.13% | ms |
| 150 | build-systems / native-10000-light-j4/global / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 71765.428 | 61391.417 | -14.46% | ms |
| 151 | build-systems / native-100-light-j4/clean-rebuild / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 772.519 | 660.451 | -14.51% | ms |
| 152 | build-systems / native-100-light-j2/clean-rebuild / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1408.698 | 1201.926 | -14.68% | ms |
| 153 | build-systems / native-1000-light-j4/batch10pct / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 972.265 | 825.868 | -15.06% | ms |
| 154 | filesystem-automation / large-write-100x1048576 / booted | 372.830 | 315.721 | -15.32% | ms |
| 155 | filesystem-automation / detect-hash-2-1000 / fresh | 2394.625 | 2019.836 | -15.65% | ms |
| 156 | build-systems / native-100-light-j2/global / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1355.738 | 1139.787 | -15.93% | ms |
| 157 | build-systems / native-100-heavy-j2/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 142.340 | 119.593 | -15.98% | ms |
| 158 | filesystem-automation / detect-hash-1-1000 / booted | 2378.252 | 1992.423 | -16.22% | ms |
| 159 | task-runners / tiny-1000-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 1741.247 | 1457.303 | -16.31% | ms |
| 160 | filesystem-automation / detect-hash-3-1000 / fresh | 2385.448 | 1996.309 | -16.31% | ms |
| 161 | task-runners / mixed-20-j4/target-subgraph / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 477.659 | 398.739 | -16.52% | ms |
| 162 | filesystem-automation / large-write-100x1048576 / fresh | 390.652 | 325.942 | -16.56% | ms |
| 163 | concurrency / schedule-100 / fresh | 22.406 | 18.692 | -16.58% | ms |
| 164 | filesystem-automation / detect-hash-3-1000 / booted | 2382.486 | 1987.155 | -16.59% | ms |
| 165 | task-runners / mixed-1000-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 203.318 | 168.475 | -17.14% | ms |
| 166 | concurrency / tiny-10 / persistent | 3.633 | 3.006 | -17.26% | ms |
| 167 | build-systems / native-100-light-j1/clean-rebuild / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 2740.129 | 2265.480 | -17.32% | ms |
| 168 | build-systems / native-100-light-j2/batch10 / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 247.580 | 204.535 | -17.39% | ms |
| 169 | filesystem-automation / detect-hash-1-1000 / fresh | 2407.164 | 1988.065 | -17.41% | ms |
| 170 | task-runners / mixed-1000-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 1825.911 | 1506.146 | -17.51% | ms |
| 171 | build-systems / native-100-light-j4/batch10pct / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 157.942 | 130.258 | -17.53% | ms |
| 172 | build-systems / native-100-light-j1/global / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 2591.349 | 2135.681 | -17.58% | ms |
| 173 | concurrency / pool-heavy-2 / fresh | 194.045 | 159.824 | -17.64% | ms |
| 174 | task-runners / tiny-1000-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 115.362 | 94.904 | -17.73% | ms |
| 175 | template-engines / nested-loops / fresh | 6.943 | 5.711 | -17.74% | ms/invocation |
| 176 | build-systems / native-1000-light-j4/batch10 / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 428.843 | 352.375 | -17.83% | ms |
| 177 | build-systems / native-100-light-j1/generated / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 2713.898 | 2225.920 | -17.98% | ms |
| 178 | concurrency / nested-10 / fresh | 18.153 | 14.887 | -17.99% | ms |
| 179 | filesystem-automation / mirror-12-1000 / booted | 2717.647 | 2226.552 | -18.07% | ms |
| 180 | task-runners / mixed-20-j4/target-leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 66.499 | 54.437 | -18.14% | ms |
| 181 | filesystem-automation / clean-1000 / booted | 2495.676 | 2041.598 | -18.19% | ms |
| 182 | build-systems / native-100-light-j4/batch10 / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 163.261 | 133.209 | -18.41% | ms |
| 183 | build-systems / native-100-light-j1/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 2725.794 | 2223.858 | -18.41% | ms |
| 184 | task-runners / mixed-100-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 78.617 | 64.114 | -18.45% | ms |
| 185 | build-systems / native-100-light-j4/target / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 44.858 | 36.544 | -18.53% | ms |
| 186 | filesystem-automation / clean-1000 / fresh | 2511.627 | 2044.397 | -18.60% | ms |
| 187 | task-runners / mixed-20-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 67.987 | 55.061 | -19.01% | ms |
| 188 | build-systems / native-1000-light-j4/medium / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 944.938 | 764.766 | -19.07% | ms |
| 189 | task-runners / mixed-20-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 564.383 | 455.552 | -19.28% | ms |
| 190 | concurrency / schedule-100 / persistent | 16.911 | 13.619 | -19.47% | ms |
| 191 | task-runners / mixed-1000-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 17207.546 | 13829.675 | -19.63% | ms |
| 192 | build-systems / native-100-light-j2/batch10pct / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 246.833 | 198.321 | -19.65% | ms |
| 193 | task-runners / mixed-100-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 19.503 | 15.662 | -19.69% | ms |
| 194 | concurrency / pool-heavy-1 / persistent | 360.219 | 289.215 | -19.71% | ms |
| 195 | filesystem-automation / mirror-11-1000 / fresh | 2756.074 | 2212.627 | -19.72% | ms |
| 196 | task-runners / mixed-1000-j4/shared / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 8716.525 | 6995.226 | -19.75% | ms |
| 197 | concurrency / tiny-10 / fresh | 10.738 | 8.611 | -19.81% | ms |
| 198 | filesystem-automation / mirror-0-1000 / fresh | 2746.026 | 2201.077 | -19.85% | ms |
| 199 | task-runners / mixed-20-j4/uncached-full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 561.923 | 449.246 | -20.05% | ms |
| 200 | build-systems / tiny-100-light-j2/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 168.643 | 134.747 | -20.10% | ms |
| 201 | filesystem-automation / mirror-1-1000 / booted | 2728.258 | 2177.040 | -20.20% | ms |
| 202 | concurrency / pool-heavy-1 / fresh | 374.196 | 298.090 | -20.34% | ms |
| 203 | filesystem-automation / mirror-10-1000 / booted | 2779.361 | 2213.279 | -20.37% | ms |
| 204 | filesystem-automation / mirror-10-1000 / fresh | 2799.917 | 2221.436 | -20.66% | ms |
| 205 | filesystem-automation / detect-hash-2-10000 / fresh | 25258.316 | 20016.924 | -20.75% | ms |
| 206 | concurrency / pool-heavy-2 / persistent | 190.570 | 150.951 | -20.79% | ms |
| 207 | filesystem-automation / clean-10000 / fresh | 25584.467 | 20225.230 | -20.95% | ms |
| 208 | filesystem-automation / mirror-1-1000 / fresh | 2758.028 | 2179.618 | -20.97% | ms |
| 209 | build-systems / native-100-light-j1/batch10pct / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 424.912 | 334.663 | -21.24% | ms |
| 210 | build-systems / native-100-light-j2/medium / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 214.885 | 169.120 | -21.30% | ms |
| 211 | task-runners / mixed-20-j4/shared / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 516.503 | 405.928 | -21.41% | ms |
| 212 | task-runners / mixed-20-j4/multi-target / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 69.917 | 54.831 | -21.58% | ms |
| 213 | filesystem-automation / detect-hash-1-10000 / booted | 24994.973 | 19561.214 | -21.74% | ms |
| 214 | build-systems / native-100-light-j2/target / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 45.074 | 35.274 | -21.74% | ms |
| 215 | build-systems / native-1000-heavy-j4/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 17631.333 | 13794.567 | -21.76% | ms |
| 216 | filesystem-automation / detect-hash-3-10000 / booted | 25289.469 | 19772.223 | -21.82% | ms |
| 217 | build-systems / native-100-light-j4/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 106.009 | 82.751 | -21.94% | ms |
| 218 | filesystem-automation / mirror-12-1000 / fresh | 2762.040 | 2154.643 | -21.99% | ms |
| 219 | filesystem-automation / mirror-11-1000 / booted | 2786.770 | 2173.383 | -22.01% | ms |
| 220 | filesystem-automation / detect-hash-2-10000 / booted | 25509.328 | 19874.134 | -22.09% | ms |
| 221 | concurrency / nested-100 / fresh | 81.891 | 63.798 | -22.09% | ms |
| 222 | task-runners / mixed-100-j2/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 3350.508 | 2602.624 | -22.32% | ms |
| 223 | filesystem-automation / mirror-0-10000 / fresh | 27815.870 | 21590.134 | -22.38% | ms |
| 224 | filesystem-automation / mirror-0-1000 / booted | 2809.307 | 2178.396 | -22.46% | ms |
| 225 | build-systems / native-100-light-j1/target / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 46.614 | 36.125 | -22.50% | ms |
| 226 | filesystem-automation / large-read-100x1048576 / fresh | 261.461 | 202.330 | -22.62% | ms |
| 227 | filesystem-automation / detect-hash-3-10000 / fresh | 25551.046 | 19756.367 | -22.68% | ms |
| 228 | filesystem-automation / detect-hash-1-10000 / fresh | 25483.690 | 19703.429 | -22.68% | ms |
| 229 | task-runners / tiny-1000-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 129.333 | 99.942 | -22.73% | ms |
| 230 | filesystem-automation / clean-10000 / booted | 25735.120 | 19821.980 | -22.98% | ms |
| 231 | build-systems / native-100-light-j2/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 114.317 | 87.978 | -23.04% | ms |
| 232 | concurrency / failures / persistent | 4.154 | 3.188 | -23.24% | ms |
| 233 | task-runners / mixed-20-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 78.884 | 60.539 | -23.26% | ms |
| 234 | filesystem-automation / mirror-1-10000 / booted | 28697.724 | 22012.325 | -23.30% | ms |
| 235 | build-systems / native-100-heavy-j4/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 152.126 | 116.651 | -23.32% | ms |
| 236 | filesystem-automation / generate-1000 / fresh | 1789.784 | 1372.182 | -23.33% | ms |
| 237 | filesystem-automation / mirror-10-10000 / fresh | 28660.504 | 21964.886 | -23.36% | ms |
| 238 | task-runners / mixed-100-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 1907.843 | 1455.905 | -23.69% | ms |
| 239 | filesystem-automation / generate-10000 / booted | 17730.147 | 13529.468 | -23.69% | ms |
| 240 | task-runners / mixed-100-j1/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 6248.376 | 4759.579 | -23.83% | ms |
| 241 | task-runners / tiny-1000-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 316.058 | 240.522 | -23.90% | ms |
| 242 | build-systems / tiny-100-light-j4/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 13.981 | 10.629 | -23.98% | ms |
| 243 | build-systems / tiny-100-light-j2/batch10 / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 35.175 | 26.735 | -23.99% | ms |
| 244 | build-systems / native-100-light-j4/relink / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 76.190 | 57.825 | -24.10% | ms |
| 245 | task-runners / mixed-100-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 216.855 | 164.566 | -24.11% | ms |
| 246 | filesystem-automation / generate-1000 / booted | 1793.995 | 1360.202 | -24.18% | ms |
| 247 | filesystem-automation / generate-10000 / fresh | 17772.164 | 13466.959 | -24.22% | ms |
| 248 | build-systems / native-100-light-j1/medium / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 361.056 | 273.029 | -24.38% | ms |
| 249 | concurrency / cpu-2 / persistent | 7254.004 | 5482.127 | -24.43% | ms |
| 250 | filesystem-automation / mirror-11-10000 / fresh | 28484.547 | 21518.444 | -24.46% | ms |
| 251 | filesystem-automation / mirror-11-10000 / booted | 28820.485 | 21725.430 | -24.62% | ms |
| 252 | concurrency / tiny-10000 / persistent | 26505.789 | 19978.451 | -24.63% | ms |
| 253 | build-systems / native-100-light-j4/private / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 110.281 | 83.087 | -24.66% | ms |
| 254 | filesystem-automation / large-read-100x1048576 / booted | 248.136 | 186.806 | -24.72% | ms |
| 255 | build-systems / native-1000-light-j4/target / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 127.698 | 96.046 | -24.79% | ms |
| 256 | filesystem-automation / mirror-0-10000 / booted | 28734.412 | 21433.438 | -25.41% | ms |
| 257 | build-systems / native-100-light-j1/batch10 / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 427.606 | 318.623 | -25.49% | ms |
| 258 | build-systems / native-100-heavy-j1/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 167.627 | 124.852 | -25.52% | ms |
| 259 | concurrency / cpu-2 / fresh | 7287.127 | 5410.661 | -25.75% | ms |
| 260 | filesystem-automation / mirror-10-10000 / booted | 29132.371 | 21612.024 | -25.81% | ms |
| 261 | concurrency / schedule-10 / fresh | 11.213 | 8.312 | -25.87% | ms |
| 262 | filesystem-automation / mixed-1000 / fresh | 841.505 | 622.891 | -25.98% | ms |
| 263 | task-runners / mixed-100-j4/shared / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 1229.016 | 909.355 | -26.01% | ms |
| 264 | filesystem-automation / manifest-10000 / booted | 14598.613 | 10788.130 | -26.10% | ms |
| 265 | concurrency / cpu-1 / fresh | 14608.057 | 10791.349 | -26.13% | ms |
| 266 | concurrency / schedule-10000 / persistent | 27511.876 | 20311.090 | -26.17% | ms |
| 267 | filesystem-automation / read-10000 / fresh | 13866.782 | 10203.037 | -26.42% | ms |
| 268 | filesystem-automation / mixed-1000 / booted | 838.987 | 617.213 | -26.43% | ms |
| 269 | filesystem-automation / mirror-1-10000 / fresh | 29107.740 | 21398.801 | -26.48% | ms |
| 270 | concurrency / cpu-4 / fresh | 3915.860 | 2876.454 | -26.54% | ms |
| 271 | filesystem-automation / mirror-12-10000 / fresh | 29507.589 | 21661.765 | -26.59% | ms |
| 272 | build-systems / native-100-light-j2/private / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 118.902 | 87.155 | -26.70% | ms |
| 273 | filesystem-automation / manifest-10000 / fresh | 14827.573 | 10860.767 | -26.75% | ms |
| 274 | build-systems / tiny-100-light-j4/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 18.242 | 13.346 | -26.84% | ms |
| 275 | filesystem-automation / mirror-12-10000 / booted | 29010.223 | 21206.362 | -26.90% | ms |
| 276 | build-systems / native-1000-light-j4/private / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 334.881 | 244.627 | -26.95% | ms |
| 277 | filesystem-automation / read-10000 / booted | 13950.634 | 10188.374 | -26.97% | ms |
| 278 | build-systems / tiny-1000-light-j4/batch10 / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 101.964 | 74.449 | -26.98% | ms |
| 279 | concurrency / cpu-4 / persistent | 3905.406 | 2850.945 | -27.00% | ms |
| 280 | task-runners / tiny-1000-j4/one-percent / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 154.322 | 112.575 | -27.05% | ms |
| 281 | filesystem-automation / manifest-1000 / fresh | 1453.898 | 1059.782 | -27.11% | ms |
| 282 | filesystem-automation / read-1000 / booted | 1389.264 | 1011.877 | -27.16% | ms |
| 283 | build-systems / native-1000-light-j4/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 334.255 | 243.262 | -27.22% | ms |
| 284 | task-runners / tiny-100-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 34.812 | 25.311 | -27.29% | ms |
| 285 | filesystem-automation / manifest-1000 / booted | 1448.537 | 1052.834 | -27.32% | ms |
| 286 | build-systems / tiny-100-light-j1/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 334.593 | 242.790 | -27.44% | ms |
| 287 | build-systems / native-1000-heavy-j4/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 389.092 | 282.094 | -27.50% | ms |
| 288 | concurrency / pool-heavy-4 / fresh | 117.665 | 84.975 | -27.78% | ms |
| 289 | build-systems / native-100-light-j2/relink / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 86.015 | 62.000 | -27.92% | ms |
| 290 | build-systems / tiny-100-light-j4/batch10 / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 27.201 | 19.537 | -28.17% | ms |
| 291 | filesystem-automation / read-1000 / fresh | 1405.609 | 1008.808 | -28.23% | ms |
| 292 | filesystem-automation / mixed-10000 / fresh | 8406.441 | 6028.387 | -28.29% | ms |
| 293 | concurrency / schedule-10000 / fresh | 27241.043 | 19493.458 | -28.44% | ms |
| 294 | build-systems / tiny-100-light-j4/full / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 135.541 | 96.936 | -28.48% | ms |
| 295 | build-systems / native-100-light-j1/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 137.573 | 97.995 | -28.77% | ms |
| 296 | build-systems / native-1000-light-j4/relink / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 276.141 | 196.341 | -28.90% | ms |
| 297 | build-systems / tiny-1000-light-j4/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 92.532 | 65.392 | -29.33% | ms |
| 298 | filesystem-automation / mixed-10000 / booted | 8552.832 | 6036.915 | -29.42% | ms |
| 299 | concurrency / tiny-100 / fresh | 26.408 | 18.625 | -29.47% | ms |
| 300 | build-systems / tiny-10000-light-j4/batch10 / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 774.439 | 543.637 | -29.80% | ms |
| 301 | concurrency / cpu-1 / persistent | 15425.973 | 10807.809 | -29.94% | ms |
| 302 | concurrency / pool-heavy-4 / persistent | 111.049 | 77.766 | -29.97% | ms |
| 303 | build-systems / tiny-10000-light-j4/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 775.735 | 542.542 | -30.06% | ms |
| 304 | build-systems / tiny-1000-light-j4/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 88.538 | 61.847 | -30.15% | ms |
| 305 | build-systems / tiny-10000-light-j4/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 780.191 | 544.418 | -30.22% | ms |
| 306 | filesystem-automation / read-100000 / fresh | 148672.806 | 103189.194 | -30.59% | ms |
| 307 | task-runners / tiny-100-j4/one-percent / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 26.243 | 18.067 | -31.15% | ms |
| 308 | filesystem-automation / read-100000 / booted | 148706.872 | 101939.221 | -31.45% | ms |
| 309 | task-runners / tiny-100-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 171.716 | 116.526 | -32.14% | ms |
| 310 | build-systems / tiny-100-light-j1/batch10 / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 59.806 | 40.557 | -32.19% | ms |
| 311 | build-systems / native-1000-heavy-j2/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 457.984 | 310.577 | -32.19% | ms |
| 312 | task-runners / tiny-100-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 19.809 | 13.368 | -32.52% | ms |
| 313 | build-systems / tiny-100-light-j2/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 19.134 | 12.890 | -32.63% | ms |
| 314 | build-systems / native-10000-light-j4/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 2959.917 | 1986.184 | -32.90% | ms |
| 315 | build-systems / native-100-light-j1/private / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 144.503 | 96.945 | -32.91% | ms |
| 316 | task-runners / mixed-20-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 10.386 | 6.950 | -33.08% | ms |
| 317 | task-runners / tiny-100-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 26.779 | 17.818 | -33.46% | ms |
| 318 | build-systems / native-5000-light-j4/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1577.866 | 1043.840 | -33.84% | ms |
| 319 | build-systems / native-100-light-j1/relink / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 104.252 | 68.942 | -33.87% | ms |
| 320 | build-systems / tiny-100-light-j1/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 32.717 | 21.517 | -34.23% | ms |
| 321 | build-systems / tiny-100-light-j2/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 24.851 | 16.099 | -35.22% | ms |
| 322 | template-engines / article / source-render | 0.435 | 0.278 | -35.94% | ms/render |
| 323 | build-systems / native-100-heavy-j4/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 21.645 | 13.842 | -36.05% | ms |
| 324 | concurrency / tiny-10000 / fresh | 27282.324 | 17297.852 | -36.60% | ms |
| 325 | build-systems / native-100-light-j4/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 21.267 | 13.355 | -37.20% | ms |
| 326 | build-systems / native-1000-heavy-j1/leaf / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 613.902 | 383.017 | -37.61% | ms |
| 327 | build-systems / tiny-100-light-j1/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 28.320 | 17.587 | -37.90% | ms |
| 328 | template-engines / loop-1000 / fresh | 17.714 | 10.476 | -40.86% | ms/invocation |
| 329 | build-systems / native-100-heavy-j2/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 30.601 | 17.883 | -41.56% | ms |
| 330 | filesystem-automation / overwrite-10000 / fresh | 6518.302 | 3782.107 | -41.98% | ms |
| 331 | filesystem-automation / overwrite-1000 / fresh | 649.862 | 372.370 | -42.70% | ms |
| 332 | filesystem-automation / overwrite-10000 / booted | 6428.777 | 3651.606 | -43.20% | ms |
| 333 | concurrency / failures / fresh | 17.916 | 9.954 | -44.44% | ms |
| 334 | filesystem-automation / overwrite-1000 / booted | 644.418 | 354.394 | -45.01% | ms |
| 335 | template-engines / collection / fresh | 32.222 | 17.563 | -45.49% | ms/invocation |
| 336 | build-systems / native-1000-heavy-j4/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 141.847 | 77.313 | -45.50% | ms |
| 337 | build-systems / native-10000-light-j4/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 1278.913 | 692.382 | -45.86% | ms |
| 338 | build-systems / native-100-light-j2/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 32.174 | 17.412 | -45.88% | ms |
| 339 | build-systems / native-5000-light-j4/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 648.167 | 349.748 | -46.04% | ms |
| 340 | build-systems / native-1000-light-j4/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 144.650 | 76.235 | -47.30% | ms |
| 341 | filesystem-automation / write-1000 / fresh | 594.607 | 313.204 | -47.33% | ms |
| 342 | filesystem-automation / write-10000 / booted | 5842.863 | 3064.102 | -47.56% | ms |
| 343 | build-systems / native-100-heavy-j1/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 47.998 | 24.861 | -48.20% | ms |
| 344 | filesystem-automation / write-10000 / fresh | 5955.361 | 3074.272 | -48.38% | ms |
| 345 | filesystem-automation / write-1000 / booted | 593.706 | 303.492 | -48.88% | ms |
| 346 | build-systems / native-100-light-j1/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 48.782 | 24.778 | -49.21% | ms |
| 347 | build-systems / native-1000-heavy-j2/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 223.849 | 112.423 | -49.78% | ms |
| 348 | filesystem-automation / copy-10000 / fresh | 5440.883 | 2723.460 | -49.94% | ms |
| 349 | template-engines / loop-10000 / fresh | 150.338 | 74.001 | -50.78% | ms/invocation |
| 350 | filesystem-automation / copy-1000 / fresh | 552.206 | 270.720 | -50.97% | ms |
| 351 | filesystem-automation / copy-10000 / booted | 5376.916 | 2626.688 | -51.15% | ms |
| 352 | filesystem-automation / copy-1000 / booted | 546.499 | 259.715 | -52.48% | ms |
| 353 | build-systems / native-1000-heavy-j1/noop / C CLOCK_MONOTONIC fork/exec through wait4; setup outside clock | 385.124 | 179.197 | -53.47% | ms |
| 354 | filesystem-automation / copy-100000 / booted | 59348.510 | 26655.207 | -55.09% | ms |
| 355 | filesystem-automation / copy-100000 / fresh | 59353.577 | 26527.248 | -55.31% | ms |
| 356 | template-engines / loop-10 / source-render | 0.139 | 0.061 | -55.81% | ms/render |
| 357 | template-engines / nested-loops / source-render | 2.561 | 1.089 | -57.47% | ms/render |
| 358 | concurrency / mutex-8-2 / fresh | 766.447 | 265.976 | -65.30% | ms |
| 359 | concurrency / atomic-4 / fresh | 174.935 | 60.134 | -65.62% | ms |
| 360 | concurrency / mutex-8-2 / persistent | 791.154 | 257.462 | -67.46% | ms |
| 361 | template-engines / collection / source-render | 22.809 | 7.263 | -68.16% | ms/render |
| 362 | template-engines / loop-100 / source-render | 1.137 | 0.360 | -68.32% | ms/render |
| 363 | concurrency / mutex-1-2 / fresh | 692.266 | 218.317 | -68.46% | ms |
| 364 | concurrency / mutex-8-1 / fresh | 753.812 | 232.701 | -69.13% | ms |
| 365 | concurrency / mutex-8-1 / persistent | 747.244 | 227.523 | -69.55% | ms |
| 366 | template-engines / loop-10000 / source-render | 113.578 | 34.408 | -69.71% | ms/render |
| 367 | template-engines / loop-1000 / source-render | 11.324 | 3.385 | -70.11% | ms/render |
| 368 | concurrency / mutex-1-2 / persistent | 700.684 | 209.273 | -70.13% | ms |
| 369 | concurrency / atomic-1 / fresh | 473.330 | 139.685 | -70.49% | ms |
| 370 | concurrency / mutex-8-4 / fresh | 928.116 | 273.036 | -70.58% | ms |
| 371 | concurrency / mutex-8-4 / persistent | 900.410 | 264.153 | -70.66% | ms |
| 372 | concurrency / mutex-1-1 / persistent | 651.407 | 187.105 | -71.28% | ms |
| 373 | concurrency / atomic-1 / persistent | 461.996 | 130.693 | -71.71% | ms |
| 374 | concurrency / mutex-1-1 / fresh | 671.583 | 189.138 | -71.84% | ms |
| 375 | concurrency / atomic-2 / persistent | 239.459 | 66.909 | -72.06% | ms |
| 376 | concurrency / queue-10000-4-4 / persistent | 4360.838 | 1214.875 | -72.14% | ms |
| 377 | concurrency / queue-1000-4-4 / persistent | 454.944 | 125.297 | -72.46% | ms |
| 378 | concurrency / atomic-2 / fresh | 272.812 | 74.700 | -72.62% | ms |
| 379 | concurrency / queue-10000-4-4 / fresh | 4593.155 | 1247.884 | -72.83% | ms |
| 380 | concurrency / queue-1000-4-4 / fresh | 474.916 | 128.907 | -72.86% | ms |
| 381 | concurrency / atomic-4 / persistent | 160.248 | 43.423 | -72.90% | ms |
| 382 | concurrency / queue-10000-1-1 / fresh | 3961.919 | 1070.626 | -72.98% | ms |
| 383 | concurrency / queue-1000-4-1 / fresh | 489.307 | 131.717 | -73.08% | ms |
| 384 | concurrency / queue-10000-1-1 / persistent | 3894.848 | 1039.407 | -73.31% | ms |
| 385 | concurrency / mutex-1-4 / fresh | 897.207 | 237.836 | -73.49% | ms |
| 386 | concurrency / mutex-1-4 / persistent | 851.626 | 220.942 | -74.06% | ms |
| 387 | concurrency / queue-100000-4-4 / persistent | 45620.753 | 11745.837 | -74.25% | ms |
| 388 | concurrency / queue-100000-4-4 / fresh | 47276.732 | 12116.366 | -74.37% | ms |
| 389 | concurrency / queue-100000-1-1 / fresh | 42139.649 | 10692.397 | -74.63% | ms |
| 390 | concurrency / queue-100000-1-1 / persistent | 41922.289 | 10616.424 | -74.68% | ms |
| 391 | filesystem-automation / delete-1000 / fresh | 362.253 | 86.429 | -76.14% | ms |
| 392 | concurrency / queue-1000-1-1 / fresh | 475.301 | 111.971 | -76.44% | ms |
| 393 | filesystem-automation / filter-1-1000 / fresh | 272.385 | 63.949 | -76.52% | ms |
| 394 | concurrency / queue-10000-4-1 / persistent | 5020.116 | 1176.023 | -76.57% | ms |
| 395 | concurrency / queue-1000-4-1 / persistent | 511.042 | 119.052 | -76.70% | ms |
| 396 | filesystem-automation / rename-1000 / fresh | 376.035 | 87.532 | -76.72% | ms |
| 397 | concurrency / queue-10000-4-1 / fresh | 4951.985 | 1152.334 | -76.73% | ms |
| 398 | concurrency / queue-10000-1-4 / persistent | 5119.801 | 1179.031 | -76.97% | ms |
| 399 | concurrency / queue-100000-4-1 / persistent | 52088.629 | 11976.754 | -77.01% | ms |
| 400 | filesystem-automation / filter-10-1000 / fresh | 284.117 | 65.169 | -77.06% | ms |
| 401 | concurrency / queue-1000-1-4 / persistent | 513.538 | 115.802 | -77.45% | ms |
| 402 | filesystem-automation / delete-10000 / fresh | 3486.409 | 783.569 | -77.53% | ms |
| 403 | filesystem-automation / delete-10000 / booted | 3475.843 | 772.377 | -77.78% | ms |
| 404 | concurrency / queue-10000-1-4 / fresh | 5095.886 | 1131.556 | -77.79% | ms |
| 405 | concurrency / queue-1000-1-1 / persistent | 461.287 | 102.209 | -77.84% | ms |
| 406 | concurrency / queue-100000-1-4 / fresh | 52534.894 | 11587.311 | -77.94% | ms |
| 407 | filesystem-automation / delete-1000 / booted | 354.935 | 78.226 | -77.96% | ms |
| 408 | concurrency / queue-100000-1-4 / persistent | 53145.334 | 11648.111 | -78.08% | ms |
| 409 | filesystem-automation / rename-10000 / fresh | 3597.063 | 782.918 | -78.23% | ms |
| 410 | filesystem-automation / filter-1-10000 / fresh | 2557.605 | 553.636 | -78.35% | ms |
| 411 | concurrency / queue-100000-4-1 / fresh | 53848.599 | 11642.459 | -78.38% | ms |
| 412 | concurrency / queue-1000-1-4 / fresh | 591.527 | 127.162 | -78.50% | ms |
| 413 | filesystem-automation / filter-1-1000 / booted | 266.923 | 57.310 | -78.53% | ms |
| 414 | filesystem-automation / filter-50-1000 / fresh | 342.708 | 73.573 | -78.53% | ms |
| 415 | filesystem-automation / filter-10-10000 / booted | 2683.746 | 573.921 | -78.61% | ms |
| 416 | filesystem-automation / rename-1000 / booted | 373.010 | 79.327 | -78.73% | ms |
| 417 | filesystem-automation / rename-10000 / booted | 3582.672 | 757.302 | -78.86% | ms |
| 418 | filesystem-automation / filter-10-1000 / booted | 283.951 | 59.689 | -78.98% | ms |
| 419 | filesystem-automation / filter-1-10000 / booted | 2555.942 | 536.867 | -79.00% | ms |
| 420 | filesystem-automation / filter-10-10000 / fresh | 2745.111 | 574.897 | -79.06% | ms |
| 421 | filesystem-automation / filter-1-100000 / fresh | 27087.903 | 5528.397 | -79.59% | ms |
| 422 | filesystem-automation / filter-10-100000 / booted | 28785.682 | 5790.287 | -79.88% | ms |
| 423 | filesystem-automation / filter-50-10000 / booted | 3305.815 | 656.690 | -80.14% | ms |
| 424 | filesystem-automation / filter-10-100000 / fresh | 28941.684 | 5748.250 | -80.14% | ms |
| 425 | filesystem-automation / filter-1-100000 / booted | 27695.909 | 5475.102 | -80.23% | ms |
| 426 | filesystem-automation / walk-1000 / fresh | 151.290 | 29.888 | -80.24% | ms |
| 427 | filesystem-automation / filter-50-10000 / fresh | 3330.431 | 655.821 | -80.31% | ms |
| 428 | filesystem-automation / filter-prefix-1000 / fresh | 217.239 | 42.674 | -80.36% | ms |
| 429 | filesystem-automation / filter-50-1000 / booted | 338.488 | 65.896 | -80.53% | ms |
| 430 | filesystem-automation / filter-extension-1000 / fresh | 233.497 | 44.846 | -80.79% | ms |
| 431 | filesystem-automation / filter-50-100000 / booted | 35747.490 | 6693.413 | -81.28% | ms |
| 432 | filesystem-automation / filter-50-100000 / fresh | 34973.328 | 6438.018 | -81.59% | ms |
| 433 | filesystem-automation / filter-prefix-10000 / fresh | 2021.881 | 351.924 | -82.59% | ms |
| 434 | filesystem-automation / relocate-1000 / fresh | 325.153 | 55.802 | -82.84% | ms |
| 435 | filesystem-automation / filter-prefix-1000 / booted | 214.073 | 36.646 | -82.88% | ms |
| 436 | filesystem-automation / filter-extension-10000 / fresh | 2215.675 | 377.594 | -82.96% | ms |
| 437 | filesystem-automation / filter-prefix-10000 / booted | 2003.612 | 340.228 | -83.02% | ms |
| 438 | filesystem-automation / filter-prefix-100000 / fresh | 21014.625 | 3514.817 | -83.27% | ms |
| 439 | filesystem-automation / filter-extension-1000 / booted | 230.652 | 38.398 | -83.35% | ms |
| 440 | filesystem-automation / filter-extension-10000 / booted | 2209.662 | 367.552 | -83.37% | ms |
| 441 | filesystem-automation / filter-prefix-100000 / booted | 20634.374 | 3371.324 | -83.66% | ms |
| 442 | filesystem-automation / filter-extension-100000 / booted | 22378.261 | 3628.238 | -83.79% | ms |
| 443 | filesystem-automation / filter-size-1000 / fresh | 271.694 | 43.983 | -83.81% | ms |
| 444 | filesystem-automation / walk-100000 / fresh | 14798.817 | 2336.417 | -84.21% | ms |
| 445 | filesystem-automation / filter-extension-100000 / fresh | 23171.204 | 3648.602 | -84.25% | ms |
| 446 | filesystem-automation / walk-1000 / booted | 147.538 | 21.696 | -85.29% | ms |
| 447 | filesystem-automation / walk-10000 / fresh | 1332.426 | 195.374 | -85.34% | ms |
| 448 | filesystem-automation / relocate-10000 / fresh | 3102.432 | 451.027 | -85.46% | ms |
| 449 | filesystem-automation / relocate-1000 / booted | 321.400 | 45.976 | -85.70% | ms |
| 450 | filesystem-automation / relocate-10000 / booted | 3078.197 | 430.593 | -86.01% | ms |
| 451 | filesystem-automation / walk-10000 / booted | 1349.687 | 184.959 | -86.30% | ms |
| 452 | filesystem-automation / filter-size-10000 / fresh | 2549.157 | 340.600 | -86.64% | ms |
| 453 | filesystem-automation / filter-size-1000 / booted | 265.545 | 35.159 | -86.76% | ms |
| 454 | filesystem-automation / filter-size-100000 / booted | 25600.161 | 3334.847 | -86.97% | ms |
| 455 | filesystem-automation / filter-size-100000 / fresh | 25878.120 | 3317.358 | -87.18% | ms |
| 456 | filesystem-automation / walk-100000 / booted | 14268.921 | 1824.631 | -87.21% | ms |
| 457 | filesystem-automation / filter-size-10000 / booted | 2583.761 | 326.770 | -87.35% | ms |
| 458 | filesystem-automation / stat-1000 / fresh | 323.829 | 38.179 | -88.21% | ms |
| 459 | filesystem-automation / stat-1000 / booted | 316.802 | 30.091 | -90.50% | ms |
| 460 | filesystem-automation / stat-10000 / fresh | 3120.415 | 284.683 | -90.88% | ms |
| 461 | filesystem-automation / stat-100000 / booted | 33129.951 | 2954.971 | -91.08% | ms |
| 462 | filesystem-automation / stat-10000 / booted | 3054.717 | 269.615 | -91.17% | ms |
| 463 | filesystem-automation / stat-100000 / fresh | 33557.673 | 2794.862 | -91.67% | ms |

Task gains13.83–33.46% remain here only. No causal version percentage is established from historical cross-node movement.

## Memory and capabilities — separate

Held1k tasks:143.625MiB Nift/5.375MiB Go=26.72×; prior143.5MiB, old weakness unchanged. Template/filesystem inherited wait4 supervisor floors are unranked. Task maximum-childRSS leads31/31 configurations; not aggregate-treeRSS. NativeSHA256/statmtime/recursive removal, prepared-template artifacts, public channels/cancellation, outputless tracked nodes/env invalidation/cache restoration/ensure/-j/structured graph remain major separate capability gaps. Exactly-once inlinefilesystem reproducer now passes; do not infer universal bug absence.

## Core priorities

Release blockers:1)call regression corroborated by scripting/shell;2)freshwebsite full-build regression. Preserve filesystem metadata/traversal/filter gains, template loops, queue throughput and sorting. Old pathological weaknesses:retained-runtime growth, task creation/retention, blockingwaits, scalarCPU, bulkfilesystem checksum/mirror policy, preparedreuse. Priorities depend on product centrality and changed preferences, not raw percentage alone.

Near-flat controls excluded from established-change tables:concurrency schedule1k, templatefresharticle, shelltraversal. Persistent reuse degradation is an old weakness, not a confirmed new regression. No new public capability was established beyond the certified exactly-once reproducer behavior. Labs unchanged; no release recommendation.

# Interim direct preferences

Diagnostic drafts only. Before/after scope is explained in the synthesis; no Labs publication.

| Category | Human + agent | Agent-primary | Why / changed |
|---|---|---|---|
| Scripting | Python for new general data/automation; Nift for bounded Nift-owned policy | Same choices | Calls/collections/JSON costs remain; concrete Python libraries and runtime recovery matter. No broad preference reversal. |
| Task running | Nift for authored DAGs; Turbo/Nx for required restoration/discovery | Nift for authored DAGs; same specific exceptions | Nift lowest wall/RSS31/31; preference unchanged, confidence strengthened. |
| Template engine | Nift for Nift-owned composition; native library in Python/JS; prepared peer for hot service | Nift for programmable authored generation; prepared peer for high-volume hot service | Loop gains are real; no public prepared-template artifact and15.4×large source-render gap remain. Scope improves, default hot-service preference unchanged. |
| Concurrency | Go for standalone/high fanout; Nift for bounded Nift-owned jobs | Same choices | Queue improves67%, but scheduling/memory/waits/reuse still block a general Nift choice. |
| Website generation | Hugo for conventional content site; Nift for existing/mixed programmable project | Nift for mixed authored website/assets/helpers; Hugo for plain content site | Freshfull regression and current Hugo advantage weaken blanket Nift preference; incremental paths improve. |
| Shell | Bash/Zsh interactive/compatibility; Nift for project-owned mixed policy | Nift for owned policy; Bash/Zsh for compatibility | Call regression corroborated; no universal shell replacement |
| Filesystem | Nift bounded existing policy; Go/Bun/Node bulk processing | Same choices | Huge stat/walk/filter gains, bulk policy still far behind |
| Build systems | Nift procedural/mixed; Make tiny conventional; CMake/Meson→Ninja conventional C++ | Same scope-specific choices | No-op/metadata costs and depfile/multi-output/toolchain gaps persist; explicit policy still preferred for authored work |

# Interim top10 core priorities

1. **Fix function-call regression.** Confirmed+145.76%; central policy-language path. Investigate extra argument parsing/classification/allocation; preserve exactly-once and ownership.

2. **Fix fresh website full-build regression.** Confirmed+38.29%; strategically central product. Extra filesystem probes merit investigation independent of call cause.

3. **Resolve retained-runtime state/time growth.** Ten scheduling requests grow7.17×; prior also grows. Blocks long-lived embedding/service preference; prove lifetime cause before calling it a leak.

4. **Reduce lightweight task creation/retention cost.** 10k scheduling1376.9×Go and held1k memory26.7×Go. Tiny work is infeasible despite queue wins.

5. **Improve scalar/value execution throughput.** 4-worker CPU186.5×Go despite useful parallel scaling; large calls289.1×LuaJIT. Separate interpreter cost from scheduling.

6. **Add nonblocking waits/timers.** 1k wait2576ms vsGo14.484ms; historical Nift2659.6ms shows little movement. Blocking workers remain the architectural/API boundary to address.

7. **Add public prepared-template artifacts.** Missing today; source-render cannot be relabelled prepared reuse. High-volume rendering still selects prepared peers.

8. **Reduce remaining collection/JSON costs.** BFS/frequency/transform paired medians increase; BFS allocations rise39.8%, frequency counts barely change. Investigate independently; keep sorting wins.

9. **Add channels/cancellation with explicit lifetime contracts.** Queue polling/mutex value copies persist; native bounded channel/condition and public cancellation remain absent. Do not replace semantic safety with terseness.

10. **Close task-runner contract/cache ergonomics gaps.** Outputless nodes, env invalidation, restoration, ensure,-j,structured graph remain incomplete. Existing repair works; Nift is already preferred for authored tasks.

Detailed subsystem discussion is retained in INTERIM-DIAGNOSTIC-DETAILS.md.
