# Nift v4.12.0 — independent eight-suite recertification

**RELEASE-READY. I recommend releasing v4.12 exact c14d06835bca515a5281e41da0e40219c2d60ef0.** All67,153 official observations across eight suites and required exact-source diagnostics independently passed. No identified material release-blocking regression remains. This is a technical recommendation, not tag/release/package authorization.

The original call/fresh/full-build/RSS blockers are recovered or bounded near release. Heavy native no-op is a consistent11.90% slowdown versus original7f (28/30pairs), while46.35% faster than releasedbaseline and15.87%loweroriginalRSS. Preserve this nonblocking tradeoff. Other positive changes are descriptive, not hidden or reclassified as zero.

# Regression recovery — interim

Exact clean same-node releases: prior `c8d9c266518d115e4f289c5c6a2b94ddd7ee9968`, original `7f7e487c47a87e871dfef53345e2b71288008bff`, final `c14d06835bca515a5281e41da0e40219c2d60ef0`. Version names are shorthand; the original measured CLI reports v4.11.0 even though the user calls it the broken v4.12 candidate.

| Prior blocker | Release ms | Original ms | Final ms | Recovered? | Residual vs release |
|---|---:|---:|---:|---|---:|
| sanity/function-calls/small | 4.710201 | 7.374958 | 4.678490 | Yes, major original regression recovered | -0.67% |
| sanity/function-calls/large | 193.600459 | 469.418897 | 198.619788 | Yes, major original regression recovered | +2.59% |
| shell calls | 20.989496 | 44.971487 | 21.655463 | Partial: major original regression recovered | +3.17% |
| shell strings | 59.695733 | 66.950305 | 18.680012 | Yes; substantially faster than release | -68.71% |
| website fresh 10k | 2871.544599 | 3278.509241 | 2951.495366 | Partial: near-release recovery | +2.78% |
| tiny10k full | 16676.004755 | 20975.957026 | 14976.488604 | Yes | -10.19% |
| tiny child RSS (KiB, separate metric) | 17952 | 33312 | 17572 | Yes | -2.12% |

All 72 scripting observations and exact rotation/source/oracles passed independent audit. Final is faster than original in all 10 paired blocks for both sizes, with disjoint ranges. Final/release ranges overlap. Large calls remain +5.01933 ms (+2.59%) and are slower in 8/10 pairs; this residual is retained as a descriptive increase, not dismissed as zero or treated as a formal significance result. Small is −0.031711 ms (−0.67%), with 6/10 final pairs slower: near-flat. Original→final recovery: 36.56% small and 57.69% large.

Template controlled gains versus release remain: 72.19% source-render 10k loop,51.21% fresh 10k loop,38.09% article source. Checkpoint→final fresh loop +4.90% and article source +0.35% have overlapping ranges and remain listed as descriptive increases. Memory floor controls prove raw inherited-floor values unsuitable for runtime-memory ranking.

Website: all 18 diagnostic observations independently audited. Final is 9.97% faster than original, all five paired blocks faster with disjoint ranges. Final remains +79.950767 ms (+2.78%) versus release, overlapping ranges and three of five slower; no exact parity claim. Child peaks release/original/final are 17468/39872/17596 KiB.

Shell all72 diagnostic observations independently audited. Original/final calls disjoint ranges and all10 final faster; release residual+0.665967ms,+3.17%,8/10 slower with overlapping ranges. Strings all10 final faster with disjoint ranges against both baselines; final−72.10% versus original.

Website RSS(KiB) release17468/original39872/final17596, +0.73% release but−55.87% original, major growth recovered. Tiny full RSSrelease17952/original33312/final17572; fulltime and peakchild blockers recovered. Heavy native no-op release406.815/original195.063/final218.274ms: +11.90%original,28/30pairs slower, but−46.35%release all30pairsfaster; explicit bounded tradeoff, no release blocker identified.


# Interim final-candidate recertification

Audited official suites: scripting, template-engines, concurrency, website-generator, task-runners, shell, filesystem-automation, build-systems. Exact-source three-way version diagnostics remain separate from current official peer results and historical cross-node trends. No publication or release is authorized.

## Best same-node wall improvements versus explicit baseline — complete

| Rank | Suite / scenario | Baseline | Previous | Final | Unit | Improvement | Evidence basis |
|---:|---|---|---:|---:|---|---:|---|
| 1 | filesystem-automation / stat-10000/booted | release | 3526.404935 | 324.338002 | ms/request | 90.80% | Same node, 3 samples/version; descriptive same-node threepair; no formal significance |
| 2 | filesystem-automation / filter-size-10000/booted | release | 2812.878497 | 321.283145 | ms/request | 88.58% | Same node, 3 samples/version; descriptive same-node threepair; no formal significance |
| 3 | filesystem-automation / walk-10000/booted | release | 1629.322275 | 211.440930 | ms/request | 87.02% | Same node, 3 samples/version; descriptive same-node threepair; no formal significance |
| 4 | template-engines / loop-10000/source-render | release | 118.471604 | 32.942846 | ms/render | 72.19% | Same node, 3 samples/version; descriptive same-node three-version3samples; no formal significance; checkpoint increases have overlapping ranges |
| 5 | shell / string-transform | original | 66.950305 | 18.680011 | ms/invocation | 72.10% | Same node, 10 samples/version; All10 final pairs faster than original with disjoint ranges. Strings also all10 faster than release with disjoint ranges; calls/release overlap and8/10 final slower, residual descriptive. |
| 6 | concurrency / queue-100000-4-4 | release | 37528.313677 | 11455.302198 | ms/request | 69.48% | Same node, 3 samples/version; descriptive same-node3pairs; schedule ranges overlap, no formal significance |
| 7 | shell / string-transform | release | 59.695733 | 18.680011 | ms/invocation | 68.71% | Same node, 10 samples/version; All10 final pairs faster than original with disjoint ranges. Strings also all10 faster than release with disjoint ranges; calls/release overlap and8/10 final slower, residual descriptive. |
| 8 | scripting / sanity/function-calls/large | original | 469.418897 | 198.619788 | ms/invocation | 57.69% | Same node, 10 samples/version; Descriptive paired same-node. Final/release ranges overlap; large8/10 pairs slower despite modest residual, small6/10 slower. Original/final ranges disjoint and all10 final faster. |
| 9 | shell / function-calls | original | 44.971487 | 21.655462 | ms/invocation | 51.85% | Same node, 10 samples/version; All10 final pairs faster than original with disjoint ranges. Strings also all10 faster than release with disjoint ranges; calls/release overlap and8/10 final slower, residual descriptive. |
| 10 | template-engines / loop-10000/fresh | release | 158.529676 | 77.354308 | ms/invocation | 51.21% | Same node, 3 samples/version; descriptive same-node three-version3samples; no formal significance; checkpoint increases have overlapping ranges |
| 11 | build-systems / native-1000-heavy-j1/noop | release | 406.815025 | 218.274221 | ms/invocation | 46.35% | Same node, 30 samples/version; Exact-source same-node rotating independent audit; heavy no-op28/30 slower than original but30/30 faster release; bounded non-blocker, not dismissed as noise |
| 12 | template-engines / article/source-render | release | 0.433770 | 0.268566 | ms/render | 38.09% | Same node, 3 samples/version; descriptive same-node three-version3samples; no formal significance; checkpoint increases have overlapping ranges |
| 13 | scripting / sanity/function-calls/small | original | 7.374958 | 4.678490 | ms/invocation | 36.56% | Same node, 10 samples/version; Descriptive paired same-node. Final/release ranges overlap; large8/10 pairs slower despite modest residual, small6/10 slower. Original/final ranges disjoint and all10 final faster. |
| 14 | build-systems / tiny-10000-light-j4/full | original | 20975.957026 | 14976.488604 | ms/invocation | 28.60% | Same node, 5 samples/version; Exact-source same-node rotating independent audit; heavy no-op28/30 slower than original but30/30 faster release; bounded non-blocker, not dismissed as noise |
| 15 | build-systems / tiny-10000-light-j4/noop | release | 754.151091 | 586.915060 | ms/invocation | 22.18% | Same node, 20 samples/version; Exact-source same-node rotating independent audit; heavy no-op28/30 slower than original but30/30 faster release; bounded non-blocker, not dismissed as noise |
| 16 | filesystem-automation / filter-size-10000/booted | original | 385.269169 | 321.283145 | ms/request | 16.61% | Same node, 3 samples/version; descriptive same-node threepair; no formal significance |
| 17 | build-systems / tiny-10000-light-j4/full | release | 16676.004755 | 14976.488604 | ms/invocation | 10.19% | Same node, 5 samples/version; Exact-source same-node rotating independent audit; heavy no-op28/30 slower than original but30/30 faster release; bounded non-blocker, not dismissed as noise |
| 18 | website-generator / 10000/application-cold | original | 3278.509241 | 2951.495366 | ms/invocation | 9.97% | Same node, 5 samples/version; Descriptive paired same-node: final/original disjoint ranges, all five faster; final/release overlapping ranges, three of five slower; no equality or formal significance claim. |
| 19 | concurrency / schedule-1000 | original | 386.410787 | 362.049988 | ms/request | 6.30% | Same node, 3 samples/version; descriptive same-node3pairs; schedule ranges overlap, no formal significance |
| 20 | template-engines / article/fresh | release | 3.689644 | 3.507010 | ms/invocation | 4.95% | Same node, 3 samples/version; descriptive same-node three-version3samples; no formal significance; checkpoint increases have overlapping ranges |
| 21 | concurrency / queue-100000-4-4 | original | 12015.063135 | 11455.302198 | ms/request | 4.66% | Same node, 3 samples/version; descriptive same-node3pairs; schedule ranges overlap, no formal significance |
| 22 | build-systems / tiny-10000-light-j4/noop | original | 603.387523 | 586.915060 | ms/invocation | 2.73% | Same node, 20 samples/version; Exact-source same-node rotating independent audit; heavy no-op28/30 slower than original but30/30 faster release; bounded non-blocker, not dismissed as noise |
| 23 | task-runners / tiny-100-j4/full | release | 138.332636 | 134.851296 | ms/invocation | 2.52% | Same node, 5 samples/version; Descriptive same-node rotated five samples/source; overlapping ranges, no formal significance or major regression claim. |
| 24 | template-engines / loop-10000/source-render | original | 33.514301 | 32.942846 | ms/render | 1.71% | Same node, 3 samples/version; descriptive same-node three-version3samples; no formal significance; checkpoint increases have overlapping ranges |
| 25 | template-engines / article/fresh | original | 3.558491 | 3.507010 | ms/invocation | 1.45% | Same node, 3 samples/version; descriptive same-node three-version3samples; no formal significance; checkpoint increases have overlapping ranges |
| 26 | scripting / sanity/function-calls/small | release | 4.710201 | 4.678490 | ms/invocation | 0.67% | Same node, 10 samples/version; Descriptive paired same-node. Final/release ranges overlap; large8/10 pairs slower despite modest residual, small6/10 slower. Original/final ranges disjoint and all10 final faster. |
| 27 | filesystem-automation / walk-10000/booted | original | 211.759266 | 211.440930 | ms/request | 0.15% | Same node, 3 samples/version; descriptive same-node threepair; no formal significance |

## Every measured positive same-node wall change — complete

