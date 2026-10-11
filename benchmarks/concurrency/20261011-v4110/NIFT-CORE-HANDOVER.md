# Concurrency diagnostics for the separate core workspace

Frozen core: 445f4d3545cf031bcce4bf77a2b4a61ffb3b4c4f. No core edits made here. Diagnostic timings are not accepted benchmark samples.

## 1. Task environment growth
Minimal `probes/scheduling-growth.f` creates and retains futures for a one-increment task. Separate local diagnostics: 100 tasks ~8.7ms; 1000 ~133.6ms; 3000 ~1212.1ms. These individual diagnostic observations support investigating superlinear creation overhead, not a formal complexity proof.

The held-gate adapter additionally retains all unfinished tasks. 1000 used ~148MiB, 10000 ~13700MiB on the local host. The latter cannot be certified on the 8GiB official machine and is an explicitly unavailable official cell. Completed tasks can release captured environments, so it is incorrect to infer that ordinary 10000-task scheduling holds the same RSS.

Frozen ParserExpression.cpp line 1922 traverses transferable values in every variable scope and clone_worker_binding snapshots them. Submission also moves callable/module/resource registries into each worker. The growing future list and async registry are plausible amplification mechanisms. This is a source-informed hypothesis; use the retained profiles/reproducers to locate the actual allocation and CPU hot paths before changing semantics.

Proposed direction: measure copied environment/registry bytes and task allocations; share immutable callable/module metadata; persistent/COW snapshots or explicit capture selection that preserves snapshot isolation and shared-resource identity. Do not silently convert ordinary captured mutable values to shared state just to improve benchmarks. Expected benefit: bounded memory and creation cost for held/queued work, including agent-created fan-out.

## 2. Wait semantics
Nift async pool uses max(2, hardware_concurrency) native workers. `sleep` blocks a worker. Large timer sets queue behind available workers instead of registering suspended timers. Add nonblocking timer/wait futures with explicit cancellation/lifetime contracts if lightweight waiting concurrency is a target. Expose a documented pool override that respects affinity/deployment limits. Keep explicit native threads for CPU work.

## 3. Queue / synchronization ergonomics
The suite needs a mutex ring with 1ms backoff because no public blocking channel/condition variable was found. Provide bounded channel/send/receive/close or a condition primitive with precise ownership/backpressure/error contracts. Preserve useful explicitness; remove redundant manual coordination.

`probes/queue-lock-error.f` fails while owning a mutex and a sibling waits forever; the diagnostic supervisor kills it after three seconds. A guarded-lock helper or scoped ownership/cleanup contract would make error paths safer. Do not auto-unlock another thread's mutex without a defined contract. Validate malformed expression failures and recoverable error paths separately.

## 4. Task errors and cancellation
Recoverable `user.*` errors transfer through await, repeated await re-observes the same error, successful siblings finish. Add documented cooperative cancellation/group ownership, deadline handling and aggregate failure collection if structured concurrency is desired. Existing lifetime cleanup does not substitute for cancellability. Explicit joins, shared handles and typed error codes are useful agent-visible contracts.

## 5. Profiles / limitations
Local syscall summary for 1000 scheduled tasks spends most cumulative traced syscall time in futex calls; readlink/path checks also recur thousands of times. Cumulative futex time includes waiting across threads and is not wall-time CPU attribution. Local perf access is restricted (`perf_event_paranoid=4`); the failed attempt is retained rather than weakening desktop policy. Cloud profiles, when available after the official run, are separate evidence.

Numeric CPU work is in-language for all engines. Before claiming a global interpreter lock or blaming native stack memory, inspect accepted CPU scaling and profiles. This campaign does not establish either claim merely from slower arithmetic.

## 6. Completed-future retention across requests
The rejected first cloud cohort isolates a second issue: schedule-1000 fresh requests remained about250ms, whereas the same persistent parser grew from244ms to8782ms by request20; RSS rose9→29MiB. The work and worker policy were unchanged. This motivates inspecting growth of `async_instances_` and worker registry cloning after handles leave user scope. It does not prove a specific leak without an ownership audit.

Accepted comparisons now use new, already-booted isolated request state for **all** participants; startup remains excluded from that boundary. They do not claim steady-state long-lived runtime throughput. Rejected repeated-request observations and a separate repeated-runtime probe stay visible. Core fix should reclaim unreachable completed-task bookkeeping without breaking repeated await on live handles, snapshot resource transfer or owned work cleanup.

## 7. Post-measurement cloud profiles and fixed-work scaling

See DIAGNOSTICS.md and canonical diagnostics/cloud/. Software CPU-clock captures contain 239/1648/505 samples for scheduling 3000, CPU 4 and queue 10000. All outputs checked; no samples pooled. AsyncState/hash-table work appears in scheduling self samples; AST/expression/parser and RuntimeValue handling appear in CPU/queue. Partial unresolved stacks and overlapping children percentages limit attribution. Instrument copied binding/registry sizes and allocation counts before claiming a single root cause.

Nift fixed-work CPU scaling is 3.950× at four workers (98.7% efficiency), so native execution is genuinely parallel for this kernel. Its 3905.406ms absolute four-worker median versus Go 15.741ms motivates scalar interpreter/value-path work separately from the concurrency scheduler. Native thread architecture should not be discarded merely because scalar dispatch is expensive. Native channels/guarded synchronization can remove polling/manual-copy coordination while preserving explicit sharing contracts.
