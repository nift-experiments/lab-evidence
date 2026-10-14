# Task runners — final v4.12.0 candidate

Frozen candidate c14d06835bca515a5281e41da0e40219c2d60ef0 and unchanged suite f37b63bd13cf71256607ba4652bcc911e270f94e. Full clean run: 1,527 observations, 1,434 measured + 93 warmups, 93 participant cells, 31 configurations. Independent cloud/local audits pass counts, rotation, action/output/order/concurrency/cache evidence and recomputed distributions; all 6,114 retained cloud result files are byte verified. No outliers removed. All 31 Nift wall and maximum-child RSS medians are lowest among these measured participants.

The first attempted official run reused preflight fixture caches and was rejected at the first changed leaf. Its 153 observations, failed command 154, logs and complete cache fixtures remain in the campaign graph-readiness/task-rejected-attempt. None are accepted here. This run starts from a separate fresh exact suite checkout and empty fixture caches, preserving the full original protocol.

Historical screening versus original 7f7 uses different hosts: Nift wall changes range −3.78% to +12.37%; RSS changes −1.64% to +2.15%. These are trends, not controlled core attribution. No major task regression is established. The build-system three-way diagnostic is a separate gate. No release approval or Labs publication is implied.
