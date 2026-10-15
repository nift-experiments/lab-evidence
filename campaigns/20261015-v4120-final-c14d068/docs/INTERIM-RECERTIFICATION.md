# Interim final-candidate recertification

Audited official suites: scripting, template-engines, concurrency, website-generator, task-runners, shell. Exact-source three-way version diagnostics remain separate from current official peer results and historical cross-node trends. No publication or release is authorized.

## Best same-node wall improvements versus explicit baseline — complete

| Rank | Suite / scenario | Baseline | Previous | Final | Unit | Improvement | Evidence basis |
|---:|---|---|---:|---:|---|---:|---|
| 1 | template-engines / loop-10000/source-render | release | 118.471604 | 32.942846 | ms/render | 72.19% | Same node, 3 samples/version; descriptive same-node three-version3samples; no formal significance; checkpoint increases have overlapping ranges |
| 2 | shell / string-transform | original | 66.950305 | 18.680011 | ms/invocation | 72.10% | Same node, 10 samples/version; All10 final pairs faster than original with disjoint ranges. Strings also all10 faster than release with disjoint ranges; calls/release overlap and8/10 final slower, residual descriptive. |
| 3 | concurrency / queue-100000-4-4 | release | 37528.313677 | 11455.302198 | ms/request | 69.48% | Same node, 3 samples/version; descriptive same-node3pairs; schedule ranges overlap, no formal significance |
| 4 | shell / string-transform | release | 59.695733 | 18.680011 | ms/invocation | 68.71% | Same node, 10 samples/version; All10 final pairs faster than original with disjoint ranges. Strings also all10 faster than release with disjoint ranges; calls/release overlap and8/10 final slower, residual descriptive. |
| 5 | scripting / sanity/function-calls/large | original | 469.418897 | 198.619788 | ms/invocation | 57.69% | Same node, 10 samples/version; Descriptive paired same-node. Final/release ranges overlap; large8/10 pairs slower despite modest residual, small6/10 slower. Original/final ranges disjoint and all10 final faster. |
| 6 | shell / function-calls | original | 44.971487 | 21.655462 | ms/invocation | 51.85% | Same node, 10 samples/version; All10 final pairs faster than original with disjoint ranges. Strings also all10 faster than release with disjoint ranges; calls/release overlap and8/10 final slower, residual descriptive. |
| 7 | template-engines / loop-10000/fresh | release | 158.529676 | 77.354308 | ms/invocation | 51.21% | Same node, 3 samples/version; descriptive same-node three-version3samples; no formal significance; checkpoint increases have overlapping ranges |
| 8 | template-engines / article/source-render | release | 0.433770 | 0.268566 | ms/render | 38.09% | Same node, 3 samples/version; descriptive same-node three-version3samples; no formal significance; checkpoint increases have overlapping ranges |
| 9 | scripting / sanity/function-calls/small | original | 7.374958 | 4.678490 | ms/invocation | 36.56% | Same node, 10 samples/version; Descriptive paired same-node. Final/release ranges overlap; large8/10 pairs slower despite modest residual, small6/10 slower. Original/final ranges disjoint and all10 final faster. |
| 10 | website-generator / 10000/application-cold | original | 3278.509241 | 2951.495366 | ms/invocation | 9.97% | Same node, 5 samples/version; Descriptive paired same-node: final/original disjoint ranges, all five faster; final/release overlapping ranges, three of five slower; no equality or formal significance claim. |
| 11 | concurrency / schedule-1000 | original | 386.410787 | 362.049988 | ms/request | 6.30% | Same node, 3 samples/version; descriptive same-node3pairs; schedule ranges overlap, no formal significance |
| 12 | template-engines / article/fresh | release | 3.689644 | 3.507010 | ms/invocation | 4.95% | Same node, 3 samples/version; descriptive same-node three-version3samples; no formal significance; checkpoint increases have overlapping ranges |
| 13 | concurrency / queue-100000-4-4 | original | 12015.063135 | 11455.302198 | ms/request | 4.66% | Same node, 3 samples/version; descriptive same-node3pairs; schedule ranges overlap, no formal significance |
| 14 | task-runners / tiny-100-j4/full | release | 138.332636 | 134.851296 | ms/invocation | 2.52% | Same node, 5 samples/version; Descriptive same-node rotated five samples/source; overlapping ranges, no formal significance or major regression claim. |
| 15 | template-engines / loop-10000/source-render | original | 33.514301 | 32.942846 | ms/render | 1.71% | Same node, 3 samples/version; descriptive same-node three-version3samples; no formal significance; checkpoint increases have overlapping ranges |
| 16 | template-engines / article/fresh | original | 3.558491 | 3.507010 | ms/invocation | 1.45% | Same node, 3 samples/version; descriptive same-node three-version3samples; no formal significance; checkpoint increases have overlapping ranges |
| 17 | scripting / sanity/function-calls/small | release | 4.710201 | 4.678490 | ms/invocation | 0.67% | Same node, 10 samples/version; Descriptive paired same-node. Final/release ranges overlap; large8/10 pairs slower despite modest residual, small6/10 slower. Original/final ranges disjoint and all10 final faster. |

