# Nift old-to-new improvements

Audited suite exports only. Time, memory and throughput are ranked separately. Historical changes are cross-node trends, not controlled same-machine A/B. Percentages are descriptive. Capability gaps and product priorities require separate explicit assessments.

## Wall Time

| Rank | Benchmark / scenario / boundary | Improvement % | Evidence |
|---:|---|---:|---|

## Memory

| Rank | Benchmark / scenario / boundary | Improvement % | Evidence |
|---:|---|---:|---|

## Throughput

| Rank | Benchmark / scenario / boundary | Improvement % | Evidence |
|---:|---|---:|---|

# Regressions

Audited suite exports only. Time, memory and throughput are ranked separately. Historical changes are cross-node trends, not controlled same-machine A/B. Percentages are descriptive. Capability gaps and product priorities require separate explicit assessments.

## Wall Time

| Rank | Benchmark / scenario / boundary | Degradation % | Evidence |
|---:|---|---:|---|
| 1 | scripting / sanity/function-calls/large / fresh-process-repeated | 195.00 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 2 | scripting / sanity/function-calls/small / fresh-process-repeated | 101.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 3 | scripting / structured-data/json-parse/large / fresh-process-repeated | 53.53 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 4 | scripting / graphs-trees-search/bfs/large / fresh-process-repeated | 53.15 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 5 | scripting / arrays-strings-hash/frequency-count/large / fresh-process-repeated | 52.87 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 6 | scripting / structured-data/json-transform/large / fresh-process-repeated | 44.24 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 7 | scripting / sanity/output/large / fresh-process-repeated | 40.77 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 8 | scripting / graphs-trees-search/bfs/small / fresh-process-repeated | 39.70 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 9 | scripting / arrays-strings-hash/frequency-count/small / fresh-process-repeated | 37.98 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 10 | scripting / structured-data/json-transform/small / fresh-process-repeated | 36.91 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 11 | scripting / sanity/loops/small / fresh-process-repeated | 36.29 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 12 | scripting / arrays-strings-hash/sliding-window/small / fresh-process-repeated | 35.06 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 13 | scripting / dynamic-programming/fibonacci/small / fresh-process-repeated | 34.48 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 14 | scripting / arrays-strings-hash/map-set/small / fresh-process-repeated | 34.16 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 15 | scripting / structured-data/json-parse/small / fresh-process-repeated | 33.71 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 16 | scripting / arrays-strings-hash/map-set/large / fresh-process-repeated | 32.43 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 17 | scripting / structured-data/json-traverse/large / fresh-process-repeated | 32.40 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 18 | scripting / filesystem/traverse/large / fresh-process-repeated | 30.47 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 19 | scripting / sanity/noop/large / fresh-process-repeated | 29.68 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 20 | scripting / filesystem/traverse/small / fresh-process-repeated | 29.00 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 21 | scripting / arrays-strings-hash/scan/small / fresh-process-repeated | 28.72 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 22 | scripting / structured-data/json-traverse/small / fresh-process-repeated | 28.31 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 23 | scripting / sanity/noop/small / fresh-process-repeated | 24.03 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 24 | scripting / sanity/output/small / fresh-process-repeated | 23.67 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 25 | scripting / arrays-strings-hash/sliding-window/large / fresh-process-repeated | 21.21 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 26 | scripting / arrays-strings-hash/scan/large / fresh-process-repeated | 16.67 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 27 | scripting / arrays-strings-hash/sort-index/small / fresh-process-repeated | 15.93 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 28 | scripting / sanity/loops/large / fresh-process-repeated | 10.04 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 29 | scripting / dynamic-programming/fibonacci/large / fresh-process-repeated | 7.95 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 30 | scripting / arrays-strings-hash/sort-index/large / fresh-process-repeated | 3.17 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |

## Memory

| Rank | Benchmark / scenario / boundary | Degradation % | Evidence |
|---:|---|---:|---|

## Throughput

| Rank | Benchmark / scenario / boundary | Degradation % | Evidence |
|---:|---|---:|---|