| Rank | Suite / scenario | Baseline | Baseline value | Final | Increase | Classification |
|---:|---|---|---:|---:|---:|---|
| 1 | build-systems / native-1000-heavy-j1/noop | original | 195.062514 | 218.274221 | 11.90% | consistent tested-cohort original-relative slowdown; bounded non-blocker relative to release |
| 2 | concurrency / schedule-1000 | release | 333.087228 | 362.049988 | 8.70% | descriptive same-node increase; not formal significance |
| 3 | template-engines / loop-10000/fresh | original | 73.741216 | 77.354308 | 4.90% | descriptive same-node increase; not formal significance |
| 4 | task-runners / tiny-100-j4/full | original | 129.031413 | 134.851296 | 4.51% | descriptive same-node increase; not formal significance |
| 5 | shell / function-calls | release | 20.989496 | 21.655462 | 3.17% | descriptive same-node increase; not formal significance |
| 6 | website-generator / 10000/application-cold | release | 2871.544599 | 2951.495366 | 2.78% | descriptive same-node increase; not formal significance |
| 7 | scripting / sanity/function-calls/large | release | 193.600459 | 198.619788 | 2.59% | descriptive same-node increase; not formal significance |
| 8 | filesystem-automation / stat-10000/booted | original | 319.134635 | 324.338002 | 1.63% | descriptive same-node increase; not formal significance |
| 9 | template-engines / article/source-render | original | 0.267626 | 0.268566 | 0.35% | descriptive same-node increase; not formal significance |

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
| 54 | filesystem-automation / detect-hash-2-10000/booted | 21031.6198 | go | 421.5935 | ms | 49.89× |
| 55 | concurrency / queue-1000-1-1/persistent | 105.5744 | go | 2.1562 | ms | 48.96× |
| 56 | filesystem-automation / detect-hash-1-10000/booted | 20165.3583 | go | 416.7773 | ms | 48.38× |
| 57 | filesystem-automation / detect-hash-3-10000/booted | 20065.5714 | go | 417.9635 | ms | 48.01× |
| 58 | scripting / graphs-trees-search/bfs/large | 799.3592 | luajit | 16.9315 | ms/invocation | 47.21× |
| 59 | filesystem-automation / detect-hash-2-10000/fresh | 19912.3056 | go | 423.2704 | ms | 47.04× |
| 60 | filesystem-automation / detect-hash-1-10000/fresh | 20196.2024 | go | 435.5925 | ms | 46.36× |
| 61 | filesystem-automation / detect-hash-3-10000/fresh | 20457.5586 | go | 447.4014 | ms | 45.73× |
| 62 | filesystem-automation / detect-hash-3-1000/booted | 2008.8096 | go | 44.7945 | ms | 44.84× |
| 63 | filesystem-automation / detect-hash-1-1000/booted | 2048.2245 | go | 46.8969 | ms | 43.68× |
| 64 | filesystem-automation / read-100000/fresh | 103416.3004 | go | 2406.4208 | ms | 42.98× |
| 65 | concurrency / pool-heavy-4/persistent | 79.3047 | go | 1.8696 | ms | 42.42× |
| 66 | filesystem-automation / read-10000/booted | 10530.1120 | go | 249.3940 | ms | 42.22× |
| 67 | concurrency / atomic-4/persistent | 46.1550 | go | 1.0964 | ms | 42.10× |
| 68 | filesystem-automation / detect-hash-2-1000/booted | 2002.2790 | go | 47.7273 | ms | 41.95× |
| 69 | filesystem-automation / read-100000/booted | 102441.2588 | go | 2472.1421 | ms | 41.44× |
| 70 | filesystem-automation / clean-10000/fresh | 21241.1869 | go | 519.4729 | ms | 40.89× |
| 71 | concurrency / pool-heavy-1/fresh | 294.3978 | go | 7.2668 | ms | 40.51× |
| 72 | filesystem-automation / manifest-1000/booted | 1085.5511 | go | 27.4136 | ms | 39.60× |
| 73 | filesystem-automation / mirror-0-10000/booted | 21479.6440 | go | 543.9930 | ms | 39.49× |
| 74 | filesystem-automation / clean-10000/booted | 20781.9702 | go | 526.5845 | ms | 39.47× |
| 75 | filesystem-automation / manifest-10000/booted | 11105.6035 | go | 283.1150 | ms | 39.23× |
| 76 | concurrency / fan-1000/fresh | 332.0085 | go | 8.4646 | ms | 39.22× |
| 77 | concurrency / tiny-1000/fresh | 305.4130 | go | 7.8016 | ms | 39.15× |
| 78 | filesystem-automation / read-10000/fresh | 10225.3037 | go | 263.6383 | ms | 38.79× |
| 79 | filesystem-automation / clean-1000/booted | 2048.2343 | go | 53.1909 | ms | 38.51× |
| 80 | filesystem-automation / read-1000/booted | 1019.0237 | go | 26.6169 | ms | 38.28× |
| 81 | filesystem-automation / mirror-0-10000/fresh | 22381.7739 | go | 593.7882 | ms | 37.69× |
| 82 | filesystem-automation / detect-hash-3-1000/fresh | 1993.7474 | go | 53.4220 | ms | 37.32× |
| 83 | filesystem-automation / mirror-12-10000/booted | 20726.1051 | go | 560.9934 | ms | 36.95× |
| 84 | filesystem-automation / mirror-1-10000/booted | 21048.0032 | go | 572.5356 | ms | 36.76× |
| 85 | filesystem-automation / manifest-10000/fresh | 10849.5834 | go | 295.2051 | ms | 36.75× |
| 86 | filesystem-automation / detect-hash-1-1000/fresh | 2039.3138 | go | 55.6329 | ms | 36.66× |
| 87 | filesystem-automation / mirror-1-10000/fresh | 21255.1911 | go | 581.8454 | ms | 36.53× |
| 88 | filesystem-automation / detect-hash-2-1000/fresh | 2063.7184 | go | 57.4378 | ms | 35.93× |
| 89 | filesystem-automation / mirror-12-10000/fresh | 20446.2450 | go | 569.5686 | ms | 35.90× |
| 90 | concurrency / schedule-1000/fresh | 262.7284 | go | 7.4816 | ms | 35.12× |
| 91 | filesystem-automation / mirror-12-1000/booted | 2023.9121 | go | 57.8264 | ms | 35.00× |
| 92 | filesystem-automation / mirror-1-1000/booted | 2070.4817 | go | 61.8650 | ms | 33.47× |
| 93 | filesystem-automation / mirror-0-1000/booted | 2091.5292 | go | 62.8276 | ms | 33.29× |
| 94 | filesystem-automation / read-1000/fresh | 1057.3648 | go | 32.0405 | ms | 33.00× |
| 95 | filesystem-automation / mirror-10-10000/booted | 21153.0511 | go | 648.5098 | ms | 32.62× |
| 96 | filesystem-automation / mirror-11-10000/booted | 20744.5351 | go | 639.0758 | ms | 32.46× |
| 97 | filesystem-automation / clean-1000/fresh | 2007.2720 | go | 63.1950 | ms | 31.76× |
| 98 | filesystem-automation / mirror-11-10000/fresh | 21188.2833 | go | 676.6380 | ms | 31.31× |
| 99 | concurrency / mutex-8-2/fresh | 268.4126 | go | 8.5771 | ms | 31.29× |
| 100 | filesystem-automation / mirror-10-10000/fresh | 20919.1710 | go | 670.4953 | ms | 31.20× |
| 101 | filesystem-automation / mirror-0-1000/fresh | 2103.5809 | go | 68.1443 | ms | 30.87× |
| 102 | concurrency / mutex-8-4/fresh | 274.3082 | go | 8.9422 | ms | 30.68× |
| 103 | filesystem-automation / mirror-10-1000/booted | 2106.4946 | go | 68.9017 | ms | 30.57× |
| 104 | filesystem-automation / mirror-12-1000/fresh | 2062.8181 | go | 67.5294 | ms | 30.55× |
| 105 | filesystem-automation / mirror-1-1000/fresh | 2076.7286 | go | 71.1475 | ms | 29.19× |
| 106 | concurrency / nested-100/persistent | 53.6530 | go | 1.8547 | ms | 28.93× |
| 107 | filesystem-automation / mirror-11-1000/booted | 2116.5977 | go | 73.8248 | ms | 28.67× |
| 108 | concurrency / mutex-8-1/fresh | 233.2463 | go | 8.1730 | ms | 28.54× |
| 109 | filesystem-automation / manifest-1000/fresh | 1047.0671 | go | 36.9683 | ms | 28.32× |
| 110 | concurrency / pool-medium-1/persistent | 32.5850 | go | 1.1604 | ms | 28.08× |
| 111 | concurrency / mutex-1-2/fresh | 221.5863 | go | 8.1503 | ms | 27.19× |
| 112 | concurrency / mutex-1-4/fresh | 241.7080 | go | 9.0440 | ms | 26.73× |
| 113 | filesystem-automation / mirror-11-1000/fresh | 2086.4347 | go | 79.4734 | ms | 26.25× |
| 114 | filesystem-automation / mirror-10-1000/fresh | 2066.0328 | go | 81.1549 | ms | 25.46× |
| 115 | concurrency / mutex-1-1/fresh | 189.4023 | go | 8.4002 | ms | 22.55× |
| 116 | concurrency / pool-light-1/persistent | 22.0090 | go | 0.9859 | ms | 22.32× |
| 117 | scripting / arrays-strings-hash/sort-index/large | 511.6308 | python | 23.0522 | ms/invocation | 22.19× |
| 118 | concurrency / waiting-memory-100/persistent | 264.0268 | go | 11.9635 | ms | 22.07× |
| 119 | concurrency / wait-100/persistent | 259.2278 | go | 11.9826 | ms | 21.63× |
| 120 | concurrency / pool-heavy-2/fresh | 155.0466 | go | 7.4547 | ms | 20.80× |
| 121 | concurrency / files-10000/persistent | 1446.8240 | go | 72.4073 | ms | 19.98× |
| 122 | filesystem-automation / mixed-10000/fresh | 5938.5322 | go | 314.7747 | ms | 18.87× |
| 123 | concurrency / files-10000/fresh | 1461.2957 | go | 79.5973 | ms | 18.36× |
| 124 | concurrency / files-1000/persistent | 145.3815 | go | 7.9992 | ms | 18.17× |
| 125 | filesystem-automation / mixed-1000/booted | 622.5871 | go | 34.9746 | ms | 17.80× |
| 126 | concurrency / atomic-1/fresh | 136.9979 | go | 7.8062 | ms | 17.55× |
| 127 | filesystem-automation / mixed-10000/booted | 5921.1169 | go | 348.1627 | ms | 17.01× |
| 128 | concurrency / queue-1000-1-4/fresh | 124.7663 | go | 7.4661 | ms | 16.71× |
| 129 | filesystem-automation / generate-10000/booted | 13139.3757 | go | 791.9760 | ms | 16.59× |
| 130 | concurrency / queue-1000-4-4/fresh | 127.2198 | go | 7.8016 | ms | 16.31× |
| 131 | concurrency / queue-1000-4-1/fresh | 123.8996 | go | 7.6017 | ms | 16.30× |
| 132 | concurrency / wait-100/fresh | 265.5381 | go | 16.3085 | ms | 16.28× |
| 133 | template-engines / loop-10000/source-render | 34.0847 | handlebars | 2.2486 | ms/render | 15.16× |
| 134 | concurrency / pool-medium-2/persistent | 18.4455 | go | 1.2235 | ms | 15.08× |
| 135 | filesystem-automation / generate-1000/booted | 1342.8580 | go | 89.1373 | ms | 15.07× |
| 136 | filesystem-automation / generate-10000/fresh | 13415.8439 | go | 909.8670 | ms | 14.74× |
| 137 | concurrency / queue-1000-1-1/fresh | 111.5006 | go | 7.5685 | ms | 14.73× |
| 138 | filesystem-automation / generate-1000/fresh | 1337.2332 | go | 93.8949 | ms | 14.24× |
| 139 | filesystem-automation / mixed-1000/fresh | 612.2146 | go | 44.1991 | ms | 13.85× |
| 140 | concurrency / waiting-memory-100/fresh | 274.6798 | go | 20.3128 | ms | 13.52× |
| 141 | concurrency / schedule-100/persistent | 16.4205 | go | 1.2373 | ms | 13.27× |
| 142 | concurrency / stagger-100/persistent | 279.9780 | go | 22.0836 | ms | 12.68× |
| 143 | build-systems / native-1000-heavy-j1/noop | 230.4782 | ninja | 18.4633 | ms | 12.48× |
| 144 | concurrency / tiny-100/persistent | 14.8006 | go | 1.1894 | ms | 12.44× |
| 145 | concurrency / fan-100/persistent | 15.3168 | go | 1.3008 | ms | 11.77× |
| 146 | concurrency / files-100/persistent | 22.6972 | go | 1.9601 | ms | 11.58× |
| 147 | concurrency / pool-light-2/persistent | 13.0158 | go | 1.1585 | ms | 11.23× |
| 148 | concurrency / pool-heavy-4/fresh | 87.2585 | go | 8.0942 | ms | 10.78× |
| 149 | concurrency / stagger-100/fresh | 287.4284 | go | 27.0907 | ms | 10.61× |
| 150 | concurrency / files-1000/fresh | 154.3703 | go | 14.7866 | ms | 10.44× |
| 151 | filesystem-automation / walk-100000/booted | 2029.2680 | bun | 210.8797 | ms | 9.62× |
| 152 | filesystem-automation / large-read-100x1048576/booted | 220.7429 | python | 23.5254 | ms | 9.38× |
| 153 | concurrency / atomic-2/fresh | 88.3376 | go | 9.7062 | ms | 9.10× |
| 154 | filesystem-automation / filter-10-100000/booted | 5848.9603 | bun | 657.5007 | ms | 8.90× |
| 155 | concurrency / pool-medium-4/persistent | 11.2288 | go | 1.2728 | ms | 8.82× |
| 156 | build-systems / tiny-100-light-j1/noop | 21.4944 | make | 2.4668 | ms | 8.71× |
| 157 | filesystem-automation / filter-50-100000/booted | 6292.6970 | bun | 729.4314 | ms | 8.63× |
| 158 | template-engines / collection/source-render | 7.1487 | handlebars | 0.8673 | ms/render | 8.24× |
| 159 | filesystem-automation / filter-50-100000/fresh | 6205.5808 | bun | 753.2677 | ms | 8.24× |
| 160 | filesystem-automation / filter-1-10000/booted | 550.0207 | go | 67.6463 | ms | 8.13× |
| 161 | filesystem-automation / filter-1-100000/booted | 5298.3963 | bun | 657.6567 | ms | 8.06× |
| 162 | filesystem-automation / filter-1-100000/fresh | 5511.7034 | go | 688.3674 | ms | 8.01× |
| 163 | filesystem-automation / filter-50-10000/booted | 607.1536 | go | 76.1841 | ms | 7.97× |
| 164 | filesystem-automation / filter-10-100000/fresh | 5744.0764 | bun | 721.1544 | ms | 7.97× |
| 165 | filesystem-automation / walk-100000/fresh | 2283.0594 | bun | 290.5696 | ms | 7.86× |
| 166 | filesystem-automation / filter-10-10000/booted | 543.7347 | go | 71.6272 | ms | 7.59× |
| 167 | build-systems / native-1000-heavy-j2/noop | 136.5782 | ninja | 18.3435 | ms | 7.45× |
| 168 | concurrency / nested-10/persistent | 7.4980 | go | 1.0446 | ms | 7.18× |
| 169 | build-systems / native-100-light-j1/noop | 30.8278 | ninja | 4.3353 | ms | 7.11× |
| 170 | concurrency / nested-100/fresh | 68.9687 | go | 9.7549 | ms | 7.07× |
| 171 | filesystem-automation / filter-1-10000/fresh | 560.6973 | go | 80.6054 | ms | 6.96× |
| 172 | filesystem-automation / filter-10-10000/fresh | 570.0869 | go | 82.0884 | ms | 6.94× |
| 173 | build-systems / tiny-1000-light-j4/leaf | 75.3909 | make | 11.0246 | ms | 6.84× |
| 174 | filesystem-automation / filter-50-1000/booted | 64.2483 | go | 9.4462 | ms | 6.80× |
| 175 | build-systems / native-100-heavy-j1/noop | 31.7580 | ninja | 4.6891 | ms | 6.77× |
| 176 | filesystem-automation / filter-1-1000/booted | 58.9042 | go | 8.7057 | ms | 6.77× |
| 177 | filesystem-automation / filter-50-10000/fresh | 626.4052 | go | 92.9901 | ms | 6.74× |
| 178 | build-systems / tiny-1000-light-j4/noop | 68.9471 | make | 10.2871 | ms | 6.70× |
| 179 | filesystem-automation / filter-10-1000/booted | 59.8198 | go | 8.9911 | ms | 6.65× |
| 180 | build-systems / tiny-10000-light-j4/batch10 | 701.0993 | make | 107.0070 | ms | 6.55× |
| 181 | concurrency / pool-light-4/persistent | 7.9990 | go | 1.2280 | ms | 6.51× |
| 182 | build-systems / tiny-10000-light-j4/leaf | 633.4706 | make | 99.1071 | ms | 6.39× |
| 183 | build-systems / tiny-10000-light-j4/noop | 617.3281 | make | 96.9502 | ms | 6.37× |
| 184 | concurrency / pool-medium-1/fresh | 39.6197 | go | 6.2228 | ms | 6.37× |
| 185 | filesystem-automation / large-read-10x10485760/booted | 293.8577 | go | 46.9966 | ms | 6.25× |
| 186 | scripting / structured-data/json-transform/large | 462.8532 | node | 74.5456 | ms/invocation | 6.21× |
| 187 | build-systems / tiny-100-light-j1/leaf | 26.0570 | make | 4.1969 | ms | 6.21× |
| 188 | filesystem-automation / filter-prefix-100000/booted | 3815.7994 | bun | 616.7908 | ms | 6.19× |
| 189 | concurrency / atomic-4/fresh | 56.5908 | go | 9.1779 | ms | 6.17× |
| 190 | filesystem-automation / walk-10000/booted | 196.0606 | bun | 31.9650 | ms | 6.13× |
| 191 | scripting / graphs-trees-search/bfs/small | 11.4051 | lua54 | 1.8680 | ms/invocation | 6.11× |
| 192 | build-systems / tiny-100-light-j2/noop | 15.3469 | make | 2.5700 | ms | 5.97× |
| 193 | filesystem-automation / filter-extension-100000/booted | 3782.8717 | bun | 656.5571 | ms | 5.76× |
| 194 | filesystem-automation / filter-prefix-100000/fresh | 3775.2457 | go | 677.5062 | ms | 5.57× |
| 195 | filesystem-automation / filter-extension-100000/fresh | 3856.2137 | bun | 693.2050 | ms | 5.56× |
| 196 | filesystem-automation / overwrite-10000/booted | 2567.1175 | bun | 464.2818 | ms | 5.53× |
| 197 | filesystem-automation / filter-prefix-10000/booted | 365.0172 | go | 67.4361 | ms | 5.41× |
| 198 | scripting / structured-data/json-traverse/large | 370.4149 | node | 68.6082 | ms/invocation | 5.40× |
| 199 | scripting / arrays-strings-hash/frequency-count/small | 7.0682 | luajit | 1.3125 | ms/invocation | 5.39× |
| 200 | filesystem-automation / filter-size-100000/booted | 3425.0966 | bun | 636.0797 | ms | 5.38× |
| 201 | filesystem-automation / filter-extension-10000/booted | 378.7658 | go | 70.4589 | ms | 5.38× |
| 202 | filesystem-automation / overwrite-10000/fresh | 2601.1766 | bun | 501.0773 | ms | 5.19× |
| 203 | build-systems / tiny-1000-light-j4/batch10 | 82.4381 | make | 15.8838 | ms | 5.19× |
| 204 | template-engines / loop-1000/source-render | 3.2934 | handlebars | 0.6493 | ms/render | 5.07× |
| 205 | build-systems / native-1000-light-j4/noop | 91.1865 | ninja | 18.1519 | ms | 5.02× |
| 206 | filesystem-automation / relocate-10000/booted | 419.6147 | bun | 84.2040 | ms | 4.98× |
| 207 | build-systems / native-1000-heavy-j4/noop | 91.7300 | ninja | 18.5901 | ms | 4.93× |
| 208 | filesystem-automation / filter-extension-10000/fresh | 391.9228 | go | 79.9359 | ms | 4.90× |
| 209 | build-systems / tiny-100-light-j2/leaf | 19.1122 | make | 3.9173 | ms | 4.88× |
| 210 | build-systems / native-5000-light-j4/noop | 398.9716 | ninja | 81.9409 | ms | 4.87× |
| 211 | filesystem-automation / filter-prefix-10000/fresh | 377.5784 | go | 77.8717 | ms | 4.85× |
| 212 | build-systems / native-100-light-j2/noop | 22.6038 | ninja | 4.6686 | ms | 4.84× |
| 213 | build-systems / native-100-heavy-j2/noop | 22.6666 | ninja | 4.7084 | ms | 4.81× |
| 214 | filesystem-automation / stat-100000/booted | 3210.5829 | bun | 670.5396 | ms | 4.79× |
| 215 | filesystem-automation / filter-prefix-1000/booted | 39.1129 | go | 8.2107 | ms | 4.76× |
| 216 | filesystem-automation / filter-extension-1000/booted | 42.1535 | go | 8.8684 | ms | 4.75× |
| 217 | filesystem-automation / stat-100000/fresh | 3416.2071 | bun | 721.9765 | ms | 4.73× |
| 218 | filesystem-automation / overwrite-1000/booted | 263.7253 | bun | 56.2063 | ms | 4.69× |
| 219 | filesystem-automation / filter-size-100000/fresh | 3294.2548 | bun | 702.1274 | ms | 4.69× |
| 220 | filesystem-automation / large-read-100x1048576/fresh | 237.1961 | go | 51.0175 | ms | 4.65× |
| 221 | filesystem-automation / large-read-10x10485760/fresh | 310.3273 | go | 67.1469 | ms | 4.62× |
| 222 | build-systems / native-10000-light-j4/noop | 793.8650 | ninja | 171.8466 | ms | 4.62× |
| 223 | concurrency / pool-light-1/fresh | 27.9631 | go | 6.1161 | ms | 4.57× |
| 224 | scripting / arrays-strings-hash/sort-index/small | 6.8471 | luajit | 1.5076 | ms/invocation | 4.54× |
| 225 | build-systems / tiny-100-light-j4/noop | 11.8530 | make | 2.6492 | ms | 4.47× |
| 226 | filesystem-automation / filter-size-10000/booted | 324.3832 | bun | 73.1929 | ms | 4.43× |
| 227 | template-engines / literal/source-render | 0.0152 | liquid | 0.0036 | ms/render | 4.21× |
| 228 | filesystem-automation / filter-10-1000/fresh | 69.1495 | go | 16.4528 | ms | 4.20× |
| 229 | filesystem-automation / filter-50-1000/fresh | 72.1717 | go | 17.2031 | ms | 4.20× |
| 230 | concurrency / mixed-wait-100/persistent | 89.3006 | go | 21.5602 | ms | 4.14× |
| 231 | concurrency / schedule-100/fresh | 24.9326 | go | 6.1022 | ms | 4.09× |
| 232 | filesystem-automation / walk-1000/booted | 22.8769 | go | 5.6188 | ms | 4.07× |
| 233 | shell / traverse-100000/shell-workloads.json | 1032.9553 | nu | 255.0395 | ms | 4.05× |
| 234 | filesystem-automation / stat-10000/booted | 309.6842 | bun | 77.5312 | ms | 3.99× |
| 235 | filesystem-automation / relocate-1000/booted | 44.5655 | go | 11.1672 | ms | 3.99× |
| 236 | filesystem-automation / filter-size-10000/fresh | 337.0324 | go | 84.6915 | ms | 3.98× |
| 237 | filesystem-automation / filter-1-1000/fresh | 65.7123 | go | 16.6054 | ms | 3.96× |
| 238 | scripting / arrays-strings-hash/sliding-window/small | 5.2873 | luajit | 1.3394 | ms/invocation | 3.95× |
| 239 | filesystem-automation / filter-size-1000/booted | 34.7896 | go | 8.8239 | ms | 3.94× |
| 240 | build-systems / tiny-100-light-j4/leaf | 16.0839 | make | 4.1644 | ms | 3.86× |
| 241 | filesystem-automation / relocate-10000/fresh | 416.1732 | go | 110.6942 | ms | 3.76× |
| 242 | concurrency / pool-medium-2/fresh | 25.0479 | go | 6.7361 | ms | 3.72× |
| 243 | filesystem-automation / walk-10000/fresh | 213.0929 | go | 57.7539 | ms | 3.69× |
| 244 | build-systems / native-100-heavy-j4/noop | 16.9881 | ninja | 4.6059 | ms | 3.69× |
| 245 | concurrency / tiny-100/fresh | 22.9509 | go | 6.2963 | ms | 3.65× |
| 246 | concurrency / mixed-wait-100/fresh | 96.2921 | go | 26.6700 | ms | 3.61× |
| 247 | build-systems / native-100-light-j4/noop | 16.2743 | ninja | 4.5130 | ms | 3.61× |
| 248 | concurrency / fan-100/fresh | 21.4875 | go | 6.0013 | ms | 3.58× |
| 249 | scripting / sanity/function-calls/small | 4.6504 | luajit | 1.3011 | ms/invocation | 3.57× |
| 250 | filesystem-automation / stat-1000/booted | 34.0560 | go | 9.5384 | ms | 3.57× |
| 251 | concurrency / schedule-10/persistent | 3.3856 | go | 0.9958 | ms | 3.40× |
| 252 | filesystem-automation / stat-10000/fresh | 338.3692 | go | 99.8467 | ms | 3.39× |
| 253 | scripting / arrays-strings-hash/map-set/small | 4.7012 | luajit | 1.3955 | ms/invocation | 3.37× |
| 254 | concurrency / fan-10/persistent | 3.4225 | go | 1.0168 | ms | 3.37× |
| 255 | concurrency / tiny-10/persistent | 3.4552 | go | 1.0271 | ms | 3.36× |
| 256 | scripting / filesystem/traverse/large | 25.0047 | luajit | 7.6408 | ms/invocation | 3.27× |
| 257 | filesystem-automation / write-10000/fresh | 2122.1548 | go | 653.9608 | ms | 3.25× |
| 258 | concurrency / files-100/fresh | 25.0290 | go | 7.7302 | ms | 3.24× |
| 259 | concurrency / failures/persistent | 3.6130 | go | 1.1228 | ms | 3.22× |
| 260 | filesystem-automation / filter-extension-1000/fresh | 49.4720 | go | 15.8167 | ms | 3.13× |
| 261 | concurrency / pool-light-2/fresh | 18.7950 | go | 6.0366 | ms | 3.11× |
| 262 | filesystem-automation / filter-prefix-1000/fresh | 47.8932 | go | 15.6227 | ms | 3.07× |
| 263 | filesystem-automation / overwrite-1000/fresh | 275.5315 | bun | 91.1196 | ms | 3.02× |
| 264 | filesystem-automation / delete-10000/booted | 851.6482 | bun | 283.9042 | ms | 3.00× |
| 265 | concurrency / process-1000/fresh | 986.5840 | go | 330.7045 | ms | 2.98× |
| 266 | concurrency / process-1000/persistent | 1001.1120 | go | 336.3992 | ms | 2.98× |
| 267 | filesystem-automation / write-1000/booted | 207.1363 | go | 70.5515 | ms | 2.94× |
| 268 | shell / metadata-10000/shell-workloads.json | 118.6269 | fish | 40.6527 | ms | 2.92× |
| 269 | filesystem-automation / write-10000/booted | 1961.1666 | go | 675.8928 | ms | 2.90× |
| 270 | build-systems / tiny-100-light-j4/batch10 | 25.1431 | make | 8.8297 | ms | 2.85× |
| 271 | filesystem-automation / rename-10000/booted | 793.8146 | bun | 281.8145 | ms | 2.82× |
| 272 | filesystem-automation / delete-1000/booted | 84.7321 | go | 30.2473 | ms | 2.80× |
| 273 | build-systems / tiny-100-light-j2/batch10 | 35.3906 | make | 12.6698 | ms | 2.79× |
| 274 | filesystem-automation / write-1000/fresh | 219.9603 | go | 78.8647 | ms | 2.79× |
| 275 | scripting / arrays-strings-hash/scan/small | 3.5558 | luajit | 1.2906 | ms/invocation | 2.76× |
| 276 | filesystem-automation / filter-size-1000/fresh | 43.0676 | go | 15.7762 | ms | 2.73× |
| 277 | scripting / structured-data/json-parse/large | 182.0766 | node | 66.9882 | ms/invocation | 2.72× |
| 278 | filesystem-automation / copy-100000/booted | 16647.7805 | go | 6175.2135 | ms | 2.70× |
| 279 | concurrency / process-one-failure/persistent | 99.5204 | go | 37.0044 | ms | 2.69× |
| 280 | filesystem-automation / relocate-1000/fresh | 52.2297 | go | 19.4520 | ms | 2.69× |
| 281 | filesystem-automation / large-write-10x10485760/booted | 407.8015 | python | 152.4887 | ms | 2.67× |
| 282 | filesystem-automation / delete-10000/fresh | 848.7326 | go | 323.1023 | ms | 2.63× |
| 283 | build-systems / tiny-10000-light-j4/full | 15846.3097 | make | 6065.2814 | ms | 2.61× |
| 284 | scripting / sanity/loops/small | 3.3463 | luajit | 1.2815 | ms/invocation | 2.61× |
| 285 | build-systems / tiny-100-light-j1/batch10 | 50.2201 | make | 19.4441 | ms | 2.58× |
| 286 | concurrency / process-100/persistent | 96.9259 | go | 37.5413 | ms | 2.58× |
| 287 | filesystem-automation / copy-100000/fresh | 16734.8613 | go | 6616.8994 | ms | 2.53× |
| 288 | filesystem-automation / copy-10000/fresh | 1586.3447 | go | 628.0252 | ms | 2.53× |
| 289 | concurrency / pool-medium-4/fresh | 17.6773 | go | 7.0240 | ms | 2.52× |
| 290 | concurrency / process-many-failures/persistent | 90.3119 | go | 35.9896 | ms | 2.51× |
| 291 | concurrency / process-100/fresh | 103.2234 | go | 41.5633 | ms | 2.48× |
| 292 | filesystem-automation / walk-1000/fresh | 30.7777 | go | 12.4125 | ms | 2.48× |
| 293 | concurrency / process-one-failure/fresh | 106.1708 | go | 42.9256 | ms | 2.47× |
| 294 | filesystem-automation / stat-1000/fresh | 41.6152 | go | 16.8309 | ms | 2.47× |
| 295 | filesystem-automation / rename-1000/booted | 79.6292 | python | 32.2901 | ms | 2.47× |
| 296 | concurrency / process-many-failures/fresh | 107.4996 | go | 44.0543 | ms | 2.44× |
| 297 | filesystem-automation / delete-1000/fresh | 96.5446 | go | 39.7160 | ms | 2.43× |
| 298 | filesystem-automation / rename-10000/fresh | 841.8410 | go | 346.8381 | ms | 2.43× |
| 299 | filesystem-automation / copy-1000/booted | 159.4206 | go | 65.8257 | ms | 2.42× |
| 300 | filesystem-automation / large-write-100x1048576/booted | 343.6599 | python | 142.3333 | ms | 2.41× |
| 301 | shell / concat-small-10000/shell-workloads.json | 252.6080 | zsh | 105.0090 | ms | 2.41× |
| 302 | concurrency / process-10/persistent | 12.2189 | go | 5.1030 | ms | 2.39× |
| 303 | filesystem-automation / copy-10000/booted | 1568.4696 | go | 660.2457 | ms | 2.38× |
| 304 | filesystem-automation / large-write-10x10485760/fresh | 430.9240 | go | 181.6619 | ms | 2.37× |
| 305 | filesystem-automation / large-write-100x1048576/fresh | 372.6883 | go | 157.9900 | ms | 2.36× |
| 306 | filesystem-automation / copy-1000/fresh | 166.7575 | go | 72.9585 | ms | 2.29× |
| 307 | shell / create-small-100000/shell-workloads.json | 10823.5322 | nu | 4769.2090 | ms | 2.27× |
| 308 | concurrency / pool-light-4/fresh | 15.3313 | go | 6.8087 | ms | 2.25× |
| 309 | scripting / dynamic-programming/fibonacci/small | 2.8171 | luajit | 1.2633 | ms/invocation | 2.23× |
| 310 | filesystem-automation / rename-1000/fresh | 92.1560 | go | 43.2040 | ms | 2.13× |
| 311 | concurrency / nested-10/fresh | 17.1503 | go | 8.0910 | ms | 2.12× |
| 312 | template-engines / many-templates-100/source-render | 0.0214 | liquid | 0.0102 | ms/render | 2.09× |
| 313 | template-engines / nested-loops/source-render | 1.0676 | nunjucks | 0.5115 | ms/render | 2.09× |
| 314 | scripting / sanity/output/small | 2.5214 | luajit | 1.2174 | ms/invocation | 2.07× |
| 315 | template-engines / many-templates-1000/source-render | 0.0215 | liquid | 0.0105 | ms/render | 2.06× |
| 316 | build-systems / tiny-100-light-j4/full | 124.9606 | make | 61.8814 | ms | 2.02× |
| 317 | scripting / sanity/noop/large | 2.3885 | luajit | 1.1839 | ms/invocation | 2.02× |
| 318 | scripting / sanity/noop/small | 2.4628 | luajit | 1.2283 | ms/invocation | 2.01× |
| 319 | scripting / sanity/output/large | 2.4649 | luajit | 1.2294 | ms/invocation | 2.00× |
| 320 | template-engines / many-templates-10/source-render | 0.0212 | liquid | 0.0108 | ms/render | 1.96× |
| 321 | build-systems / native-1000-heavy-j1/leaf | 486.0913 | ninja | 248.6606 | ms | 1.95× |
| 322 | build-systems / tiny-100-light-j1/full | 300.4674 | make | 154.0678 | ms | 1.95× |
| 323 | build-systems / tiny-1000-light-j4/full | 1046.2921 | make | 546.0065 | ms | 1.92× |
| 324 | build-systems / tiny-100-light-j2/full | 156.2428 | make | 82.2865 | ms | 1.90× |
| 325 | build-systems / native-1000-light-j4/target | 113.2444 | ninja | 61.8373 | ms | 1.83× |
| 326 | concurrency / schedule-10/fresh | 9.2472 | go | 5.0691 | ms | 1.82× |
| 327 | concurrency / tiny-10/fresh | 9.5623 | go | 5.6499 | ms | 1.69× |
| 328 | concurrency / process-10/fresh | 18.3494 | go | 11.0670 | ms | 1.66× |
| 329 | concurrency / fan-10/fresh | 10.1324 | go | 6.1978 | ms | 1.63× |
| 330 | concurrency / mixed-64/persistent | 93.2786 | go | 58.5399 | ms | 1.59× |
| 331 | shell / rename-selected-10000/shell-workloads.json | 546.7870 | zsh | 344.7020 | ms | 1.59× |
| 332 | build-systems / native-1000-heavy-j2/leaf | 379.8695 | ninja | 248.9454 | ms | 1.53× |
| 333 | concurrency / failures/fresh | 11.8777 | go | 7.8232 | ms | 1.52× |
| 334 | concurrency / mixed-64/fresh | 102.4158 | go | 68.2898 | ms | 1.50× |
| 335 | concurrency / process-mixed/persistent | 119.1383 | go | 79.6985 | ms | 1.49× |
| 336 | build-systems / native-100-light-j1/relink | 83.5640 | make | 55.9626 | ms | 1.49× |
| 337 | template-engines / many-renders-1000/source-render | 0.0225 | liquid | 0.0151 | ms/render | 1.49× |
| 338 | template-engines / loop-100/source-render | 0.3643 | nunjucks | 0.2449 | ms/render | 1.49× |
| 339 | concurrency / process-mixed/fresh | 128.1481 | go | 86.6269 | ms | 1.48× |
| 340 | shell / copy-small-10000/shell-workloads.json | 768.2193 | zsh | 523.0843 | ms | 1.47× |
| 341 | build-systems / native-1000-light-j4/relink | 209.8247 | ninja | 143.6563 | ms | 1.46× |
| 342 | build-systems / native-10000-light-j4/leaf | 2207.7797 | ninja | 1513.2471 | ms | 1.46× |
| 343 | build-systems / native-100-light-j1/private | 109.5451 | make | 77.1818 | ms | 1.42× |
| 344 | shell / bare/immediate-exit/shell-repeated.json | 2.4251 | bash | 1.7123 | ms | 1.42× |
| 345 | build-systems / native-1000-light-j4/leaf | 269.9767 | ninja | 193.4232 | ms | 1.40× |
| 346 | build-systems / native-5000-light-j4/leaf | 1113.4117 | ninja | 800.8301 | ms | 1.39× |
| 347 | build-systems / native-1000-heavy-j4/leaf | 325.2883 | ninja | 234.9363 | ms | 1.38× |
| 348 | build-systems / native-100-light-j1/leaf | 117.9427 | make | 85.2590 | ms | 1.38× |
| 349 | shell / selected-cleanup/shell-workloads.json | 44.7825 | bash | 32.4980 | ms | 1.38× |
| 350 | build-systems / native-1000-light-j4/private | 273.8487 | ninja | 199.5892 | ms | 1.37× |
| 351 | shell / bare/trivial-command/shell-application-cold.json | 2.2155 | bash | 1.6213 | ms | 1.37× |
| 352 | shell / bare/immediate-exit/shell-application-cold.json | 2.3335 | bash | 1.7165 | ms | 1.36× |
| 353 | shell / bare/trivial-command/shell-repeated.json | 2.2018 | bash | 1.6202 | ms | 1.36× |
| 354 | build-systems / native-100-light-j2/target | 42.0032 | make | 31.1228 | ms | 1.35× |
| 355 | template-engines / many-renders-100/source-render | 0.0218 | liquid | 0.0161 | ms/render | 1.35× |
| 356 | shell / delete-selected-100000/shell-workloads.json | 2966.7268 | bash | 2218.0972 | ms | 1.34× |
| 357 | shell / processes-1/shell-workloads.json | 3.5277 | bash | 2.6390 | ms | 1.34× |
| 358 | build-systems / native-100-heavy-j1/leaf | 152.9944 | make | 114.9823 | ms | 1.33× |
| 359 | build-systems / native-100-light-j2/relink | 69.1394 | make | 52.0052 | ms | 1.33× |
| 360 | shell / processes-1000/shell-workloads.json | 910.4066 | fish | 685.0305 | ms | 1.33× |
| 361 | shell / bare/function-string/shell-application-cold.json | 2.2527 | bash | 1.7073 | ms | 1.32× |
| 362 | build-systems / native-100-light-j2/leaf | 105.1196 | make | 80.0297 | ms | 1.31× |
| 363 | shell / string-transform/shell-workloads.json | 18.9177 | zsh | 14.4408 | ms | 1.31× |
| 364 | shell / bare/function-string/shell-repeated.json | 2.2555 | bash | 1.7233 | ms | 1.31× |
| 365 | shell / delete-tree-100000/shell-workloads.json | 2847.6944 | bash | 2198.8773 | ms | 1.30× |
| 366 | build-systems / native-100-light-j4/target | 45.9992 | ninja | 35.8451 | ms | 1.28× |
| 367 | shell / bare/file-roundtrip/shell-application-cold.json | 4.8790 | bash | 3.8105 | ms | 1.28× |
| 368 | shell / processes-100/shell-workloads.json | 93.5047 | fish | 73.1391 | ms | 1.28× |
| 369 | build-systems / native-1000-light-j4/batch10 | 379.1021 | make | 296.7151 | ms | 1.28× |
| 370 | build-systems / native-100-light-j1/target | 44.7910 | make | 35.1944 | ms | 1.27× |
| 371 | build-systems / native-100-light-j2/private | 103.1534 | make | 81.3883 | ms | 1.27× |
| 372 | shell / bare/external-100/shell-repeated.json | 92.9689 | fish | 74.4041 | ms | 1.25× |
| 373 | shell / bare/external-100/shell-application-cold.json | 90.8337 | fish | 73.1076 | ms | 1.24× |
| 374 | template-engines / includes-8/source-render | 0.1629 | nunjucks | 0.1315 | ms/render | 1.24× |
| 375 | build-systems / native-100-light-j2/batch10pct | 244.9215 | make | 199.3725 | ms | 1.23× |
| 376 | build-systems / native-100-light-j2/batch10 | 240.6186 | make | 196.5331 | ms | 1.22× |
| 377 | build-systems / native-100-light-j4/leaf | 95.1283 | make | 77.7327 | ms | 1.22× |
| 378 | build-systems / native-100-light-j1/batch10pct | 409.0884 | make | 334.8027 | ms | 1.22× |
| 379 | shell / bare/file-roundtrip/shell-repeated.json | 4.9104 | bash | 4.0217 | ms | 1.22× |
| 380 | build-systems / native-100-light-j4/relink | 67.6966 | ninja | 55.7482 | ms | 1.21× |
| 381 | build-systems / native-100-light-j4/medium | 158.3530 | make | 130.6036 | ms | 1.21× |
| 382 | build-systems / native-1000-light-j4/medium | 862.0829 | make | 712.8791 | ms | 1.21× |
| 383 | shell / bare/command-capture/shell-application-cold.json | 3.5446 | bash | 2.9322 | ms | 1.21× |
| 384 | build-systems / native-100-light-j4/batch10pct | 159.4101 | make | 132.0991 | ms | 1.21× |
| 385 | build-systems / native-100-light-j4/private | 102.4991 | ninja | 85.0666 | ms | 1.20× |
| 386 | build-systems / native-100-light-j4/batch10 | 155.7611 | make | 129.7095 | ms | 1.20× |
| 387 | shell / delete-selected-10000/shell-workloads.json | 240.2922 | fish | 201.8814 | ms | 1.19× |
| 388 | build-systems / native-100-light-j1/medium | 306.0410 | make | 258.4995 | ms | 1.18× |
| 389 | shell / bare/short-pipeline/shell-repeated.json | 5.0983 | bash | 4.3345 | ms | 1.18× |
| 390 | build-systems / native-100-heavy-j2/leaf | 136.7353 | ninja | 116.6721 | ms | 1.17× |
| 391 | build-systems / native-10000-light-j4/full | 68583.8982 | make | 58543.3141 | ms | 1.17× |
| 392 | build-systems / native-10000-light-j4/global | 69193.4977 | make | 59402.0548 | ms | 1.16× |
| 393 | build-systems / native-100-light-j1/batch10 | 368.8380 | make | 316.7162 | ms | 1.16× |
| 394 | shell / pipeline-2/shell-workloads.json | 4.8866 | bash | 4.2130 | ms | 1.16× |
| 395 | shell / processes-10/shell-workloads.json | 11.7661 | bash | 10.1922 | ms | 1.15× |
| 396 | build-systems / native-100-heavy-j4/leaf | 131.2570 | make | 113.7767 | ms | 1.15× |
| 397 | build-systems / native-1000-light-j4/batch10pct | 919.9807 | ninja | 797.5039 | ms | 1.15× |
| 398 | build-systems / native-100-light-j2/medium | 205.2528 | make | 178.1147 | ms | 1.15× |
| 399 | shell / bare/short-pipeline/shell-application-cold.json | 4.8216 | bash | 4.1906 | ms | 1.15× |
| 400 | build-systems / native-5000-light-j4/global | 32085.1264 | make | 27891.9701 | ms | 1.15× |
| 401 | website-generator / 10000/application-cold | 3015.9805 | Hugo | 2623.3373 | ms/build | 1.15× |
| 402 | shell / pipeline-4/shell-workloads.json | 7.2302 | fish | 6.3260 | ms | 1.14× |
| 403 | build-systems / native-100-light-j4/generated | 788.9880 | make | 692.0228 | ms | 1.14× |
| 404 | build-systems / native-1000-light-j4/global | 6155.3327 | make | 5432.9635 | ms | 1.13× |
| 405 | build-systems / native-1000-light-j4/full | 6256.2898 | make | 5533.9211 | ms | 1.13× |
| 406 | shell / bare/command-capture/shell-repeated.json | 3.5143 | bash | 3.1195 | ms | 1.13× |
| 407 | build-systems / native-100-light-j2/generated | 1317.6604 | make | 1171.9408 | ms | 1.12× |
| 408 | shell / create-empty-1000/shell-workloads.json | 38.3239 | bash | 34.0955 | ms | 1.12× |
| 409 | shell / pipeline-8/shell-workloads.json | 11.6971 | fish | 10.4197 | ms | 1.12× |
| 410 | build-systems / native-100-light-j1/clean-rebuild | 2528.3165 | make | 2267.9140 | ms | 1.11× |
| 411 | build-systems / native-1000-light-j4/generated | 6093.1851 | make | 5471.6286 | ms | 1.11× |
| 412 | shell / create-empty-10000/shell-workloads.json | 367.9989 | bash | 330.9692 | ms | 1.11× |
| 413 | shell / create-empty-100000/shell-workloads.json | 3884.6723 | bash | 3499.2959 | ms | 1.11× |
| 414 | build-systems / native-100-light-j1/generated | 2482.6623 | make | 2240.1857 | ms | 1.11× |
| 415 | build-systems / native-5000-light-j4/full | 31739.1255 | make | 28646.4170 | ms | 1.11× |
| 416 | build-systems / native-100-light-j2/clean-rebuild | 1401.8553 | make | 1266.4258 | ms | 1.11× |
| 417 | build-systems / native-100-light-j2/full | 1372.0893 | make | 1240.8971 | ms | 1.11× |
| 418 | build-systems / native-100-light-j1/global | 2337.7085 | make | 2123.8469 | ms | 1.10× |
| 419 | build-systems / native-100-light-j4/clean-rebuild | 778.4792 | make | 711.9316 | ms | 1.09× |
| 420 | build-systems / native-100-light-j2/global | 1296.4271 | ninja | 1186.3827 | ms | 1.09× |
| 421 | build-systems / native-1000-light-j4/clean-rebuild | 6070.6235 | make | 5558.1076 | ms | 1.09× |
| 422 | shell / delete-selected-1000/shell-workloads.json | 25.0485 | bash | 23.0955 | ms | 1.08× |
| 423 | website-generator / 1000/application-cold | 303.1342 | Hugo | 279.8608 | ms/build | 1.08× |
| 424 | build-systems / native-100-light-j4/global | 700.5728 | make | 648.4609 | ms | 1.08× |
| 425 | build-systems / native-100-light-j4/full | 784.2937 | make | 729.3117 | ms | 1.08× |
| 426 | build-systems / native-100-light-j1/full | 2426.6442 | make | 2268.1541 | ms | 1.07× |
| 427 | build-systems / native-100-heavy-j4/full | 1621.6924 | make | 1520.3456 | ms | 1.07× |
| 428 | build-systems / native-100-heavy-j2/full | 3155.3187 | make | 2972.9693 | ms | 1.06× |
| 429 | build-systems / native-1000-heavy-j4/full | 15621.5800 | make | 14866.7152 | ms | 1.05× |
| 430 | build-systems / native-100-heavy-j1/full | 6268.8248 | make | 5985.9382 | ms | 1.05× |
| 431 | build-systems / native-100-heavy-j1/global | 6043.6883 | make | 5783.6280 | ms | 1.04× |
| 432 | shell / log-filter-group/shell-workloads.json | 47.6859 | fish | 45.6456 | ms | 1.04× |
| 433 | shell / source-tree-report/shell-workloads.json | 229.7415 | bash | 220.3906 | ms | 1.04× |
| 434 | template-engines / includes-4/source-render | 0.0890 | liquid | 0.0859 | ms/render | 1.04× |
| 435 | build-systems / native-1000-heavy-j2/full | 30222.0560 | make | 29326.7931 | ms | 1.03× |
| 436 | build-systems / native-100-heavy-j2/global | 3053.9714 | make | 2975.3450 | ms | 1.03× |
| 437 | build-systems / native-100-heavy-j4/global | 1583.1934 | ninja | 1552.6183 | ms | 1.02× |
| 438 | build-systems / native-1000-heavy-j1/full | 58537.5903 | make | 57589.2497 | ms | 1.02× |

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

