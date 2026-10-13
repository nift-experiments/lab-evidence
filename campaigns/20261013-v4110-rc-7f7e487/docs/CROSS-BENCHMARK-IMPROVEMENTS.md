# Nift old-to-new improvements

Audited suite exports only. Time, memory and throughput are ranked separately. Historical changes are cross-node trends, not controlled same-machine A/B. Percentages are descriptive. Capability gaps and product priorities require separate explicit assessments.

## Wall Time

| Rank | Benchmark / scenario / boundary | Improvement % | Evidence |
|---:|---|---:|---|
| 1 | concurrency / queue-1000-1-4 / fresh | 78.50 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 2 | concurrency / queue-100000-4-1 / fresh | 78.38 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 3 | concurrency / queue-100000-1-4 / persistent | 78.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 4 | concurrency / queue-100000-1-4 / fresh | 77.94 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 5 | concurrency / queue-1000-1-1 / persistent | 77.84 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 6 | concurrency / queue-10000-1-4 / fresh | 77.79 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 7 | concurrency / queue-1000-1-4 / persistent | 77.45 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 8 | concurrency / queue-100000-4-1 / persistent | 77.01 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 9 | concurrency / queue-10000-1-4 / persistent | 76.97 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 10 | concurrency / queue-10000-4-1 / fresh | 76.73 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 11 | concurrency / queue-1000-4-1 / persistent | 76.70 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 12 | concurrency / queue-10000-4-1 / persistent | 76.57 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 13 | concurrency / queue-1000-1-1 / fresh | 76.44 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 14 | concurrency / queue-100000-1-1 / persistent | 74.68 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 15 | concurrency / queue-100000-1-1 / fresh | 74.63 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 16 | concurrency / queue-100000-4-4 / fresh | 74.37 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 17 | concurrency / queue-100000-4-4 / persistent | 74.25 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 18 | concurrency / mutex-1-4 / persistent | 74.06 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 19 | concurrency / mutex-1-4 / fresh | 73.49 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 20 | concurrency / queue-10000-1-1 / persistent | 73.31 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 21 | concurrency / queue-1000-4-1 / fresh | 73.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 22 | concurrency / queue-10000-1-1 / fresh | 72.98 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 23 | concurrency / atomic-4 / persistent | 72.90 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 24 | concurrency / queue-1000-4-4 / fresh | 72.86 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 25 | concurrency / queue-10000-4-4 / fresh | 72.83 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 26 | concurrency / atomic-2 / fresh | 72.62 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 27 | concurrency / queue-1000-4-4 / persistent | 72.46 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 28 | concurrency / queue-10000-4-4 / persistent | 72.14 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 29 | concurrency / atomic-2 / persistent | 72.06 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 30 | concurrency / mutex-1-1 / fresh | 71.84 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 31 | concurrency / atomic-1 / persistent | 71.71 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 32 | concurrency / mutex-1-1 / persistent | 71.28 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 33 | concurrency / mutex-8-4 / persistent | 70.66 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 34 | concurrency / mutex-8-4 / fresh | 70.58 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 35 | concurrency / atomic-1 / fresh | 70.49 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 36 | concurrency / mutex-1-2 / persistent | 70.13 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 37 | template-engines / loop-1000 / source-render | 70.11 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 38 | template-engines / loop-10000 / source-render | 69.71 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 39 | concurrency / mutex-8-1 / persistent | 69.55 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 40 | concurrency / mutex-8-1 / fresh | 69.13 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 41 | concurrency / mutex-1-2 / fresh | 68.46 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 42 | template-engines / loop-100 / source-render | 68.32 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 43 | template-engines / collection / source-render | 68.16 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 44 | concurrency / mutex-8-2 / persistent | 67.46 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 45 | concurrency / atomic-4 / fresh | 65.62 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 46 | concurrency / mutex-8-2 / fresh | 65.30 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 47 | template-engines / nested-loops / source-render | 57.47 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 48 | template-engines / loop-10 / source-render | 55.81 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 49 | template-engines / loop-10000 / fresh | 50.78 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 50 | template-engines / collection / fresh | 45.49 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 51 | concurrency / failures / fresh | 44.44 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 52 | template-engines / loop-1000 / fresh | 40.86 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 53 | concurrency / tiny-10000 / fresh | 36.60 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 54 | template-engines / article / source-render | 35.94 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 55 | task-runners / tiny-100-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 33.46 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 56 | task-runners / mixed-20-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 33.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 57 | task-runners / tiny-100-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 32.52 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 58 | task-runners / tiny-100-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 32.14 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 59 | task-runners / tiny-100-j4/one-percent / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 31.15 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 60 | concurrency / pool-heavy-4 / persistent | 29.97 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 61 | concurrency / cpu-1 / persistent | 29.94 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 62 | concurrency / tiny-100 / fresh | 29.47 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 63 | concurrency / schedule-10000 / fresh | 28.44 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 64 | concurrency / pool-heavy-4 / fresh | 27.78 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 65 | task-runners / tiny-100-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 27.29 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 66 | task-runners / tiny-1000-j4/one-percent / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 27.05 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 67 | concurrency / cpu-4 / persistent | 27.00 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 68 | concurrency / cpu-4 / fresh | 26.54 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 69 | concurrency / schedule-10000 / persistent | 26.17 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 70 | concurrency / cpu-1 / fresh | 26.13 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 71 | task-runners / mixed-100-j4/shared / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 26.01 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 72 | concurrency / schedule-10 / fresh | 25.87 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 73 | concurrency / cpu-2 / fresh | 25.75 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 74 | concurrency / tiny-10000 / persistent | 24.63 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 75 | concurrency / cpu-2 / persistent | 24.43 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 76 | task-runners / mixed-100-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 24.11 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 77 | task-runners / tiny-1000-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 23.90 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 78 | task-runners / mixed-100-j1/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 23.83 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 79 | task-runners / mixed-100-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 23.69 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 80 | task-runners / mixed-20-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 23.26 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 81 | concurrency / failures / persistent | 23.24 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 82 | task-runners / tiny-1000-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 22.73 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 83 | task-runners / mixed-100-j2/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 22.32 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 84 | concurrency / nested-100 / fresh | 22.09 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 85 | task-runners / mixed-20-j4/multi-target / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 21.58 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 86 | task-runners / mixed-20-j4/shared / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 21.41 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 87 | concurrency / pool-heavy-2 / persistent | 20.79 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 88 | concurrency / pool-heavy-1 / fresh | 20.34 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 89 | task-runners / mixed-20-j4/uncached-full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 20.05 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 90 | concurrency / tiny-10 / fresh | 19.81 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 91 | task-runners / mixed-1000-j4/shared / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 19.75 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 92 | concurrency / pool-heavy-1 / persistent | 19.71 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 93 | task-runners / mixed-100-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 19.69 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 94 | task-runners / mixed-1000-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 19.63 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 95 | concurrency / schedule-100 / persistent | 19.47 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 96 | task-runners / mixed-20-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 19.28 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 97 | task-runners / mixed-20-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 19.01 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 98 | task-runners / mixed-100-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 18.45 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 99 | task-runners / mixed-20-j4/target-leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 18.14 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 100 | concurrency / nested-10 / fresh | 17.99 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 101 | template-engines / nested-loops / fresh | 17.74 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 102 | task-runners / tiny-1000-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 17.73 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 103 | concurrency / pool-heavy-2 / fresh | 17.64 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 104 | task-runners / mixed-1000-j4/fanout / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 17.51 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 105 | concurrency / tiny-10 / persistent | 17.26 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 106 | task-runners / mixed-1000-j4/leaf / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 17.14 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 107 | concurrency / schedule-100 / fresh | 16.58 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 108 | task-runners / mixed-20-j4/target-subgraph / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 16.52 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 109 | task-runners / tiny-1000-j4/full / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 16.31 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 110 | concurrency / schedule-10 / persistent | 13.95 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 111 | task-runners / mixed-1000-j4/noop / fresh CLI; C CLOCK_MONOTONIC fork/exec through wait4 | 13.83 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/task-runners/20261013-v4110-rc-7f7e487/results/summary.json) |
| 112 | concurrency / fan-1000 / persistent | 13.68 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 113 | concurrency / schedule-1000 / fresh | 13.15 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 114 | concurrency / fan-10 / fresh | 13.00 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 115 | concurrency / schedule-1000 / persistent | 12.52 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 116 | concurrency / nested-10 / persistent | 12.23 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 117 | concurrency / fan-10 / persistent | 11.85 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 118 | concurrency / mixed-64 / fresh | 9.90 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 119 | concurrency / nested-100 / persistent | 9.24 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 120 | concurrency / tiny-100 / persistent | 8.33 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 121 | concurrency / mixed-64 / persistent | 7.98 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 122 | concurrency / process-10 / persistent | 7.82 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 123 | concurrency / process-1000 / persistent | 7.42 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 124 | concurrency / fan-100 / persistent | 7.11 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 125 | concurrency / process-10 / fresh | 6.85 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 126 | concurrency / pool-medium-2 / fresh | 6.83 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 127 | concurrency / process-many-failures / persistent | 6.83 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 128 | concurrency / tiny-1000 / fresh | 6.75 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 129 | template-engines / loop-100 / fresh | 6.26 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 130 | concurrency / process-mixed / fresh | 6.06 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 131 | concurrency / tiny-1000 / persistent | 5.95 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 132 | concurrency / waiting-memory-1000 / fresh | 5.59 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 133 | concurrency / process-mixed / persistent | 5.04 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 134 | concurrency / waiting-memory-1000 / persistent | 5.00 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 135 | concurrency / pool-medium-4 / fresh | 4.00 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 136 | concurrency / mixed-wait-100 / fresh | 3.95 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 137 | concurrency / wait-1000 / fresh | 3.71 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 138 | concurrency / waiting-memory-100 / fresh | 3.55 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 139 | concurrency / process-100 / persistent | 3.44 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 140 | concurrency / pool-light-4 / fresh | 3.24 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 141 | concurrency / pool-medium-4 / persistent | 3.23 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 142 | concurrency / wait-1000 / persistent | 3.13 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 143 | concurrency / mixed-wait-100 / persistent | 2.91 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 144 | concurrency / wait-100 / fresh | 2.56 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 145 | concurrency / process-1000 / fresh | 2.53 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 146 | concurrency / wait-100 / persistent | 2.16 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 147 | concurrency / stagger-100 / fresh | 2.10 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 148 | concurrency / waiting-memory-100 / persistent | 2.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 149 | concurrency / process-many-failures / fresh | 2.02 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 150 | concurrency / stagger-100 / persistent | 1.32 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 151 | template-engines / includes-1 / files | 0.86 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 152 | template-engines / includes-8 / source-render | 0.26 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |

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
| 11 | concurrency / pool-light-1 / persistent | 36.72 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 12 | scripting / sanity/loops/small / fresh-process-repeated | 36.29 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 13 | scripting / arrays-strings-hash/sliding-window/small / fresh-process-repeated | 35.06 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 14 | scripting / dynamic-programming/fibonacci/small / fresh-process-repeated | 34.48 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 15 | scripting / arrays-strings-hash/map-set/small / fresh-process-repeated | 34.16 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 16 | scripting / structured-data/json-parse/small / fresh-process-repeated | 33.71 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 17 | scripting / arrays-strings-hash/map-set/large / fresh-process-repeated | 32.43 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 18 | scripting / structured-data/json-traverse/large / fresh-process-repeated | 32.40 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 19 | scripting / filesystem/traverse/large / fresh-process-repeated | 30.47 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 20 | scripting / sanity/noop/large / fresh-process-repeated | 29.68 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 21 | scripting / filesystem/traverse/small / fresh-process-repeated | 29.00 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 22 | scripting / arrays-strings-hash/scan/small / fresh-process-repeated | 28.72 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 23 | scripting / structured-data/json-traverse/small / fresh-process-repeated | 28.31 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 24 | concurrency / fan-1000 / fresh | 25.13 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 25 | scripting / sanity/noop/small / fresh-process-repeated | 24.03 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 26 | scripting / sanity/output/small / fresh-process-repeated | 23.67 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 27 | scripting / arrays-strings-hash/sliding-window/large / fresh-process-repeated | 21.21 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 28 | concurrency / pool-light-2 / persistent | 18.82 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 29 | template-engines / condition / fresh | 17.27 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 30 | template-engines / many-templates-10 / fresh | 17.24 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 31 | scripting / arrays-strings-hash/scan/large / fresh-process-repeated | 16.67 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 32 | concurrency / files-100 / persistent | 16.40 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 33 | concurrency / files-10000 / fresh | 16.13 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 34 | concurrency / pool-light-4 / persistent | 15.97 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 35 | scripting / arrays-strings-hash/sort-index/small / fresh-process-repeated | 15.93 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 36 | template-engines / literal / fresh | 15.46 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 37 | concurrency / fan-100 / fresh | 14.24 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 38 | template-engines / includes-4 / fresh | 13.44 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 39 | template-engines / includes-1 / fresh | 12.85 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 40 | template-engines / interpolation / fresh | 12.54 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 41 | template-engines / transform / fresh | 11.03 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 42 | template-engines / nested-object / fresh | 10.98 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 43 | template-engines / loop-10 / fresh | 10.79 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 44 | scripting / sanity/loops/large / fresh-process-repeated | 10.04 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 45 | concurrency / files-10000 / persistent | 9.75 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 46 | concurrency / pool-light-1 / fresh | 9.02 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 47 | template-engines / many-templates-100 / fresh | 7.99 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 48 | scripting / dynamic-programming/fibonacci/large / fresh-process-repeated | 7.95 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 49 | template-engines / nested-object / source-render | 7.72 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 50 | template-engines / many-templates-10 / source-render | 7.56 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 51 | concurrency / process-one-failure / fresh | 7.53 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 52 | concurrency / files-1000 / persistent | 7.15 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 53 | concurrency / process-one-failure / persistent | 7.11 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 54 | template-engines / includes-8 / fresh | 7.08 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 55 | template-engines / many-templates-1000 / source-render | 6.53 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 56 | template-engines / many-templates-1000 / fresh | 6.48 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 57 | template-engines / includes-4 / files | 6.40 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 58 | concurrency / pool-light-2 / fresh | 6.23 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 59 | template-engines / interpolation / source-render | 5.87 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 60 | concurrency / process-100 / fresh | 5.67 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 61 | template-engines / many-renders-100 / fresh | 5.59 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 62 | template-engines / includes-8 / files | 5.56 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 63 | template-engines / transform / source-render | 5.41 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 64 | template-engines / many-renders-1000 / fresh | 5.24 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 65 | template-engines / many-renders-1000 / source-render | 4.92 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 66 | concurrency / files-100 / fresh | 4.59 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 67 | template-engines / includes-4 / source-render | 4.58 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 68 | concurrency / files-1000 / fresh | 4.15 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 69 | template-engines / many-templates-100 / source-render | 4.12 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 70 | concurrency / pool-medium-1 / persistent | 3.86 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 71 | template-engines / condition / source-render | 3.83 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 72 | template-engines / literal / source-render | 3.80 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 73 | concurrency / pool-medium-1 / fresh | 3.35 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 74 | scripting / arrays-strings-hash/sort-index/large / fresh-process-repeated | 3.17 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/campaigns/20261013-v4110-rc-7f7e487/accepted-working/scripting) |
| 75 | template-engines / article / fresh | 2.77 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 76 | template-engines / many-renders-100 / source-render | 2.29 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |
| 77 | concurrency / pool-medium-2 / persistent | 1.80 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/concurrency/20261013-v4110-rc-7f7e487) |
| 78 | template-engines / includes-1 / source-render | 1.14 | [source](https://github.com/nift-experiments/lab-evidence/tree/main/benchmarks/template-engines/20261013-v4110-rc-7f7e487) |

## Memory

| Rank | Benchmark / scenario / boundary | Degradation % | Evidence |
|---:|---|---:|---|

## Throughput

| Rank | Benchmark / scenario / boundary | Degradation % | Evidence |
|---:|---|---:|---|

## Separate same-node scripting diagnostic wins

| Scenario | Old ms | Candidate ms | Improvement |
|---|---:|---:|---:|
| arrays-strings-hash/sort-index/large | 1088.855 | 754.437 | 30.71% |
| arrays-strings-hash/scan/large | 110.635 | 93.988 | 15.05% |
| structured-data/json-parse/small | 6.812 | 5.979 | 12.23% |
| dynamic-programming/fibonacci/large | 182.107 | 164.111 | 9.88% |
| arrays-strings-hash/sliding-window/large | 339.164 | 307.064 | 9.46% |
| arrays-strings-hash/sort-index/small | 10.823 | 9.843 | 9.06% |
| arrays-strings-hash/scan/small | 4.901 | 4.541 | 7.34% |
| arrays-strings-hash/map-set/large | 295.962 | 278.617 | 5.86% |
| arrays-strings-hash/map-set/small | 7.007 | 6.615 | 5.60% |
| sanity/loops/large | 92.539 | 88.115 | 4.78% |
| sanity/output/small | 3.720 | 3.562 | 4.25% |
| sanity/loops/small | 4.945 | 4.780 | 3.35% |
| arrays-strings-hash/sliding-window/small | 7.381 | 7.157 | 3.02% |
| structured-data/json-traverse/small | 8.969 | 8.772 | 2.19% |
| sanity/noop/large | 3.426 | 3.359 | 1.96% |
| sanity/output/large | 3.778 | 3.707 | 1.88% |
| structured-data/json-traverse/large | 491.211 | 489.025 | 0.45% |

## Additional targeted same-node diagnostic wins

These small paired controls are separate from official peer distributions. Scheduler change is noisy, not an established improvement.

| Benchmark / scenario / boundary | Old ms | Candidate ms | Improvement | Pairs |
|---|---:|---:|---:|---:|
| template-engines / loop-10000 / source-render | 119.508 | 33.683 | 71.82% | 3 |
| concurrency / queue-100000-4-4 / fresh runtime/readiness request | 36066.073 | 11887.314 | 67.04% | 3 |
| template-engines / loop-10000 / fresh | 168.238 | 75.854 | 54.91% | 3 |
| template-engines / article / source-render | 0.430 | 0.266 | 38.05% | 3 |
| website-generator / incremental/no-op / 10000pages targeted adjacent paired versions | 932.931 | 813.536 | 12.80% | 5 |
| website-generator / warm-full / 10000pages targeted adjacent paired versions | 3176.786 | 2776.981 | 12.59% | 5 |
| website-generator / incremental/one-page / 10000pages targeted adjacent paired versions | 920.908 | 821.310 | 10.82% | 5 |
| concurrency / schedule-1000 / fresh runtime/readiness request | 367.189 | 360.724 | 1.76% | 3 |
