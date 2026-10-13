# Cross-benchmark regressions — interim diagnostic draft

## Same-node scripting diagnostic

All720observations audited. Callcases have10/10pairs slower and nonoverlapping ranges; other numerical increases are descriptive with varying noise.

| Rank | Scenario | Old ms | Candidate ms | Increase | Basis |
|---:|---|---:|---:|---:|---|
| 1 | sanity/function-calls/large | 228.284 | 561.026 | 145.76% | 10/10pairs slower, nonoverlapping ranges |
| 2 | sanity/function-calls/small | 6.080 | 10.069 | 65.63% | 10/10pairs slower, nonoverlapping ranges |
| 3 | arrays-strings-hash/frequency-count/small | 8.303 | 10.659 | 28.37% | paired diagnostic median; significance not established |
| 4 | graphs-trees-search/bfs/small | 12.723 | 15.270 | 20.02% | paired diagnostic median; significance not established |
| 5 | structured-data/json-transform/large | 586.317 | 703.648 | 20.01% | paired diagnostic median; significance not established |
| 6 | arrays-strings-hash/frequency-count/large | 473.156 | 567.263 | 19.89% | paired diagnostic median; significance not established |
| 7 | graphs-trees-search/bfs/large | 844.177 | 999.076 | 18.35% | paired diagnostic median; significance not established |
| 8 | sanity/noop/small | 3.293 | 3.621 | 9.96% | paired diagnostic median; significance not established |
| 9 | structured-data/json-transform/small | 9.078 | 9.956 | 9.66% | paired diagnostic median; significance not established |
| 10 | structured-data/json-parse/large | 245.533 | 262.571 | 6.94% | paired diagnostic median; significance not established |
| 11 | dynamic-programming/fibonacci/small | 3.786 | 3.908 | 3.24% | paired diagnostic median; significance not established |
| 12 | filesystem/traverse/large | 38.742 | 39.603 | 2.22% | paired diagnostic median; significance not established |
| 13 | filesystem/traverse/small | 4.989 | 5.072 | 1.66% | paired diagnostic median; significance not established |

## Cross-node suspected wall regressions