## AI-DX: separate primary dimension

See AI-DX-SCORECARD.md/JSON for all eight suites and WEBSITE-AI-DX-WORKFLOWS.md for workflow-specific verdicts. Choose Nift for new agent-primary authored/mixed publishing; Hugo for conventional human/theme fit where appropriate. These are bounded qualitative judgments; no measured agent-productivity score. Normal Nift publish may use incremental build; forced full is a separate boundary.

## Complete separate controlled memory changes

| Suite/scenario | Baseline | PreviousKiB | FinalKiB | Change | Qualification |
|---|---|---:|---:|---:|---|
| website-generator/10000/application-cold | original | 39872.0 | 17596.0 | -55.87% | separate same-node diagnostic; quantized raw child peak, no leak claim |
| build-systems/tiny-10000-light-j4/full | original | 33312.0 | 17572.0 | -47.25% | separate controlled diagnostic, quantized memory; not aggregate tree |
| build-systems/tiny-10000-light-j4/noop | original | 21542.0 | 12576.0 | -41.62% | separate controlled diagnostic, quantized memory; not aggregate tree |
| build-systems/native-1000-heavy-j1/noop | original | 8064.0 | 6784.0 | -15.87% | separate controlled diagnostic, quantized memory; not aggregate tree |
| build-systems/tiny-10000-light-j4/full | release | 17952.0 | 17572.0 | -2.12% | separate controlled diagnostic, quantized memory; not aggregate tree |
| build-systems/native-1000-heavy-j1/noop | release | 6832.0 | 6784.0 | -0.70% | separate controlled diagnostic, quantized memory; not aggregate tree |
| scripting/sanity/function-calls/large | original | 7104.0 | 7104.0 | +0.00% | raw diagnostic peak, small quantized differences; no memory superiority or leak claim |
| task-runners/tiny-100-j4/full | original | 7936.0 | 7936.0 | +0.00% | raw quantized diagnostic; original/final equal; no leak claim |
| shell/function-calls | original | 7040.0 | 7040.0 | +0.00% | raw quantized child peak; separate from wall ranking |
| shell/string-transform | original | 6912.0 | 6912.0 | +0.00% | raw quantized child peak; separate from wall ranking |
| website-generator/10000/application-cold | release | 17468.0 | 17596.0 | +0.73% | separate same-node diagnostic; quantized raw child peak, no leak claim |
| build-systems/tiny-10000-light-j4/noop | release | 12452.0 | 12576.0 | +1.00% | separate controlled diagnostic, quantized memory; not aggregate tree |
| scripting/sanity/function-calls/small | original | 7040.0 | 7168.0 | +1.82% | raw diagnostic peak, small quantized differences; no memory superiority or leak claim |
| scripting/sanity/function-calls/large | release | 6976.0 | 7104.0 | +1.83% | raw diagnostic peak, small quantized differences; no memory superiority or leak claim |
| shell/function-calls | release | 6912.0 | 7040.0 | +1.85% | raw quantized child peak; separate from wall ranking |
| shell/string-transform | release | 6784.0 | 6912.0 | +1.89% | raw quantized child peak; separate from wall ranking |
| task-runners/tiny-100-j4/full | release | 7680.0 | 7936.0 | +3.33% | raw quantized diagnostic; original/final equal; no leak claim |
| scripting/sanity/function-calls/small | release | 6912.0 | 7168.0 | +3.70% | raw diagnostic peak, small quantized differences; no memory superiority or leak claim |