## Every measured positive same-node wall change — complete

| Rank | Suite / scenario | Baseline | Baseline value | Final | Increase | Classification |
|---:|---|---|---:|---:|---:|---|
| 1 | concurrency / schedule-1000 | release | 333.087228 | 362.049988 | 8.70% | descriptive same-node increase; not formal significance |
| 2 | template-engines / loop-10000/fresh | original | 73.741216 | 77.354308 | 4.90% | descriptive same-node increase; not formal significance |
| 3 | task-runners / tiny-100-j4/full | original | 129.031413 | 134.851296 | 4.51% | descriptive same-node increase; not formal significance |
| 4 | shell / function-calls | release | 20.989496 | 21.655462 | 3.17% | descriptive same-node increase; not formal significance |
| 5 | website-generator / 10000/application-cold | release | 2871.544599 | 2951.495366 | 2.78% | descriptive same-node increase; not formal significance |
| 6 | scripting / sanity/function-calls/large | release | 193.600459 | 198.619788 | 2.59% | descriptive same-node increase; not formal significance |
| 7 | template-engines / article/source-render | original | 0.267626 | 0.268566 | 0.35% | descriptive same-node increase; not formal significance |

Every comparison above uses the same node, exact versions and frozen diagnostic boundaries. Template diagnostics have three measured observations/version and remain descriptive. Scripting has ten; final/release ranges overlap, and large calls are slower in eight of ten paired blocks. Overlapping ranges do not prove equality or eliminate a small regression. Major original call regressions have disjoint ranges and all ten final blocks faster. Near-flat changes are retained. Original/checkpoint and release baselines are explicitly distinguished.

## Current same-node peer wall deficits — complete

Previous controlled peer deficits and their direction are unavailable unless explicitly derived below. Do not substitute historical cross-node ratios. Ratios at or below one are strengths and excluded from this deficit league.

