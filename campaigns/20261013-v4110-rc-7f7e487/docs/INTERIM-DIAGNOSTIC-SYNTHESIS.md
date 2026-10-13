# Interim diagnostic synthesis — five completed suites

Candidate7f7e487 is frozen and not release-approved. Same-node diagnostic values are separate from official current-vs-peer series. Three suites are still running; conclusions below are interim. No Labs publication.

## Biggest regressions so far

| Rank | Benchmark / scenario | Old ms | Candidate ms | Increase | Evidence basis | Likely subsystem |
|---:|---|---:|---:|---:|---|---|
| 1 | scripting / sanity/function-calls/large | 228.284 | 561.026 | 145.76% | same-node 10 paired samples; clear nonoverlap/10 slower pairs | call argument/value staging |
| 2 | scripting / sanity/function-calls/small | 6.080 | 10.069 | 65.63% | same-node 10 paired samples; clear nonoverlap/10 slower pairs | call argument/value staging |
| 3 | website-generator / application-cold | 2561.445 | 3542.237 | 38.29% | independently audited same-node targeted diagnostic; all observed ranges disjoint | fresh build path/filesystem probes |
| 4 | scripting / arrays-strings-hash/frequency-count/small | 8.303 | 10.659 | 28.37% | same-node 10 paired samples; descriptive increase, significance unestablished | collections/value paths; attribution unresolved |
| 5 | scripting / graphs-trees-search/bfs/small | 12.723 | 15.270 | 20.02% | same-node 10 paired samples; descriptive increase, significance unestablished | collections/value paths; attribution unresolved |
| 6 | scripting / structured-data/json-transform/large | 586.317 | 703.648 | 20.01% | same-node 10 paired samples; descriptive increase, significance unestablished | collections/value paths; attribution unresolved |
| 7 | scripting / arrays-strings-hash/frequency-count/large | 473.156 | 567.263 | 19.89% | same-node 10 paired samples; descriptive increase, significance unestablished | collections/value paths; attribution unresolved |
| 8 | scripting / graphs-trees-search/bfs/large | 844.177 | 999.076 | 18.35% | same-node 10 paired samples; descriptive increase, significance unestablished | collections/value paths; attribution unresolved |

Calls and website freshfull are the strongest release-blocking specimens. Other paired increases are supported descriptive signals, not automatically statistically confirmed. Historical cross-node regressions remain separately ranked. Reused-runtime degradation is an old unresolved weakness, not a proven new regression.

## Biggest improvements so far

| Rank | Benchmark / scenario | Old ms | Candidate ms | Improvement | Basis |
|---:|---|---:|---:|---:|---|
| 1 | template-engines / loop-10000 / source-render | 119.508 | 33.683 | 71.82% | independently audited same-node targeted diagnostic; descriptive three-pair control |
| 2 | concurrency / queue-100000-4-4 / fresh runtime/readiness request | 36066.073 | 11887.314 | 67.04% | independently audited same-node targeted diagnostic; descriptive three-pair control |
| 3 | template-engines / loop-10000 / fresh | 168.238 | 75.854 | 54.91% | independently audited same-node targeted diagnostic; descriptive three-pair control |
| 4 | template-engines / article / source-render | 0.430 | 0.266 | 38.05% | independently audited same-node targeted diagnostic; descriptive three-pair control |
| 5 | scripting / arrays-strings-hash/sort-index/large | 1088.855 | 754.437 | 30.71% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 6 | scripting / arrays-strings-hash/scan/large | 110.635 | 93.988 | 15.05% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 7 | website-generator / incremental/no-op / 10000pages targeted adjacent paired versions | 932.931 | 813.536 | 12.80% | independently audited same-node targeted diagnostic; all observed ranges disjoint |
| 8 | website-generator / warm-full / 10000pages targeted adjacent paired versions | 3176.786 | 2776.981 | 12.59% | independently audited same-node targeted diagnostic; all observed ranges disjoint |
| 9 | scripting / structured-data/json-parse/small | 6.812 | 5.979 | 12.23% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 10 | website-generator / incremental/one-page / 10000pages targeted adjacent paired versions | 920.908 | 821.310 | 10.82% | independently audited same-node targeted diagnostic; all observed ranges disjoint |
| 11 | scripting / dynamic-programming/fibonacci/large | 182.107 | 164.111 | 9.88% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 12 | scripting / arrays-strings-hash/sliding-window/large | 339.164 | 307.064 | 9.46% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 13 | scripting / arrays-strings-hash/sort-index/small | 10.823 | 9.843 | 9.06% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 14 | scripting / arrays-strings-hash/scan/small | 4.901 | 4.541 | 7.34% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 15 | scripting / arrays-strings-hash/map-set/large | 295.962 | 278.617 | 5.86% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 16 | scripting / arrays-strings-hash/map-set/small | 7.007 | 6.615 | 5.60% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 17 | scripting / sanity/loops/large | 92.539 | 88.115 | 4.78% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 18 | scripting / sanity/output/small | 3.720 | 3.562 | 4.25% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 19 | scripting / sanity/loops/small | 4.945 | 4.780 | 3.35% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 20 | scripting / arrays-strings-hash/sliding-window/small | 7.381 | 7.157 | 3.02% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 21 | scripting / structured-data/json-traverse/small | 8.969 | 8.772 | 2.19% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 22 | scripting / sanity/noop/large | 3.426 | 3.359 | 1.96% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 23 | scripting / sanity/output/large | 3.778 | 3.707 | 1.88% | same-node 10 paired samples; sort large nonoverlap, others descriptive |
| 24 | scripting / structured-data/json-traverse/large | 491.211 | 489.025 | 0.45% | same-node 10 paired samples; sort large nonoverlap, others descriptive |