Memory values are never merged into wall rankings. Template/concurrency inherited-floor controls move16.75→80.75MiB after64MiBsupervisor allocation: excluded from runtime-memory ranking. Held10k beforeREADY timeout is censored/unavailable, not a measured wall/memory deficit. No independent throughput improvement league or numeric capability scores was established.

## Worst non-concurrency wall deficits

| Rank | Suite/scenario | Niftms | Bestpeer(ms) | Deficit | Importance |
|---:|---|---:|---|---:|---|
| 1 | scripting/arrays-strings-hash/frequency-count/large | 416.542 | luajit 3.022 | 137.83× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 2 | scripting/sanity/function-calls/large | 193.726 | luajit 1.419 | 136.53× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 3 | scripting/arrays-strings-hash/sliding-window/large | 250.116 | luajit 2.404 | 104.04× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 4 | scripting/arrays-strings-hash/map-set/large | 212.697 | luajit 2.633 | 80.77× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 5 | scripting/dynamic-programming/fibonacci/large | 141.525 | luajit 2.060 | 68.72× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 6 | scripting/arrays-strings-hash/scan/large | 82.874 | luajit 1.374 | 60.32× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 7 | scripting/sanity/loops/large | 72.592 | luajit 1.419 | 51.15× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 8 | filesystem-automation/detect-hash-2-10000/booted | 21031.620 | go 421.593 | 49.89× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 9 | filesystem-automation/detect-hash-1-10000/booted | 20165.358 | go 416.777 | 48.38× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 10 | filesystem-automation/detect-hash-3-10000/booted | 20065.571 | go 417.963 | 48.01× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 11 | scripting/graphs-trees-search/bfs/large | 799.359 | luajit 16.932 | 47.21× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 12 | filesystem-automation/detect-hash-2-10000/fresh | 19912.306 | go 423.270 | 47.04× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 13 | filesystem-automation/detect-hash-1-10000/fresh | 20196.202 | go 435.592 | 46.36× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 14 | filesystem-automation/detect-hash-3-10000/fresh | 20457.559 | go 447.401 | 45.73× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 15 | filesystem-automation/detect-hash-3-1000/booted | 2008.810 | go 44.795 | 44.84× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 16 | filesystem-automation/detect-hash-1-1000/booted | 2048.224 | go 46.897 | 43.68× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 17 | filesystem-automation/read-100000/fresh | 103416.300 | go 2406.421 | 42.98× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 18 | filesystem-automation/read-10000/booted | 10530.112 | go 249.394 | 42.22× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 19 | filesystem-automation/detect-hash-2-1000/booted | 2002.279 | go 47.727 | 41.95× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |
| 20 | filesystem-automation/read-100000/booted | 102441.259 | go 2472.142 | 41.44× | Common interpreter/bulk/render path where applicable; workflow requirements determine centrality |