| Rank | Benchmark / scenario / boundary | Old | Candidate | Increase |
|---:|---|---:|---:|---:|
| 1 | scripting / sanity/function-calls/large / fresh-process-repeated | 185.103 | 546.056 | 195.00% |
| 2 | scripting / sanity/function-calls/small / fresh-process-repeated | 4.987 | 10.027 | 101.08% |
| 3 | scripting / structured-data/json-parse/large / fresh-process-repeated | 192.276 | 295.195 | 53.53% |
| 4 | scripting / graphs-trees-search/bfs/large / fresh-process-repeated | 654.593 | 1002.530 | 53.15% |
| 5 | scripting / arrays-strings-hash/frequency-count/large / fresh-process-repeated | 385.547 | 589.370 | 52.87% |
| 6 | scripting / structured-data/json-transform/large / fresh-process-repeated | 464.025 | 669.316 | 44.24% |
| 7 | scripting / sanity/output/large / fresh-process-repeated | 2.709 | 3.814 | 40.77% |
| 8 | scripting / graphs-trees-search/bfs/small / fresh-process-repeated | 10.358 | 14.471 | 39.70% |
| 9 | scripting / arrays-strings-hash/frequency-count/small / fresh-process-repeated | 7.112 | 9.813 | 37.98% |
| 10 | scripting / structured-data/json-transform/small / fresh-process-repeated | 7.439 | 10.185 | 36.91% |
| 11 | concurrency / pool-light-1 / persistent | 16.488 | 22.541 | 36.72% |
| 12 | scripting / sanity/loops/small / fresh-process-repeated | 3.852 | 5.251 | 36.29% |
| 13 | scripting / arrays-strings-hash/sliding-window/small / fresh-process-repeated | 5.867 | 7.923 | 35.06% |
| 14 | scripting / dynamic-programming/fibonacci/small / fresh-process-repeated | 3.083 | 4.147 | 34.48% |
| 15 | scripting / arrays-strings-hash/map-set/small / fresh-process-repeated | 5.173 | 6.940 | 34.16% |
| 16 | scripting / structured-data/json-parse/small / fresh-process-repeated | 4.877 | 6.521 | 33.71% |
| 17 | scripting / arrays-strings-hash/map-set/large / fresh-process-repeated | 215.188 | 284.963 | 32.43% |
| 18 | scripting / structured-data/json-traverse/large / fresh-process-repeated | 357.846 | 473.779 | 32.40% |
| 19 | scripting / filesystem/traverse/large / fresh-process-repeated | 32.037 | 41.798 | 30.47% |
| 20 | scripting / sanity/noop/large / fresh-process-repeated | 2.553 | 3.310 | 29.68% |
| 21 | scripting / filesystem/traverse/small / fresh-process-repeated | 3.624 | 4.675 | 29.00% |
| 22 | scripting / arrays-strings-hash/scan/small / fresh-process-repeated | 4.129 | 5.315 | 28.72% |
| 23 | scripting / structured-data/json-traverse/small / fresh-process-repeated | 6.380 | 8.186 | 28.31% |
| 24 | concurrency / fan-1000 / fresh | 271.582 | 339.842 | 25.13% |
| 25 | scripting / sanity/noop/small / fresh-process-repeated | 4.721 | 5.855 | 24.03% |
| 26 | scripting / sanity/output/small / fresh-process-repeated | 2.959 | 3.659 | 23.67% |
| 27 | scripting / arrays-strings-hash/sliding-window/large / fresh-process-repeated | 271.359 | 328.926 | 21.21% |
| 28 | concurrency / pool-light-2 / persistent | 10.645 | 12.648 | 18.82% |
| 29 | template-engines / condition / fresh | 3.457 | 4.055 | 17.27% |
| 30 | template-engines / many-templates-10 / fresh | 3.517 | 4.124 | 17.24% |
| 31 | scripting / arrays-strings-hash/scan/large / fresh-process-repeated | 88.809 | 103.618 | 16.67% |
| 32 | concurrency / files-100 / persistent | 17.054 | 19.850 | 16.40% |
| 33 | concurrency / files-10000 / fresh | 1385.434 | 1608.951 | 16.13% |
| 34 | concurrency / pool-light-4 / persistent | 6.902 | 8.004 | 15.97% |
| 35 | scripting / arrays-strings-hash/sort-index/small / fresh-process-repeated | 8.230 | 9.541 | 15.93% |
| 36 | template-engines / literal / fresh | 3.392 | 3.917 | 15.46% |
| 37 | concurrency / fan-100 / fresh | 21.550 | 24.618 | 14.24% |
| 38 | template-engines / includes-4 / fresh | 3.501 | 3.972 | 13.44% |
| 39 | template-engines / includes-1 / fresh | 3.474 | 3.921 | 12.85% |
| 40 | template-engines / interpolation / fresh | 3.466 | 3.901 | 12.54% |
| 41 | template-engines / transform / fresh | 3.554 | 3.946 | 11.03% |
| 42 | template-engines / nested-object / fresh | 3.538 | 3.927 | 10.98% |
| 43 | template-engines / loop-10 / fresh | 3.689 | 4.087 | 10.79% |
| 44 | scripting / sanity/loops/large / fresh-process-repeated | 74.997 | 82.525 | 10.04% |
| 45 | concurrency / files-10000 / persistent | 1448.103 | 1589.358 | 9.75% |
| 46 | concurrency / pool-light-1 / fresh | 25.187 | 27.460 | 9.02% |
| 47 | template-engines / many-templates-100 / fresh | 6.439 | 6.953 | 7.99% |
| 48 | scripting / dynamic-programming/fibonacci/large / fresh-process-repeated | 152.071 | 164.168 | 7.95% |
| 49 | template-engines / nested-object / source-render | 0.021 | 0.023 | 7.72% |
| 50 | template-engines / many-templates-10 / source-render | 0.020 | 0.021 | 7.56% |
| 51 | concurrency / process-one-failure / fresh | 95.537 | 102.732 | 7.53% |
| 52 | concurrency / files-1000 / persistent | 150.382 | 161.134 | 7.15% |
| 53 | concurrency / process-one-failure / persistent | 82.619 | 88.492 | 7.11% |
| 54 | template-engines / includes-8 / fresh | 3.792 | 4.061 | 7.08% |
| 55 | template-engines / many-templates-1000 / source-render | 0.020 | 0.021 | 6.53% |
| 56 | template-engines / many-templates-1000 / fresh | 31.760 | 33.820 | 6.48% |
| 57 | template-engines / includes-4 / files | 0.156 | 0.166 | 6.40% |
| 58 | concurrency / pool-light-2 / fresh | 17.130 | 18.198 | 6.23% |
| 59 | template-engines / interpolation / source-render | 0.025 | 0.026 | 5.87% |
| 60 | concurrency / process-100 / fresh | 93.137 | 98.413 | 5.67% |
| 61 | template-engines / many-renders-100 / fresh | 5.540 | 5.850 | 5.59% |
| 62 | template-engines / includes-8 / files | 0.274 | 0.289 | 5.56% |
| 63 | template-engines / transform / source-render | 0.020 | 0.021 | 5.41% |
| 64 | template-engines / many-renders-1000 / fresh | 24.484 | 25.767 | 5.24% |
| 65 | template-engines / many-renders-1000 / source-render | 0.021 | 0.022 | 4.92% |
| 66 | concurrency / files-100 / fresh | 24.279 | 25.392 | 4.59% |
| 67 | template-engines / includes-4 / source-render | 0.085 | 0.089 | 4.58% |
| 68 | concurrency / files-1000 / fresh | 162.225 | 168.950 | 4.15% |
| 69 | template-engines / many-templates-100 / source-render | 0.020 | 0.021 | 4.12% |
| 70 | concurrency / pool-medium-1 / persistent | 31.897 | 33.129 | 3.86% |
| 71 | template-engines / condition / source-render | 0.021 | 0.021 | 3.83% |
| 72 | template-engines / literal / source-render | 0.014 | 0.015 | 3.80% |
| 73 | concurrency / pool-medium-1 / fresh | 36.690 | 37.919 | 3.35% |
| 74 | scripting / arrays-strings-hash/sort-index/large / fresh-process-repeated | 876.868 | 904.664 | 3.17% |
| 75 | template-engines / article / fresh | 4.201 | 4.318 | 2.77% |
| 76 | template-engines / many-renders-100 / source-render | 0.021 | 0.021 | 2.29% |
| 77 | concurrency / pool-medium-2 / persistent | 17.576 | 17.893 | 1.80% |
| 78 | template-engines / includes-1 / source-render | 0.040 | 0.041 | 1.14% |

These historical rankings are cross-node trends, not causal attribution. Targeted template/concurrency/website A/B is in progress. No capability/correctness regression has yet been reported in accepted audits; remaining suites are unfinished. See subsystem report for qualified source leads.

## Additional targeted same-node findings

Website10k freshfull:2561.445→3542.237ms, **+38.29%**, +980.792ms; all observed ranges disjoint in five paired measured samples. Warmfull/no-op/leaf improve10.82–12.80%. Separate profiles show330,820→404,209syscalls; investigatefilesystem/path probes, without assumingthe scriptingcall rootcause. Tinytemplate fresharticle increases3.28% across threepairs with noisyoverlapping values; not aconfirmed materialregression.

## Confirmed shell additions

Functioncalls+119.68%(22.086→48.519ms),stringtransform+15.32%(60.516→69.788ms);10/10pairedcandidateslower,disjointranges. Callsrankbetweenlargescriptingcalls(+145.76%)andsmallscriptingcalls(+65.63%). Traversalflatdescriptively; do notcountitsoldcross-nodegainasacausalfix.
