# October 2026 benchmark campaign

This is the preserved initial Nift 4.7.2 campaign report. The shell and scripting pages now display the separate [8 October Nift 4.8.0 rerun](BENCHMARK-RERUN-20261008.md); website-generator measurements remain the series documented below.

Completed correctness-gated measurements on one disposable Ubuntu 24.04 Linode g6-standard-4: 8 GB RAM, four shared vCPUs, us-east, AMD EPYC 7601. All timings ran serially on CPU 0. Kernel 6.8.0-134-generic, Python 3.12.3. Tool/fixture preparation is outside timing; OS caches were uncontrolled.

## Repository and methodology changes

Scripting: retired the correctness-blind timed runner and historical cross-run aggregation. Every invocation now passes its exit/output oracle. Exact finite Decimal equality replaces approximate numeric checks. JSON transformation and frequency counting v2 remove unequal scratch-file/grouped-array work. sort-index replaces a misleading sort-search name; endpoint-only two-pointer is omitted. Unimplemented/partial families remain explicit gaps. Historical evidence is preserved and labelled.

Website: current CLI, complete route/title/heading/body checks, Hugo raw HTML, Astro file routes and minimal VitePress theme. Nift incremental output is checked byte-for-byte against a full rebuild. Fresh-fixture and warm full are separate. Website raw mode application-cold retains shared node_modules dependency caches; it is not a complete application-cache reset. Historical schema-4 fixtures and aggregate RSS are incomparable.

Shell: Bash, Zsh, Fish, Nushell and Nift; bare/empty/light/moderate synthetic RC, separate login paths where supported, prepared and fresh-HOME distributions, six small orchestration/native/file workloads. Every invocation is validated; full config state is independently certified. Native Bash/Zsh RC-body diagnostics remain separate from total startup.

All suites use a compiled C fork/exec-to-wait4 timing boundary. RSS is waited-child high-water, not simultaneous aggregate process-tree memory. PTY first-prompt timing uses a compiled bridge and excludes Python heap-fork overhead; calibration is disclosed, never subtracted. Original PTY and earlier-pin/workload runs are retained as diagnostics.

## Tested versions

bash: GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu) · zsh: zsh 5.9 (x86_64-ubuntu-linux-gnu) · fish: fish, version 4.9.3 · nu: 0.116.1 · nift: Nift v4.7.2
nift: Nift v4.7.2 · python: Python 3.12.3 · ruby: ruby 3.2.3 (2024-01-18 revision 52bb2ac0a6) [x86_64-linux-gnu] · lua54: Lua 5.4.6  Copyright (C) 1994-2023 Lua.org, PUC-Rio · luajit: LuaJIT 2.1.1703358377 -- Copyright (C) 2005-2023 Mike Pall. https://luajit.org/ · node: v24.21.0 · bash: GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu)
Nift: Nift v4.7.2 · Hugo: hugo v0.167.0-3fff6fb5c267dacb26280c78dbe8c344054249c8 linux/amd64 BuildDate=2026-09-28T14:50:38Z VendorInfo=gohugoio · Node.js: v24.21.0 · Astro: 7.3.6 · VitePress: 1.6.4

## Headline observations

| Shell | Bare prompt median ms | p95 ms | p99 ms |
|---|---:|---:|---:|
| bash | 3.085 | 4.389 | 10.181 |
| zsh | 4.066 | 6.018 | 9.531 |
| fish | 28.816 | 38.159 | 63.973 |
| nu | 24.791 | 34.054 | 50.740 |
| nift | 2.846 | 4.128 | 9.780 |

These are 100-sample prepared-state distributions; fresh-state startup has 30 samples. The PTY floor and shared-CPU scheduling limit interpretation of differences of only a few milliseconds.

| Generator | 10,000-page fresh full median s | Warm full median s | Fresh RSS MiB |
|---|---:|---:|---:|
| Nift | 3.853 | 6.516 | 16.4 |
| Hugo | 5.005 | 6.455 | 230.2 |
| Astro | 217.771 | 216.335 | 3553.3 |
| VitePress | 264.538 | 256.875 | 2518.5 |

Scripting representative Nift medians (10 samples each):
- sanity/noop/small/nift: 4.242 ms
- sanity/loops/large/nift: 111.160 ms
- sanity/function-calls/large/nift: 453.703 ms
- graphs-trees-search/bfs/large/nift: 1156.251 ms
- structured-data/json-parse/large/nift: 252.523 ms
- filesystem/traverse/large/nift: 143.794 ms

## Caveats, surprises and defensibility

The Zsh normal configuration path invokes Ubuntu system compinit; fresh HOME rebuilds completion state. This is retained and documented rather than disabled. Rich shells, POSIX pipelines, Nift structured process capture and native file APIs have differing architecture; equivalent output is not feature parity. Tail observations are visible and no corrected samples are cherry-picked.

Scripting is defensible as a bounded idiomatic corpus, with startup-sensitive, compute and practical rows. It is not a universal language score; SQLite/mixed workflows and broader practical coverage remain gaps. Website is defensible as minimal generated-page throughput, not real-site migration or equally shipped client features. Shell is defensible for the exact terminal/configuration/invocation boundaries; concurrent jobs and long pipelines require separate future experiments. No Nift source changes or winner-oriented tuning were made.

Nift’s warm full build was slower than its fresh-fixture build; warm is a state boundary, not a promised speedup. Bash won the trivial invocation comparison and Fish the external-100 comparison against Nift.

Presentation: eight standalone measured figures, including corpus scaling curves and startup distributions; visible all-language scripting tables; aligned numeric headers; keyboard-accessible horizontal scrolling. Browser checks at 320, 390 and 1440 px found no root overflow or broken images.

## Verification and publication

All published tables are generated from validated raw samples. Clean-checkout reproduction, complete RC certification, measurement tests, full Labs build, local-link/palette validation, desktop/mobile rendering and credential scans are recorded in the evidence and source history. Disposable-instance deletion was verified by a subsequent Linode API HTTP 404. Address, credentials and private connection state are excluded.

- https://lab.nift.dev/benchmarks/
- https://lab.nift.dev/benchmarks/scripting/
- https://lab.nift.dev/benchmarks/website-generator/
- https://lab.nift.dev/benchmarks/shell/

Measured source revisions:
- shell: `e5078b5a79e33b09e5d23af8946ccc264867b385`
- scripting: `67171ae1a7f93a54d224bbf55dff4143a9871cdc`
- website: `4947b42c863782ba6be0fdbbd2003d60d6d0d3d4`

Published benchmark source revisions:
- shell-benchmark: `e79253d24fd9c74ccc8616186a0a1cd2bbf7e726`
- scripting-benchmark: `4c648ef761423a20173f6095691955dc4040ce53`
- website-generator-benchmark: `be3bd5f8eb059d8a54197e4706dd1c11d442b97c`

Follow-up presentation: scope exclusions use compact accessible dashes to preserve numeric-column widths. Corpus scaling includes original no-op, changed-leaf and shared-template incremental curves. A separate explicitly targeted one-page series is measured on another same-plan node, with its own full-build reference and complete-output gates; it is never pooled with original observations.

Targeted supplement: Ubuntu 24.04, same g6-standard-4/us-east plan, AMD EPYC 7542, pinned Nift 4.7.2, one CPU and build thread. Five measured samples plus one warmup per mode/size. Explicit changed-page target medians: 100 pages: 8.071 ms, 1,000 pages: 25.847 ms, 10,000 pages: 188.069 ms. Measured source: `803f35667049ff36330468467a522c356292927d`. Follow-up deletion also verified by HTTP 404.