Task wall medians improve13.83–33.46% across all31matched configurations, but only cross-node evidence exists. This strengthens observed orchestration performance without assigning the whole gain to core. Turbo/Nx changes are host-confounded; current tiny-full1000 is Nift1457ms, Nx10830ms, Turbo101823ms.

## Biggest remaining competitive gaps

Wall ranking below uses official same-node valid peers, not diagnostic old/new samples. It ranks whole-problem boundaries, not isolated scheduler/lock instruction costs.

| Rank | Benchmark / scenario / boundary | Nift ms | Best peer ms | Deficit | Previous deficit | Classification |
|---:|---|---:|---|---:|---|---|
| 1 | concurrency / schedule-10000 / persistent | 20311.090 | go: 14.752 | 1376.9× | 1591.3× (cross-node) | B: old weakness, improved |
| 2 | concurrency / tiny-10000 / persistent | 19978.451 | go: 16.164 | 1236.0× | 1296.2× (cross-node) | old weakness; movement not causally established |
| 3 | concurrency / schedule-10000 / fresh | 19493.458 | go: 18.540 | 1051.4× | 1108.9× (cross-node) | B: old weakness, improved |
| 4 | concurrency / tiny-10000 / fresh | 17297.852 | go: 21.370 | 809.5× | 1037.2× (cross-node) | old weakness; movement not causally established |
| 5 | scripting / sanity/function-calls/large / fresh-process-repeated | 546.056 | luajit: 1.889 | 289.1× | not retained in normalized peer exports | A: new call regression plus old weakness |
| 6 | concurrency / mutex-8-2 / persistent | 257.462 | go: 0.895 | 287.6× | 578.1× (cross-node) | old weakness; movement not causally established |
| 7 | concurrency / mutex-8-1 / persistent | 227.523 | go: 0.851 | 267.3× | 661.9× (cross-node) | old weakness; movement not causally established |
| 8 | concurrency / mutex-8-4 / persistent | 264.153 | go: 0.991 | 266.6× | 749.2× (cross-node) | old weakness; movement not causally established |
| 9 | concurrency / mutex-1-2 / persistent | 209.273 | go: 0.868 | 241.0× | 510.1× (cross-node) | old weakness; movement not causally established |
| 10 | concurrency / mutex-1-4 / persistent | 220.942 | go: 0.935 | 236.2× | 742.1× (cross-node) | old weakness; movement not causally established |
| 11 | concurrency / queue-100000-4-4 / persistent | 11745.837 | bun: 56.266 | 208.8× | 607.0× (cross-node) | B: old weakness, improved |
| 12 | concurrency / cpu-1 / persistent | 10807.809 | go: 52.767 | 204.8× | 283.0× (cross-node) | B: old weakness, improved |
| 13 | concurrency / cpu-2 / persistent | 5482.127 | go: 26.945 | 203.5× | 247.8× (cross-node) | B: old weakness, improved |
| 14 | concurrency / mutex-1-1 / persistent | 187.105 | go: 0.954 | 196.2× | 519.9× (cross-node) | old weakness; movement not causally established |
| 15 | concurrency / cpu-1 / fresh | 10791.349 | go: 57.828 | 186.6× | 235.4× (cross-node) | B: old weakness, improved |

