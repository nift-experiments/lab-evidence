# Eight-suite diagnostic closeout

Candidate `7f7e487c47a87e871dfef53345e2b71288008bff` remains **not release-approved**. All eight official suites passed independent audits; all required diagnostics are retained. Labs was not changed or published.

## Worst same-node regressions

There are17 numerical increases, not20; none are invented. Same-node correctness and measurement direction are established, but confidence differs. Call, website, shell-string and tiny-full-build specimens have particularly strong nonoverlap evidence. Smaller increases remain descriptive.

| Rank | Benchmark / scenario | Old ms | Candidate ms | Increase | Evidence confidence |
|---:|---|---:|---:|---:|---|
| 1 | scripting / sanity/function-calls/large | 228.284 | 561.026 | 145.76% | 10/10 pairs and disjoint ranges |
| 2 | shell / function-calls | 22.086 | 48.519 | 119.68% | 10/10 slower pairs; disjoint ranges |
| 3 | scripting / sanity/function-calls/small | 6.080 | 10.069 | 65.63% | 10/10 pairs and disjoint ranges |
| 4 | website-generator / application-cold / 10000pages targeted adjacent paired versions | 2561.445 | 3542.237 | 38.29% | small paired diagnostic; descriptive |
| 5 | scripting / arrays-strings-hash/frequency-count/small | 8.303 | 10.659 | 28.37% | descriptive median; significance not established |
| 6 | build-systems / tiny/10000/light/4/full | 13743.692 | 16663.644 | 21.25% | disjoint ranges |
| 7 | scripting / graphs-trees-search/bfs/small | 12.723 | 15.270 | 20.02% | descriptive median; significance not established |
| 8 | scripting / structured-data/json-transform/large | 586.317 | 703.648 | 20.01% | descriptive median; significance not established |
| 9 | scripting / arrays-strings-hash/frequency-count/large | 473.156 | 567.263 | 19.89% | descriptive median; significance not established |
| 10 | scripting / graphs-trees-search/bfs/large | 844.177 | 999.076 | 18.35% | descriptive median; significance not established |
| 11 | shell / string-transform | 60.516 | 69.788 | 15.32% | 10/10 slower pairs; disjoint ranges |
| 12 | scripting / sanity/noop/small | 3.293 | 3.621 | 9.96% | descriptive median; significance not established |
| 13 | scripting / structured-data/json-transform/small | 9.078 | 9.956 | 9.66% | descriptive median; significance not established |
| 14 | scripting / structured-data/json-parse/large | 245.533 | 262.571 | 6.94% | descriptive median; significance not established |
| 15 | scripting / dynamic-programming/fibonacci/small | 3.786 | 3.908 | 3.24% | descriptive median; significance not established |
| 16 | scripting / filesystem/traverse/large | 38.742 | 39.603 | 2.22% | descriptive median; significance not established |
| 17 | scripting / filesystem/traverse/small | 4.989 | 5.072 | 1.66% | descriptive median; significance not established |

## Best same-node improvements — top20

Small paired controls are descriptive, not population significance tests. Task historical gains are excluded from this ranking.

| Rank | Benchmark / scenario | Old ms | Candidate ms | Improvement |
|---:|---|---:|---:|---:|
| 1 | filesystem-automation / stat-10000 | 3049.752 | 274.114 | 91.01% |
| 2 | filesystem-automation / filter-size-10000 | 2353.088 | 335.618 | 85.74% |
| 3 | filesystem-automation / walk-10000 | 1295.283 | 187.531 | 85.52% |
| 4 | template-engines / loop-10000 / source-render | 119.508 | 33.683 | 71.82% |
| 5 | concurrency / queue-100000-4-4 / fresh runtime/readiness request | 36066.073 | 11887.314 | 67.04% |
| 6 | template-engines / loop-10000 / fresh | 168.238 | 75.854 | 54.91% |
| 7 | build-systems / native/1000/heavy/1/noop | 335.381 | 176.276 | 47.44% |
| 8 | template-engines / article / source-render | 0.430 | 0.266 | 38.05% |
| 9 | scripting / arrays-strings-hash/sort-index/large | 1088.855 | 754.437 | 30.71% |
| 10 | build-systems / tiny/10000/light/4/noop | 640.435 | 539.484 | 15.76% |
| 11 | scripting / arrays-strings-hash/scan/large | 110.635 | 93.988 | 15.05% |
| 12 | website-generator / incremental/no-op / 10000pages targeted adjacent paired versions | 932.931 | 813.536 | 12.80% |
| 13 | website-generator / warm-full / 10000pages targeted adjacent paired versions | 3176.786 | 2776.981 | 12.59% |
| 14 | scripting / structured-data/json-parse/small | 6.812 | 5.979 | 12.23% |
| 15 | website-generator / incremental/one-page / 10000pages targeted adjacent paired versions | 920.908 | 821.310 | 10.82% |
| 16 | scripting / dynamic-programming/fibonacci/large | 182.107 | 164.111 | 9.88% |
| 17 | scripting / arrays-strings-hash/sliding-window/large | 339.164 | 307.064 | 9.46% |
| 18 | scripting / arrays-strings-hash/sort-index/small | 10.823 | 9.843 | 9.06% |
| 19 | scripting / arrays-strings-hash/scan/small | 4.901 | 4.541 | 7.34% |
| 20 | scripting / arrays-strings-hash/map-set/large | 295.962 | 278.617 | 5.86% |

