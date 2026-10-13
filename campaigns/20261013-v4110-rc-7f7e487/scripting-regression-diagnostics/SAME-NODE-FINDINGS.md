# Same-node diagnostic findings

This is a separate pre-release diagnostic, not a replacement for the accepted campaign. Both binaries ran on the retained scripting node, CPU 0, with the same frozen measurement supervisor, workload sources, fixtures, oracles, environment and 10 measured + 2 warmup policy. Every old/new pair was adjacent; first-version order alternated and was balanced 5/5 in measured rounds. All 720 observations passed correctness. The freshly built old binary is byte-identical to the previous accepted 4.10.0 binary; the candidate binary remains unchanged.

The results are mixed: 13 medians increased and 17 decreased. These counts describe numerical medians, not statistical significance. They do not support the claim that every workload regressed on the same node.

| Case | Old median ms | New median ms | Absolute delta ms | Relative change | Pair/range check |
| --- | ---: | ---: | ---: | ---: | --- |
| function calls, large | 228.284 | 561.026 | +332.742 | +145.76% | 10/10 pairs slower; new minimum exceeds old maximum |
| function calls, small | 6.080 | 10.069 | +3.990 | +65.63% | 10/10 pairs slower; nonoverlapping ranges |
| sort/index, large | 1088.855 | 754.437 | −334.417 | −30.71% | 10/10 pairs faster; nonoverlapping ranges |
| scan, large | 110.635 | 93.988 | −16.646 | −15.05% | 9/10 pairs faster; ranges overlap |
| Fibonacci, large | 182.107 | 164.111 | −17.995 | −9.88% | 9/10 pairs faster; ranges overlap |

The two function-call cases give particularly clear evidence of a current-revision regression under the tested boundary. The large sort/index result is an equally important counterexample to a blanket slowdown story. Smaller and overlapping changes need their absolute size and paired observations considered rather than a universal percentage cutoff.

## Comparable allocation and syscall diagnostics

After timing completed and was collected, unchanged full-size sources ran once per binary under the same heaptrack 1.5.0, strace and software-CPU perf commands. All 24 instrumented invocations produced the expected output. These observations are never merged into timing distributions.

| Case | Old allocation calls | New allocation calls | Additional calls |
| --- | ---: | ---: | ---: |
| function calls, large | 900,967 | 1,701,054 | 800,087 |
| function calls, small | 9,967 | 18,054 | 8,087 |
| BFS, large | 2,748,737 | 3,842,094 | 1,093,357 |
| frequency count, large | 1,501,237 | 1,501,254 | 17 |

Across the 1,000- and 100,000-iteration function-call sources, allocation slope increases from 9 to 17 allocations per call-loop iteration. That is eight additional allocations per iteration plus an 87-allocation difference in the constant component. It includes loop/call machinery, not only the callee body. Heaptrack's reported peak heap remains about `116.6K` in both call versions (tool-printed units, not converted MiB/KiB), consistent with allocation churn rather than growth in retained heap.

Both large function-call runs have exactly 110 syscalls with identical per-syscall counts, including 17 `newfstatat`, 10 `openat`, seven `read` and three `readlink`. Their extra execution cost is not explained by filesystem syscall amplification in this specimen. Do not extrapolate that finding to the separate filesystem benchmark.

The new call allocation stacks contain `evaluate_call_operand` and `form_call_arguments`; these are absent from the old report. The profiles also show source-call dispatch, source/string handling and RuntimeValue work. The source review's call-argument staging/ownership/provenance paths are therefore an evidence-supported investigation lead. This is not a commit bisection or a proof that all added staging is redundant. Preserve exactly-once evaluation, ownership and provenance semantics while examining repeated parsing/classification and avoidable temporary allocations.

Frequency count slows descriptively in the paired run without a material change in allocation count. Therefore allocation churn is not an adequate single explanation for every observed difference. BFS has increased allocations, but source and profile inspection must determine the relevant paths independently.

Perf is a low-sample diagnostic (large call: old 24 samples, new 53, no losses). Unnamed libc addresses remain unnamed. Percentages are not used as precise causal shares of the regression. Heaptrack's end-of-process "leaked" label is not treated as proof of a program leak.

## Preservation and next boundary

Accepted raw observations, benchmark sources, candidate source/binary, both core checkouts and kernel policy remain unchanged. Full timing provenance, launch order, machine snapshots, libraries, raw/warmup observations, software profiles, syscall summaries and allocation traces are retained in `same-node/`.

No release recommendation is made here. This diagnostic establishes the specific call regression and the mixed overall result, and provides a focused lead for read-only investigation or a separately authorized future fix.
