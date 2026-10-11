# Implementation notes

2026-10-11: Nift maintained tests show snapshot closures, native thread join, bounded-pool async functions, transferable atomics/mutexes and owner-checked values. Nested futures have forward-progress tests. Investigate callable snapshots and queue/cancellation contracts before claiming equivalence. Extra syntax can carry useful ownership/error information.

Nift pool source uses hardware_concurrency threads and has no public worker override. Blocking sleep occupies a pool worker, unlike asyncio/promises timers. Pool/job limits will be implemented explicitly. Atomics use transferable native handles; mutex protected data has checked ownership. JS has SharedArrayBuffer atomics, but no standard native mutex: mutex cells will be unavailable rather than inventing a third-party lock for a headline.

- Queue implementation exposed parser limits: nested object/index reads and writes need intermediate bindings. A failure while holding a mutex can strand sibling threads during cleanup. Rejected local attempts retain this diagnostic; no core changes. Native user error codes require the `user.` namespace; checked and normalized only at the protocol boundary.

- Held memory at 10k futures was about 13,700MiB (about 13.4GiB) locally, vs ~148MiB at 1k. Ordinary completed scheduler tasks did not hold this memory concurrently. Frozen official range must respect the 8GiB host; Nift 10k held cells unavailable, preserve diagnostic and show 100/1k growth. Need task environment/capture profiling, not native stack guesses.

- Python's process pool makes its CPU parallelism honest but adds process startup and value transfer. A thread-pool substitute would have been misleading for ordinary-GIL bytecode. Executor context managers make teardown straightforward; cancellation of a running process is not ordinary future cancellation.
- JS needs explicit worker messaging and exit joining for CPU work; promise timers are far simpler for waiting. Bun's Node-compatible worker API keeps the equivalent adapter inspectable, with compatibility semantics stated. Promise queue is cooperative, not a shared-memory channel.
- Go buffered channels express capacity/close naturally. WaitGroup plus channel close has explicit lifecycle; using an undersized result channel while joining producers first can deadlock, caught during development and fixed by concurrent-capacity collection. Go error values and context cancellation require explicit policy, not automatic structured task-group semantics.
- Native Nift atomics and owner-checked mutex handles are clear sharing boundaries. Snapshot ordinary values avoid accidental implicit sharing but impose capture costs. Intermediates for nested object accesses are redundant parser ceremony, while join/await/lock ownership declarations carry useful semantics.

- First cloud cohort rejected before completion: Nift schedule-1000 fresh stayed ~250ms, reused runtime grew from ~244ms to 8.8s by request20 while RSS rose9→29MiB. This is retained-runtime work registry growth, not merely host noise. Equal already-booted isolated request policy applies to all five runtimes; repeated-host behavior remains separate prominent diagnostic evidence.

- Typed Nift bindings rejected replacing an atomic handle with a mutex handle. Separate construction branches made ownership/model explicit; that validation is useful semantics, not automatically bad ceremony. By contrast nested indexing intermediates carry no additional concurrency meaning.