## Worst current competitive deficits — top20

Official candidate/peer cohort values; do not substitute diagnostic old/new values. Whole-workload boundaries differ and remain visible.

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

The full17/29/520 rankings and463 historical cross-node trends are in DIAGNOSTIC-LEAGUE-TABLES.md and its JSON. Historical results are separate from controlled version comparisons.

## Improved substantially but still behind

| Scenario | Same-node improvement | Current official deficit |
|---|---:|---:|
| Filesystem stat10k | 91.01% | 3.87×Bun |
| Filesystem walk10k | 85.52% | 6.98×Bun |
| Concurrency queue100k | 67.04% | 208.76×Bun |
| Template10k source-render | 71.82% | 15.35×Handlebars |
| Build native1k heavy no-op | 47.44% | 10.64×Ninja |

## Memory and throughput

Stable1k-held-task READY memory is143.625MiB vsGo5.375MiB(26.72×), essentially unchanged from143.5MiB. Template/filesystem inherited supervisor-floor RSS stays unranked. Valid maximum-child RSS rows for build/task are separately ranked in CROSS-BENCHMARK-MEMORY-GAPS.json; none are aggregate process-tree claims.

Controlled build tiny10kfull maximum-childRSS increases19492→31780KiB(+63.04%); tiny10kno-op+62.15%, native1kheavy no-op+15.09%. Faster no-op time therefore has a memory tradeoff. Website fresh-full peakRSS also increases in its separate same-node diagnostic.

Filesystem operational files/sec and sourceMiB/sec deficits are separately retained in CROSS-BENCHMARK-THROUGHPUT-GAPS.json. They derive from accepted medians/workload quantities, not independent disk-bandwidth measurements. No global throughput score is computed.

## Capabilities

Newly verified changed behavior: the retained exactly-once inline/bound filesystem reproducer passes. This is a corrected specimen, not a new public API or universal proof of correctness. No other new public capability was established in this refresh.

Major gaps remain: nativeSHA256/statmtime/recursive-directory removal; public prepared-template artifacts; native channels/condition-variable and cancellation APIs; outputless tracked task nodes, declared environment invalidation, cached result restoration, ensure-targeting, CLI worker override and complete structured graph query/explain. Native compiler-dependency ingestion and rich multi-output/toolchain/IDE handling are not established by the external benchmark adapter. Existing configured workers, repair and future error propagation remain useful. See CROSS-BENCHMARK-CAPABILITIES.json.

## Direct practitioner choices

| Category | Human + agent | Agent-primary | Preference change |
|---|---|---|---|
| Scripting | Python for new general data/automation; Nift bounded existing policy | Same scope choices | No broad reversal; call regression reinforces general-runtime limits |
| Shell | Bash/Zsh interactive/compatibility; Nift project-owned policy | Nift owned mixed policy; Bash/Zsh compatibility | Scope unchanged; call/string regressions now confirmed |
| Task running | Nift authored DAG; Turbo/Nx required cache/discovery | Same | Nift preference retained and confidence strengthened |
| Build systems | Nift procedural/mixed; Make tiny conventional; CMake/Meson→Ninja conventional C++ | Same | No architectural need for Ninja in mature counterfactual, but present gaps/overhead remain |
| Templates | Nift native composition; native/prepared peer for standalone hot service | Nift authored generation; prepared peer high-volume hot rendering | Loop gains strengthen confidence, do not supply prepared reuse |
| Concurrency | Go standalone/high-fanout; Nift bounded owned jobs | Same | Queue gain does not remove scheduling/wait/memory/reuse blockers |
| Website | Hugo plain content; Nift existing/mixed procedural project | Nift mixed authored project; Hugo plain content | Fresh ranking reverses prior corpus result; no universal Nift choice |
| Filesystem | Nift bounded existing policy; Go/Bun/Node bulk processing | Same | Huge metadata gains, bulk policy still blocks general preference |

