# Fairness review and cohort boundaries

Accepted measured suite: bb62138daf8bb7cda20a2194ab97fe8395a9e337.

- Same fixture bytes, child executable, kernel iterations and exact result contract. No Nift native shortcut for the workload.
- Scripting/compiled deployment differs intentionally: Go is the compiled concurrency reference, not labelled a scripting runtime with identical startup.
- Async waits use each natural execution model. Nift native blocking sleep is documented instead of describing it as a suspended event-loop timer.
- True CPU parallelism uses Nift threads, Python spawn processes, JS worker isolates and Go goroutines; ordinary Python GIL threads are not passed off as multicore bytecode execution.
- All engines inherit four-CPU affinity. Explicit pool workers 1/2/4; native async runtime policy remains visible. The scheduler is not silently changed for one participant.
- Every result validates exact IDs/values, count, expected errors/exits and canonical hashes. CPU oracle is independently audited through modular exponentiation; file hashes through a polynomial representation of the fixture bytes.
- Genuine atomics only; unavailable Python atomics and JS native mutex cells are not filled with incompatible substitutes.
- Queues capacity64, but authored promise/mutex rings and native channels are explicitly different contracts. Nift polling and copy costs remain measured.
- Fresh wall includes start/work/output/exit. Persistent-labelled wall is an **isolated already-booted request**, not steady-state reuse: a new runtime reaches BOOT before each observation, then one request is clocked and exit is excluded. All participants follow this policy. Per-request CPU-pool creation remains included.
- Warmup rounds are retained; they warm host/cache state, not an indefinitely retained parser/VM. No accepted sample is removed for its value.
- The first partial cloud cohort at 7ea2963 reused runtimes across rounds and exposed increasing Nift completed-task registry cost. Its raw observations remain rejected campaign evidence because the cohort did not complete its frozen coverage and its retained-state feasibility had not been certified. The behavior is a real finding, shown prominently, plus a separate ten-request reuse diagnostic for all participants. Calling it rejected does not deny that its results demonstrate runtime growth.
- Nift 10000 held futures used13700MiB locally. Both official boundaries are outside the practical8GiB host range. This is a visible unsupported-range result, not an OOM timing or a faster substituted task count. Remaining participants retain their10k cells.
- Scheduling tiny-arithmetic and fan-out use the same flat create/join shape in independently sampled cohorts. They are not claimed as different executor capabilities.
- 5ms process-tree RSS may miss short-lived children and double-count shared pages. wait4 maximum RSS is maximum individual participant/descendant high-water RSS, not a precise helper-only or simultaneous-tree peak. Short CPU tick values have limited precision; wall time is primary.
- Profile and reuse diagnostics are never pooled into accepted timing distributions. Shared cloud CPUs, warmed filesystem cache and fixed workload sizes bound the conclusions.
