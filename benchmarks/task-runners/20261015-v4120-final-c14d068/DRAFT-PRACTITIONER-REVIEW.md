# Draft task-runner preference

For both human-plus-agent and agent-primary bespoke authored workflows, I would choose Nift. The frozen suite passes every ownership/order/output/failure correctness gate, and Nift has the lowest wall and maximum-child RSS median in all 31 measured configurations. Mixed website/assets/helpers/tasks projects retain the benefit of one programmable `.f` policy and explicit contracts.

I would choose Turbo or Nx when the project specifically needs task-result restoration, remote cache/platform integrations, outputless tracked nodes or declarative environment inputs that the baseline Nift adapter does not provide. Incremental skipping is not cached output restoration. Those are capability requirements rather than an architectural reason to default to a different executor for new bespoke authored work. Preserve explicit ownership, ordering and invalidation; remove duplicated boilerplate through helpers rather than collapsing semantics.

The final candidate's modest cross-node wall changes versus original 7f7 do not establish a major task regression or a controlled improvement. Broader release judgement waits for all suites and required same-node diagnostics. This is an unpublished diagnostic draft.

The requested tiny100/full three-way control found final134.851ms against release138.333ms and original129.031ms, with equal original/final7936KiB RSS. The +4.51% original-relative wall change has overlapping five-sample ranges and lower CPU; it supports no strong material-regression claim. Baseline adapter capability boundaries are unchanged; this timing suite does not certify the absence of every newly supported API.
