# Retained-runtime diagnostic

Separate guarded ten-request schedule-1000 trajectory, after official timing completed. All six runtime trajectories passed every exact result/count oracle. This is not pooled with official medians and has no significance claim. Candidate and historical Nift run the same frozen adapter; peer implementations retain their own native concurrency primitives.

Candidate Nift remains sensitive to runtime reuse: first request 229.567 ms, tenth 1646.006 ms; post-response RSS 9808→18724 kB. Prior Nift also slows (229.949→1372.881 ms; RSS 9144→18236 kB). This establishes that the retained-runtime slowdown remains in this bounded reproduction. A single trajectory cannot establish a candidate regression or diagnose the cause. The official isolated-request series cannot support claims about sustained reuse.

The collector applied a 60-second per-request bound and a 6 GiB process-tree RSS watchdog; neither was reached. `/proc` RSS checkpoints are separate from inherited launch-floor affected wait4 memory. All raw trajectories are retained. Reference adapter/fixture symlinks in the collected archive were skipped on extraction; the frozen suite protocol supplies their source.
