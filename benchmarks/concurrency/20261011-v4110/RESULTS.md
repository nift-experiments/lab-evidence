# Concurrency results — accepted 2026-10-11 series

64 scenarios; 608 supported cells; 32 unavailable cells; 10,290 measured observations and 1,216 retained warmups. All 11,506 exact result digests/counts and coverage/rotation checks passed independent audit. No outlier removal.

Measured suite: bb62138daf8bb7cda20a2194ab97fe8395a9e337. Nift source: 445f4d3545cf031bcce4bf77a2b4a61ffb3b4c4f.

Fresh invocation includes launch, work, response and exit. Persistent-labelled rows are **equally isolated already-booted requests**, not reused-runtime steady-state throughput. Every engine boots afresh outside that timer; CPU worker pools are still created inside the request. The incomplete earlier reused-runtime cohort is retained as separate rejected/diagnostic evidence, with its Nift growth visible.

## Representative booted request medians (ms)

| Workload | Nift | Python | Node | Bun | Go |
|---|---:|---:|---:|---:|---:|
| schedule-10 | 3.502 | 1.572 | 2.378 | 11.393 | 1.140 |
| schedule-1000 | 267.316 | 9.505 | 7.551 | 13.833 | 3.337 |
| schedule-10000 | 27,511.876 | 74.696 | 33.765 | 26.452 | 17.288 |
| wait-1000 | 2,659.625 | 23.060 | 22.043 | 24.281 | 15.658 |
| cpu-1 | 15,425.973 | 2,386.950 | 341.808 | 445.102 | 54.510 |
| cpu-2 | 7,254.004 | 1,210.472 | 206.010 | 245.587 | 29.275 |
| cpu-4 | 3,905.406 | 763.011 | 144.374 | 162.964 | 15.741 |
| queue-100000-4-4 | 45,620.753 | 387.031 | 97.069 | 75.152 | 123.325 |
| process-100 | 91.162 | 63.008 | 194.861 | 85.156 | 37.845 |
| process-1000 | 902.037 | 453.014 | 1,886.327 | 506.293 | 338.342 |
| files-10000 | 1,448.103 | 985.181 | 680.399 | 130.909 | 69.775 |
| atomic-4 | 160.248 | — | 82.441 | 55.511 | 1.401 |
| mutex-1-4 | 851.626 | 5.512 | — | — | 1.148 |
| mixed-64 | 93.551 | 69.312 | 168.651 | 80.852 | 61.034 |

## Fixed-work CPU scaling

Ratios of medians for 64 jobs × 200,000 iterations. Python ordinary-GIL spawn processes; JS worker isolates; Nift threads; Go goroutines. Pool setup/teardown included; five samples, no significance claim.

| Runtime | 1-worker ms | 2-worker ms | 4-worker ms | 4-worker speedup | 4-worker efficiency |
|---|---:|---:|---:|---:|---:|
| Nift | 15,425.973 | 7,254.004 | 3,905.406 | 3.950× | 98.7% |
| Python | 2,386.950 | 1,210.472 | 763.011 | 3.128× | 78.2% |
| Node | 341.808 | 206.010 | 144.374 | 2.368× | 59.2% |
| Bun | 445.102 | 245.587 | 162.964 | 2.731× | 68.3% |
| Go | 54.510 | 29.275 | 15.741 | 3.463× | 86.6% |

## Held-task tree RSS (MiB)

Same unfinished-work gate, sampled after staging. Queued futures need not all be running. Shared mappings may be counted more than once; not unique physical memory. Nift 10000 local ~13,700MiB is outside official 8GiB range, not a chart point.

| Held tasks | Nift | Python | Node | Bun | Go |
|---|---:|---:|---:|---:|---:|
| 100 | 10.125 | 20.828 | 48.750 | 23.000 | 3.000 |
| 1000 | 143.500 | 21.949 | 50.125 | 26.000 | 5.375 |
| 10000 | — | 31.574 | 55.000 | 29.375 | 29.375 |

## Interpretation and limitations

Nift native concurrency is real and useful for bounded existing-project work, but large task capture, blocking sleeps, polling queue coordination and retained-runtime registry growth prevent a broad high-concurrency-strength conclusion. Go is the standalone concurrency reference; JS/Python remain natural when their async APIs/libraries are required. See the separate practitioner review for equal-performance preferences and agent-visible contracts.

