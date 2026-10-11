# Separate diagnostics, outside accepted timings

After accepted measurement and audit completed, the same cloud host ran software CPU-clock perf profiles at 99Hz with DWARF stacks: minimal 3000-task scheduling (239 samples), fixed 64-job/200000-iteration/four-worker CPU (1648 samples), and 10000-message 4→4 queue (505 samples). No lost samples were reported. CPU and queue outputs passed independent modular/value/count checks. Raw perf.data, text reports, request bytes, commands, binary identities and correctness receipts remain in canonical diagnostics/cloud/.

The scheduling profile contains string-keyed hash-table and shared AsyncState node work among its leading self samples. CPU profiles show AST/expression evaluation, parser execution and RuntimeValue handling; queue profiles show expression dispatch and value handling. Many frames in scheduling/queue call chains are unresolved, and cumulative children percentages overlap. These profiles support investigating registry/capture costs and interpreter/value overhead; they do not prove one allocation site is the sole cause or measure unique allocation bytes. Source-informed capture/registry hypotheses remain labelled as hypotheses in the core handover.

Cloud strace of minimal 1000-task scheduling attributes most cumulative syscall time to futex waiting; readlink/path checks recur thousands of times. Cumulative syscall time across threads is not a CPU-wall attribution. Local perf was blocked by desktop policy and no policy was weakened.

The first cloud diagnostic wrapper used find -type f and missed installed versioned perf symlinks. Its initial outputs are retained separately. The official Ubuntu package was already installed; selecting command -v perf corrected the wrapper (perf 6.8.12). Only diagnostic profiles were rerun; accepted observations were sealed and unchanged.

The cloud ten-request reused-runtime probe checks every result for all five engines and is not pooled with booted-isolated accepted timings. Nift schedule 1000 request 1/request 10: 275.644ms/2142.862ms. Python 10.693/5.150ms, Node 7.239/2.062ms, Bun 14.412/1.083ms, Go 6.745/2.464ms. Individual diagnostic samples are descriptive, not campaign medians. The earlier incomplete cloud cohort and local probe are separate origins, not merged distributions.

Local held-memory and lock-error reproducers remain labelled local: Nift 10000 unfinished captures used about 13,700MiB, outside the official 8GiB range; a malformed expression while owning a mutex stranded a waiting sibling until the diagnostic watchdog. No Nift core was modified.
