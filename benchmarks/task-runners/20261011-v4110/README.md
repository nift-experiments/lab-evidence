# Nift / Turbo / Nx — task orchestration

Accepted same-node series `20261011-v4110`: 1,527 observations (1,434 measured and 93 warmups), 93 runner cells. Frozen suite `56384cace6821a1541e7773cf1d8ce7a4c688ed8`; Nift source `8f90fd49d8b2484c1d732cb440ea442e53e08172`. All samples retained. See environment, scope and independent validation.

`observations.jsonl` references row IDs: raw `<id>.trace.jsonl` lives in `action-traces/`, `<id>.metrics.json` in `metrics/`, and stdout/stderr in `action-logs/`. To rerun the frozen auditor, stage these files flat in an external working directory alongside observations/plan, then run the measured suite's scripts/audit.py. No values are transformed by this canonical directory organization. Frozen protocol sources are in `protocol/`; current explanatory methodology is explicitly outside that frozen export.

Graph definitions, mutation records, exact event sets and independently reconstructed output-manifest digests are retained. Explicit per-output SHA maps are independently reconstructed and verified against the original observed manifest digests in output-hashes/. Identical maps are stored once and referenced by an observation index. The frozen auditor also reconstructs deterministic output bytes. Semantic failure/recovery traces and input snapshots are separate diagnostics, never pooled with successful timing observations.

Nift tracked clean-state validation is distinguished from native Turbo/Nx local cache hits and missing-output replay. Outputless DAG and environment-input capability differences are scoped visibly. Fresh CLI invocation, daemon off, no remote cache, fixed scenario order, rotated runner order, Linux wait4 maximum-child RSS (not summed process-tree memory). The tiny body includes each runner's native launch layer.

Lifecycle and publication receipts are added after source/main and live checks, then verified node deletion. Measured, evidence, publication and lifecycle revisions remain distinct.
