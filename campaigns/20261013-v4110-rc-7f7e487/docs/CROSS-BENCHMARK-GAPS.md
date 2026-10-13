# Current competitive gaps

Audited suite exports only. Time, memory and throughput are ranked separately. Historical changes are cross-node trends, not controlled same-machine A/B. Percentages are descriptive. Capability gaps and product priorities require separate explicit assessments.

## Wall Time

| Rank | Benchmark / scenario / boundary | Deficit multiple | Evidence |
|---:|---|---:|---|
| 1 | scripting / sanity/function-calls/large / fresh-process-repeated | 289.09 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 2 | scripting / arrays-strings-hash/frequency-count/large / fresh-process-repeated | 148.96 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 3 | scripting / arrays-strings-hash/sliding-window/large / fresh-process-repeated | 87.11 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 4 | scripting / arrays-strings-hash/map-set/large / fresh-process-repeated | 75.59 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 5 | scripting / dynamic-programming/fibonacci/large / fresh-process-repeated | 64.39 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 6 | scripting / arrays-strings-hash/scan/large / fresh-process-repeated | 54.97 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 7 | scripting / graphs-trees-search/bfs/large / fresh-process-repeated | 45.84 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 8 | scripting / sanity/loops/large / fresh-process-repeated | 42.44 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 9 | scripting / arrays-strings-hash/sort-index/large / fresh-process-repeated | 29.53 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 10 | scripting / structured-data/json-transform/large / fresh-process-repeated | 7.00 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 11 | scripting / graphs-trees-search/bfs/small / fresh-process-repeated | 5.72 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 12 | scripting / sanity/function-calls/small / fresh-process-repeated | 5.68 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 13 | scripting / arrays-strings-hash/frequency-count/small / fresh-process-repeated | 5.37 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 14 | scripting / structured-data/json-traverse/large / fresh-process-repeated | 5.02 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 15 | scripting / arrays-strings-hash/sort-index/small / fresh-process-repeated | 4.80 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 16 | scripting / arrays-strings-hash/sliding-window/small / fresh-process-repeated | 4.16 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 17 | scripting / filesystem/traverse/large / fresh-process-repeated | 3.94 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 18 | scripting / arrays-strings-hash/map-set/small / fresh-process-repeated | 3.56 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 19 | scripting / structured-data/json-parse/large / fresh-process-repeated | 2.99 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 20 | scripting / arrays-strings-hash/scan/small / fresh-process-repeated | 2.93 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 21 | scripting / sanity/loops/small / fresh-process-repeated | 2.91 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 22 | scripting / sanity/noop/small / fresh-process-repeated | 2.69 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 23 | scripting / dynamic-programming/fibonacci/small / fresh-process-repeated | 2.22 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 24 | scripting / sanity/output/large / fresh-process-repeated | 2.16 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 25 | scripting / sanity/output/small / fresh-process-repeated | 2.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 26 | scripting / sanity/noop/large / fresh-process-repeated | 2.03 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 27 | scripting / filesystem/traverse/small / fresh-process-repeated | 0.70 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 28 | scripting / structured-data/json-transform/small / fresh-process-repeated | 0.32 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 29 | scripting / structured-data/json-traverse/small / fresh-process-repeated | 0.24 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 30 | scripting / structured-data/json-parse/small / fresh-process-repeated | 0.17 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |

## Memory

| Rank | Benchmark / scenario / boundary | Deficit multiple | Evidence |
|---:|---|---:|---|

## Throughput

| Rank | Benchmark / scenario / boundary | Deficit multiple | Evidence |
|---:|---|---:|---|