## Current strengths

1. Taskrunning: lowestwall andmaximum-childRSS medians inall31officialconfigurations.
2. Filesystemnative stat90.80%,sizefilter88.58%,walk87.02%lower versusrelease, exactoutput/mutationaudits.
3. Supplementaldefaultallcorewebsite fresh27.0% andwarm44.1%lesswall thanHugo onhostA; notpooledwithofficialCPU0.
4. ValidatedNiftincremental/noop842.446ms,leaf858.452ms,target151.855ms; no matchedHugoincrementalclaim.
5. Shellstrings68.71%faster release; measured arithmetic/callspeerleads.
6. Template10ksource72.19%gain andfresh51.21%gain; sourcehotloopstill15.16xHandlebars.
7. Buildtiny10kfulltime/RSSrecovery andheavy-noop46.35%releasegain; officialheavy-noopstill12.48xNinja.

## Website final interpretation

# Supplemental website investigation — amended defaults-only cohort

This supplements the frozen official campaign; it does not replace or pool its CPU-0 results. Exact final core c14d068, normal GCC13.3/O2 CLI7dd42dce…, and Hugo0.167.0 binary8f6ddd98… are unchanged. Both new g6-standard-4 hosts expose four CPUs and EPYC7642. The user stopped future 1/2/4 scaling: original A120 checkpointed plus one completed boundary observation, and B48, remain intact under PLANv2. PLANv3 separately contains 107 new observations plus references to13 unchanged necessary replay observations. No uncollected original sample was silently classified as a failure or discarded for being slow.

