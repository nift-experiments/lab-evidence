# Current competitive gaps — interim diagnostic draft

Four independently accepted suite wall exports only. Lower-is-better deficit = Nift / fastest valid same-node peer. Different boundaries remain explicit; cross-suite ranking is descriptive, not a universal workload score.

| Rank | Benchmark / scenario | Boundary | Nift | Best peer | Peer value | Multiple |
|---:|---|---|---:|---|---:|---:|
| 1 | concurrency / schedule-10000 | persistent | 20311.090 ms | go | 14.752 | 1376.88× |
| 2 | concurrency / tiny-10000 | persistent | 19978.451 ms | go | 16.164 | 1235.97× |
| 3 | concurrency / schedule-10000 | fresh | 19493.458 ms | go | 18.540 | 1051.42× |
| 4 | concurrency / tiny-10000 | fresh | 17297.852 ms | go | 21.370 | 809.45× |
| 5 | scripting / sanity/function-calls/large | fresh-process-repeated | 546.056 ms | luajit | 1.889 | 289.09× |
| 6 | concurrency / mutex-8-2 | persistent | 257.462 ms | go | 0.895 | 287.64× |
| 7 | concurrency / mutex-8-1 | persistent | 227.523 ms | go | 0.851 | 267.31× |
| 8 | concurrency / mutex-8-4 | persistent | 264.153 ms | go | 0.991 | 266.64× |
| 9 | concurrency / mutex-1-2 | persistent | 209.273 ms | go | 0.868 | 240.97× |
| 10 | concurrency / mutex-1-4 | persistent | 220.942 ms | go | 0.935 | 236.22× |
| 11 | concurrency / queue-100000-4-4 | persistent | 11745.837 ms | bun | 56.266 | 208.76× |
| 12 | concurrency / cpu-1 | persistent | 10807.809 ms | go | 52.767 | 204.82× |
| 13 | concurrency / cpu-2 | persistent | 5482.127 ms | go | 26.945 | 203.46× |
| 14 | concurrency / mutex-1-1 | persistent | 187.105 ms | go | 0.954 | 196.17× |
| 15 | concurrency / cpu-1 | fresh | 10791.349 ms | go | 57.828 | 186.61× |
| 16 | concurrency / cpu-4 | persistent | 2850.945 ms | go | 15.286 | 186.51× |
| 17 | concurrency / queue-100000-4-1 | persistent | 11976.754 ms | bun | 65.372 | 183.21× |
| 18 | concurrency / wait-1000 | persistent | 2576.345 ms | go | 14.484 | 177.88× |
| 19 | concurrency / waiting-memory-1000 | persistent | 2772.812 ms | go | 15.600 | 177.74× |
| 20 | concurrency / queue-100000-1-1 | persistent | 10616.424 ms | bun | 60.019 | 176.88× |
| 21 | concurrency / queue-100000-1-4 | persistent | 11648.111 ms | bun | 67.150 | 173.46× |
| 22 | concurrency / cpu-2 | fresh | 5410.661 ms | go | 31.683 | 170.78× |
| 23 | concurrency / atomic-1 | persistent | 130.693 ms | go | 0.847 | 154.29× |
| 24 | scripting / arrays-strings-hash/frequency-count/large | fresh-process-repeated | 589.370 ms | luajit | 3.957 | 148.96× |
| 25 | concurrency / queue-100000-4-4 | fresh | 12116.366 ms | bun | 85.354 | 141.95× |
| 26 | concurrency / cpu-4 | fresh | 2876.454 ms | go | 20.507 | 140.27× |
| 27 | concurrency / wait-1000 | fresh | 2594.638 ms | go | 19.028 | 136.36× |
| 28 | concurrency / pool-heavy-1 | persistent | 289.215 ms | go | 2.170 | 133.27× |
| 29 | concurrency / waiting-memory-1000 | fresh | 2798.030 ms | go | 21.405 | 130.72× |
| 30 | concurrency / queue-100000-4-1 | fresh | 11642.459 ms | bun | 90.086 | 129.24× |
| 31 | concurrency / queue-100000-1-1 | fresh | 10692.397 ms | bun | 84.193 | 127.00× |
| 32 | concurrency / queue-100000-1-4 | fresh | 11587.311 ms | bun | 91.422 | 126.74× |
| 33 | concurrency / queue-10000-4-4 | persistent | 1214.875 ms | go | 11.884 | 102.22× |
| 34 | concurrency / queue-10000-4-1 | persistent | 1176.023 ms | go | 11.927 | 98.60× |
| 35 | concurrency / queue-10000-1-4 | persistent | 1179.031 ms | go | 11.967 | 98.52× |
| 36 | concurrency / tiny-1000 | persistent | 261.055 ms | go | 2.672 | 97.70× |
| 37 | concurrency / queue-10000-1-1 | persistent | 1039.407 ms | go | 11.084 | 93.78× |
| 38 | concurrency / schedule-1000 | persistent | 233.856 ms | go | 2.498 | 93.62× |
| 39 | concurrency / fan-1000 | persistent | 229.789 ms | go | 2.605 | 88.20× |
| 40 | scripting / arrays-strings-hash/sliding-window/large | fresh-process-repeated | 328.926 ms | luajit | 3.776 | 87.11× |
| 41 | concurrency / pool-heavy-2 | persistent | 150.951 ms | go | 1.874 | 80.56× |
| 42 | concurrency / queue-10000-4-4 | fresh | 1247.884 ms | go | 16.257 | 76.76× |
| 43 | scripting / arrays-strings-hash/map-set/large | fresh-process-repeated | 284.963 ms | luajit | 3.770 | 75.59× |
| 44 | concurrency / queue-10000-1-4 | fresh | 1131.556 ms | go | 15.929 | 71.04× |
| 45 | concurrency / queue-10000-4-1 | fresh | 1152.334 ms | go | 16.399 | 70.27× |
| 46 | concurrency / atomic-2 | persistent | 66.909 ms | go | 0.961 | 69.62× |
| 47 | concurrency / queue-10000-1-1 | fresh | 1070.626 ms | go | 16.619 | 64.42× |
| 48 | scripting / dynamic-programming/fibonacci/large | fresh-process-repeated | 164.168 ms | luajit | 2.549 | 64.39× |
| 49 | concurrency / queue-1000-1-4 | persistent | 115.802 ms | go | 1.824 | 63.50× |
| 50 | concurrency / queue-1000-4-1 | persistent | 119.052 ms | go | 1.882 | 63.27× |
| 51 | concurrency / queue-1000-4-4 | persistent | 125.297 ms | go | 2.007 | 62.43× |
| 52 | concurrency / queue-1000-1-1 | persistent | 102.209 ms | go | 1.804 | 56.65× |
| 53 | scripting / arrays-strings-hash/scan/large | fresh-process-repeated | 103.618 ms | luajit | 1.885 | 54.97× |
| 54 | concurrency / pool-heavy-4 | persistent | 77.766 ms | go | 1.582 | 49.17× |
| 55 | scripting / graphs-trees-search/bfs/large | fresh-process-repeated | 1002.530 ms | luajit | 21.869 | 45.84× |
| 56 | concurrency / pool-heavy-1 | fresh | 298.090 ms | go | 6.792 | 43.89× |
| 57 | concurrency / fan-1000 | fresh | 339.842 ms | go | 7.880 | 43.13× |
| 58 | concurrency / atomic-4 | persistent | 43.423 ms | go | 1.013 | 42.87× |
| 59 | scripting / sanity/loops/large | fresh-process-repeated | 82.525 ms | luajit | 1.945 | 42.44× |
| 60 | concurrency / mutex-8-2 | fresh | 265.976 ms | go | 6.842 | 38.87× |
| 61 | concurrency / tiny-1000 | fresh | 256.266 ms | go | 6.706 | 38.21× |
| 62 | concurrency / schedule-1000 | fresh | 229.708 ms | go | 6.409 | 35.84× |
| 63 | concurrency / mutex-8-1 | fresh | 232.701 ms | go | 6.536 | 35.60× |
| 64 | concurrency / mutex-1-4 | fresh | 237.836 ms | go | 6.856 | 34.69× |
| 65 | concurrency / mutex-8-4 | fresh | 273.036 ms | go | 7.874 | 34.68× |
| 66 | concurrency / pool-medium-1 | persistent | 33.129 ms | go | 0.958 | 34.58× |
| 67 | concurrency / nested-100 | persistent | 56.421 ms | go | 1.658 | 34.02× |
| 68 | concurrency / mutex-1-2 | fresh | 218.317 ms | go | 6.665 | 32.75× |
| 69 | scripting / arrays-strings-hash/sort-index/large | fresh-process-repeated | 904.664 ms | python | 30.633 | 29.53× |
| 70 | concurrency / mutex-1-1 | fresh | 189.138 ms | go | 6.888 | 27.46× |
| 71 | concurrency / pool-light-1 | persistent | 22.541 ms | go | 0.872 | 25.84× |
| 72 | concurrency / files-10000 | persistent | 1589.358 ms | go | 62.994 | 25.23× |
| 73 | concurrency / files-10000 | fresh | 1608.951 ms | go | 66.757 | 24.10× |
| 74 | concurrency / waiting-memory-100 | persistent | 262.937 ms | go | 11.790 | 22.30× |
| 75 | concurrency / wait-100 | persistent | 258.189 ms | go | 11.781 | 21.92× |
| 76 | concurrency / pool-heavy-2 | fresh | 159.824 ms | go | 7.694 | 20.77× |
| 77 | concurrency / files-1000 | persistent | 161.134 ms | go | 7.978 | 20.20× |
| 78 | concurrency / queue-1000-4-4 | fresh | 128.907 ms | go | 6.486 | 19.87× |
| 79 | concurrency / atomic-1 | fresh | 139.685 ms | go | 7.172 | 19.48× |
| 80 | concurrency / queue-1000-1-4 | fresh | 127.162 ms | go | 6.604 | 19.26× |
| 81 | concurrency / queue-1000-4-1 | fresh | 131.717 ms | go | 6.906 | 19.07× |
| 82 | concurrency / pool-medium-2 | persistent | 17.893 ms | go | 0.976 | 18.33× |
| 83 | concurrency / queue-1000-1-1 | fresh | 111.971 ms | go | 6.582 | 17.01× |
| 84 | concurrency / wait-100 | fresh | 264.840 ms | go | 15.635 | 16.94× |
| 85 | concurrency / waiting-memory-100 | fresh | 270.362 ms | go | 17.576 | 15.38× |
| 86 | template-engines / loop-10000 | source-render | 34.408 ms/render | handlebars | 2.241 | 15.35× |
| 87 | concurrency / pool-light-2 | persistent | 12.648 ms | go | 0.915 | 13.82× |
| 88 | concurrency / pool-heavy-4 | fresh | 84.975 ms | go | 6.153 | 13.81× |
| 89 | concurrency / files-1000 | fresh | 168.950 ms | go | 12.734 | 13.27× |
| 90 | concurrency / schedule-100 | persistent | 13.619 ms | go | 1.068 | 12.76× |
| 91 | concurrency / files-100 | persistent | 19.850 ms | go | 1.560 | 12.72× |
| 92 | concurrency / fan-100 | persistent | 14.262 ms | go | 1.126 | 12.66× |
| 93 | concurrency / stagger-100 | persistent | 279.584 ms | go | 22.200 | 12.59× |
| 94 | concurrency / tiny-100 | persistent | 14.888 ms | go | 1.208 | 12.32× |
| 95 | concurrency / atomic-2 | fresh | 74.700 ms | go | 6.625 | 11.28× |
| 96 | concurrency / stagger-100 | fresh | 285.665 ms | go | 26.011 | 10.98× |
| 97 | concurrency / pool-medium-4 | persistent | 10.734 ms | go | 1.066 | 10.07× |
| 98 | concurrency / nested-100 | fresh | 63.798 ms | go | 7.402 | 8.62× |
| 99 | concurrency / atomic-4 | fresh | 60.134 ms | go | 7.088 | 8.48× |
| 100 | concurrency / nested-10 | persistent | 7.742 ms | go | 0.948 | 8.17× |
| 101 | concurrency / pool-light-4 | persistent | 8.004 ms | go | 1.032 | 7.76× |
| 102 | concurrency / pool-medium-1 | fresh | 37.919 ms | go | 5.057 | 7.50× |
| 103 | template-engines / collection | source-render | 7.263 ms/render | handlebars | 0.974 | 7.45× |
| 104 | scripting / structured-data/json-transform/large | fresh-process-repeated | 669.316 ms | python | 95.607 | 7.00× |
| 105 | scripting / graphs-trees-search/bfs/small | fresh-process-repeated | 14.471 ms | lua54 | 2.529 | 5.72× |
| 106 | scripting / sanity/function-calls/small | fresh-process-repeated | 10.027 ms | luajit | 1.764 | 5.68× |
| 107 | concurrency / pool-light-1 | fresh | 27.460 ms | go | 4.893 | 5.61× |
| 108 | scripting / arrays-strings-hash/frequency-count/small | fresh-process-repeated | 9.813 ms | luajit | 1.829 | 5.37× |
| 109 | scripting / structured-data/json-traverse/large | fresh-process-repeated | 473.779 ms | node | 94.393 | 5.02× |
| 110 | scripting / arrays-strings-hash/sort-index/small | fresh-process-repeated | 9.541 ms | luajit | 1.986 | 4.80× |
| 111 | template-engines / loop-1000 | source-render | 3.385 ms/render | handlebars | 0.749 | 4.52× |
| 112 | concurrency / fan-100 | fresh | 24.618 ms | go | 5.850 | 4.21× |
| 113 | concurrency / files-100 | fresh | 25.392 ms | go | 6.038 | 4.21× |
| 114 | scripting / arrays-strings-hash/sliding-window/small | fresh-process-repeated | 7.923 ms | lua54 | 1.904 | 4.16× |
| 115 | concurrency / mixed-wait-100 | persistent | 89.072 ms | go | 21.562 | 4.13× |
| 116 | concurrency / pool-medium-2 | fresh | 23.692 ms | go | 5.786 | 4.09× |
| 117 | template-engines / literal | source-render | 0.015 ms/render | liquid | 0.004 | 3.98× |
| 118 | scripting / filesystem/traverse/large | fresh-process-repeated | 41.798 ms | luajit | 10.608 | 3.94× |
| 119 | concurrency / schedule-100 | fresh | 18.692 ms | go | 4.788 | 3.90× |
| 120 | concurrency / tiny-100 | fresh | 18.625 ms | go | 4.971 | 3.75× |
| 121 | concurrency / mixed-wait-100 | fresh | 95.620 ms | go | 25.792 | 3.71× |
| 122 | concurrency / tiny-10 | persistent | 3.006 ms | go | 0.830 | 3.62× |
| 123 | concurrency / fan-10 | persistent | 3.265 ms | go | 0.906 | 3.60× |
| 124 | scripting / arrays-strings-hash/map-set/small | fresh-process-repeated | 6.940 ms | luajit | 1.952 | 3.56× |
| 125 | concurrency / failures | persistent | 3.188 ms | go | 0.924 | 3.45× |
| 126 | concurrency / schedule-10 | persistent | 3.013 ms | go | 0.890 | 3.39× |
| 127 | concurrency / pool-light-2 | fresh | 18.198 ms | go | 5.416 | 3.36× |
| 128 | scripting / structured-data/json-parse/large | fresh-process-repeated | 295.195 ms | node | 98.649 | 2.99× |
| 129 | concurrency / pool-medium-4 | fresh | 17.269 ms | go | 5.870 | 2.94× |
| 130 | scripting / arrays-strings-hash/scan/small | fresh-process-repeated | 5.315 ms | luajit | 1.811 | 2.93× |
| 131 | concurrency / process-1000 | fresh | 886.230 ms | go | 302.553 | 2.93× |
| 132 | scripting / sanity/loops/small | fresh-process-repeated | 5.251 ms | lua54 | 1.802 | 2.91× |
| 133 | concurrency / process-1000 | persistent | 835.100 ms | go | 288.374 | 2.90× |
| 134 | concurrency / process-100 | persistent | 88.028 ms | go | 32.722 | 2.69× |
| 135 | concurrency / process-one-failure | persistent | 88.492 ms | go | 32.902 | 2.69× |
| 136 | scripting / sanity/noop/small | fresh-process-repeated | 5.855 ms | luajit | 2.180 | 2.69× |
| 137 | concurrency / process-100 | fresh | 98.413 ms | go | 37.260 | 2.64× |
| 138 | concurrency / process-many-failures | persistent | 78.885 ms | go | 30.687 | 2.57× |
| 139 | concurrency / pool-light-4 | fresh | 14.070 ms | go | 5.636 | 2.50× |
| 140 | concurrency / process-many-failures | fresh | 95.028 ms | go | 38.399 | 2.47× |
| 141 | concurrency / process-one-failure | fresh | 102.732 ms | go | 41.588 | 2.47× |
| 142 | concurrency / process-10 | persistent | 10.717 ms | go | 4.461 | 2.40× |
| 143 | template-engines / nested-loops | source-render | 1.089 ms/render | nunjucks | 0.483 | 2.26× |
| 144 | scripting / dynamic-programming/fibonacci/small | fresh-process-repeated | 4.147 ms | luajit | 1.871 | 2.22× |
| 145 | scripting / sanity/output/large | fresh-process-repeated | 3.814 ms | luajit | 1.765 | 2.16× |
| 146 | concurrency / nested-10 | fresh | 14.887 ms | go | 6.957 | 2.14× |
| 147 | scripting / sanity/output/small | fresh-process-repeated | 3.659 ms | luajit | 1.762 | 2.08× |
| 148 | template-engines / many-templates-1000 | source-render | 0.021 ms/render | liquid | 0.010 | 2.04× |
| 149 | scripting / sanity/noop/large | fresh-process-repeated | 3.310 ms | luajit | 1.634 | 2.03× |
| 150 | template-engines / many-templates-10 | source-render | 0.021 ms/render | liquid | 0.011 | 1.97× |
| 151 | template-engines / many-templates-100 | source-render | 0.021 ms/render | liquid | 0.011 | 1.96× |
| 152 | concurrency / schedule-10 | fresh | 8.312 ms | go | 4.356 | 1.91× |
| 153 | concurrency / fan-10 | fresh | 8.891 ms | go | 4.874 | 1.82× |
| 154 | concurrency / tiny-10 | fresh | 8.611 ms | go | 4.789 | 1.80× |
| 155 | concurrency / process-10 | fresh | 19.188 ms | go | 10.709 | 1.79× |
| 156 | concurrency / mixed-64 | persistent | 86.083 ms | go | 54.877 | 1.57× |
| 157 | concurrency / mixed-64 | fresh | 90.836 ms | go | 60.018 | 1.51× |
| 158 | concurrency / failures | fresh | 9.954 ms | go | 6.590 | 1.51× |
| 159 | template-engines / loop-100 | source-render | 0.360 ms/render | nunjucks | 0.253 | 1.42× |
| 160 | template-engines / many-renders-1000 | source-render | 0.022 ms/render | liquid | 0.015 | 1.41× |
| 161 | concurrency / process-mixed | persistent | 105.262 ms | go | 75.021 | 1.40× |
| 162 | concurrency / process-mixed | fresh | 113.424 ms | go | 81.269 | 1.40× |
| 163 | template-engines / many-renders-100 | source-render | 0.021 ms/render | liquid | 0.016 | 1.34× |
| 164 | template-engines / includes-8 | source-render | 0.159 ms/render | nunjucks | 0.119 | 1.33× |
| 165 | template-engines / article | source-render | 0.278 ms/render | nunjucks | 0.289 | 0.96× |
| 166 | template-engines / includes-4 | source-render | 0.089 ms/render | nunjucks | 0.101 | 0.88× |
| 167 | template-engines / loop-10000 | fresh | 74.001 ms/invocation | nunjucks | 94.838 | 0.78× |
| 168 | template-engines / interpolation | source-render | 0.026 ms/render | liquid | 0.034 | 0.77× |
| 169 | task-runners / mixed-1000-j4/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 13829.675 ms | nx | 18414.227 | 0.75× |
| 170 | task-runners / mixed-100-j2/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 2602.624 ms | nx | 3514.926 | 0.74× |
| 171 | task-runners / mixed-100-j1/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 4759.579 ms | nx | 6430.672 | 0.74× |
| 172 | scripting / filesystem/traverse/small | fresh-process-repeated | 4.675 ms | luajit | 6.719 | 0.70× |
| 173 | task-runners / mixed-1000-j4/shared | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 6995.226 ms | nx | 10424.701 | 0.67× |
| 174 | task-runners / mixed-100-j4/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 1455.905 ms | nx | 2177.828 | 0.67× |
| 175 | template-engines / condition | source-render | 0.021 ms/render | liquid | 0.039 | 0.55× |
| 176 | template-engines / includes-1 | source-render | 0.041 ms/render | liquid | 0.073 | 0.55× |
| 177 | task-runners / mixed-100-j4/shared | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 909.355 ms | nx | 1651.660 | 0.55× |
| 178 | template-engines / nested-object | source-render | 0.023 ms/render | liquid | 0.042 | 0.55× |
| 179 | template-engines / transform | source-render | 0.021 ms/render | liquid | 0.038 | 0.54× |
| 180 | template-engines / loop-10 | source-render | 0.061 ms/render | nunjucks | 0.129 | 0.48× |
| 181 | template-engines / includes-8 | files | 0.289 ms/render | nunjucks | 0.616 | 0.47× |
| 182 | template-engines / includes-4 | files | 0.166 ms/render | nunjucks | 0.394 | 0.42× |
| 183 | task-runners / mixed-1000-j4/fanout | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 1506.146 ms | nx | 3642.456 | 0.41× |
| 184 | task-runners / mixed-20-j4/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 455.552 ms | nx | 1109.375 | 0.41× |
| 185 | task-runners / mixed-20-j4/uncached-full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 449.246 ms | nx | 1100.772 | 0.41× |
| 186 | task-runners / mixed-20-j4/shared | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 405.928 ms | nx | 1109.660 | 0.37× |
| 187 | template-engines / includes-1 | files | 0.075 ms/render | nunjucks | 0.209 | 0.36× |
| 188 | task-runners / mixed-20-j4/target-subgraph | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 398.739 ms | nx | 1117.192 | 0.36× |
| 189 | scripting / structured-data/json-transform/small | fresh-process-repeated | 10.185 ms | python | 32.257 | 0.32× |
| 190 | template-engines / collection | fresh | 17.563 ms/invocation | nunjucks | 60.855 | 0.29× |
| 191 | task-runners / mixed-1000-j4/noop | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 116.052 ms | turbo | 448.494 | 0.26× |
| 192 | scripting / structured-data/json-traverse/small | fresh-process-repeated | 8.186 ms | python | 34.804 | 0.24× |
| 193 | task-runners / mixed-1000-j4/leaf | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 168.475 ms | turbo | 760.235 | 0.22× |
| 194 | task-runners / tiny-1000-j4/noop | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 94.904 ms | turbo | 429.131 | 0.22× |
| 195 | task-runners / mixed-100-j4/noop | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 15.662 ms | turbo | 72.615 | 0.22× |
| 196 | template-engines / many-templates-1000 | fresh | 33.820 ms/invocation | liquid | 158.811 | 0.21× |
| 197 | task-runners / tiny-100-j4/noop | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 13.368 ms | turbo | 70.396 | 0.19× |
| 198 | template-engines / loop-1000 | fresh | 10.476 ms/invocation | nunjucks | 56.397 | 0.19× |
| 199 | task-runners / mixed-100-j4/fanout | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 164.566 ms | nx | 918.172 | 0.18× |
| 200 | scripting / structured-data/json-parse/small | fresh-process-repeated | 6.521 ms | python | 38.055 | 0.17× |
| 201 | template-engines / many-renders-1000 | fresh | 25.767 ms/invocation | liquid | 167.375 | 0.15× |
| 202 | task-runners / mixed-100-j4/leaf | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 64.114 ms | turbo | 423.983 | 0.15× |
| 203 | task-runners / tiny-1000-j4/leaf | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 99.942 ms | turbo | 694.264 | 0.14× |
| 204 | task-runners / mixed-20-j4/fanout | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 60.539 ms | turbo | 444.168 | 0.14× |
| 205 | task-runners / tiny-1000-j4/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 1457.303 ms | nx | 10830.442 | 0.13× |
| 206 | task-runners / mixed-20-j4/leaf | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 55.061 ms | turbo | 415.621 | 0.13× |
| 207 | task-runners / mixed-20-j4/target-leaf | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 54.437 ms | turbo | 423.341 | 0.13× |
| 208 | task-runners / mixed-20-j4/multi-target | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 54.831 ms | turbo | 439.947 | 0.12× |
| 209 | task-runners / mixed-20-j4/noop | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 6.950 ms | turbo | 58.651 | 0.12× |
| 210 | template-engines / nested-loops | fresh | 5.711 ms/invocation | nunjucks | 52.368 | 0.11× |
| 211 | task-runners / tiny-1000-j4/fanout | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 240.522 ms | nx | 2550.482 | 0.09× |
| 212 | template-engines / loop-100 | fresh | 4.673 ms/invocation | nunjucks | 51.498 | 0.09× |
| 213 | template-engines / many-templates-100 | fresh | 6.953 ms/invocation | liquid | 79.544 | 0.09× |
| 214 | template-engines / article | fresh | 4.318 ms/invocation | nunjucks | 51.942 | 0.08× |
| 215 | task-runners / tiny-100-j4/full | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 116.526 ms | nx | 1404.365 | 0.08× |
| 216 | template-engines / literal | fresh | 3.917 ms/invocation | nunjucks | 48.173 | 0.08× |
| 217 | template-engines / transform | fresh | 3.946 ms/invocation | nunjucks | 49.010 | 0.08× |
| 218 | template-engines / condition | fresh | 4.055 ms/invocation | nunjucks | 50.355 | 0.08× |
| 219 | template-engines / loop-10 | fresh | 4.087 ms/invocation | nunjucks | 51.372 | 0.08× |
| 220 | template-engines / many-templates-10 | fresh | 4.124 ms/invocation | nunjucks | 52.388 | 0.08× |
| 221 | template-engines / nested-object | fresh | 3.927 ms/invocation | nunjucks | 50.023 | 0.08× |
| 222 | template-engines / includes-1 | fresh | 3.921 ms/invocation | nunjucks | 50.284 | 0.08× |
| 223 | template-engines / interpolation | fresh | 3.901 ms/invocation | nunjucks | 50.401 | 0.08× |
| 224 | template-engines / many-renders-100 | fresh | 5.850 ms/invocation | liquid | 75.591 | 0.08× |
| 225 | template-engines / includes-8 | fresh | 4.061 ms/invocation | nunjucks | 54.251 | 0.07× |
| 226 | template-engines / includes-4 | fresh | 3.972 ms/invocation | nunjucks | 53.366 | 0.07× |
| 227 | task-runners / tiny-1000-j4/one-percent | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 112.575 ms | turbo | 1518.250 | 0.07× |
| 228 | task-runners / tiny-100-j4/one-percent | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 18.067 ms | turbo | 378.943 | 0.05× |
| 229 | task-runners / tiny-100-j4/leaf | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 17.818 ms | turbo | 386.138 | 0.05× |
| 230 | task-runners / tiny-100-j4/fanout | fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 25.311 ms | nx | 746.596 | 0.03× |

Memory/throughput/capabilities require their own comparable scope. Template fresh-process memory floor is confirmed and unranked; maximum-child RSS is not aggregate-tree memory. Practical priority and likely subsystems are tracked separately. Previous peer deficits and remaining suites will be added after their audits.