Template10k source-render34.408ms vsHandlebars2.241ms =15.4×: B, improved but still smoked. Prepared-template reuse remains unsupported, not a zero-time comparison. Retained-runtime scheduling229.567→1646.006ms is C, old weakness unresolved; prior229.949→1372.881ms, while tenth requests areGo2.273ms, Bun1.051ms, Node1.149ms, Python4.554ms. These single trajectories are descriptive.

Memory is separate: stable1k-held READY Nift143.625MiB vsGo5.375MiB =26.72×; priorNift143.5MiB, essentially unchanged(C). 10kheld watchdog crossing6GiB is censored, not an exact deficit. Template fresh memory has confirmed inherited supervisor floors and is unranked. Task maximum-childRSS leads31/31(D:competitive in this scope), not aggregate-tree memory. Website same-node fresh peakRSS16920→39744KiB (+134.9%) is a separate measured peak boundary; current officialfresh Nift38.56MiB vsHugo246MiB still lower. No general memory-efficiency score.

## Template engines

Large-loop fresh improves54.91%, source-render71.82%; article source-render38.05%. These directly improve source preparation/rendering work, but do not isolate context copying or establish a cache/reuse API. Repeated-source1000 workloads did not establish a material version-caused gain. Public prepared-template artifact is still absent. I choose Nift for Nift-owned/programmatic generation; I still choose a prepared peer for standalone hot rendering. Better performance strengthens confidence without reversing that boundary-specific preference.

## Concurrency

Queue100k4→4 improves67.04% same-node, yet current officialqueue208.8×Bun. Schedule1k paired367→361ms is noisy;10kscheduling remains1376.9×Go. Held memory unchanged. Wait1k2576ms vsGo14.484ms:177.9×, only3.1%historical Nift improvement across nodes. Four-worker CPU3905→2851ms is a27.0%cross-node trend, still186.5×Go; no controlled CPU A/B. Native task parallelism works, but absolute scalar cost remains severe. Public channels/condition variables and cancellation remain absent; cooperative atomic-stop/all-settled behavior is not structured cancellation. Reuse slowdown remains and blocks my selecting Nift for a long-lived async service.

## Task runners

Nift is still my human+agent and agent-primary choice for authored workflows. Outputless trackedDAG nodes/env invalidation/result restoration remain absent; ensure targeting and-j rejected. Configured workercounts work; state/reason inspection exists but complete structured graph explanation is missing. Repair after injected failure succeeds; missing artifacts rebuild rather than restore cached outputs. No new capability win should be invented from faster timing.

## Website generator

Freshfull materially regresses38.29% same-node; warmfull/noop/leaf improve12.59/12.80/10.82%. Official10k fresh Nift3.739s vsHugo2.943s:1.27×slower, reversing priorcross-node Nift3.853/Hugo5.005s. Officialwarm Nift2.999s vsHugo3.182s leads narrowly. FreshRSS rises as noted above while remaining belowHugo. Nift is no longer an obvious universal winner: chooseHugo for a plain content site, Nift for existingNift or mixed authored policy.

## Scripting root-cause status

Largecalls allocations900967→1701054 (+88.8%); small9967→18054. Cross-size slope9→17allocations perloop iteration (includesloop/call machinery). Newstacks include evaluate_call_operand/form_call_arguments, consistent with argument source parsing/classification and RuntimeValue snapshot/location-provenance staging introduced in55cb323. Immutable lambda metadata091c002 is another nearby change, but capture/frame causality is not isolated. No comparable total allocated-byte statistic has been established; peakheap~116.6K(toolunits) stays similar. CPU profiles agree on call/source/string/value paths but are low-sample, not precise causal shares. Identical110syscalls weakens syscallamplification explanation; it does not rule out all OSnoise. Adjacent10/10slower pairs and nonoverlapping ranges supply the strongest regression evidence. No bisect/corepatch performed. Frequency slowdown has almost unchanged allocations, so one allocation explanation cannot cover every bad case.

