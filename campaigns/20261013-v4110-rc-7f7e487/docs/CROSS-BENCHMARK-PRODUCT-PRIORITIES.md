# Product priorities — interim diagnostic draft

1. **Function-call/value-path overhead:** confirmed same-node scripting regression, central to authored and agent-maintained policy code. Investigate repeated argument parsing/classification and temporary allocation while retaining exactly-once evaluation, ownership and provenance. This is the current release blocker; no core edits in this campaign.
2. **BFS / collection runtime cost:** sizeable current deficits and a paired slowdown; inspect its own allocation paths rather than assigning the call-staging cause automatically.
3. **Preserve sorting/scan wins:** large sort/index improves30.71%; scan improves15.05% descriptively. Regression remediation must not erase these wins or alter semantics.

This is provisional, not a completed eight-suite ranking. Frequency, practical project impact, repeated signals and concrete preference blockers will be considered once all audits and targeted diagnostics finish. Raw deficit alone is not product priority.