## Actual defaults, all four CPUs

Five measured plus one warmup per engine/mode; Nift build-threads=-1, Hugo GOMAXPROCS unset, affinity0–3. These are the **new PLANv3 default-main** medians:

| Engine | Fresh wall ms | Warm-full wall ms | Fresh CPU ms | Warm CPU ms | Fresh child RSS KiB |
|---|---:|---:|---:|---:|---:|
| Nift |1194.468|803.743|3938.726|2718.638|17468|
| Hugo |1635.544|1436.616|3841.195|3250.870|250088|

Nift uses27.0% less fresh wall time and44.1% less warm wall time in this small cohort. Fresh observed ranges overlap (Nift1122.922–1458.843; Hugo1324.989–2667.728), with Nift faster in four of five matched rounds. Warm ranges are disjoint and Nift faster in all five rounds. No outlier was removed, and these are descriptive observations rather than a population significance claim.

CPU/wall is329.7%/338.2% for Nift fresh/warm and234.9%/226.3% for Hugo. Thus Nift's shorter fresh wall time is not evidence of lower total CPU work: its fresh CPU total is slightly higher. The observed concurrent execution is different. The separate50ms process-sampling controls show median maximum **target** OS threads5 for Nift and7 for Hugo, one target process each; the time wrapper adds one process/thread. OS threads are not equivalent to active workers. Nift resolves -1 through hardware_concurrency (observed4). Exact Hugo source uses CPU-limit-aware maxprocs.Set and a separate HUGO_NUMWORKERMULTIPLIER/runtime.NumCPU worker multiplier; unset/default is not invented `-j` behavior.

HostB's already-collected PLANv2 **default-only subset**, kept as separate host-variance context, gives fresh Nift1088.733/Hugo1460.816ms. A is9.71% slower for Nift and11.96% slower for Hugo. Both hosts favor Nift under their defaults; this is not a cross-host pooled estimate. The other previously collected scaling rows remain available but no further scaling was scheduled after the user amendment.

## Fresh versus warm: measured work and supported mechanism

New main fresh-minus-warm gaps are390.725ms for Nift and198.928ms for Hugo. In the separate GNU-time-only controls, median Nift user/system CPU is1070/2660ms fresh versus1230/1630ms warm. This points to a substantial system-side difference, not a claim that every390ms is explained by a single function. Observer values are coarse separate specimens, not substitutes for the primary C-supervised clock.

Untimed full project accounting collected on B before the scope amendment (one-worker fixture, explicitly labelled) finds initial Nift10003files/1376973bytes, versus Hugo10002files/1046878bytes. Both produce10000 correct HTML routes: Nift1317780public bytes and Hugo1327780bytes (one additional byte/page). Nift also persists10001 additional internal files totaling6584541bytes; Hugo adds a zero-byte build lock. Nift's actual info artifact records ownership/output/template/content and dependencies, not meaningless data. Source formats differ: Nift HTML plus tracked JSON/template versus Hugo Markdown/frontmatter/Goldmark pass-through. Matching semantic output is not identical parser/metadata work.

The bounded strace specimens corroborate a specific fresh/warm distinction. Nift fresh performs20002writes,10000renames and20000chmod calls; warm performs10001writes,10000utimensat and10000chmod calls. Frozen FileSystem.cpp:365–390 explains why: byte-identical retained metadata is read/checked and its mtime refreshed instead of a temporary write/atomic replacement. Public HTML is removed before every full build and must still be rendered/written. Warm nevertheless has **more** stat/open/read operations (e.g.190026stat versus140033), demonstrating why raw syscall count is not a cost model. We have not performed a core-change counterfactual that assigns an exact millisecond fraction to metadata persistence.

Strace greatly perturbs multithreaded scheduling; its summed syscall seconds include waiting and are not product latency/CPU measurements. All8 default fresh/warm syscall/software-CPU profiles pass correctness. Perf has368/265 Nift and382/394 Hugo samples, zero lost; filesystem/path/locking functions appear in kernel samples. Hugo's supplied stripped binary limits reliable userspace symbol attribution, so no unsupported Markdown/GC percentage is claimed. Hardware counters were not used or claimed; software CPU profiles succeeded without a permission workaround.

## Historical47.59% movement and frozen replay

The historical accepted10k fresh numbers are Nift3853.309/Hugo5005.257ms (Hugo/Nift1.299), not a2x Nift advantage in this particular dataset. Final official CPU-0 numbers remain Nift3015.980/Hugo2623.337ms, a1.1497 Nift/Hugo ratio. The separate Nift-only three-way2951.495ms must not be inserted into that peer ratio.

Historical and current campaign.py, benchmark.py, campaign_measure.py and measure.c hashes are identical, as verified from exact4947b42/a2890bc clones. The selected-engine replay wrapper calls those frozen fixture/clock/validation helpers and reproduces the Hugo configuration and persistent-warm cleanup policy; it is not the entire interleaved four-engine campaign. Input fingerprinting reads files outside the measured clock and can condition caches. The same prehash policy is applied to both source snapshots; this remains a supplemental control, not a literal machine-cold or full-schedule reproduction of the historical run. Hugo's binary is also identical. Necessary same-host CPU-0/Hugo GOMAXPROCS1 replay (five measured/one warmup, some exact old observations linked rather than rerun) yields historical fresh2750.020/warm2697.703ms and current fresh2644.857/warm2779.250ms. Fresh ranges2609.360–4021.924 versus2474.044–3287.218 overlap widely. That small replay difference is not evidence of a source/harness version effect: source bytes are identical.

The original host exposed EPYC7601; current official and both supplemental hosts EPYC7642. New preparation-inclusive pre/post counters show low observed steal (maximum~0.30%) and iowait (~0.23%); frequency control is not exposed and cpu.max is unavailable. Cgroup receipt reports no throttling, cpuset0–3. These observations describe the new runs, not the historical machine's timed interval. We cannot retrospectively prove which hardware, storage/cache, scheduling or host-load component caused exactly47.59% of historical movement. Software/fixture drift is unsupported; environment change is consistent with the evidence but its exact contribution is unresolved. No further timing is needed to manufacture an unwarranted causal claim.

## Boundaries and judgment

Observer controls are separate: Python outer wall includes wrapper/wait/poll completion delays up to roughly50ms, including the GNU-time-only case. Some observed controls are faster than their unobserved comparison because noise/order effects outweigh this overhead; that is not negative observer cost. Full reports and primary C timings remain distinct. The warm regime retains internal state and source paths but launches a fresh process; it is not Hugo's live development server.

The all-core default evidence strengthens Nift's case for authored, agent-maintained, mixed website/asset/procedural workflows. Its explicit ownership/dependency/lifecycle metadata can be useful even when it has a measurable persistence cost. Conventional Hugo content/theme workflows can still favor Hugo's model or an existing Hugo estate. This campaign does not provide a matched authoring-error/recovery experiment proving one product automatically safer. Full-output parity and route checks here are harness validations, not universal product-native guarantees. No core or Labs edits, selective reruns, or official evidence replacement occurred.

## Final practitioner / AI-DX choices

# Practitioner preference checkpoint — draft

These are current workflow-specific choices from audited final-candidate evidence, not a release endorsement. Final comparisons, capability findings and the complete preference matrix will be refreshed as the remaining suites close. Prior preference wording must be linked to its original review rather than reconstructed from memory.

| Category / workflow | Human + agent: current choice | Agent-primary: current choice | Evidence and remaining reservation | Status |
|---|---|---|---|---|
| Standalone general scripting with libraries | Python | Python | Current Nift frequency-count, calls and sliding-window deficits remain large. LuaJIT is the fastest measured compute peer, but the choice of Python also considers library coverage. Nift remains appropriate for hooks authored inside a Nift project. | Audited data; qualitative draft |
| Templates within a Nift publishing project | Nift | Nift | Controlled source-loop/fresh-loop/article gains retained; integrated procedural policy is useful. This is not a preference for every standalone templating application. | Audited data and version diagnostics |
| Standalone Python / Node application with prepared templates | Jinja / Handlebars, respectively | Jinja / Handlebars, respectively | Match the host application; Nift public prepared-AST reuse remains absent in the frozen public-API matrix, and the 10k source loop is 15.16× behind Handlebars. | Audited data; qualitative draft |
| High-fan-out concurrency and tiny-task throughput | Go | Go | Persistent 10k tiny tasks are 1,740.60× slower in Nift. Controlled queue gain69.48% coexists with retained-runtime slowdown8.07×; this current deficit does not establish a new regression. Coarse orchestration in an existing Nift project is a different workload. | Official and diagnostic audits complete |
| Website: exact fresh10k objective / warm-full objective | Hugo / Nift, respectively | Hugo / Nift, respectively | Exact official fresh3015.980/2623.337ms favors Hugo; warm2613.877/2723.813 favors Nift. Withdraw categorical plain-content-site switch: minimal-page throughput does not choose a platform without project requirements. | See WEBSITE-RATIO-RECONCILIATION.md |
| Native builds: bespoke/mixed authored / conventional C++ | Nift / CMake or Meson→Ninja | Nift / CMake or Meson→Ninja | Audited contracts and explicit policy favor bespoke Nift; native integration favors established generators. Heavy1k no-op12.48xNinja; controlled recovery pending. | Official audit complete; diagnostics pending |
| Filesystem: standalone policy / bulk throughput / bounded existing Nift project | Python / Go / Nift | Python / Go / Nift | Audited exact mutations and retained native gains; portable hash detection still49.89xGo. AI-DX explicit boundaries help project work, not proof of transactional recovery. | Official+diagnostic audit complete |
| Interactive shells | Pending complete audit | Pending complete audit | Startup, RC, strings, calls, files and pipelines have distinct boundaries. | Full collection active |
| Bespoke authored / mixed-project task running | Nift | Nift | Lowest wall and maximum-child RSS in all31 configurations. Choose Turbo/Nx for required result restoration/platform integration beyond the frozen adapter. | Official and diagnostic audits complete |

