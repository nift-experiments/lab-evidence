# Read-only candidate source review

Compared exact accepted old core `2eaec7d70e9ce2e698d0ba23a605fb9cf85317ff` with candidate `7f7e487c47a87e871dfef53345e2b71288008bff`. No core or benchmark edits.

Plausible leads, not established causes:

- `55cb323` unifies exactly-once expression and readonly-method completion. The added `Parser::evaluate_call_operand` parses argument expressions, resolves binding paths, takes owned RuntimeValue snapshots, determines binding types and checks location provenance. `form_call_arguments` retains source and operand vectors. These are concrete extra staging/parsing/copying paths to examine for the disproportionately slower function-call workloads; compare profile and allocation counts across both binaries before attributing a regression.
- `091c002` shares immutable lambda syntax metadata. This aims to avoid repeated syntax ownership while preserving fresh captures/identity; whether ordinary named calls benefit is workload-dependent.
- `2c14413` prepares numeric AST operator dispatch; `58ddd70` partially prepares heterogeneous loop bodies; `1f61884` restores shrink-safe prepared loops. These can affect scalar/loop workloads, including fallback and safety checks. They cannot explain every scenario without measurements.
- `b820fe0` compacts Number keys for single-selector sort_by. It targets a restricted sorting path rather than all collection operations.
- `021e763` adds prepared filesystem entry pipelines and `d55d149` uses one Linux statx snapshot. These plausibly affect filesystem cases, but the scripting traversal workload must actually exercise those paths to benefit.
- `10822e7` prepares restricted template loop emission; this is not automatically relevant to ordinary scripting.
- JSON parsing remains a profile lead: the existing separate candidate profile is dominated by parse_runtime_json / clear_page_rep. No direct RuntimeValue.h change appears in this revision diff; RuntimeValue use and copying still changed through evaluator code.

Existing candidate-only profiles identify hot regions, not old-versus-new cost differences. Source changes above are hypotheses to test with the same-node diagnostic, not a release verdict. Allocation/syscall instrumentation must remain outside measured A/B samples.
