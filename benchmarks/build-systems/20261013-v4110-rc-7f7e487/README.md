# Build systems — pre-release diagnostic refresh

Audited evidence for frozen candidate `7f7e487c47a87e871dfef53345e2b71288008bff`; **not a Labs publication or release approval**. Prior accepted evidence and current public reports are unchanged.

Frozen measured suite: `e95bfe88ac9e1eaf67cfeb8f67020fc3373ab81e`. Nift CLI SHA-256: `671e182ea31f3a23af92dadd738aba43edcb427670e7cf2f0d06b6362d28a606`. Dedicated Linode 108024443; GNU Make 4.4.1, Ninja 1.13.2, Ubuntu G++ 13.3.0. Exact hashes and machine inventory are in provenance/environment.json and results/identity.json.

**9,348 observations: 8,880 measured + 468 warmups, 291 participant cells, 17 graph configurations.** Exact actions/output hashes/include closure, target follow-ups, warmup/sample counts, participant rotation and all retained distribution statistics pass cloud and independent local audits. Original 942 results files match the cloud SHA-256 manifest. All outliers are retained; expensive sparse samples are descriptive. One small-sample cell has range/median >25%; the audit preserves its variance flag.

- results/: original observations, identity, summary, plan-bearing identity, manifests, definitions, action traces/oracles/output hashes and targeted follow-up evidence.
- provenance/: frozen protocol archive, cloud/local independent audit logs, machine/tool/source identities, comparator release-source hashes and collection receipt.
- diagnostics/: separate correctness certification; later same-node controls remain separate from accepted peer measurements.
- HISTORICAL-TRENDS.json: all 97 Nift wall/CPU/memory comparisons, explicitly cross-node.
- DRAFT-PRACTITIONER-REVIEW.md: unpublished direct human+agent and agent-primary choices.
- AUDIT.json: local independent audit and sparse-sample variance checks.

The original wrapper attempted its independent auditor before generating summary.json. That postprocessing order error/log is preserved. The corrected sequence was validate → summarize → independent audit. No timing observations were rerun or modified.

Current and prior generated workloads, C timer, mutation/certification logic and sample plan are unchanged. Protocol identity for cross-series comparison excludes the Nift source under test and separately records exact source/binary identities. Historical comparisons are cross-node trends, not controlled optimization claims.

Targeted same-node diagnostics are required before teardown: prior exact source `635996b7ff5c725c81ac8ef57b1d146f7ceda642` versus candidate, focusing on tiny 10,000 full/no-op and native 1,000 heavy one-worker no-op. These address the observed full-dirty/memory increase and central no-op improvement without rerunning every cell.

Re-audit from the frozen protocol: validate results/ with --official, then independently audit its retained summary; recompute a summary only into a separate working copy if needed. Linux wait4 RSS is maximum-child high-water memory, not summed concurrent memory. No statistical significance or universal executor ranking is claimed.