Useful explicitness includes declared inputs, ordering, invalidation, lifecycle, action identity and artifact ownership. Redundant synchronization without additional meaning is a separate disadvantage. Canonical machine-readable contracts plus concise authoring helpers are preferable to deleting semantics solely to reduce syntax.

Task runners: for human-plus-agent and agent-primary bespoke authored or mixed-project workflows, choose Nift. All31 frozen configurations have lower wall and maximum-child RSS medians. Choose Turbo/Nx when specifically requiring cache restoration/platform integration or adapter-unsupported contracts; incremental skipping is not restoration. These are frozen-adapter observations, not blanket absence claims about new core APIs. Same-node tiny100/full is −2.52% versus release and +4.51% versus original with overlapping ranges.

Shell current choices (human-plus-agent / agent-primary): Nift / Nift for bespoke mixed workflows owned by Nift; Bash/Zsh / Bash/Zsh for compatibility-driven shell work; Nu / Nu when structured pipeline requirements dominate; Fish / Fish when interactive ergonomics dominate. These workflow judgments coexist with Nift arithmetic/call leads and traversal/metadata/concatenation deficits; matched version recovery remains pending.

## AI-DX is a primary dimension

See WEBSITE-AI-DX-WORKFLOWS.md and AI-DX-SCORECARD.md/JSON. New agent-primary authored websites and mixed procedural publishing: Nift/Nift. Conventional human content/theme sites: Hugo when those conventions satisfy requirements, rather than on a fresh10k speed result alone. Existing Hugo estates can reasonably remain Hugo. These are conditional design judgments, not measured agent productivity. Incremental/target parity is harness-validated for tested Nift scenarios; structured harness output is not product-native build feedback. All eight suite closeouts must include this axis.

# AI-DX / agent-maintainability — primary campaign axis

This is independent of clean-build speed, steady-state latency, memory, correctness and ecosystem fit. Familiarity to a human is not equivalent to safety for an agent. More explicit structure is valuable when it separates inputs, output ownership, execution order, invalidation and lifecycle; synchronization without additional semantics remains a liability. Helpers should reduce repetition while preserving these contracts.

No numerical productivity or safety score is assigned: this campaign did not measure autonomous authoring success, repair rate or token/time costs. Record demonstrated affordances, evidence gaps and conditional judgments. Never relabel harness JSON or output validation as product-native structured feedback or automatic safety guarantees.

## Recurring checklist for each suite

Evaluate project structure; declared inputs/dependencies; artifact ownership; targeted changes; incremental semantics; rebuild explanation; structured feedback; mixed content/assets/helpers; hidden conventions; failure/debug clarity; autonomous edit safety; intended-output validation; partial-state recovery. For every claim mark observed test, source/documented capability, qualitative inference, or not evaluated. An unavailable probe is not proof a competitor lacks a capability.

## All eight suites

| Suite | Conditional direct choice | Evidence | Remaining AI-DX qualification |
|---|---|---|---|
| website-generator | Nift for agent-owned explicit/mixed projects; Hugo for conventional human/theme-led sites | Nift incremental/target output parity checked by harness; explicit tracked title/template/name | No matched Hugo incremental/recovery or comparative authoring trial; build JSON feedback not established (qualitative preference with audited workflow evidence) |
| task-runners | Nift for bespoke authored/agent-primary; Turbo/Nx for specific restoration/platform requirements | 31 wall and maximum-child RSS leads plus action/output/failure checks; explicit contracts | Incremental skip is not cache restoration; frozen adapter limits do not establish all core API limits (audited timing/contracts; qualitative AI-DX) |
| build-systems | Pending full audit; assess explicit order, invalidation, ownership independently | Frozen correctness preflight; current full collection active | No final AI-DX winner before native depfile/toolchain/recovery evidence reconciliation (provisional) |
| filesystem-automation | Pending full audit; prefer bounded native operations when evidence supports them | Frozen fixture/output mutation gates; official collection active | Path/error/partial mutation recovery and helper dependence require explicit review (provisional) |
| scripting | Python standalone libraries; Nift for project-owned .f hooks | Calls recovery audited; programmable integrated policy | Library coverage and large compute deficits matter; no agent-edit benchmark (audited performance; qualitative AI-DX) |
| shell | Nift for bespoke mixed project; Bash/Zsh compatibility; Nu structured pipelines; Fish interactive ergonomics | RC state, output and workload oracles audited; calls/strings recovery | Harness validation not proof arbitrary shell edits are safe; compatibility separate from familiarity (audited boundaries; qualitative AI-DX) |
| template-engines | Nift within Nift projects; Jinja/Handlebars matching host application/prepared API needs | Source/fresh boundaries and output digests audited | Prepared API absent in frozen Nift public matrix; no comparative template-edit/recovery trial (audited render contracts; qualitative AI-DX) |
| concurrency | Go for standalone high fan-out; Nift for bounded existing-project orchestration | Output/queue oracles and retained-runtime diagnostics audited | Explicitness does not cancel >1000x tiny-task gaps or retained runtime slowdown; no autonomous race-repair trial (audited runtime; qualitative AI-DX) |

## Reporting and priority policy

Each final suite review must state human-plus-agent and agent-primary choices and why AI-DX does or does not change the performance-only preference. Keep outputless/environment/cache/depfile/recovery capabilities explicit rather than inferred from timed adapters. Do not trade correctness for speed or award Nift a blanket win for programmable syntax. Large runtime gaps can override an authoring advantage for latency-sensitive or high-fanout jobs.

Remaining build/filesystem reviews must fill this checklist on closeout. Prioritize machine-checkable artifact/input/order/invalidation contracts, bounded mutations, actionable diagnostics and recovery alongside speed; do not collapse semantics to minimize line count. Existing raw evidence stays immutable and no new benchmark methodology is introduced.

Filesystem closeout: choose Python for standalone policy, Go for heavy bulk, Nift for bounded existing-project operations in both authoring modes. Full official+diagnostic audits passed; explicit contracts help reasoning, but arbitrary partial rollback/autonomous repair remain untested. See canonical filesystem AI-DX-ASSESSMENT.json/PRACTITIONER-DRAFT.md.

## Product priorities

1. New/bounded residuals: trackheavy-noop original-relativewall/CPU+11.90%/11.85%, shellcalls+3.17%release, scriptinglargecalls+2.59%, websiteCPU0fresh+2.78%, schedule1k+8.70%; do not infer sharedcauses. Noneidentifiedasmaterialreleaseblocker.
2. Oldinterpreter/collections weaknesses: frequency137.83x,calls136.53x,sliding104.04x,portablehash49.89x; commonworkflowscanchangechoice.
3. Nativebuildintegration andno-opmetadata/pathcosts: heavy-noop12.48xNinja, preserveexplicitorder/invalidation/ownership; improvecompiler/toolchainintegration byverifiedgaps.
4. Templatehotreuse: prepared-templatepublicAPI/loopexecution15.16xbehinddespite72%gain.
5. Concurrencytiny/scheduling>1000x,retainedruntime8.07xtrajectory andheldmemorycensoring: throughputimportantforstandaloneGochoice, distinguishproductcentralityfromgapmagnitude.
6. Taskcache/env/outputless/ensure/worker/graph/recoverycapabilities: frozenadaptercoverageisnotproofallnewcoreAPIsabsent; verifycurrentpubliccontracts beforedeclaringgaps.
7. AI-DXco-primary: inspectableinputs/outputownership/order/invalidation, actionableexplanations/structuredfeedback/recovery; nofabricatedagentproductivityscores.

## Closeout / publication boundary

Finalevidencepush andhostlifecycle receipts appended ascompleted. Official/supplementrawseries immutable. Labsrefresh authorizedconditionally byRELEASE-GATE.json, sourcebeforepublic, graph/table/link/storage/responsive/livebytechecks, preservehistoricalseries/unrelatedreports. No v4.12tag,release,packagesordownloadpublicationauthorized.

## Verified measurement closeout

Official hosts:0remaining. Supplement hosts:0remaining. All10CLIabsences/API404 verified with individual lifecycle receipts. Original sharedSSH/config/privatecloudstate and supplementalindependentaccess/state removed; credentialsourceunchanged. Original finalcleanupreceipt lifecycle/final-access-cleanup.json; supplement counterpart campaigns/20261015-website-supplement-c14d068/lifecycle/final-access-cleanup.json. Finalmeasurement evidence19e3901; laterlifecycle/publicationreceiptcommits append independently.

## Separate current memory deficits — complete eligible cohort

KiB maximum/waited-child high-water, not aggregate process tree; template/concurrency/filesystem inherited-floor raw excluded; missing PTY rows excluded; external helper baseline excluded.

