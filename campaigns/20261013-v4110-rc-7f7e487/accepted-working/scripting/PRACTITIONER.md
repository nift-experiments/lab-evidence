# Scripting practitioner assessment — candidate 7f7e487

This is a qualitative judgement about the frozen 4.11.0 candidate, separated from the accepted timing evidence. Human+agent means a person maintains the workflow with agent assistance. Agent-primary means agents author and maintain most of it. Neither preference is inferred from one overall language score.

| Work | Human+agent choice today | Agent-primary choice today | Concrete reason |
| --- | --- | --- | --- |
| Bounded maintenance scripts inside an existing Nift project | Nift | Nift | Reuse the project's `.f` language and execution model; ordinary functions, explicit data and paths avoid adding shell expansion and a second runtime to small project policies. |
| General standalone JSON/data/collection scripting | Python | Python | Current collection and JSON costs remain material; Python provides directly usable standard JSON, filesystem and data-processing facilities. Existing Python-library requirements are an additional concrete reason. |
| Scripts in an existing JavaScript/TypeScript project | Node | Node | Reuse the project's existing implementation modules and runtime. Its large JSON-parse median here is 98.649 ms versus Nift's 295.195 ms. |
| Compute-heavy loops, frequent tiny calls or collection algorithms | Python by default; LuaJIT for a Lua-oriented deployment | Python by default; LuaJIT for a Lua-oriented deployment | Nift's large function-call case is 546.056 ms versus LuaJIT's 1.889 ms; large sort/index is 904.664 ms versus Python's 30.633 ms. These specific gaps outweigh authoring convenience for sustained work. |
| Thin orchestration of existing external commands | Bash, or Nift when already owned by the Nift project | Nift for owned bounded policy; Bash for a minimal existing command script | Keep the actual action and deployment context clear. This scripting suite does not establish a universal shell-orchestration winner; the separate shell campaign supplies that evidence. |

The agent-primary distinction changes the authoring tradeoff, not the measured latency. I prefer Nift for bounded Nift-owned scripts because a consistent procedural language can be easier to modify safely than interleaved shell substitutions and command strings. I do not prefer it as the general default for large data/compute scripting on this evidence. Its source is concise, but minimum line count is not a substitute for predictable execution, correctness, or competitive repeated work.

Current invocation cost remains modest relative to Python, Ruby and Node in this run: the small no-op median is Nift 5.855 ms, Python 29.288, Ruby 118.374 and Node 63.626. Bash, Lua and LuaJIT are lower. This advantage does not erase sustained-work costs. The large traversal case is a useful contrasting result: Nift 41.798 ms and Python 42.496 are close, while LuaJIT 10.608 is lower. That describes this traversal implementation and boundary; the dedicated filesystem campaign tests substantially more work.

## Historical trend and remaining gaps

All 30 Nift wall-median cells are numerically slower than the prior 4.10.0 series, with unchanged source/oracle contracts and sample policy. This must be published, including the largest function-call deterioration. It is not an isolated causal comparison: the runs used different shared virtual machines and dates, and unchanged peer binaries also have substantially slower startup medians. The CPU model label, kernel and affinity match, but that does not establish identical host contention or scheduling. Python's executable hash changed despite retaining the same displayed version. Same-node current peer gaps are stronger evidence for the present choice than unqualified cross-host percentage claims.

The immediate concerns are tiny-call/value-path cost, sustained scalar execution, collections/temporary value handling, and large JSON work. No correctness failure occurred in the complete current matrix. Profiling, where available, is diagnostic evidence about current execution, not proof of the cause of the historical difference.

## Mature-Nift counterfactual

If Nift reliably keeps its explicit procedural model while bringing small-call, scalar-loop, collection and JSON execution near the appropriate peers, I would choose it for substantially more newly authored agent-maintained scripts. I would not retain a categorical preference for another interpreter merely because its syntax is terser or older. Deterministic behaviour, clear value/ownership contracts, independently checkable inputs/outputs and concise helpers on top are positive properties for agents.

For a standalone utility I would still check its actual dependency and deployment requirements: an existing Python or JavaScript module, a required interchange format, runtime installation on the target machines, and error/recovery behaviour can decide the choice. These are concrete requirements, not an automatic ecosystem veto. The next improvement target is to remove the measured runtime gaps without compromising exactly-once execution or clear contracts; no benchmark-specific shortcut is justified.