## Current Codex preferences

| Category | Human + agent | Agent-primary | Why / change |
|---|---|---|---|
| Scripting | Python for new general data/automation; Nift for bounded Nift-owned policy | Same choices | Calls/collections/JSON costs remain; concrete Python libraries and runtime recovery matter. No broad preference reversal. |
| Task running | Nift for authored DAGs; Turbo/Nx for required restoration/discovery | Nift for authored DAGs; same specific exceptions | Nift lowest wall/RSS31/31; preference unchanged, confidence strengthened. |
| Template engine | Nift for Nift-owned composition; native library in Python/JS; prepared peer for hot service | Nift for programmable authored generation; prepared peer for high-volume hot service | Loop gains are real; no public prepared-template artifact and15.4×large source-render gap remain. Scope improves, default hot-service preference unchanged. |
| Concurrency | Go for standalone/high fanout; Nift for bounded Nift-owned jobs | Same choices | Queue improves67%, but scheduling/memory/waits/reuse still block a general Nift choice. |
| Website generation | Hugo for conventional content site; Nift for existing/mixed programmable project | Nift for mixed authored website/assets/helpers; Hugo for plain content site | Freshfull regression and current Hugo advantage weaken blanket Nift preference; incremental paths improve. |

## Highest-priority core work

1. **Fix function-call regression.** Confirmed+145.76%; central policy-language path. Investigate extra argument parsing/classification/allocation; preserve exactly-once and ownership.
2. **Fix fresh website full-build regression.** Confirmed+38.29%; strategically central product. Extra filesystem probes merit investigation independent of call cause.
3. **Resolve retained-runtime state/time growth.** Ten scheduling requests grow7.17×; prior also grows. Blocks long-lived embedding/service preference; prove lifetime cause before calling it a leak.
4. **Reduce lightweight task creation/retention cost.** 10k scheduling1376.9×Go and held1k memory26.7×Go. Tiny work is infeasible despite queue wins.
5. **Improve scalar/value execution throughput.** 4-worker CPU186.5×Go despite useful parallel scaling; large calls289.1×LuaJIT. Separate interpreter cost from scheduling.
6. **Add nonblocking waits/timers.** 1k wait2576ms vsGo14.484ms; historical Nift2659.6ms shows little movement. Blocking workers remain the architectural/API boundary to address.
7. **Add public prepared-template artifacts.** Missing today; source-render cannot be relabelled prepared reuse. High-volume rendering still selects prepared peers.
8. **Reduce remaining collection/JSON costs.** BFS/frequency/transform paired medians increase; BFS allocations rise39.8%, frequency counts barely change. Investigate independently; keep sorting wins.
9. **Add channels/cancellation with explicit lifetime contracts.** Queue polling/mutex value copies persist; native bounded channel/condition and public cancellation remain absent. Do not replace semantic safety with terseness.
10. **Close task-runner contract/cache ergonomics gaps.** Outputless nodes, env invalidation, restoration, ensure,-j,structured graph remain incomplete. Existing repair works; Nift is already preferred for authored tasks.

Newly supported capabilities(E): none established in these five refreshed suites; performance gains are not newAPIs. Fixed/competitive(D): authored taskorchestration remainsstrong; bounded projectcomposition retainsutility. No shared rootcause is inferred from naming similarity.

## Campaign status

Five suites closed with retained/pushed evidence and verifiedteardown. Build/shell/filesystem continue unchanged. Do not modify core or publishLabs. Fold remaining acceptedresults into these reports as theyfinish.

## Newly audited shell — diagnostic pending

All8,566observations passed independent count/correctness/distribution audit (7,855measured+711warmups,293jobs; Bash/Zsh/Fish/Nu/Nift). Historical shellfunction-calls22.586→46.722ms (+106.86%) is cross-node screening only; targeted same-node call/string/traversal controls are pending. Do not promote this to a confirmed shared runtime regression yet. Most other historical cases improve or vary modestly.