| Rank | Suite / scenario / boundary | Nift | Best peer | Peer | Unit | Nift / peer |
|---:|---|---:|---|---:|---|---:|
| 1 | concurrency / tiny-10000/persistent | 30949.0168 | go | 17.7807 | ms | 1740.60× |
| 2 | concurrency / schedule-10000/persistent | 28018.8325 | go | 17.9894 | ms | 1557.52× |
| 3 | concurrency / schedule-10000/fresh | 31801.9653 | go | 29.0270 | ms | 1095.60× |
| 4 | concurrency / tiny-10000/fresh | 28070.5369 | go | 26.4739 | ms | 1060.31× |
| 5 | concurrency / mutex-8-2/persistent | 253.5942 | go | 0.9629 | ms | 263.38× |
| 6 | concurrency / mutex-8-4/persistent | 275.1630 | go | 1.1600 | ms | 237.22× |
| 7 | concurrency / mutex-1-2/persistent | 211.7520 | go | 1.0000 | ms | 211.74× |
| 8 | concurrency / mutex-1-4/persistent | 221.8101 | go | 1.0646 | ms | 208.35× |
| 9 | concurrency / cpu-1/persistent | 10913.0155 | go | 52.8554 | ms | 206.47× |
| 10 | concurrency / mutex-8-1/persistent | 225.6658 | go | 1.1313 | ms | 199.47× |
| 11 | concurrency / cpu-2/persistent | 5409.6732 | go | 27.5158 | ms | 196.60× |
| 12 | concurrency / queue-100000-4-4/persistent | 11833.7858 | bun | 62.2320 | ms | 190.16× |
| 13 | concurrency / cpu-4/persistent | 2866.4145 | go | 15.3793 | ms | 186.38× |
| 14 | concurrency / waiting-memory-1000/persistent | 2796.1579 | go | 15.2108 | ms | 183.83× |
| 15 | concurrency / cpu-1/fresh | 10808.9056 | go | 60.9390 | ms | 177.37× |
| 16 | concurrency / wait-1000/persistent | 2579.5202 | go | 14.6987 | ms | 175.49× |
| 17 | concurrency / queue-100000-1-1/persistent | 10500.5619 | bun | 61.3428 | ms | 171.18× |
| 18 | concurrency / mutex-1-1/persistent | 181.6757 | go | 1.1000 | ms | 165.16× |
| 19 | concurrency / queue-100000-4-1/persistent | 11683.5527 | bun | 70.8110 | ms | 165.00× |
| 20 | concurrency / cpu-2/fresh | 5540.9751 | go | 33.6799 | ms | 164.52× |
| 21 | concurrency / queue-100000-1-4/persistent | 11340.7873 | bun | 76.7329 | ms | 147.80× |
| 22 | concurrency / atomic-1/persistent | 131.8174 | go | 0.9252 | ms | 142.48× |
| 23 | scripting / arrays-strings-hash/frequency-count/large | 416.5421 | luajit | 3.0221 | ms/invocation | 137.83× |
| 24 | scripting / sanity/function-calls/large | 193.7259 | luajit | 1.4189 | ms/invocation | 136.53× |
| 25 | concurrency / wait-1000/fresh | 2607.2294 | go | 20.7751 | ms | 125.50× |
| 26 | concurrency / pool-heavy-1/persistent | 292.2988 | go | 2.4181 | ms | 120.88× |
| 27 | concurrency / waiting-memory-1000/fresh | 2853.1283 | go | 23.7630 | ms | 120.07× |
| 28 | concurrency / queue-100000-4-4/fresh | 11409.9278 | bun | 95.7602 | ms | 119.15× |
| 29 | concurrency / cpu-4/fresh | 2836.4923 | go | 24.1281 | ms | 117.56× |
| 30 | concurrency / queue-100000-4-1/fresh | 11790.8268 | bun | 106.5410 | ms | 110.67× |
| 31 | concurrency / queue-100000-1-1/fresh | 10301.0362 | bun | 94.4906 | ms | 109.02× |
| 32 | concurrency / fan-1000/persistent | 326.7255 | go | 3.0122 | ms | 108.47× |
| 33 | concurrency / tiny-1000/persistent | 328.2792 | go | 3.0598 | ms | 107.29× |
| 34 | concurrency / queue-100000-1-4/fresh | 11194.0954 | bun | 105.0965 | ms | 106.51× |
| 35 | concurrency / schedule-1000/persistent | 307.2421 | go | 2.9273 | ms | 104.96× |
| 36 | scripting / arrays-strings-hash/sliding-window/large | 250.1156 | luajit | 2.4040 | ms/invocation | 104.04× |
| 37 | concurrency / queue-10000-4-4/persistent | 1166.0923 | go | 12.5924 | ms | 92.60× |
| 38 | concurrency / queue-10000-4-1/persistent | 1122.0983 | go | 12.2044 | ms | 91.94× |
| 39 | concurrency / queue-10000-1-1/persistent | 1060.8077 | go | 12.0501 | ms | 88.03× |
| 40 | concurrency / queue-10000-1-4/persistent | 1125.6212 | go | 12.9023 | ms | 87.24× |
| 41 | scripting / arrays-strings-hash/map-set/large | 212.6967 | luajit | 2.6333 | ms/invocation | 80.77× |
| 42 | concurrency / pool-heavy-2/persistent | 150.4878 | go | 1.9216 | ms | 78.31× |
| 43 | concurrency / atomic-2/persistent | 75.2671 | go | 1.0665 | ms | 70.58× |
| 44 | scripting / dynamic-programming/fibonacci/large | 141.5248 | luajit | 2.0596 | ms/invocation | 68.72× |
| 45 | concurrency / queue-10000-1-4/fresh | 1135.5370 | go | 18.2026 | ms | 62.38× |
| 46 | scripting / arrays-strings-hash/scan/large | 82.8741 | luajit | 1.3739 | ms/invocation | 60.32× |
| 47 | concurrency / queue-10000-4-1/fresh | 1131.3235 | go | 18.8516 | ms | 60.01× |
| 48 | concurrency / queue-10000-4-4/fresh | 1155.8607 | go | 19.3877 | ms | 59.62× |
| 49 | concurrency / queue-10000-1-1/fresh | 1055.3027 | go | 17.8419 | ms | 59.15× |
| 50 | concurrency / queue-1000-4-4/persistent | 120.4391 | go | 2.1225 | ms | 56.74× |
| 51 | concurrency / queue-1000-1-4/persistent | 118.6310 | go | 2.0944 | ms | 56.64× |
| 52 | concurrency / queue-1000-4-1/persistent | 120.9598 | go | 2.1435 | ms | 56.43× |
| 53 | scripting / sanity/loops/large | 72.5922 | luajit | 1.4192 | ms/invocation | 51.15× |
| 54 | concurrency / queue-1000-1-1/persistent | 105.5744 | go | 2.1562 | ms | 48.96× |
| 55 | scripting / graphs-trees-search/bfs/large | 799.3592 | luajit | 16.9315 | ms/invocation | 47.21× |
| 56 | concurrency / pool-heavy-4/persistent | 79.3047 | go | 1.8696 | ms | 42.42× |
| 57 | concurrency / atomic-4/persistent | 46.1550 | go | 1.0964 | ms | 42.10× |
| 58 | concurrency / pool-heavy-1/fresh | 294.3978 | go | 7.2668 | ms | 40.51× |
| 59 | concurrency / fan-1000/fresh | 332.0085 | go | 8.4646 | ms | 39.22× |
| 60 | concurrency / tiny-1000/fresh | 305.4130 | go | 7.8016 | ms | 39.15× |
| 61 | concurrency / schedule-1000/fresh | 262.7284 | go | 7.4816 | ms | 35.12× |
| 62 | concurrency / mutex-8-2/fresh | 268.4126 | go | 8.5771 | ms | 31.29× |
| 63 | concurrency / mutex-8-4/fresh | 274.3082 | go | 8.9422 | ms | 30.68× |
| 64 | concurrency / nested-100/persistent | 53.6530 | go | 1.8547 | ms | 28.93× |
| 65 | concurrency / mutex-8-1/fresh | 233.2463 | go | 8.1730 | ms | 28.54× |
| 66 | concurrency / pool-medium-1/persistent | 32.5850 | go | 1.1604 | ms | 28.08× |
| 67 | concurrency / mutex-1-2/fresh | 221.5863 | go | 8.1503 | ms | 27.19× |
| 68 | concurrency / mutex-1-4/fresh | 241.7080 | go | 9.0440 | ms | 26.73× |
| 69 | concurrency / mutex-1-1/fresh | 189.4023 | go | 8.4002 | ms | 22.55× |
| 70 | concurrency / pool-light-1/persistent | 22.0090 | go | 0.9859 | ms | 22.32× |
| 71 | scripting / arrays-strings-hash/sort-index/large | 511.6308 | python | 23.0522 | ms/invocation | 22.19× |
| 72 | concurrency / waiting-memory-100/persistent | 264.0268 | go | 11.9635 | ms | 22.07× |
| 73 | concurrency / wait-100/persistent | 259.2278 | go | 11.9826 | ms | 21.63× |
| 74 | concurrency / pool-heavy-2/fresh | 155.0466 | go | 7.4547 | ms | 20.80× |
| 75 | concurrency / files-10000/persistent | 1446.8240 | go | 72.4073 | ms | 19.98× |
| 76 | concurrency / files-10000/fresh | 1461.2957 | go | 79.5973 | ms | 18.36× |
| 77 | concurrency / files-1000/persistent | 145.3815 | go | 7.9992 | ms | 18.17× |
| 78 | concurrency / atomic-1/fresh | 136.9979 | go | 7.8062 | ms | 17.55× |
| 79 | concurrency / queue-1000-1-4/fresh | 124.7663 | go | 7.4661 | ms | 16.71× |
| 80 | concurrency / queue-1000-4-4/fresh | 127.2198 | go | 7.8016 | ms | 16.31× |
| 81 | concurrency / queue-1000-4-1/fresh | 123.8996 | go | 7.6017 | ms | 16.30× |
| 82 | concurrency / wait-100/fresh | 265.5381 | go | 16.3085 | ms | 16.28× |
| 83 | template-engines / loop-10000/source-render | 34.0847 | handlebars | 2.2486 | ms/render | 15.16× |
| 84 | concurrency / pool-medium-2/persistent | 18.4455 | go | 1.2235 | ms | 15.08× |
| 85 | concurrency / queue-1000-1-1/fresh | 111.5006 | go | 7.5685 | ms | 14.73× |
| 86 | concurrency / waiting-memory-100/fresh | 274.6798 | go | 20.3128 | ms | 13.52× |
| 87 | concurrency / schedule-100/persistent | 16.4205 | go | 1.2373 | ms | 13.27× |
| 88 | concurrency / stagger-100/persistent | 279.9780 | go | 22.0836 | ms | 12.68× |
| 89 | concurrency / tiny-100/persistent | 14.8006 | go | 1.1894 | ms | 12.44× |
| 90 | concurrency / fan-100/persistent | 15.3168 | go | 1.3008 | ms | 11.77× |
| 91 | concurrency / files-100/persistent | 22.6972 | go | 1.9601 | ms | 11.58× |
| 92 | concurrency / pool-light-2/persistent | 13.0158 | go | 1.1585 | ms | 11.23× |
| 93 | concurrency / pool-heavy-4/fresh | 87.2585 | go | 8.0942 | ms | 10.78× |
| 94 | concurrency / stagger-100/fresh | 287.4284 | go | 27.0907 | ms | 10.61× |
| 95 | concurrency / files-1000/fresh | 154.3703 | go | 14.7866 | ms | 10.44× |
| 96 | concurrency / atomic-2/fresh | 88.3376 | go | 9.7062 | ms | 9.10× |
| 97 | concurrency / pool-medium-4/persistent | 11.2288 | go | 1.2728 | ms | 8.82× |
| 98 | template-engines / collection/source-render | 7.1487 | handlebars | 0.8673 | ms/render | 8.24× |
| 99 | concurrency / nested-10/persistent | 7.4980 | go | 1.0446 | ms | 7.18× |
| 100 | concurrency / nested-100/fresh | 68.9687 | go | 9.7549 | ms | 7.07× |
| 101 | concurrency / pool-light-4/persistent | 7.9990 | go | 1.2280 | ms | 6.51× |
| 102 | concurrency / pool-medium-1/fresh | 39.6197 | go | 6.2228 | ms | 6.37× |
| 103 | scripting / structured-data/json-transform/large | 462.8532 | node | 74.5456 | ms/invocation | 6.21× |
| 104 | concurrency / atomic-4/fresh | 56.5908 | go | 9.1779 | ms | 6.17× |
| 105 | scripting / graphs-trees-search/bfs/small | 11.4051 | lua54 | 1.8680 | ms/invocation | 6.11× |
| 106 | scripting / structured-data/json-traverse/large | 370.4149 | node | 68.6082 | ms/invocation | 5.40× |
| 107 | scripting / arrays-strings-hash/frequency-count/small | 7.0682 | luajit | 1.3125 | ms/invocation | 5.39× |
| 108 | template-engines / loop-1000/source-render | 3.2934 | handlebars | 0.6493 | ms/render | 5.07× |
| 109 | concurrency / pool-light-1/fresh | 27.9631 | go | 6.1161 | ms | 4.57× |
| 110 | scripting / arrays-strings-hash/sort-index/small | 6.8471 | luajit | 1.5076 | ms/invocation | 4.54× |
| 111 | template-engines / literal/source-render | 0.0152 | liquid | 0.0036 | ms/render | 4.21× |
| 112 | concurrency / mixed-wait-100/persistent | 89.3006 | go | 21.5602 | ms | 4.14× |
| 113 | concurrency / schedule-100/fresh | 24.9326 | go | 6.1022 | ms | 4.09× |
| 114 | shell / traverse-100000/shell-workloads.json | 1032.9553 | nu | 255.0395 | ms | 4.05× |
| 115 | scripting / arrays-strings-hash/sliding-window/small | 5.2873 | luajit | 1.3394 | ms/invocation | 3.95× |
| 116 | concurrency / pool-medium-2/fresh | 25.0479 | go | 6.7361 | ms | 3.72× |
| 117 | concurrency / tiny-100/fresh | 22.9509 | go | 6.2963 | ms | 3.65× |
| 118 | concurrency / mixed-wait-100/fresh | 96.2921 | go | 26.6700 | ms | 3.61× |
| 119 | concurrency / fan-100/fresh | 21.4875 | go | 6.0013 | ms | 3.58× |
| 120 | scripting / sanity/function-calls/small | 4.6504 | luajit | 1.3011 | ms/invocation | 3.57× |
| 121 | concurrency / schedule-10/persistent | 3.3856 | go | 0.9958 | ms | 3.40× |
| 122 | scripting / arrays-strings-hash/map-set/small | 4.7012 | luajit | 1.3955 | ms/invocation | 3.37× |
| 123 | concurrency / fan-10/persistent | 3.4225 | go | 1.0168 | ms | 3.37× |
| 124 | concurrency / tiny-10/persistent | 3.4552 | go | 1.0271 | ms | 3.36× |
| 125 | scripting / filesystem/traverse/large | 25.0047 | luajit | 7.6408 | ms/invocation | 3.27× |
| 126 | concurrency / files-100/fresh | 25.0290 | go | 7.7302 | ms | 3.24× |
| 127 | concurrency / failures/persistent | 3.6130 | go | 1.1228 | ms | 3.22× |
| 128 | concurrency / pool-light-2/fresh | 18.7950 | go | 6.0366 | ms | 3.11× |
| 129 | concurrency / process-1000/fresh | 986.5840 | go | 330.7045 | ms | 2.98× |
| 130 | concurrency / process-1000/persistent | 1001.1120 | go | 336.3992 | ms | 2.98× |
| 131 | shell / metadata-10000/shell-workloads.json | 118.6269 | fish | 40.6527 | ms | 2.92× |
| 132 | scripting / arrays-strings-hash/scan/small | 3.5558 | luajit | 1.2906 | ms/invocation | 2.76× |
| 133 | scripting / structured-data/json-parse/large | 182.0766 | node | 66.9882 | ms/invocation | 2.72× |
| 134 | concurrency / process-one-failure/persistent | 99.5204 | go | 37.0044 | ms | 2.69× |
| 135 | scripting / sanity/loops/small | 3.3463 | luajit | 1.2815 | ms/invocation | 2.61× |
| 136 | concurrency / process-100/persistent | 96.9259 | go | 37.5413 | ms | 2.58× |
| 137 | concurrency / pool-medium-4/fresh | 17.6773 | go | 7.0240 | ms | 2.52× |
| 138 | concurrency / process-many-failures/persistent | 90.3119 | go | 35.9896 | ms | 2.51× |
| 139 | concurrency / process-100/fresh | 103.2234 | go | 41.5633 | ms | 2.48× |
| 140 | concurrency / process-one-failure/fresh | 106.1708 | go | 42.9256 | ms | 2.47× |
| 141 | concurrency / process-many-failures/fresh | 107.4996 | go | 44.0543 | ms | 2.44× |
| 142 | shell / concat-small-10000/shell-workloads.json | 252.6080 | zsh | 105.0090 | ms | 2.41× |
| 143 | concurrency / process-10/persistent | 12.2189 | go | 5.1030 | ms | 2.39× |
| 144 | shell / create-small-100000/shell-workloads.json | 10823.5322 | nu | 4769.2090 | ms | 2.27× |
| 145 | concurrency / pool-light-4/fresh | 15.3313 | go | 6.8087 | ms | 2.25× |
| 146 | scripting / dynamic-programming/fibonacci/small | 2.8171 | luajit | 1.2633 | ms/invocation | 2.23× |
| 147 | concurrency / nested-10/fresh | 17.1503 | go | 8.0910 | ms | 2.12× |
| 148 | template-engines / many-templates-100/source-render | 0.0214 | liquid | 0.0102 | ms/render | 2.09× |
| 149 | template-engines / nested-loops/source-render | 1.0676 | nunjucks | 0.5115 | ms/render | 2.09× |
| 150 | scripting / sanity/output/small | 2.5214 | luajit | 1.2174 | ms/invocation | 2.07× |
| 151 | template-engines / many-templates-1000/source-render | 0.0215 | liquid | 0.0105 | ms/render | 2.06× |
| 152 | scripting / sanity/noop/large | 2.3885 | luajit | 1.1839 | ms/invocation | 2.02× |
| 153 | scripting / sanity/noop/small | 2.4628 | luajit | 1.2283 | ms/invocation | 2.01× |
| 154 | scripting / sanity/output/large | 2.4649 | luajit | 1.2294 | ms/invocation | 2.00× |
| 155 | template-engines / many-templates-10/source-render | 0.0212 | liquid | 0.0108 | ms/render | 1.96× |
| 156 | concurrency / schedule-10/fresh | 9.2472 | go | 5.0691 | ms | 1.82× |
| 157 | concurrency / tiny-10/fresh | 9.5623 | go | 5.6499 | ms | 1.69× |
| 158 | concurrency / process-10/fresh | 18.3494 | go | 11.0670 | ms | 1.66× |
| 159 | concurrency / fan-10/fresh | 10.1324 | go | 6.1978 | ms | 1.63× |
| 160 | concurrency / mixed-64/persistent | 93.2786 | go | 58.5399 | ms | 1.59× |
| 161 | shell / rename-selected-10000/shell-workloads.json | 546.7870 | zsh | 344.7020 | ms | 1.59× |
| 162 | concurrency / failures/fresh | 11.8777 | go | 7.8232 | ms | 1.52× |
| 163 | concurrency / mixed-64/fresh | 102.4158 | go | 68.2898 | ms | 1.50× |
| 164 | concurrency / process-mixed/persistent | 119.1383 | go | 79.6985 | ms | 1.49× |
| 165 | template-engines / many-renders-1000/source-render | 0.0225 | liquid | 0.0151 | ms/render | 1.49× |
| 166 | template-engines / loop-100/source-render | 0.3643 | nunjucks | 0.2449 | ms/render | 1.49× |
| 167 | concurrency / process-mixed/fresh | 128.1481 | go | 86.6269 | ms | 1.48× |
| 168 | shell / copy-small-10000/shell-workloads.json | 768.2193 | zsh | 523.0843 | ms | 1.47× |
| 169 | shell / bare/immediate-exit/shell-repeated.json | 2.4251 | bash | 1.7123 | ms | 1.42× |
| 170 | shell / selected-cleanup/shell-workloads.json | 44.7825 | bash | 32.4980 | ms | 1.38× |
| 171 | shell / bare/trivial-command/shell-application-cold.json | 2.2155 | bash | 1.6213 | ms | 1.37× |
| 172 | shell / bare/immediate-exit/shell-application-cold.json | 2.3335 | bash | 1.7165 | ms | 1.36× |
| 173 | shell / bare/trivial-command/shell-repeated.json | 2.2018 | bash | 1.6202 | ms | 1.36× |
| 174 | template-engines / many-renders-100/source-render | 0.0218 | liquid | 0.0161 | ms/render | 1.35× |
| 175 | shell / delete-selected-100000/shell-workloads.json | 2966.7268 | bash | 2218.0972 | ms | 1.34× |
| 176 | shell / processes-1/shell-workloads.json | 3.5277 | bash | 2.6390 | ms | 1.34× |
| 177 | shell / processes-1000/shell-workloads.json | 910.4066 | fish | 685.0305 | ms | 1.33× |
| 178 | shell / bare/function-string/shell-application-cold.json | 2.2527 | bash | 1.7073 | ms | 1.32× |
| 179 | shell / string-transform/shell-workloads.json | 18.9177 | zsh | 14.4408 | ms | 1.31× |
| 180 | shell / bare/function-string/shell-repeated.json | 2.2555 | bash | 1.7233 | ms | 1.31× |
| 181 | shell / delete-tree-100000/shell-workloads.json | 2847.6944 | bash | 2198.8773 | ms | 1.30× |
| 182 | shell / bare/file-roundtrip/shell-application-cold.json | 4.8790 | bash | 3.8105 | ms | 1.28× |
| 183 | shell / processes-100/shell-workloads.json | 93.5047 | fish | 73.1391 | ms | 1.28× |
| 184 | shell / bare/external-100/shell-repeated.json | 92.9689 | fish | 74.4041 | ms | 1.25× |
| 185 | shell / bare/external-100/shell-application-cold.json | 90.8337 | fish | 73.1076 | ms | 1.24× |
| 186 | template-engines / includes-8/source-render | 0.1629 | nunjucks | 0.1315 | ms/render | 1.24× |
| 187 | shell / bare/file-roundtrip/shell-repeated.json | 4.9104 | bash | 4.0217 | ms | 1.22× |
| 188 | shell / bare/command-capture/shell-application-cold.json | 3.5446 | bash | 2.9322 | ms | 1.21× |
| 189 | shell / delete-selected-10000/shell-workloads.json | 240.2922 | fish | 201.8814 | ms | 1.19× |
| 190 | shell / bare/short-pipeline/shell-repeated.json | 5.0983 | bash | 4.3345 | ms | 1.18× |
| 191 | shell / pipeline-2/shell-workloads.json | 4.8866 | bash | 4.2130 | ms | 1.16× |
| 192 | shell / processes-10/shell-workloads.json | 11.7661 | bash | 10.1922 | ms | 1.15× |
| 193 | shell / bare/short-pipeline/shell-application-cold.json | 4.8216 | bash | 4.1906 | ms | 1.15× |
| 194 | website-generator / 10000/application-cold | 3015.9805 | Hugo | 2623.3373 | ms/build | 1.15× |
| 195 | shell / pipeline-4/shell-workloads.json | 7.2302 | fish | 6.3260 | ms | 1.14× |
| 196 | shell / bare/command-capture/shell-repeated.json | 3.5143 | bash | 3.1195 | ms | 1.13× |
| 197 | shell / create-empty-1000/shell-workloads.json | 38.3239 | bash | 34.0955 | ms | 1.12× |
| 198 | shell / pipeline-8/shell-workloads.json | 11.6971 | fish | 10.4197 | ms | 1.12× |
| 199 | shell / create-empty-10000/shell-workloads.json | 367.9989 | bash | 330.9692 | ms | 1.11× |
| 200 | shell / create-empty-100000/shell-workloads.json | 3884.6723 | bash | 3499.2959 | ms | 1.11× |
| 201 | shell / delete-selected-1000/shell-workloads.json | 25.0485 | bash | 23.0955 | ms | 1.08× |
| 202 | website-generator / 1000/application-cold | 303.1342 | Hugo | 279.8608 | ms/build | 1.08× |
| 203 | shell / log-filter-group/shell-workloads.json | 47.6859 | fish | 45.6456 | ms | 1.04× |
| 204 | shell / source-tree-report/shell-workloads.json | 229.7415 | bash | 220.3906 | ms | 1.04× |
| 205 | template-engines / includes-4/source-render | 0.0890 | liquid | 0.0859 | ms/render | 1.04× |

