# Task runners — pre-release diagnostic refresh

This is audited diagnostic evidence for candidate `7f7e487c47a87e871dfef53345e2b71288008bff`, **not a Labs publication or release approval**. The current public report and previous accepted series are unchanged.

Frozen suite: `f37b63bd13cf71256607ba4652bcc911e270f94e`. Nift CLI SHA-256: `671e182ea31f3a23af92dadd738aba43edcb427670e7cf2f0d06b6362d28a606`. Dedicated Linode: 108024433. Node 22.22.1, npm 9.2.0, Turbo 2.11.7, Nx 23.3.0; exact executable/library hashes and machine inventory in provenance/environment.json.

**1,527 retained observations: 1,434 measured, 93 warmups, 93 participant cells.** Independent output reconstruction, exact task sets, dependency order, concurrency limits, cache receipts, sample counts, participant rotation, identities and every retained summary statistic passed. Cloud/local summary bytes match. All 6,113 original results files are byte-verified against the cloud manifest. See AUDIT.json.

## Layout

- results/: original flat cloud observations, metrics, stdout/stderr, task traces, plan, identity, complete marker and summary. This layout permits running the frozen task auditor directly.
- provenance/: exact protocol source archive, machine/tool identities, raw-file manifest, wrapper/install/collection logs and collection receipt.
- diagnostics/: separate initial semantic certification and cache-disabled correctness smoke; excluded from official distributions.
- HISTORICAL-TRENDS.json: all 31 Nift median comparisons, qualified as cross-node trends.
- DRAFT-PRACTITIONER-REVIEW.md: unpublished candidate assessment.
- SAME-NODE-DIAGNOSTIC-ASSESSMENT.json: explicit assessment of whether targeted old/candidate controls are needed.

Re-audit: extract provenance/protocol.tar into an isolated directory; run its scripts/audit.py against results/. The additional shared campaign graph-readiness/audit-task-order-distributions.py independently checks rotation, full frozen plan, source/binary identity and distributions without changing results.

The fresh refresh harness uses the previously accepted Nx disabled-cache receipt correction. Commands, C timing boundary, generated work and sample plan are unchanged. Generated workflow and task bodies have no changes relative to the prior measured suite; example .f scripts outside the generated protocol acquired explanatory/example additions only.

Nift has the lowest observed wall-time and maximum-child RSS median in all 31 configurations here. This covers the specified generated authored workflows; it is not a universal task-runner ranking. Linux wait4 RSS is maximum-child high-water memory, not aggregate concurrent project memory. Sparse expensive-cell samples remain descriptive; no outliers were removed.
