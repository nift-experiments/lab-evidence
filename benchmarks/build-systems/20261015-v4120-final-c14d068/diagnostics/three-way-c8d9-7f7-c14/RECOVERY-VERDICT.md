# Build recovery verdict — controlled exact-source comparison

The final candidate recovers the targeted full-dirty time/memory regression and retains strong no-op gains relative to released v4.11.0. It does not preserve every best original-candidate no-op median: heavy native one-worker no-op remains 11.90% slower than original 7f7, alongside 15.87% less maximum-child RSS. Keep that tradeoff visible.

All 180 observations (165 measured+15 warmups), nine variant cells, independent raw action/output/FNV/statistical checks, exact source/build identities and rotation pass cloud and local audits. Final CLI SHA matches the common all-eight artifact. No prior official samples were changed. Source/build identities are release c8d9c266, original 7f7e487, final c14d068. Comparison sources were built with the same GCC 13.3 normal C++17/O2/pthread configuration; all three use the same host, affinity 0–3, frozen fixture/action/timer and correctness boundaries. Mutation, baseline creation and reset/copy stay outside timing.

| Workload | Samples/source | Release median wall | Original median wall | Final median wall | Final maximum-child RSS |
|---|---:|---:|---:|---:|---:|
| Tiny 10,000 full, four workers | 5 | 16.676s | 20.976s | 14.976s | 17,572KiB |
| Native 1,000 heavy no-op, one worker | 30 | 406.815ms | 195.063ms | 218.274ms | 6,784KiB |
| Tiny 10,000 no-op, four workers | 20 | 754.151ms | 603.388ms | 586.915ms | 12,576KiB |

Tiny full versus release: wall−10.19%, CPU−10.95%, RSS−2.12%. Versus original: wall−28.60%, CPU−25.91%, RSS−47.25%. Five measured full builds per source are descriptive, not a significance claim.

Heavy native no-op versus release: wall−46.35%, CPU−46.95%, RSS−0.70%. Versus original: wall+11.90%, CPU+11.85%, RSS−15.87%. This is a remaining original-relative latency/CPU tradeoff, not a complete return to its fastest measured median. No causal attribution to a specific implementation change is established.

Tiny no-op versus release: wall−22.18%, CPU−24.84%, RSS+1.00%. Versus original: wall−2.73%, CPU+2.61%, RSS−41.62%. Wall/CPU/memory remain separate metrics. Linux wait4 RSS is maximum-child high-water usage, not summed concurrent memory.

No further build-host diagnostic work is needed for the authorized bounded sweep. All required primary and diagnostic evidence is retained. Host teardown is eligible after parent scan/push. Global release/publication approval remains the parent's all-eight decision; no tags, releases or package actions are implied.

Round-matched heavy no-op analysis confirms wall/CPU are higher than original in 28/30 pairs, while RSS is lower in 30/30. Marginal ranges overlap; this is a consistent tested-cohort slowdown, not a cross-machine inference. Build-only recommendation remains a bounded non-blocker relative to the released baseline; retain it in remaining gaps. See HEAVY-NOOP-PAIRED-ASSESSMENT.json and ALL-METRICS-AND-GATE.md.