Prior broad scope preferences are retained where explicitly supported by reviews; a previous universal website preference was not established. Changes in confidence and measured competitive position are distinguished from changes in tool choice.

## Core priorities and release blockers

1. Fix call-path regression, corroborated by scripting and shell. Investigate argument parsing/classification, snapshots and allocation churn while preserving exactly-once/ownership/provenance.
2. Fix fresh website-build regression38.29%; investigate extra path/filesystem probes without assuming the call cause.
3. Investigate tiny10k full-build regression21.25% and63.04%RSS growth; determine metadata/action-dispatch cause and acceptable memory/time tradeoffs.
4. Resolve retained-runtime state/time growth; the prior also degrades, so this is an old persistent weakness.
5. Reduce lightweight task creation/retention cost and held-task memory.
6. Improve scalar/value execution; preserve real parallel scaling and sorting gains.
7. Provide nonblocking waits and clearer channels/cancellation/lifetime contracts.
8. Address bulk filesystem checksum/mirror policy costs and missing native hashing/metadata/removal capabilities.
9. Add reliable prepared-template artifacts and competitive hot-render reuse.
10. Close concrete task/build contract and native-integration gaps: outputless/env/cache/ensure/workers/graph, depfiles/multi-output/toolchains.

Preserve the91%stat,86%filter/walk,72%template-loop,67%queue and31%sorting gains. A large improvement does not mean a competitive gap is solved.

## Evidence, infrastructure and publication

Official observations total67,153, including retained warmups. Raw results, rejected orchestration attempts, correctness/distribution audits, build/runtime identities, diagnostic traces and exact protocol sources are in the new series under lab-evidence/benchmarks and this campaign. No official observations were discarded or selectively rerun for unfavourable results. The build wrapper ordering failure and local temporary inode exhaustion are retained separately from benchmark correctness.

All eight campaign Linodes have verified CLI absence/API404 receipts under lifecycle/. Shared temporary SSH key, known-hosts, CLI configuration and private cloud state were removed; the user credential source was untouched. The previous filesystem host was closed separately under its earlier approval. Labs source/public remain unchanged.

Candidate/source/suite freeze IDs are in campaign.json; evidence commits and lifecycle gates are in Git history and per-host ready/teardown receipts. The final receipt links are below.
- build-systems: node108024443, evidence`8426a26c3d608d7af71bf3b589dbefa67aee7209`, CLI absent/API404; [receipt](../lifecycle/build-systems/teardown.json)
- concurrency: node108024477, evidence`22a0d21c3f122041206933b208c6d70b53b4c3a3`, CLI absent/API404; [receipt](../lifecycle/concurrency/teardown.json)
- filesystem-automation: node108024451, evidence`4206b478a692aa753be5822014a9f53f9fe21c64`, CLI absent/API404; [receipt](../lifecycle/filesystem-automation/teardown.json)
- scripting-benchmark: node108024446, evidence`2b98e0610c566783ad74769e047bc4f7e2204d98`, CLI absent/API404; [receipt](../lifecycle/scripting-benchmark/teardown.json)
- shell-benchmark: node108024467, evidence`d277cf2e98fa76d2ec0ba6035403bd804e64ad8c`, CLI absent/API404; [receipt](../lifecycle/shell-benchmark/teardown.json)
- task-runners: node108024433, evidence`d5b7b1bba2598ecd6ad32dabde5f1cb68c068784`, CLI absent/API404; [receipt](../lifecycle/task-runners/teardown.json)
- template-engines: node108024438, evidence`22a0d21c3f122041206933b208c6d70b53b4c3a3`, CLI absent/API404; [receipt](../lifecycle/template-engines/teardown.json)
- website-generator-benchmark: node108024456, evidence`57bb46ae9504217ad5e350847ec502ca4d2d8f23`, CLI absent/API404; [receipt](../lifecycle/website-generator-benchmark/teardown.json)

No core fixes, new candidate or rerun were performed here. Those are the next user-directed phase; publication must wait for a new frozen candidate and complete rerun.

## Final build profile lead

Separate captures retain identical20,001execve calls, but candidate adds30,236openat/read/close calls each and60,708lseek calls. Sampled copy_present_pte self share rises8.91→16.11% through fork/nift_run_pipeline. Larger parentmemory and metadataI/O are plausible contributors to tiny-fullbuild slowdown; no source ablation or causal share established. Sharedcaches existed in both revisions. Full rawprofiles, exact replaybinaries and handover are retained in the build series.

The recurring follow-up automation is PAUSED following completed diagnostic closeout.
