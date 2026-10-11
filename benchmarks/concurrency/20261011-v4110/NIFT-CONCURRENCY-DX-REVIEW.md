# Would I actually choose Nift for concurrent scripting?

Qualitative practitioner assessment, not benchmark evidence. This judgement comes from implementing and debugging the five adapters, the separate semantics probes and the accepted campaign. It is not an overall concurrency score. See RESULTS.md for numbers and METHOD.md for boundaries.

## Current preference

I would choose Nift for bounded concurrent work inside an existing Nift project, particularly native helper/subprocess orchestration that benefits from one programmable project runtime. I would not currently choose it as the general default for high-concurrency lightweight work or a long-lived async service. For a new standalone concurrent tool, Go's buffered channels, explicit cancellation contexts and compiled deployment are a stronger package today. Node/Bun remain natural choices for promise-based I/O inside a JS project; Python remains natural when the required automation libraries are Python libraries. These are specific requirements, not an unexplained appeal to ecosystem.

| Workload | Present preference | Reason / boundary |
|---|---|---|
| Concurrent work in an existing Nift project | Nift, with bounded jobs | Native joins, argv process capture and explicit shared handles integrate with existing .f policy; avoid very large retained task sets. |
| New concurrent project automation | Nift for project-centered .f policy; Go for a standalone concurrency-heavy tool | Integration matters; Nift's scheduler/retention and missing cancellation/channel contracts limit the general case. |
| Async-heavy I/O service/tool | Node/Bun in JS; Go for standalone tooling | Suspended timers, async APIs and explicit cancellation/deadline mechanisms; this suite measures timers/files/processes, not networking capacity. |
| Parallel CPU scripting | Go for a new tool; Python when Python libraries are required | Fixed-work scaling matters alongside absolute interpreter throughput and pool startup. Nift native CPU threads are real, but do not make its scalar interpreter fast. |
| Agent-maintained Nift automation | Nift for bounded .f workflows | Snapshot captures, typed handles, explicit join/await and owner checks are useful contracts. Lock cleanup and cancellation still need discipline. |
| High-concurrency lightweight tasks | Go / Node / Bun according to deployment | Nift task capture/retained registry costs and blocking sleeps are material limitations. |
| Existing JS project | Its current Node/Bun runtime | Promise waits, worker isolates and existing APIs; worker messaging is additional CPU-path work. |
| Existing Python project | Python | asyncio for waits, threads for blocking APIs, processes for ordinary-GIL CPU; process startup and running-task cancellation are explicit costs. |
| New standalone concurrent tool | Go | Channels/backpressure, context cancellation, race-debugging tooling and one compiled executable. |

This preference does not imply using another executor underneath Nift for every concurrent project. Small, bounded native work is already a legitimate Nift capability. It also does not turn a Nift project into a reason to accept an unbounded future registry or unsafe lock error path.

## What worked in Nift

Native threads/futures returned exact results, shared atomics coordinated real native workers, and owner-checked mutex values made sharing boundaries visible. The same in-language arithmetic ran at one/two/four workers; no C++ helper did Nift's calculation. Nift achieved 3.95× fixed-work speedup at four workers, but its roughly 3.91s four-worker median remained far above Go's 15.7ms on this kernel; see the exact table rather than treating scaling as absolute speed. Subprocess work used argv commands and captured outputs/statuses, fitting its project-automation role. At four concurrent helpers, the 1000-child booted median was 902.037ms for Nift, versus 1886.327ms Node, 506.293ms Bun, 453.014ms Python and 338.342ms Go. Nift is viable here and faster than Node in this boundary, but does not lead the field. Explicit await and join are inspectable, and repeat-await error observation worked in the separate probe. Recoverable user errors reached the parent while successful siblings finished.

Ordinary captured values are snapshots rather than silently shared mutable objects. Transferable atomic/mutex handles are explicit exceptions. That is a useful safety model for agents: a reviewer can identify shared state and synchronization without reconstructing arbitrary closure aliasing. A typed binding rejected changing an atomic handle into a mutex handle. More syntax here carries a real contract.

## What was difficult