Python atomics (6 cells), Node/Bun native mutexes (24 cells) and Nift 10k held-memory (2 cells) are unavailable, not zero or failed timings. All timed failure cases are all-settled; separate cancellation probes retain different semantics. Shared 4-vCPU host noise, warmed Linux file cache, 5ms tree sampling and per-request pool setup limit extrapolation.

## All accepted median cells

Full raw distributions, CPU/RSS/process/thread counts, output hashes and warmups are canonical in lab-evidence. The following is a compact readable summary, not replacement raw evidence.

### fresh / median ms

| Workload | Nift | Python | Node | Bun | Go |
|---|---:|---:|---:|---:|---:|
| schedule-10 | 11.213 | 98.013 | 54.104 | 35.332 | 6.471 |
| schedule-100 | 22.406 | 91.547 | 52.277 | 35.271 | 6.270 |
| schedule-1000 | 264.495 | 105.543 | 60.437 | 37.528 | 8.248 |
| schedule-10000 | 27,241.043 | 174.006 | 102.005 | 55.100 | 24.566 |
| tiny-10 | 10.738 | 94.817 | 53.682 | 35.104 | 6.548 |
| tiny-100 | 26.408 | 108.390 | 58.606 | 40.312 | 7.620 |
| tiny-1000 | 274.828 | 107.156 | 60.283 | 38.703 | 9.353 |
| tiny-10000 | 27,282.324 | 203.800 | 101.548 | 60.460 | 26.303 |
| fan-10 | 10.220 | 92.118 | 52.304 | 34.618 | 6.429 |
| fan-100 | 21.550 | 93.492 | 52.485 | 36.045 | 6.764 |
| fan-1000 | 271.582 | 110.047 | 60.450 | 39.579 | 9.031 |
| wait-100 | 271.795 | 114.660 | 65.680 | 48.358 | 16.992 |
| wait-1000 | 2,694.718 | 121.473 | 76.590 | 50.087 | 21.691 |
| stagger-100 | 291.779 | 124.001 | 76.767 | 57.761 | 28.203 |
| mixed-wait-100 | 99.553 | 122.036 | 72.847 | 55.875 | 28.276 |
| pool-light-1 | 25.187 | 263.704 | 120.367 | 75.053 | 6.877 |
| pool-light-2 | 17.130 | 248.247 | 117.992 | 71.330 | 6.627 |
| pool-light-4 | 14.541 | 289.609 | 144.415 | 82.577 | 7.439 |
| pool-medium-1 | 36.690 | 246.110 | 114.623 | 68.821 | 6.166 |
| pool-medium-2 | 25.428 | 248.593 | 120.420 | 73.154 | 7.397 |
| pool-medium-4 | 17.988 | 286.503 | 135.365 | 83.285 | 7.341 |
| pool-heavy-1 | 374.196 | 294.417 | 123.449 | 84.881 | 8.598 |
| pool-heavy-2 | 194.045 | 271.223 | 124.560 | 76.217 | 8.124 |
| pool-heavy-4 | 117.665 | 286.872 | 138.906 | 88.133 | 8.586 |
| cpu-1 | 14,608.057 | 2,547.447 | 406.473 | 462.426 | 62.056 |
| cpu-2 | 7,287.127 | 1,416.899 | 273.554 | 287.456 | 36.762 |
| cpu-4 | 3,915.860 | 922.533 | 227.529 | 190.777 | 22.758 |
| process-10 | 20.599 | 117.303 | 91.603 | 56.678 | 12.503 |
| process-100 | 93.137 | 161.075 | 255.046 | 110.725 | 42.691 |
| process-1000 | 909.268 | 564.610 | 1,928.274 | 532.466 | 331.405 |
| process-mixed | 120.736 | 193.792 | 248.414 | 136.659 | 86.749 |
| process-one-failure | 95.537 | 181.945 | 299.683 | 131.420 | 46.597 |
| process-many-failures | 96.989 | 161.005 | 258.728 | 110.189 | 42.091 |
| files-100 | 24.279 | 115.682 | 68.523 | 41.137 | 7.396 |
| files-1000 | 162.225 | 217.303 | 145.197 | 62.033 | 14.905 |
| files-10000 | 1,385.434 | 1,056.793 | 767.869 | 170.462 | 80.794 |
| queue-1000-1-1 | 475.301 | 131.573 | 70.833 | 52.663 | 12.549 |
| queue-1000-1-4 | 591.527 | 113.734 | 64.696 | 44.001 | 9.636 |
| queue-1000-4-1 | 489.307 | 105.812 | 61.680 | 40.728 | 8.737 |
| queue-1000-4-4 | 474.916 | 120.645 | 63.945 | 40.999 | 8.730 |
| queue-10000-1-1 | 3,961.919 | 138.206 | 80.592 | 48.902 | 19.847 |
| queue-10000-1-4 | 5,095.886 | 144.673 | 77.710 | 54.316 | 20.970 |
| queue-10000-4-1 | 4,951.985 | 140.226 | 79.845 | 49.233 | 19.705 |
| queue-10000-4-4 | 4,593.155 | 147.192 | 77.615 | 47.215 | 19.887 |
| queue-100000-1-1 | 42,139.649 | 433.035 | 194.510 | 112.068 | 145.470 |
| queue-100000-1-4 | 52,534.894 | 535.465 | 203.560 | 118.705 | 145.929 |
| queue-100000-4-1 | 53,848.599 | 514.745 | 203.049 | 121.749 | 141.861 |
| queue-100000-4-4 | 47,276.732 | 492.179 | 192.697 | 122.841 | 147.903 |
| atomic-1 | 473.330 | — | 120.532 | 72.346 | 9.436 |
| mutex-1-1 | 671.583 | 102.693 | — | — | 9.551 |
| mutex-8-1 | 753.812 | 115.924 | — | — | 9.525 |
| atomic-2 | 272.812 | — | 130.368 | 76.655 | 9.939 |
| mutex-1-2 | 692.266 | 105.562 | — | — | 9.808 |
| mutex-8-2 | 766.447 | 104.607 | — | — | 10.078 |
| atomic-4 | 174.935 | — | 141.469 | 87.834 | 10.861 |
| mutex-1-4 | 897.207 | 115.117 | — | — | 9.708 |
| mutex-8-4 | 928.116 | 112.349 | — | — | 9.673 |
| failures | 17.916 | 110.221 | 66.519 | 46.272 | 11.402 |
| mixed-64 | 100.812 | 179.256 | 228.071 | 116.435 | 69.843 |
| nested-10 | 18.153 | 100.266 | 58.315 | 39.942 | 9.750 |
| nested-100 | 81.891 | 107.596 | 59.794 | 41.629 | 11.875 |
| waiting-memory-100 | 280.327 | 108.523 | 71.214 | 49.077 | 21.553 |
| waiting-memory-1000 | 2,963.834 | 126.353 | 74.169 | 54.587 | 26.465 |
| waiting-memory-10000 | — | 242.076 | 119.889 | 63.868 | 69.911 |
### persistent / median ms

