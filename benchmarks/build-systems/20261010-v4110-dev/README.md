# GNU Make / Ninja / Nift — native build orchestration

Final official series: `20261010-v4110-dev`. One fresh shared-CPU Linode, four vCPUs, 8 GB RAM, Ubuntu 24.04. GNU Make 4.4.1, Ninja 1.13.2, and Nift v4.11.0 development snapshot rebuilt from frozen source `635996b7ff5c725c81ac8ef57b1d146f7ceda642`. The version/source/binary identities and compiler/linker details are authoritative in `identity.json` and `provenance/`.

Frozen suite: `24671011425ef8bd0b9f05adb1c87682e9ca33b7`. `protocol/` retains the exact sources and hashes. `provenance/frozen-source/` contains the patch against a public ancestor and the source-tree identity needed to reconstruct the frozen Nift snapshot. No Nift core edits were made by this campaign.

## Read the data

- `observations.jsonl`: every warmup and measured observation, with elapsed time, CPU time, maximum-child RSS, exact action oracle, output hashes and correctness status.
- `summary.json`: measured-only distributions; no observations removed. Median/min/max always; p95 when n≥20 and p99 when n≥100, linearly interpolated at (n−1)q.
- `validation.json`: complete sample plan, action-set, content-addressed artifact and output-parity checks.
- `definitions/`, `manifests/`, `action-oracles/`, `action-traces/`, `output-hashes/`: retained canonical graph/input definitions and independently checked execution/output records. Follow the paths actually referenced by observations.
- `provenance/independent-audit.json`: independent rotation and percentile recomputation, including low-sample spread qualifications.
- `diagnostics/accepted-remote-smoke/`: correctness/timing-boundary gate, not official performance samples.
- `diagnostics/accepted-noop5000/`: bounded syscall diagnostic. Strace elapsed times are distorted; use counts only.
- `diagnostics/rejected-recipe-markers/` and `diagnostics/rejected-unique-rules/`: both provisional series preserved and explicitly rejected. They are never pooled with the final official series. Interrupted attempt artifacts are not headline observations.

## Scope and boundaries

Native graph: N leaf translation units, ten static archives, two generated artifacts, generated/main objects and one executable: N+15 actions. Light and compiler-heavy profiles use identical compiler/flags across participants. Include closures, exact actions, deterministic object/archive/executable hashes and final executable stdout are checked. Tiny graphs are separate independent FNV hash actions, not C++ throughput.

Sizes 100/1,000/5,000/10,000 and workers 1/2/4 form a bounded 17-graph matrix, not a complete Cartesian product. The retained plan specifies all 291 cells and 9,348 observations including warmups. No-op n=100; modest native edits n=20; tiny leaf n=50; compiler-heavy/expensive cases n=3–10. Some bounded cases have n=5; each table reports its actual n. Large three-sample cells support descriptive medians/spreads, not robust tails or significance claims.

Fixture restoration, mutation and timestamp checks happen outside the C timer. Build orchestration, native action processes, bookkeeping and the wait are inside. Clean + rebuild includes common output cleanup inside timing; clean full removes outputs outside timing. Linux wait4 RSS is maximum-child high-water memory, not summed simultaneous process-tree memory. CPU time includes reaped descendants.

Make/Ninja use actual native inputs, compiler dependency files/database and shared rules; Nift uses its supported tracked-action/hooks model, prerequisite ordering and explicit file sidecars. A targeted Nift build is a forced named module target, compared only with a dirty target. An untimed full followup verifies the executable. Deletion/failure differences are documented in local certification; failure checks are not performance rows.

## Lifecycle

Provisioning and verified deletion receipts contain a hashed instance identity, never connection credentials. Collection precedes deletion; publication is verified before teardown. The campaign uses its frozen export even if unrelated work advances the local Nift checkout afterward.
