# Current competitive gaps

Audited suite exports only. Time, memory and throughput are ranked separately. Historical changes are cross-node trends, not controlled same-machine A/B. Percentages are descriptive. Capability gaps and product priorities require separate explicit assessments.

## Wall Time

| Rank | Benchmark / scenario / boundary | Deficit multiple | Evidence |
|---:|---|---:|---|
| 1 | concurrency / schedule-10000 / persistent | 1376.88 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 2 | concurrency / tiny-10000 / persistent | 1235.97 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 3 | concurrency / schedule-10000 / fresh | 1051.42 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 4 | concurrency / tiny-10000 / fresh | 809.45 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 5 | scripting / sanity/function-calls/large / fresh-process-repeated | 289.09 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 6 | concurrency / mutex-8-2 / persistent | 287.64 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 7 | concurrency / mutex-8-1 / persistent | 267.31 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 8 | concurrency / mutex-8-4 / persistent | 266.64 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 9 | concurrency / mutex-1-2 / persistent | 240.97 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 10 | concurrency / mutex-1-4 / persistent | 236.22 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 11 | concurrency / queue-100000-4-4 / persistent | 208.76 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 12 | concurrency / cpu-1 / persistent | 204.82 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 13 | concurrency / cpu-2 / persistent | 203.46 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 14 | concurrency / mutex-1-1 / persistent | 196.17 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 15 | concurrency / cpu-1 / fresh | 186.61 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 16 | concurrency / cpu-4 / persistent | 186.51 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 17 | concurrency / queue-100000-4-1 / persistent | 183.21 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 18 | concurrency / wait-1000 / persistent | 177.88 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 19 | concurrency / waiting-memory-1000 / persistent | 177.74 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 20 | concurrency / queue-100000-1-1 / persistent | 176.88 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 21 | concurrency / queue-100000-1-4 / persistent | 173.46 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 22 | concurrency / cpu-2 / fresh | 170.78 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 23 | concurrency / atomic-1 / persistent | 154.29 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 24 | scripting / arrays-strings-hash/frequency-count/large / fresh-process-repeated | 148.96 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 25 | concurrency / queue-100000-4-4 / fresh | 141.95 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 26 | concurrency / cpu-4 / fresh | 140.27 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 27 | concurrency / wait-1000 / fresh | 136.36 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 28 | concurrency / pool-heavy-1 / persistent | 133.27 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 29 | concurrency / waiting-memory-1000 / fresh | 130.72 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 30 | concurrency / queue-100000-4-1 / fresh | 129.24 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 31 | concurrency / queue-100000-1-1 / fresh | 127.00 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 32 | concurrency / queue-100000-1-4 / fresh | 126.74 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 33 | concurrency / queue-10000-4-4 / persistent | 102.22 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 34 | concurrency / queue-10000-4-1 / persistent | 98.60 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 35 | concurrency / queue-10000-1-4 / persistent | 98.52 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 36 | concurrency / tiny-1000 / persistent | 97.70 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 37 | concurrency / queue-10000-1-1 / persistent | 93.78 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 38 | concurrency / schedule-1000 / persistent | 93.62 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 39 | concurrency / fan-1000 / persistent | 88.20 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 40 | scripting / arrays-strings-hash/sliding-window/large / fresh-process-repeated | 87.11 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 41 | concurrency / pool-heavy-2 / persistent | 80.56 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 42 | concurrency / queue-10000-4-4 / fresh | 76.76 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 43 | scripting / arrays-strings-hash/map-set/large / fresh-process-repeated | 75.59 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 44 | concurrency / queue-10000-1-4 / fresh | 71.04 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 45 | concurrency / queue-10000-4-1 / fresh | 70.27 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 46 | concurrency / atomic-2 / persistent | 69.62 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 47 | concurrency / queue-10000-1-1 / fresh | 64.42 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 48 | scripting / dynamic-programming/fibonacci/large / fresh-process-repeated | 64.39 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 49 | concurrency / queue-1000-1-4 / persistent | 63.50 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 50 | concurrency / queue-1000-4-1 / persistent | 63.27 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 51 | concurrency / queue-1000-4-4 / persistent | 62.43 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 52 | concurrency / queue-1000-1-1 / persistent | 56.65 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 53 | scripting / arrays-strings-hash/scan/large / fresh-process-repeated | 54.97 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 54 | concurrency / pool-heavy-4 / persistent | 49.17 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 55 | scripting / graphs-trees-search/bfs/large / fresh-process-repeated | 45.84 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 56 | concurrency / pool-heavy-1 / fresh | 43.89 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 57 | concurrency / fan-1000 / fresh | 43.13 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 58 | concurrency / atomic-4 / persistent | 42.87 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 59 | scripting / sanity/loops/large / fresh-process-repeated | 42.44 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 60 | concurrency / mutex-8-2 / fresh | 38.87 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 61 | concurrency / tiny-1000 / fresh | 38.21 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 62 | concurrency / schedule-1000 / fresh | 35.84 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 63 | concurrency / mutex-8-1 / fresh | 35.60 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 64 | concurrency / mutex-1-4 / fresh | 34.69 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 65 | concurrency / mutex-8-4 / fresh | 34.68 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 66 | concurrency / pool-medium-1 / persistent | 34.58 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 67 | concurrency / nested-100 / persistent | 34.02 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 68 | concurrency / mutex-1-2 / fresh | 32.75 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 69 | scripting / arrays-strings-hash/sort-index/large / fresh-process-repeated | 29.53 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 70 | concurrency / mutex-1-1 / fresh | 27.46 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 71 | concurrency / pool-light-1 / persistent | 25.84 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 72 | concurrency / files-10000 / persistent | 25.23 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 73 | concurrency / files-10000 / fresh | 24.10 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 74 | concurrency / waiting-memory-100 / persistent | 22.30 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 75 | concurrency / wait-100 / persistent | 21.92 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 76 | concurrency / pool-heavy-2 / fresh | 20.77 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 77 | concurrency / files-1000 / persistent | 20.20 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 78 | concurrency / queue-1000-4-4 / fresh | 19.87 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 79 | concurrency / atomic-1 / fresh | 19.48 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 80 | concurrency / queue-1000-1-4 / fresh | 19.26 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 81 | concurrency / queue-1000-4-1 / fresh | 19.07 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 82 | concurrency / pool-medium-2 / persistent | 18.33 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 83 | concurrency / queue-1000-1-1 / fresh | 17.01 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 84 | concurrency / wait-100 / fresh | 16.94 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 85 | concurrency / waiting-memory-100 / fresh | 15.38 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 86 | template-engines / loop-10000 / source-render | 15.35 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 87 | concurrency / pool-light-2 / persistent | 13.82 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 88 | concurrency / pool-heavy-4 / fresh | 13.81 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 89 | concurrency / files-1000 / fresh | 13.27 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 90 | concurrency / schedule-100 / persistent | 12.76 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 91 | concurrency / files-100 / persistent | 12.72 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 92 | concurrency / fan-100 / persistent | 12.66 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 93 | concurrency / stagger-100 / persistent | 12.59 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 94 | concurrency / tiny-100 / persistent | 12.32 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 95 | concurrency / atomic-2 / fresh | 11.28 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 96 | concurrency / stagger-100 / fresh | 10.98 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 97 | concurrency / pool-medium-4 / persistent | 10.07 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 98 | concurrency / nested-100 / fresh | 8.62 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 99 | concurrency / atomic-4 / fresh | 8.48 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 100 | concurrency / nested-10 / persistent | 8.17 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 101 | concurrency / pool-light-4 / persistent | 7.76 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 102 | concurrency / pool-medium-1 / fresh | 7.50 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 103 | template-engines / collection / source-render | 7.45 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 104 | scripting / structured-data/json-transform/large / fresh-process-repeated | 7.00 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 105 | scripting / graphs-trees-search/bfs/small / fresh-process-repeated | 5.72 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 106 | scripting / sanity/function-calls/small / fresh-process-repeated | 5.68 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 107 | concurrency / pool-light-1 / fresh | 5.61 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 108 | scripting / arrays-strings-hash/frequency-count/small / fresh-process-repeated | 5.37 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 109 | scripting / structured-data/json-traverse/large / fresh-process-repeated | 5.02 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 110 | scripting / arrays-strings-hash/sort-index/small / fresh-process-repeated | 4.80 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 111 | template-engines / loop-1000 / source-render | 4.52 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 112 | concurrency / fan-100 / fresh | 4.21 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 113 | concurrency / files-100 / fresh | 4.21 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 114 | scripting / arrays-strings-hash/sliding-window/small / fresh-process-repeated | 4.16 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 115 | concurrency / mixed-wait-100 / persistent | 4.13 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 116 | concurrency / pool-medium-2 / fresh | 4.09 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 117 | template-engines / literal / source-render | 3.98 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 118 | scripting / filesystem/traverse/large / fresh-process-repeated | 3.94 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 119 | concurrency / schedule-100 / fresh | 3.90 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 120 | concurrency / tiny-100 / fresh | 3.75 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 121 | concurrency / mixed-wait-100 / fresh | 3.71 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 122 | concurrency / tiny-10 / persistent | 3.62 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 123 | concurrency / fan-10 / persistent | 3.60 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 124 | scripting / arrays-strings-hash/map-set/small / fresh-process-repeated | 3.56 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 125 | concurrency / failures / persistent | 3.45 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 126 | concurrency / schedule-10 / persistent | 3.39 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 127 | concurrency / pool-light-2 / fresh | 3.36 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 128 | scripting / structured-data/json-parse/large / fresh-process-repeated | 2.99 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 129 | concurrency / pool-medium-4 / fresh | 2.94 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 130 | scripting / arrays-strings-hash/scan/small / fresh-process-repeated | 2.93 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 131 | concurrency / process-1000 / fresh | 2.93 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 132 | scripting / sanity/loops/small / fresh-process-repeated | 2.91 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 133 | concurrency / process-1000 / persistent | 2.90 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 134 | concurrency / process-100 / persistent | 2.69 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 135 | concurrency / process-one-failure / persistent | 2.69 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 136 | scripting / sanity/noop/small / fresh-process-repeated | 2.69 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 137 | concurrency / process-100 / fresh | 2.64 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 138 | concurrency / process-many-failures / persistent | 2.57 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 139 | concurrency / pool-light-4 / fresh | 2.50 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 140 | concurrency / process-many-failures / fresh | 2.47 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 141 | concurrency / process-one-failure / fresh | 2.47 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 142 | concurrency / process-10 / persistent | 2.40 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 143 | template-engines / nested-loops / source-render | 2.26 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 144 | scripting / dynamic-programming/fibonacci/small / fresh-process-repeated | 2.22 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 145 | scripting / sanity/output/large / fresh-process-repeated | 2.16 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 146 | concurrency / nested-10 / fresh | 2.14 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 147 | scripting / sanity/output/small / fresh-process-repeated | 2.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 148 | template-engines / many-templates-1000 / source-render | 2.04 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 149 | scripting / sanity/noop/large / fresh-process-repeated | 2.03 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 150 | template-engines / many-templates-10 / source-render | 1.97 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 151 | template-engines / many-templates-100 / source-render | 1.96 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 152 | concurrency / schedule-10 / fresh | 1.91 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 153 | concurrency / fan-10 / fresh | 1.82 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 154 | concurrency / tiny-10 / fresh | 1.80 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 155 | concurrency / process-10 / fresh | 1.79 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 156 | concurrency / mixed-64 / persistent | 1.57 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 157 | concurrency / mixed-64 / fresh | 1.51 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 158 | concurrency / failures / fresh | 1.51 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 159 | template-engines / loop-100 / source-render | 1.42 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 160 | template-engines / many-renders-1000 / source-render | 1.41 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 161 | concurrency / process-mixed / persistent | 1.40 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 162 | concurrency / process-mixed / fresh | 1.40 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 163 | template-engines / many-renders-100 / source-render | 1.34 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 164 | template-engines / includes-8 / source-render | 1.33 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 165 | template-engines / article / source-render | 0.96 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 166 | template-engines / includes-4 / source-render | 0.88 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 167 | template-engines / loop-10000 / fresh | 0.78 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 168 | template-engines / interpolation / source-render | 0.77 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 169 | task-runners / mixed-1000-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.75 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 170 | task-runners / mixed-100-j2/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.74 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 171 | task-runners / mixed-100-j1/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.74 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 172 | scripting / filesystem/traverse/small / fresh-process-repeated | 0.70 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 173 | task-runners / mixed-1000-j4/shared / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.67 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 174 | task-runners / mixed-100-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.67 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 175 | template-engines / condition / source-render | 0.55 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 176 | template-engines / includes-1 / source-render | 0.55 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 177 | task-runners / mixed-100-j4/shared / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.55 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 178 | template-engines / nested-object / source-render | 0.55 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 179 | template-engines / transform / source-render | 0.54 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 180 | template-engines / loop-10 / source-render | 0.48 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 181 | template-engines / includes-8 / files | 0.47 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 182 | template-engines / includes-4 / files | 0.42 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 183 | task-runners / mixed-1000-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.41 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 184 | task-runners / mixed-20-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.41 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 185 | task-runners / mixed-20-j4/uncached-full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.41 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 186 | task-runners / mixed-20-j4/shared / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.37 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 187 | template-engines / includes-1 / files | 0.36 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 188 | task-runners / mixed-20-j4/target-subgraph / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.36 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 189 | scripting / structured-data/json-transform/small / fresh-process-repeated | 0.32 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 190 | template-engines / collection / fresh | 0.29 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 191 | task-runners / mixed-1000-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.26 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 192 | scripting / structured-data/json-traverse/small / fresh-process-repeated | 0.24 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 193 | task-runners / mixed-1000-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.22 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 194 | task-runners / tiny-1000-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.22 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 195 | task-runners / mixed-100-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.22 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 196 | template-engines / many-templates-1000 / fresh | 0.21 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 197 | task-runners / tiny-100-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.19 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 198 | template-engines / loop-1000 / fresh | 0.19 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 199 | task-runners / mixed-100-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.18 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 200 | scripting / structured-data/json-parse/small / fresh-process-repeated | 0.17 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 201 | template-engines / many-renders-1000 / fresh | 0.15 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 202 | task-runners / mixed-100-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.15 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 203 | task-runners / tiny-1000-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.14 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 204 | task-runners / mixed-20-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.14 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 205 | task-runners / tiny-1000-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.13 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 206 | task-runners / mixed-20-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.13 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 207 | task-runners / mixed-20-j4/target-leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.13 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 208 | task-runners / mixed-20-j4/multi-target / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.12 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 209 | task-runners / mixed-20-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.12 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 210 | template-engines / nested-loops / fresh | 0.11 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 211 | task-runners / tiny-1000-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.09 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 212 | template-engines / loop-100 / fresh | 0.09 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 213 | template-engines / many-templates-100 / fresh | 0.09 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 214 | template-engines / article / fresh | 0.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 215 | task-runners / tiny-100-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 216 | template-engines / literal / fresh | 0.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 217 | template-engines / transform / fresh | 0.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 218 | template-engines / condition / fresh | 0.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 219 | template-engines / loop-10 / fresh | 0.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 220 | template-engines / many-templates-10 / fresh | 0.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 221 | template-engines / nested-object / fresh | 0.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 222 | template-engines / includes-1 / fresh | 0.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 223 | template-engines / interpolation / fresh | 0.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 224 | template-engines / many-renders-100 / fresh | 0.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 225 | template-engines / includes-8 / fresh | 0.07 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 226 | template-engines / includes-4 / fresh | 0.07 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 227 | task-runners / tiny-1000-j4/one-percent / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.07 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 228 | task-runners / tiny-100-j4/one-percent / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.05 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 229 | task-runners / tiny-100-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.05 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 230 | task-runners / tiny-100-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 0.03 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |

## Memory

| Rank | Benchmark / scenario / boundary | Deficit multiple | Evidence |
|---:|---|---:|---|

## Throughput

| Rank | Benchmark / scenario / boundary | Deficit multiple | Evidence |
|---:|---|---:|---|
