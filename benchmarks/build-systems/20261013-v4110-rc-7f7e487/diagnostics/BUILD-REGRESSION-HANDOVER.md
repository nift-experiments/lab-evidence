# Controlled build diagnostic handover

Exact prior source `635996b7ff5c725c81ac8ef57b1d146f7ceda642` versus candidate `7f7e487c47a87e871dfef53345e2b71288008bff`, independently built with the same GCC 13.3 release flags on the same dedicated host. The alternating cohort independently passes identity, counts, actions, output equivalence and statistics: 120 observations, 110 measured, 10 warmups. Primary peer distributions remain unchanged.

| Controlled workload | Samples per version | Wall median change | CPU median change | Maximum-child RSS change |
|---|---:|---:|---:|---:|
| Native 1,000 heavy, one-worker no-op | 30 | −47.4400% | −47.9543% | +15.0943% |
| Tiny 10,000, four-worker no-op | 20 | −15.7628% | −25.4817% | +62.1456% |
| Tiny 10,000, four-worker full dirty | 5 | +21.2458% | +16.4340% | +63.0412% |

The full-dirty regression survives same-node control alongside substantial no-op improvements. Five full-build samples support a descriptive observation, not a significance claim. Exact medians and all raw observations appear in `same-node-635-vs-7f7/COMPARISONS.json` and its results directory. Memory is Linux wait4 maximum-child high-water RSS, not summed concurrent memory.

## Post-timing mechanism evidence

One paired strace capture and one paired CPU-clock perf capture were made after timing completed. All four instrumented runs passed producer action/output correctness checks. These are diagnostic captures, excluded from benchmark distributions. Archived raw perf data and both exact executable artifacts support replay. No samples were lost.

Both variants execute 20,001 execve calls. Candidate openat/read/close counts each increase by 30,236, and lseek increases by 60,708; newfstatat decreases by 59,764. Both retain 370,029 failed readlink probes, so those are not a newly introduced failure. Sampled kernel `copy_present_pte` self share rises from 8.91% to 16.11%. Its call chain passes through fork and `nift_run_pipeline`. Together with larger RSS this suggests investigating parent memory and fork page-table amplification, as well as extra metadata I/O. It does not isolate a root cause or assign elapsed-time percentages to either mechanism. Strace accumulated syscall seconds are not wall-clock duration.

Read-only source inspection locates fork in `src/Process.cpp`; shared runtime JSON/source caches are present in both revisions, so their mere existence cannot explain a newly introduced regression. No ablation or allocation attribution was performed. Relative malloc sample share alone does not establish greater allocation cost. The build evidence does not establish a shared cause with scripting regressions.

## Next core investigation

Measure parent RSS and retained allocation state by lifecycle phase; attribute additional metadata opens/reads to specific paths; compare fork costs with the same graph/action count. Investigate the changed process/project-state paths with an isolated reproducer before proposing a fix. Preserve the confirmed no-op wins and explicit artifact/order/invalidation/recovery contracts. A separate core change and new candidate identity would require new certification, rather than mutating this frozen cohort.

All required timing, independent audits and bounded post-timing profiles are retained locally. No further diagnostic work requires this host. Teardown is eligible after the parent verifies and pushes the canonical evidence. No Labs publication or release approval is implied.