High fan-out is expensive. Task snapshots/registries need allocation and ownership investigation; a minimal reproducer and syscall/perf evidence are retained. Holding 10000 unfinished Nift tasks required about 13,700MiB locally, beyond the official 8GiB host. Both official 10k held-memory cells are therefore unavailable, while the other engines retain that range. Completed tasks are different from simultaneously held captures; ordinary 10k scheduling is measured, not inferred from the memory probe.

The first partial cloud cohort exposed latency growth across requests in one Nift runtime. This is a real product finding even though that incomplete cohort is not pooled into the accepted distributions. Accepted booted measurements equally isolate request state for all engines and therefore do not certify long-lived steady-state throughput. A repeated-runtime probe covers all five participants separately. Reclaiming unreachable completed-task metadata must preserve repeated await on still-live handles and owned-work cleanup.

Blocking sleep occupies Nift's native async workers. It is not equivalent to suspending a thousand promise/asyncio/goroutine timers. Native threads are valuable for CPU and blocking project work, but not automatically the appropriate abstraction for mostly idle tasks. No public pool-size override was found in this frozen core; hardware_concurrency sizing can differ from allowed CPU affinity on a larger host.

There was no public bounded channel/condition variable or future cancellation API in the inspected source. The queue adapter therefore required a protected ring and 1ms empty/full polling. That limitation is visible in the measurements; it is not a claim that a hand-authored polling queue is identical to Go's native channel. A malformed expression while holding a mutex stranded a sibling in a separate watchdog-terminated reproducer. Scoped/guarded locking, aggregate task ownership and cooperative deadlines would make agent-written error paths safer.

Nested object/index accesses needed intermediate variables. Those intermediates did not add ownership or synchronization information and are redundant ceremony. Error codes had to use the user namespace, while typed handles and explicit lock ownership carried useful semantics. These are different categories and should not be collapsed into a complaint about line count.

## Other implementations were not frictionless

Python's ordinary GIL required processes for honest CPU parallelism. Spawn/import/transfer/teardown stayed inside each request; using a permanent prewarmed pool would answer a different question. Executor contexts were helpful, but cancelling a running process is not ordinary asyncio cancellation.

Node/Bun promises made timer work straightforward. CPU work required worker messages, explicit shared buffers for atomics and joining worker exit. The cooperative bounded queue is an event-loop contract, not a shared-memory channel. Standard native mutex cells were deliberately unavailable rather than filled with a custom substitute.

Go channels expressed bounded capacity and closing naturally, but still required correct collection order and lifecycle. An early undersized result-channel implementation could deadlock when joining before collecting; implementation debugging caught and fixed it. Context cancellation remains an authored policy, not automatic all-settled or structured fail-fast behavior.

## Equal-performance counterfactual

At equal reliable performance, I would prefer Nift for existing Nift project automation and bounded, agent-maintained .f policy. Explicit capture/share/join contracts can make changes easier to inspect than implicit mutable closure sharing. I would still choose Go for a new concurrency-heavy standalone tool requiring channels, deadlines, cancellation and its deployment/race-debugging workflow. JS projects still benefit from their existing async API integration; Python libraries still justify Python. Equal timings do not create missing semantic APIs.

If Nift reliably adds lightweight suspended waits, bounded channels, guarded locks, task-group cancellation/deadlines, pool overrides, bounded capture allocation and stable reused-runtime bookkeeping while retaining explicit .f semantics, I would reconsider its default role for new authored concurrent automation. There is no architectural rule that Nift must delegate to Go or JS. The mature-product judgement must wait for those contracts and measurements, rather than assuming that native threads alone satisfy them.

## Product conclusion

Concurrency in this frozen Nift is **usable, with material caveats**, and can be compelling as a bounded facility within its broader project runtime. It is not yet a demonstrated first-class strength across high-concurrency scheduling, waiting, queues and retained-runtime workloads. Native parallel work, exact values and explicit sharing are genuine capabilities; scheduler/capture growth, blocking waits and missing safer coordination APIs keep the broader claim premature.

The core handover is concrete: profile/cut capture and completed-registry growth without weakening snapshots; add suspended waits and pool controls; bounded channels; guarded lock cleanup; explicit group cancellation/deadlines and aggregate error policy. Preserve useful explicitness and remove only redundant/no-information ceremony. No Nift core was modified by this experiment.
