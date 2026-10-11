Yep. I’d make the repo **`nift-experiments/concurrency`** and frame it as a **Concurrency Benchmark**, not a “multithreading benchmark,” so each runtime can use its natural model while we still separate true parallel CPU work from async/cooperative concurrency.

I’d give Codex this:

> We’re starting the next Nift Labs benchmark:
>
> **Concurrency**
>
> The goal is to evaluate how well Nift handles concurrent and parallel work compared with contemporary scripting/runtime environments.
>
> This is not just “threads vs threads.” Different runtimes have different concurrency models, so the benchmark should compare **equivalent concurrency problems** while clearly documenting which primitive each participant uses.
>
> ## Repository setup
>
> Create a new public repository:
>
> `nift-experiments/concurrency`
>
> Clone it locally to:
>
> `/home/nick/Repositories/nift/nift-experiments/concurrency`
>
> Confirm first that the repo/path do not already exist.
>
> Follow the conventions from the recent:
>
> - build-systems;
> - task-runners;
> - template-engines
>
> experiments.
>
> Canonical evidence belongs under:
>
> `/home/nick/Repositories/nift/nift-experiments/lab-evidence`
>
> The Labs website must contain only compact publication data/assets. Do not copy raw timing samples, traces, perf captures, receipts or large result corpora into `lab`.
>
> Run the hardened Labs storage policy before every Labs publication commit.
>
> ---
>
> # 1. Core question
>
> Answer:
>
> > How effectively can contemporary scripting/runtime environments express and execute concurrent and parallel work, and where does Nift fit?
>
> We want to test:
>
> - task scheduling overhead;
> - async/waiting efficiency;
> - native parallel execution;
> - bounded worker pools;
> - fan-out/fan-in;
> - synchronization;
> - atomics;
> - producer/consumer patterns;
> - subprocess concurrency;
> - I/O concurrency;
> - mixed CPU/I/O workloads;
> - failure propagation;
> - memory scaling;
> - concurrency ergonomics/DX.
>
> Do not collapse all of these into one “concurrency score.”
>
> ---
>
> # 2. Participant set
>
> Investigate current versions and propose a compact, defensible field.
>
> Strong default candidates:
>
> - **Nift**
> - **Python**
> - **Node.js**
> - **Bun**
> - **Go**
>
> Optional:
>
> - **Ruby**
>
> only if it adds meaningful contrast and can be implemented fairly without bloating the campaign.
>
> Explain why each belongs.
>
> Suggested rationale:
>
> - Nift: native threads/futures/atomics/process APIs
> - Python: asyncio + threads/processes where appropriate
> - Node.js: event loop/promises + worker_threads
> - Bun: JS runtime with workers/subprocess concurrency
> - Go: goroutines/channels as a high-quality concurrency reference, even though it is not a scripting language in exactly the same sense
>
> Do not include a participant merely because it is popular.
>
> ---
>
> # 3. Fairness principle
>
> The benchmark should compare:
>
> > equivalent concurrency semantics
>
> rather than:
>
> > identical syntax or identical implementation primitives.
>
> For each workload:
>
> - choose the idiomatic concurrency primitive for each participant;
> - document it explicitly;
> - verify equivalent work and equivalent result semantics.
>
> Examples:
>
> - Node promises for async waiting;
> - Node worker_threads for true CPU parallelism;
> - Python asyncio for async waiting;
> - Python ThreadPoolExecutor where threading is appropriate;
> - Python ProcessPoolExecutor for CPU-parallel work if necessary;
> - Go goroutines/channels;
> - Nift’s native threads/futures/atomics/etc.
>
> Do not force Node through worker threads for a timer benchmark or Python through multiprocessing for an I/O benchmark just to make APIs look similar.
>
> ---
>
> # 4. Split the benchmark into distinct concurrency classes
>
> This is important.
>
> Publish separate sections/results for:
>
> ## A. Scheduling / task overhead
>
> Tiny concurrent jobs.
>
> ## B. Async/waiting
>
> Tasks mostly blocked on timers/I/O.
>
> ## C. Parallel CPU work
>
> Actual multicore execution.
>
> ## D. Synchronization
>
> Shared-state coordination.
>
> ## E. Process orchestration
>
> Concurrent child processes.
>
> ## F. Mixed realistic workflows
>
> CPU + I/O + subprocess work together.
>
> Do not average these into one misleading headline number.
>
> ---
>
> # 5. Scenario A — scheduling overhead
>
> Measure:
>
> - 10 tasks
> - 100 tasks
> - 1,000 tasks
> - 10,000 tasks where practical
>
> Use tiny deterministic task bodies.
>
> Consider:
>
> - create/schedule;
> - await/join all;
> - result collection;
> - cleanup.
>
> Have at least:
>
> - zero/near-zero-work tasks;
> - tiny arithmetic tasks.
>
> This should expose scheduler/runtime overhead.
>
> If a runtime cannot reasonably support 10k tasks using the selected primitive, document the supported range rather than forcing pathological behavior.
>
> ---
>
> # 6. Scenario B — fan-out / fan-in
>
> Canonical shape:
>
> ```text
> root
>  ├── A
>  ├── B
>  ├── C
>  ├── ...
>  └── N
>       ↓
>     collect
> ```
>
> Measure:
>
> - 10;
> - 100;
> - 1,000
>
> concurrent branches.
>
> Validate:
>
> - every task ran exactly once;
> - all results collected;
> - final aggregate exact.
>
> ---
>
> # 7. Scenario C — bounded worker pool
>
> Fixed queue of jobs with worker limits:
>
> - 1 worker;
> - 2 workers;
> - 4 workers;
> - perhaps 8 if useful on the 4-vCPU machine only as an oversubscription diagnostic.
>
> Workloads:
>
> - light;
> - medium;
> - CPU-heavy.
>
> This should reveal:
>
> - scheduling efficiency;
> - scaling;
> - overhead of synchronization/dispatch.
>
> ---
>
> # 8. Scenario D — timer/wait concurrency
>
> Use deterministic sleeps/timers.
>
> Examples:
>
> - 100 × 10 ms waits;
> - 1,000 × 10 ms waits;
> - staggered 1–20 ms waits;
> - mixed short/long waits.
>
> Expected lower bound should be obvious from critical path.
>
> Measure:
>
> - wall time;
> - CPU time;
> - memory.
>
> This is where event-loop runtimes may shine.
>
> Do not call this “parallel computation.”
>
> ---
>
> # 9. Scenario E — CPU-bound parallel work
>
> This is the real true-parallelism section.
>
> Use deterministic pure CPU jobs such as:
>
> - integer hashing;
> - prime/count workload;
> - fixed-size numerical loop;
> - checksum over generated buffers;
> - perhaps a small deterministic compression/hash-style kernel.
>
> Avoid libraries that secretly introduce their own thread pools.
>
> Measure with:
>
> - 1 worker;
> - 2 workers;
> - 4 workers.
>
> Validate identical results.
>
> For Node/Bun use worker mechanisms appropriate for real CPU parallelism.
>
> For Python, explicitly document whether:
>
> - threads;
> - processes;
> - free-threaded Python
>
> are being used.
>
> Do not casually describe normal CPython threads as equivalent multicore CPU execution unless the pinned Python build actually supports that semantics.
>
> ---
>
> # 10. Scenario F — subprocess concurrency
>
> This is particularly relevant to Nift’s real-world project automation.
>
> Launch:
>
> - 10;
> - 100;
> - 1,000 if practical
>
> deterministic child commands.
>
> Use a tiny purpose-built helper executable/script so the child workload is controlled and identical.
>
> Test:
>
> - successful children;
> - mixed duration children;
> - one child failure;
> - several child failures.
>
> Measure:
>
> - launch overhead;
> - wall time;
> - CPU;
> - maximum-child RSS;
> - exact exit/result collection.
>
> Ensure shell startup is not accidentally included for some languages and bypassed for others.
>
> Prefer argv-based process APIs.
>
> ---
>
> # 11. Scenario G — file-I/O concurrency
>
> Use a generated fixture tree outside the timed setup.
>
> Example:
>
> - 100 files;
> - 1,000 files;
> - 10,000 small files
>
> Tasks:
>
> - read;
> - hash;
> - aggregate exact digest.
>
> Distinguish:
>
> - synchronous worker-pool implementation;
> - native async I/O where relevant.
>
> Be cautious interpreting Linux filesystem cache results.
>
> This is not a disk benchmark.
>
> It is a runtime concurrency/orchestration benchmark over controlled file operations.
>
> ---
>
> # 12. Scenario H — producer / consumer
>
> Canonical bounded queue:
>
> ```text
> producer(s) -> queue/channel -> consumer(s)
> ```
>
> Measure:
>
> - 1→1
> - 1→4
> - 4→1
> - 4→4
>
> with:
>
> - 1k messages;
> - 10k;
> - 100k if feasible.
>
> Each message should carry a deterministic integer payload.
>
> Verify:
>
> - exact count;
> - exact aggregate;
> - no lost/duplicated values.
>
> Use each runtime’s idiomatic queue/channel primitive.
>
> ---
>
> # 13. Scenario I — atomics / shared counter
>
> Where the runtime supports genuine shared-memory atomics:
>
> - Nift atomics;
> - Go atomics;
> - Node SharedArrayBuffer/Atomics if appropriate;
> - Python only where a genuinely comparable primitive exists.
>
> Do not fake equivalence.
>
> Test:
>
> - uncontended increments;
> - 2-worker contention;
> - 4-worker contention.
>
> If a participant lacks a directly comparable primitive, mark the cell unsupported rather than inventing an unfair substitute.
>
> ---
>
> # 14. Scenario J — mutex contention
>
> Shared counter/state protected by a mutex/lock.
>
> Run:
>
> - 1;
> - 2;
> - 4 workers.
>
> Vary:
>
> - tiny critical section;
> - moderate critical section.
>
> Measure throughput and correctness.
>
> Again, unsupported models should be reported honestly.
>
> ---
>
> # 15. Scenario K — failure propagation
>
> Test separately from timing where appropriate.
>
> Canonical graph:
>
> ```text
> parent
> ├── success
> ├── success
> ├── failure
> └── success
> ```
>
> Questions:
>
> - does parent observe failure?
> - are sibling tasks allowed to finish?
> - can remaining tasks be cancelled?
> - how are errors collected?
> - what happens on join/await?
> - can multiple failures be reported?
>
> Record semantic behavior precisely.
>
> Do not force all runtimes to have identical cancellation semantics if their APIs differ.
>
> ---
>
> # 16. Scenario L — mixed CPU + wait
>
> A realistic workload:
>
> - parse/synthesize data;
> - perform small CPU transform;
> - wait/sleep or file read;
> - produce checksum;
> - aggregate.
>
> This should answer whether a concurrency model remains efficient when work is heterogeneous.
>
> ---
>
> # 17. Scenario M — nested task creation
>
> Test:
>
> ```text
> task
>   -> spawns N subtasks
>      -> each spawns M subtasks
> ```
>
> Keep total task counts bounded and deterministic.
>
> This can reveal scheduler or allocation behavior that flat task sets miss.
>
> ---
>
> # 18. Memory scaling
>
> This should be a prominent section.
>
> Measure memory for:
>
> - 100 waiting tasks;
> - 1,000 waiting tasks;
> - 10,000 waiting tasks;
> - 100/1k worker jobs;
> - CPU worker pools.
>
> Be precise about:
>
> - process RSS;
> - maximum child RSS;
> - process-tree memory;
> - host/runtime retention.
>
> Do not compare incomparable memory metrics in one chart.
>
> The particularly interesting question is:
>
> > how much memory does each runtime need to keep a large amount of concurrent work alive?
>
> ---
>
> # 19. Startup vs persistent runtime
>
> As with Template Engines, split:
>
> ## Fresh invocation
>
> Start runtime → perform workload → exit.
>
> ## Persistent worker/runtime
>
> Runtime already alive → perform workload.
>
> Startup cost can dominate scripting-language measurements.
>
> Do not mix the two boundaries.
>
> This is especially important for:
>
> - Node;
> - Bun;
> - Python;
> - Nift.
>
> ---
>
> # 20. Correctness oracle
>
> Every timed result must have a correctness check appropriate to the workload.
>
> Verify:
>
> - result counts;
> - exact aggregates;
> - exact hashes;
> - no missing tasks;
> - no duplicated tasks;
> - expected failures;
> - expected synchronization result;
> - expected produced files where relevant.
>
> A fast race-condition result is invalid.
>
> Retain explicit traces for selected semantic scenarios.
>
> ---
>
> # 21. Concurrency semantics audit
>
> Maintain a capability matrix:
>
> ```text
>                        Nift  Python  Node  Bun  Go
> async wait
> true CPU parallelism
> native threads
> worker processes
> futures/promises
> channels/queues
> atomics
> mutexes
> cancellation
> bounded scheduling
> structured join
> subprocess API
> ```
>
> But distinguish:
>
> - supported;
> - supported through a different model;
> - unsupported.
>
> Do not use a checkbox matrix to imply different models are semantically identical.
>
> ---
>
> # 22. DX review during implementation
>
> Keep a running:
>
> `docs/DX-NOTES.md`
>
> Record actual experience with:
>
> - starting work;
> - waiting for results;
> - returning values;
> - handling errors;
> - sharing state;
> - avoiding races;
> - cancellation;
> - bounding concurrency;
> - worker-pool construction;
> - subprocesses;
> - channels/queues;
> - debugging deadlocks/failures;
> - API verbosity;
> - agent readability.
>
> Do not reconstruct this from memory at the end.
>
> ---
>
> # 23. Agentic-era assessment
>
> Explicitly consider whether Nift’s concurrency model is friendly to agents.
>
> Questions:
>
> - Are lifetimes obvious?
> - Is ownership obvious?
> - Can an agent see which work is parallel?
> - Can it see synchronization boundaries?
> - Are shared mutable values explicit?
> - Is error propagation obvious?
> - Is it easy to accidentally forget an await/join?
> - Can tooling detect misuse?
> - Are atomics/mutexes semantically explicit enough?
>
> Again:
>
> **more syntax is not automatically worse if it carries useful concurrency semantics.**
>
> ---
>
> # 24. Nift-specific investigation
>
> Pay particular attention to:
>
> - thread creation overhead;
> - future creation/wait overhead;
> - scheduler behavior;
> - job queue implementation;
> - contention;
> - atomic performance;
> - process launch;
> - value/result transfer;
> - exception/error propagation between threads/tasks;
> - allocation per task;
> - stack size / memory per thread;
> - any global interpreter/runtime locks.
>
> If Nift shows a meaningful performance problem:
>
> - profile it;
> - create minimal reproducers;
> - write a core handover.
>
> **Do not modify Nift core from this experiment workspace.**
>
> ---
>
> # 25. Do not optimize the benchmark around Nift
>
> Avoid:
>
> - special Nift-only workloads;
> - hand-coded C++ doing the real task for Nift while peers do it in-language;
> - hidden native shortcuts;
> - reducing correctness requirements for Nift;
> - using an intentionally poor API for competitors.
>
> Use idiomatic implementations and document where semantic models differ.
>
> ---
>
> # 26. Local feasibility first
>
> Before cloud measurement:
>
> - install/freeze candidate versions;
> - implement all supported scenarios;
> - run correctness locally;
> - validate worker limits;
> - estimate total campaign runtime;
> - identify unsupported cells;
> - review fairness.
>
> Stop and report if a scenario cannot be compared honestly.
>
> ---
>
> # 27. Freeze before official measurement
>
> Freeze:
>
> - participant versions;
> - source implementations;
> - workload parameters;
> - sample counts;
> - commands;
> - expected outputs;
> - CPU-affinity policy;
> - environment.
>
> Record exact:
>
> - Nift source SHA;
> - suite SHA;
> - Python version/build mode;
> - Node version;
> - Bun version;
> - Go version;
> - Ruby version if included.
>
> Particularly for Python, document whether the interpreter is:
>
> - ordinary GIL build;
> - free-threaded build;
> - both, if intentionally tested as separate participants.
>
> Do not silently mix them.
>
> ---
>
> # 28. Official machine
>
> Use one fresh inexpensive Linode after local certification.
>
> Same machine for all participants.
>
> Prefer the established:
>
> - g6-standard-4;
> - us-east;
> - Ubuntu 24.04
>
> unless availability/price has changed materially.
>
> Record actual machine characteristics.
>
> Use all four CPUs for the main concurrency scenarios.
>
> If affinity is used, ensure it does not accidentally constrain a four-worker participant to fewer CPUs.
>
> Rotate participant order within rounds.
>
> ---
>
> # 29. Sample policy
>
> Use workload-sensitive counts:
>
> - tiny scheduler cells: 50–100+;
> - moderate cells: 20–50;
> - multi-second CPU cells: 5–10;
> - expensive stress cells: 3–5 if necessary.
>
> Use sufficient inner iterations for very tiny operations so clock granularity does not dominate.
>
> Preserve all raw samples.
>
> No outlier deletion.
>
> Warmups separate.
>
> ---
>
> # 30. Metrics
>
> Primary:
>
> - wall time.
>
> Also:
>
> - CPU time;
> - throughput/tasks per second;
> - maximum RSS;
> - process count where relevant;
> - worker count;
> - context switches if useful;
> - CPU utilization where useful.
>
> For parallel CPU scaling, derive:
>
> - speedup vs 1 worker;
> - efficiency vs worker count.
>
> Do not imply >1× speedup from unrelated changes in workload.
>
> ---
>
> # 31. Diagnostic profiling
>
> If something is surprising, use:
>
> - `perf`;
> - syscall summaries;
> - context-switch counts;
> - process/thread counts;
> - allocation profiling where useful.
>
> Diagnostics must remain separate from accepted timing samples.
>
> Do not pool profiling runs into benchmark results.
>
> ---
>
> # 32. Qualitative practitioner review
>
> At the end write:
>
> `docs/NIFT-CONCURRENCY-DX-REVIEW.md`
>
> Answer:
>
> > Would I actually choose Nift for concurrent scripting?
>
> Address:
>
> - Nift vs Python for concurrent automation;
> - Nift vs Node/Bun for async-heavy workflows;
> - Nift vs Go for concurrent/parallel tooling;
> - whether native threads are genuinely useful;
> - whether Nift’s futures/async abstraction is pleasant;
> - whether atomics/mutexes feel natural or too low-level;
> - whether error handling is good;
> - whether concurrency is safe enough for agent-authored code;
> - whether the APIs encourage races/deadlocks;
> - whether subprocess concurrency is particularly compelling;
> - what concrete capabilities are missing.
>
> If performance were equal, say which runtime you would prefer by workload and why.
>
> Avoid vague:
>
> > “ecosystem”
>
> explanations.
>
> Name the exact requirement:
>
> - async networking;
> - package ecosystem;
> - native libraries;
> - channels;
> - cancellation;
> - structured concurrency;
> - deployment;
> - etc.
>
> ---
>
> # 33. Explicit product conclusion
>
> Answer:
>
> > Is concurrency a genuine first-class strength of Nift, or merely a capability that exists?
>
> Possible outcomes:
>
> - weak;
> - usable;
> - good with caveats;
> - genuinely compelling.
>
> Do not decide this in advance.
>
> ---
>
> # 34. Nift Labs page
>
> Work in:
>
> `/home/nick/Repositories/nift/lab`
>
> Add:
>
> `https://lab.nift.dev/benchmarks/concurrency/`
>
> Add appropriate cards/links to:
>
> - Labs homepage;
> - benchmark collection.
>
> Preserve existing reports byte-for-byte except the intentional home/collection additions.
>
> ---
>
> # 35. Distinctive report design
>
> Give this benchmark its own visual identity.
>
> Do **not** clone Task Runners or Template Engines.
>
> Suggested direction:
>
> **“concurrency control room / execution lanes”**
>
> but visually distinguish it from task-runner DAG orchestration.
>
> Ideas:
>
> - multiple vertical execution lanes;
> - pulses/events moving concurrently;
> - worker/thread timelines;
> - fan-out/fan-in visualizations;
> - lock/atomic contention diagrams;
> - scheduler queue motifs;
> - CPU lane occupancy;
> - waiting vs running states;
> - process/thread badges.
>
> Think:
>
> > several things happening at once
>
> rather than:
>
> > dependency graph.
>
> Use:
>
> - dark charcoal background;
> - Labs fluorescent green;
> - restrained sherbet/sorbet accents;
> - high-information but uncluttered visuals.
>
> Preserve the shared fluorescent-green test-tube favicon.
>
> ---
>
> # 36. Suggested Labs page structure
>
> **Hero**
> - Nift vs Python / Node / Bun / Go
> - what “concurrency” means here
>
> **Concurrency models**
> - short capability/model comparison
>
> **Schedule almost nothing**
> - tiny task overhead
>
> **Fan out**
> - 10/100/1k concurrent jobs
>
> **Wait together**
> - timer/async workloads
>
> **Use all the cores**
> - CPU parallelism and 1/2/4 worker scaling
>
> **Worker pool**
> - bounded scheduling
>
> **Talk to each other**
> - producer/consumer
>
> **Share state carefully**
> - atomics/mutexes
>
> **Launch processes**
> - subprocess concurrency
>
> **Read together**
> - file I/O concurrency
>
> **When one fails**
> - error/cancellation semantics
>
> **Mixed workload**
> - CPU + wait + subprocess
>
> **Memory under concurrency**
> - waiting-task and worker memory scaling
>
> **Practitioner view**
> - Codex opinion
>
> **Method/evidence**
> - frozen versions, boundaries, raw evidence link
>
> ---
>
> # 37. Charts
>
> Useful charts could include:
>
> - scheduler overhead vs task count;
> - wall time vs concurrent waits;
> - CPU speedup vs worker count;
> - throughput vs workers;
> - memory vs waiting-task count;
> - subprocess throughput;
> - producer/consumer throughput;
> - contention throughput;
> - mixed-workload wall time.
>
> Every chart should have an exact table.
>
> Use logarithmic axes only where they genuinely improve readability and label them explicitly.
>
> Do not hide poor results by axis choice.
>
> ---
>
> # 38. Practitioner section on Labs page
>
> End with:
>
> **“Would I actually choose Nift for concurrent scripting?”**
>
> Label:
>
> **qualitative practitioner assessment / not benchmark evidence**
>
> Include a decision matrix such as:
>
> | Workload | Preferred runtime | Why |
> |---|---|---|
> | Concurrent project automation | ? | ? |
> | Async I/O service/tool | ? | ? |
> | Parallel CPU scripting | ? | ? |
> | Agent-maintained automation | ? | ? |
> | High-concurrency lightweight tasks | ? | ? |
> | Existing JS project | ? | ? |
> | Existing Python project | ? | ? |
> | New standalone concurrent tool | ? | ? |
>
> Fill this only after the campaign.
>
> Be candid if Go wins strongly in some categories.
>
> Be candid if Nift wins.
>
> ---
>
> # 39. Canonical evidence
>
> Publish canonical evidence under something like:
>
> `benchmarks/concurrency/<series-id>/`
>
> in:
>
> `nift-experiments/lab-evidence`
>
> Follow existing evidence structure.
>
> Preserve:
>
> - environment;
> - participant versions;
> - exact commands;
> - implementation source;
> - workload definitions;
> - raw samples;
> - warmups;
> - correctness results;
> - traces;
> - output hashes;
> - semantic capability observations;
> - profiling diagnostics;
> - rejected attempts;
> - audit;
> - publication identities;
> - browser checks;
> - teardown.
>
> ---
>
> # 40. Labs storage discipline
>
> The previous Template Engines campaign fixed Labs storage.
>
> Do not regress it.
>
> Raw benchmark data belongs in `lab-evidence`, not `lab`.
>
> Labs should receive only:
>
> - compact summary/publication input;
> - report source;
> - generated charts;
> - CSS/HTML/assets needed by the live page.
>
> At closeout report:
>
> - net tracked bytes added to Labs;
> - largest added file;
> - confirmation no raw sample arrays/traces/evidence corpora are present.
>
> Run:
>
> `python3 scripts/check_storage_policy.py`
>
> plus normal validation before publication.
>
> ---
>
> # 41. Browser validation
>
> Check:
>
> - 1440px;
> - 390px;
> - 320px.
>
> For:
>
> - concurrency report;
> - benchmark collection;
> - Labs homepage.
>
> Verify:
>
> - all charts load;
> - tables align;
> - execution-lane graphics remain understandable;
> - narrow tables scroll independently;
> - code snippets wrap/scroll safely;
> - long version/SHA values do not overflow;
> - no page-level horizontal overflow;
> - favicon unchanged.
>
> ---
>
> # 42. Preservation
>
> Verify all prior reports/assets are unchanged except intentional:
>
> - homepage card;
> - benchmark collection card.
>
> Produce a preservation receipt.
>
> ---
>
> # 43. Publication lifecycle
>
> Follow established order:
>
> 1. local implementation/correctness;
> 2. freeze suite;
> 3. official cloud campaign;
> 4. experiment result/audit commit;
> 5. canonical evidence commit;
> 6. Labs source update;
> 7. source push;
> 8. public publication;
> 9. live byte/browser verification;
> 10. teardown;
> 11. append lifecycle receipts.
>
> Keep:
>
> - measured suite SHA;
> - accepted evidence SHA;
> - lifecycle evidence SHA;
> - Labs source SHA;
> - public publication SHA
>
> distinct.
>
> ---
>
> # 44. Teardown
>
> Only after live verification:
>
> - delete Linode;
> - verify CLI absence;
> - verify authenticated API 404;
> - remove temporary SSH key;
> - remove known-host entry;
> - remove temporary CLI config/state;
> - run private-material scan.
>
> No campaign VM should remain.
>
> ---
>
> # 45. Checkpoints
>
> Commit/push at sensible stages:
>
> 1. repo + campaign brief;
> 2. participant/capability research;
> 3. canonical workloads;
> 4. participant implementations;
> 5. local correctness;
> 6. local feasibility;
> 7. frozen suite;
> 8. cloud results;
> 9. independent audit;
> 10. DX/practitioner review;
> 11. canonical evidence;
> 12. Labs report;
> 13. publication verification;
> 14. teardown/closeout.
>
> ---
>
> # 46. Final report back
>
> Return:
>
> - repository URL/local path;
> - participant set and rationale;
> - exact frozen versions/SHAs;
> - concurrency-model matrix;
> - scenario matrix;
> - unsupported cells and why;
> - sample/observation counts;
> - correctness result;
> - headline timing results;
> - CPU scaling;
> - waiting-task memory scaling;
> - subprocess results;
> - synchronization results;
> - failure/cancellation findings;
> - Nift performance bottlenecks if any;
> - Nift core handover items;
> - Codex’s qualitative preference by workload;
> - whether concurrency is a genuine Nift strength;
> - experiment commit;
> - canonical evidence commit;
> - Labs source commit;
> - public commit;
> - live URL;
> - Labs bytes added;
> - teardown status.
>
> ## Hard boundary
>
> **Do not modify Nift core from this experiment workspace.**
>
> If Nift needs changes, produce:
>
> - minimal reproducer;
> - profile evidence;
> - proposed fix direction;
> - expected general benefit
>
> for the separate Nift-core workspace.

The main thing I’d want Codex to resist is producing one giant table where “Node promise”, “Python process”, “Go goroutine”, and “Nift thread” are treated as if they’re the same primitive. The report will be much stronger if it says: **here is the problem; here is each runtime’s natural solution; here is what it costs and what semantics you get.**

That should give us a much more meaningful answer to whether Nift’s concurrency support is actually one of its standout strengths.