## Large gains but still behind

| Scenario | Baseline | Improvement | Current deficit | Interpretation |
|---|---|---:|---:|---|
| template loop10k/source-render | release | 72.19% | 15.16× | Large source-render gain; still behind Handlebars |
| scripting calls/large | original | 57.69% | 136.53× | Broken-candidate recovery; still behind LuaJIT |
| concurrency queue100k/4-4 | release | 69.48% | 190.16× | Isolated booted-request version diagnostic; official persistent peer cohort is separate, not identical boundary |

Derived old deficits divide controlled old Nift diagnostic medians by the current official peer median on the same host and matching boundary. These are cross-phase diagnostics, not a simultaneously interleaved old-Nift/peer benchmark. Current deficits use official Nift/peer medians from the same cohort. No cross-node peer denominator is substituted.

## Memory and capabilities remain separate

Supervisor allocation0→64MiB moves noopraw16.75→80.75MiB, proving inherited floor; raw retained/unranked.

Raw scripting call peak-memory diagnostics are retained separately; small quantized differences do not establish a leak or superiority. Nift public parse-only/prepared-AST template modes remain unsupported in this frozen public-API matrix. Nift has lower medians than the best other template engine in 30 of 43 supported matching fresh/source-render cells; this is not an overall engine ranking. Task Nift leads all31 official wall and maximum-child RSS configurations. Current direct practitioner choices are maintained in PREFERENCE-CHANGES.md; release recommendation waits for the remaining three suites.