| Rank | Suite/scenario | NiftKiB | BestpeerKiB | Multiple |
|---:|---|---:|---|---:|
| 1 | scripting/arrays-strings-hash/sort-index/large | 142302.0 | luajit 3328.0 | 42.76× |
| 2 | shell/delete-tree-100000 | 108592.0 | bash 3584.0 | 30.30× |
| 3 | shell/create-small-100000 | 112176.0 | bash 3712.0 | 30.22× |
| 4 | shell/delete-selected-100000 | 102320.0 | bash 3584.0 | 28.55× |
| 5 | shell/create-empty-100000 | 45124.0 | bash 3712.0 | 12.16× |
| 6 | scripting/arrays-strings-hash/map-set/large | 30822.0 | luajit 3456.0 | 8.92× |
| 7 | scripting/arrays-strings-hash/sliding-window/large | 26140.0 | luajit 3392.0 | 7.71× |
| 8 | scripting/graphs-trees-search/bfs/large | 33558.0 | luajit 5760.0 | 5.83× |
| 9 | shell/traverse-100000 | 123136.0 | nu 27344.0 | 4.50× |
| 10 | shell/delete-selected-10000 | 15948.0 | bash 3584.0 | 4.45× |
| 11 | scripting/filesystem/traverse/large | 9216.0 | lua54 2560.0 | 3.60× |
| 12 | build-systems/tiny-100-light-j4/batch10 | 7680.0 | make 2176.0 | 3.53× |
| 13 | build-systems/tiny-100-light-j4/leaf | 7680.0 | make 2176.0 | 3.53× |
| 14 | scripting/structured-data/json-parse/large | 125560.0 | python 35828.0 | 3.50× |
| 15 | scripting/structured-data/json-traverse/large | 125560.0 | python 35830.0 | 3.50× |
| 16 | build-systems/tiny-100-light-j1/batch10 | 7552.0 | make 2176.0 | 3.47× |
| 17 | build-systems/tiny-100-light-j1/leaf | 7552.0 | make 2176.0 | 3.47× |
| 18 | build-systems/tiny-100-light-j2/leaf | 7552.0 | make 2176.0 | 3.47× |
| 19 | build-systems/tiny-100-light-j2/batch10 | 7424.0 | make 2176.0 | 3.41× |
| 20 | scripting/arrays-strings-hash/sort-index/small | 8160.0 | lua54 2432.0 | 3.36× |
| 21 | build-systems/tiny-100-light-j4/full | 7680.0 | make 2304.0 | 3.33× |
| 22 | shell/concat-small-10000 | 11790.0 | bash 3584.0 | 3.29× |
| 23 | build-systems/tiny-100-light-j1/full | 7552.0 | make 2304.0 | 3.28× |
| 24 | build-systems/tiny-100-light-j2/full | 7552.0 | make 2304.0 | 3.28× |
| 25 | scripting/arrays-strings-hash/sliding-window/small | 7296.0 | lua54 2432.0 | 3.00× |
| 26 | scripting/arrays-strings-hash/map-set/small | 7168.0 | lua54 2432.0 | 2.95× |
| 27 | build-systems/tiny-1000-light-j4/leaf | 8192.0 | make 2816.0 | 2.91× |
| 28 | scripting/graphs-trees-search/bfs/small | 7424.0 | lua54 2560.0 | 2.90× |
| 29 | scripting/sanity/loops/small | 6976.0 | lua54 2432.0 | 2.87× |
| 30 | scripting/sanity/function-calls/small | 6976.0 | lua54 2432.0 | 2.87× |
| 31 | scripting/sanity/function-calls/large | 6976.0 | lua54 2432.0 | 2.87× |
| 32 | scripting/arrays-strings-hash/frequency-count/small | 6976.0 | lua54 2432.0 | 2.87× |
| 33 | scripting/dynamic-programming/fibonacci/small | 6976.0 | lua54 2432.0 | 2.87× |
| 34 | build-systems/tiny-1000-light-j4/batch10 | 8064.0 | make 2816.0 | 2.86× |
| 35 | scripting/sanity/output/large | 6592.0 | lua54 2304.0 | 2.86× |
| 36 | scripting/structured-data/json-transform/large | 96610.0 | python 33792.0 | 2.86× |
| 37 | scripting/sanity/loops/large | 6912.0 | lua54 2432.0 | 2.84× |
| 38 | scripting/arrays-strings-hash/scan/small | 6912.0 | lua54 2432.0 | 2.84× |
| 39 | scripting/arrays-strings-hash/scan/large | 6912.0 | lua54 2432.0 | 2.84× |
| 40 | scripting/arrays-strings-hash/frequency-count/large | 6912.0 | lua54 2432.0 | 2.84× |
| 41 | scripting/dynamic-programming/fibonacci/large | 6912.0 | lua54 2432.0 | 2.84× |
| 42 | shell/create-empty-10000 | 10056.0 | bash 3584.0 | 2.81× |
| 43 | shell/copy-small-10000 | 10056.0 | bash 3584.0 | 2.81× |
| 44 | shell/rename-selected-10000 | 10054.0 | bash 3584.0 | 2.81× |
| 45 | scripting/sanity/output/small | 6400.0 | lua54 2304.0 | 2.78× |
| 46 | build-systems/tiny-100-light-j4/noop | 6016.0 | make 2176.0 | 2.76× |
| 47 | build-systems/tiny-100-light-j1/noop | 5888.0 | make 2176.0 | 2.71× |
| 48 | build-systems/tiny-100-light-j2/noop | 5888.0 | make 2176.0 | 2.71× |
| 49 | shell/metadata-10000 | 10052.0 | bash 3840.0 | 2.62× |
| 50 | build-systems/native-100-heavy-j1/noop | 6016.0 | make 2304.0 | 2.61× |
| 51 | build-systems/native-100-heavy-j2/noop | 6016.0 | make 2304.0 | 2.61× |
| 52 | build-systems/native-100-heavy-j4/noop | 6016.0 | make 2304.0 | 2.61× |
| 53 | build-systems/native-100-light-j1/noop | 6016.0 | make 2304.0 | 2.61× |
| 54 | build-systems/native-100-light-j2/noop | 6016.0 | make 2304.0 | 2.61× |
| 55 | build-systems/native-100-light-j4/noop | 6016.0 | make 2304.0 | 2.61× |
| 56 | scripting/sanity/noop/small | 6016.0 | lua54 2304.0 | 2.61× |
| 57 | scripting/sanity/noop/large | 5888.0 | lua54 2304.0 | 2.56× |
| 58 | scripting/filesystem/traverse/small | 6528.0 | lua54 2560.0 | 2.55× |
| 59 | build-systems/tiny-1000-light-j4/noop | 6400.0 | make 2816.0 | 2.27× |
| 60 | shell/delete-selected-1000 | 7540.0 | bash 3584.0 | 2.10× |
| 61 | build-systems/tiny-1000-light-j4/full | 8448.0 | make 4224.0 | 2.00× |
| 62 | shell/processes-1 | 7040.0 | bash 3520.0 | 2.00× |
| 63 | shell/bare/external-100 | 7040.0 | bash 3584.0 | 1.96× |
| 64 | shell/bare/external-100 | 7040.0 | bash 3584.0 | 1.96× |
| 65 | shell/processes-10 | 7040.0 | bash 3584.0 | 1.96× |
| 66 | shell/processes-100 | 7040.0 | bash 3584.0 | 1.96× |
| 67 | shell/processes-1000 | 7040.0 | bash 3584.0 | 1.96× |
| 68 | shell/bare/short-pipeline | 6912.0 | bash 3520.0 | 1.96× |
| 69 | shell/function-calls | 6912.0 | bash 3584.0 | 1.93× |
| 70 | shell/bare/file-roundtrip | 6784.0 | bash 3520.0 | 1.93× |
| 71 | shell/bare/native-sum | 6784.0 | bash 3520.0 | 1.93× |
| 72 | shell/pipeline-8 | 6784.0 | bash 3520.0 | 1.93× |
| 73 | shell/selected-cleanup | 6880.0 | bash 3584.0 | 1.92× |
| 74 | shell/bare/command-capture | 6848.0 | bash 3584.0 | 1.91× |
| 75 | shell/create-empty-1000 | 6800.0 | bash 3584.0 | 1.90× |
| 76 | shell/bare/command-capture | 6784.0 | bash 3584.0 | 1.89× |
| 77 | shell/bare/file-roundtrip | 6784.0 | bash 3584.0 | 1.89× |
| 78 | shell/bare/native-sum | 6784.0 | bash 3584.0 | 1.89× |
| 79 | shell/bare/short-pipeline | 6784.0 | bash 3584.0 | 1.89× |
| 80 | shell/pipeline-2 | 6784.0 | bash 3584.0 | 1.89× |
| 81 | shell/pipeline-4 | 6784.0 | bash 3584.0 | 1.89× |
| 82 | shell/arithmetic | 6784.0 | bash 3584.0 | 1.89× |
| 83 | shell/fibonacci-mod | 6784.0 | bash 3584.0 | 1.89× |
| 84 | shell/string-transform | 6784.0 | bash 3648.0 | 1.86× |
| 85 | shell/bare/function-string | 6656.0 | bash 3584.0 | 1.86× |
| 86 | shell/bare/function-string | 6656.0 | bash 3584.0 | 1.86× |
| 87 | shell/bare/trivial-command | 6144.0 | bash 3456.0 | 1.78× |
| 88 | shell/bare/trivial-command | 6016.0 | bash 3456.0 | 1.74× |
| 89 | shell/source-tree-report | 6784.0 | bash 3968.0 | 1.71× |
| 90 | build-systems/native-1000-heavy-j4/noop | 6912.0 | make 4096.0 | 1.69× |
| 91 | build-systems/native-1000-light-j4/noop | 6912.0 | make 4096.0 | 1.69× |
| 92 | build-systems/native-1000-heavy-j1/noop | 6784.0 | make 4096.0 | 1.66× |
| 93 | build-systems/native-1000-heavy-j2/noop | 6784.0 | make 4096.0 | 1.66× |
| 94 | shell/bare/immediate-exit | 5376.0 | bash 3456.0 | 1.56× |
| 95 | shell/bare/immediate-exit | 5376.0 | bash 3456.0 | 1.56× |
| 96 | build-systems/tiny-10000-light-j4/leaf | 14628.0 | make 9684.0 | 1.51× |
| 97 | build-systems/tiny-10000-light-j4/batch10 | 14500.0 | make 9684.0 | 1.50× |
| 98 | build-systems/tiny-10000-light-j4/noop | 12836.0 | make 9684.0 | 1.33× |
| 99 | shell/log-filter-group | 6848.0 | bash 5888.0 | 1.16× |
| 100 | build-systems/native-5000-light-j4/noop | 12620.0 | make 11904.0 | 1.06× |
| 101 | build-systems/native-100-heavy-j2/leaf | 27392.0 | make 27264.0 | 1.00× |
| 102 | build-systems/native-100-light-j4/leaf | 21824.0 | make 21760.0 | 1.00× |
| 103 | build-systems/native-100-light-j4/target | 21824.0 | make 21760.0 | 1.00× |
| 104 | build-systems/native-1000-heavy-j1/full | 56668.0 | make 56536.0 | 1.00× |
| 105 | build-systems/native-100-light-j4/clean-rebuild | 27520.0 | ninja 27456.0 | 1.00× |
| 106 | build-systems/native-100-light-j2/clean-rebuild | 27584.0 | make 27520.0 | 1.00× |
| 107 | build-systems/native-1000-heavy-j4/full | 56668.0 | make 56540.0 | 1.00× |
| 108 | build-systems/native-1000-heavy-j1/leaf | 56664.0 | make 56540.0 | 1.00× |
| 109 | build-systems/native-1000-light-j4/medium | 56664.0 | ninja 56540.0 | 1.00× |
| 110 | build-systems/native-1000-light-j4/batch10 | 56608.0 | make 56540.0 | 1.00× |
| 111 | build-systems/native-5000-light-j4/global | 245504.0 | make 245372.0 | 1.00× |
| 112 | build-systems/native-5000-light-j4/full | 245500.0 | make 245376.0 | 1.00× |
| 113 | build-systems/native-5000-light-j4/leaf | 245438.0 | ninja 245376.0 | 1.00× |
| 114 | build-systems/native-1000-heavy-j2/leaf | 56540.0 | make 56536.0 | 1.00× |
| 115 | build-systems/native-1000-light-j4/generated | 56540.0 | make 56536.0 | 1.00× |
| 116 | build-systems/native-1000-light-j4/batch10pct | 56668.0 | make 56664.0 | 1.00× |
| 117 | build-systems/native-10000-light-j4/full | 481136.0 | make 481132.0 | 1.00× |

## Final verified publication and lifecycle

RELEASE-READY. I recommend releasing v4.12 exactc14d068. Officialhosts0; supplementhosts0. Original8 andsupplement2 teardownreceipts verifyCLIabsence/API404 andtemporarySSH/knownhost/config/statecleanup.

Labs source12e9ff2 pushedbefore public7999786; https://lab.nift.dev/benchmarks/ andall8reportHTML bytes matchlocalSHA256. Fullbuild,34HTML/868localrefs,graph/data checks,1440/390/320 browserchecks passed; taskhashoverflowfixed. Storage10,359,588bytes belowunchanged11MiBguard. Historicalgraphs linkedimmutably tooldpublic3225ebc andPNGdownloads toevidenceeeb3afe; priorrawseriesimmutable andunrelatedreportsunchanged. NoNifttag/release/packagescreated.

### Individual lifecycle receipts

- build-systems 108162775: CLI absent=True, API=404, known-host cleanup=True; campaigns/20261015-v4120-final-c14d068/lifecycle/build-systems/teardown.json.
- concurrency 108162758: CLI absent=True, API=404, known-host cleanup=True; campaigns/20261015-v4120-final-c14d068/lifecycle/concurrency/teardown.json.
- filesystem-automation 108162735: CLI absent=True, API=404, known-host cleanup=True; campaigns/20261015-v4120-final-c14d068/lifecycle/filesystem-automation/teardown.json.
- scripting-benchmark 108162749: CLI absent=True, API=404, known-host cleanup=True; campaigns/20261015-v4120-final-c14d068/lifecycle/scripting-benchmark/teardown.json.
- shell-benchmark 108162738: CLI absent=True, API=404, known-host cleanup=True; campaigns/20261015-v4120-final-c14d068/lifecycle/shell-benchmark/teardown.json.
- task-runners 108162743: CLI absent=True, API=404, known-host cleanup=True; campaigns/20261015-v4120-final-c14d068/lifecycle/task-runners/teardown.json.
- template-engines 108162740: CLI absent=True, API=404, known-host cleanup=True; campaigns/20261015-v4120-final-c14d068/lifecycle/template-engines/teardown.json.
- website-generator-benchmark 108162733: CLI absent=True, API=404, known-host cleanup=True; campaigns/20261015-v4120-final-c14d068/lifecycle/website-generator-benchmark/teardown.json.
- website-diagnostic-a 108192961: CLI absent=True, API=404, known-host cleanup=True; campaigns/20261015-website-supplement-c14d068/lifecycle/website-diagnostic-a/teardown.json.
- website-diagnostic-b 108192966: CLI absent=True, API=404, known-host cleanup=True; campaigns/20261015-website-supplement-c14d068/lifecycle/website-diagnostic-b/teardown.json.

### Separate controlled build CPU changes

| Scenario | Baseline | PreviousCPUms | FinalCPUms | Change |
|---|---|---:|---:|---:|
| native/1000/noop | original | 190.742 | 213.345 | +11.85% |
| tiny/10000/noop | original | 1692.026 | 1736.128 | +2.61% |
| tiny/10000/full | release | 51727.417 | 46060.919 | -10.95% |
| tiny/10000/noop | release | 2309.891 | 1736.128 | -24.84% |
| tiny/10000/full | original | 62165.804 | 46060.919 | -25.91% |
| native/1000/noop | release | 402.150 | 213.345 | -46.95% |