| Workload | Nift | Python | Node | Bun | Go |
|---|---:|---:|---:|---:|---:|
| schedule-10 | 3.502 | 1.572 | 2.378 | 11.393 | 1.140 |
| schedule-100 | 16.911 | 2.224 | 2.668 | 12.766 | 1.445 |
| schedule-1000 | 267.316 | 9.505 | 7.551 | 13.833 | 3.337 |
| schedule-10000 | 27,511.876 | 74.696 | 33.765 | 26.452 | 17.288 |
| tiny-10 | 3.633 | 1.571 | 2.563 | 11.796 | 1.179 |
| tiny-100 | 16.242 | 2.341 | 2.895 | 12.943 | 1.557 |
| tiny-1000 | 277.564 | 12.221 | 8.224 | 15.738 | 3.326 |
| tiny-10000 | 26,505.789 | 84.121 | 32.238 | 26.593 | 20.448 |
| fan-10 | 3.704 | 1.546 | 2.522 | 12.306 | 1.240 |
| fan-100 | 15.353 | 2.117 | 2.598 | 12.521 | 1.357 |
| fan-1000 | 266.203 | 10.516 | 7.634 | 13.582 | 3.109 |
| wait-100 | 263.893 | 15.785 | 14.054 | 22.795 | 12.766 |
| wait-1000 | 2,659.625 | 23.060 | 22.043 | 24.281 | 15.658 |
| stagger-100 | 283.336 | 25.276 | 22.918 | 32.678 | 22.204 |
| mixed-wait-100 | 91.741 | 25.314 | 23.748 | 33.131 | 22.205 |
| pool-light-1 | 16.488 | 128.925 | 62.067 | 43.261 | 1.072 |
| pool-light-2 | 10.645 | 139.592 | 63.538 | 46.426 | 1.220 |
| pool-light-4 | 6.902 | 174.482 | 82.726 | 56.201 | 1.149 |
| pool-medium-1 | 31.897 | 134.738 | 61.318 | 44.585 | 1.182 |
| pool-medium-2 | 17.576 | 139.931 | 61.123 | 46.609 | 1.193 |
| pool-medium-4 | 11.092 | 174.396 | 79.127 | 53.613 | 1.220 |
| pool-heavy-1 | 360.219 | 170.856 | 69.946 | 53.053 | 2.550 |
| pool-heavy-2 | 190.570 | 169.882 | 74.696 | 55.486 | 1.988 |
| pool-heavy-4 | 111.049 | 179.873 | 83.163 | 56.590 | 1.718 |
| cpu-1 | 15,425.973 | 2,386.950 | 341.808 | 445.102 | 54.510 |
| cpu-2 | 7,254.004 | 1,210.472 | 206.010 | 245.587 | 29.275 |
| cpu-4 | 3,905.406 | 763.011 | 144.374 | 162.964 | 15.741 |
| process-10 | 11.627 | 18.530 | 31.790 | 26.791 | 7.031 |
| process-100 | 91.162 | 63.008 | 194.861 | 85.156 | 37.845 |
| process-1000 | 902.037 | 453.014 | 1,886.327 | 506.293 | 338.342 |
| process-mixed | 110.845 | 95.802 | 189.358 | 112.324 | 81.257 |
| process-one-failure | 82.619 | 59.411 | 210.022 | 86.078 | 35.169 |
| process-many-failures | 84.664 | 60.512 | 172.513 | 82.333 | 37.448 |
| files-100 | 17.054 | 22.349 | 15.577 | 16.610 | 1.893 |
| files-1000 | 150.382 | 115.741 | 87.131 | 31.824 | 8.057 |
| files-10000 | 1,448.103 | 985.181 | 680.399 | 130.909 | 69.775 |
| queue-1000-1-1 | 461.287 | 7.019 | 7.900 | 15.648 | 2.557 |
| queue-1000-1-4 | 513.538 | 9.046 | 8.555 | 13.592 | 2.284 |
| queue-1000-4-1 | 511.042 | 10.320 | 7.194 | 14.100 | 2.505 |
| queue-1000-4-4 | 454.944 | 10.316 | 7.015 | 13.451 | 2.641 |
| queue-10000-1-1 | 3,894.848 | 31.507 | 18.197 | 20.180 | 12.556 |
| queue-10000-1-4 | 5,119.801 | 48.519 | 21.065 | 24.731 | 13.039 |
| queue-10000-4-1 | 5,020.116 | 45.703 | 20.581 | 21.589 | 13.736 |
| queue-10000-4-4 | 4,360.838 | 43.197 | 17.474 | 19.200 | 12.371 |
| queue-100000-1-1 | 41,922.289 | 288.769 | 123.527 | 72.512 | 131.619 |
| queue-100000-1-4 | 53,145.334 | 390.568 | 131.293 | 79.762 | 122.205 |
| queue-100000-4-1 | 52,088.629 | 378.463 | 122.607 | 81.366 | 122.518 |
| queue-100000-4-4 | 45,620.753 | 387.031 | 97.069 | 75.152 | 123.325 |
| atomic-1 | 461.996 | — | 63.044 | 45.099 | 1.133 |
| mutex-1-1 | 651.407 | 4.327 | — | — | 1.253 |
| mutex-8-1 | 747.244 | 6.438 | — | — | 1.129 |
| atomic-2 | 239.459 | — | 61.970 | 43.059 | 1.215 |
| mutex-1-2 | 700.684 | 6.028 | — | — | 1.374 |
| mutex-8-2 | 791.154 | 6.992 | — | — | 1.369 |
| atomic-4 | 160.248 | — | 82.441 | 55.511 | 1.401 |
| mutex-1-4 | 851.626 | 5.512 | — | — | 1.148 |
| mutex-8-4 | 900.410 | 6.470 | — | — | 1.202 |
| failures | 4.154 | 1.592 | 2.645 | 11.761 | 1.176 |
| mixed-64 | 93.551 | 69.312 | 168.651 | 80.852 | 61.034 |
| nested-10 | 8.821 | 1.989 | 2.469 | 12.498 | 1.283 |
| nested-100 | 62.165 | 7.064 | 5.260 | 12.866 | 2.063 |
| waiting-memory-100 | 268.515 | 16.302 | 13.994 | 22.399 | 13.344 |
| waiting-memory-1000 | 2,918.812 | 24.825 | 20.536 | 24.402 | 17.254 |
| waiting-memory-10000 | — | 147.079 | 56.996 | 30.971 | 59.625 |
