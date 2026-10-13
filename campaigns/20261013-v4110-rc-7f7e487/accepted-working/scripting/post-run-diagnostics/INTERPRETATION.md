# Separated current-candidate CPU diagnostics

Three single invocations of the unchanged large function-call, loop and JSON-parse sources were profiled after the complete official run. All three outputs passed the original oracle. `perf` used the software `cpu-clock` event at 99 Hz with DWARF callchains. Kernel settings were not changed. These profiles are not timing observations and are not merged into the accepted distributions.

| Workload | Samples | Lost | What the current profile supports |
| --- | ---: | ---: | --- |
| function-calls | 60 | 0 | The ordinary source-call and argument-evaluation path is visible, including `evaluate_source_call`, `form_call_arguments`, `evaluate_call_operand`, expression typing, string searches, AST parsing and allocation. |
| loops | 9 | 0 | Statement/AST dispatch, source-view handling, variable lookup and string work appear. Nine samples are too few to rank small hotspots reliably. |
| JSON parse (`inject` then `.size()`) | 38 | 0 | `parse_runtime_json` accounts for 89.47% cumulative samples, including descendants. Kernel `clear_page_rep` is 47.37% self samples; page-fault/allocation frames are prominent. |

Function-call cumulative samples include `evaluate_source_call` at 83.33%. Self samples include `malloc` at 5.00%, expression typing at 5.00%, `logical_or` AST parsing at 3.33%, and evaluated-operand vector reallocation at 3.33%. Those small percentages represent only one to three samples. Cumulative values overlap and must not be added together. Unnamed libc addresses remain unnamed; no identity is invented for them.

The useful follow-up is to inspect whether an already prepared scalar function-call argument is still routed through unnecessary generic expression/filesystem classification and reparsing, and whether argument staging can avoid repeated allocations while retaining exactly-once evaluation and error contracts. The profile shows those paths in current execution; it does not prove which work is redundant or which change caused the cross-host historical deterioration.

For the measured JSON implementation, allocation/materialization and associated page-zeroing deserve inspection alongside parsing. This is specifically the existing `inject` implementation, including construction of runtime values, rather than an abstract parser-only microbenchmark. The tiny loop profile is a directional indication of interpreter dispatch/value work, not a quantitative subsystem ranking.

No old-binary A/B was performed. Shared VM scheduling, changed observation dates and the peer startup deterioration remain qualifications on prior-to-current timing claims. No Nift source, flags, official sample, benchmark implementation or kernel policy was changed by these diagnostics.
