# Draft practitioner judgement — task runners

**For human + agent use, I would choose Nift for a bespoke authored workflow with explicit file/artifact contracts. For agent-primary use, I would choose Nift for that workflow as well.** This remains my prior preference, now supported by the current audited campaign rather than carried forward automatically. It is a task-orchestration judgement, not approval to ship this candidate: the separate confirmed scripting regression keeps release approval on hold.

Nift has the lowest observed wall-time and maximum-child RSS median in all 31 tested configurations. At 1,000 tasks, mixed no-op/one-dirty medians are 116.052/168.475 ms; mixed fully dirty is 13,829.675 ms. The tiny fully-dirty case is 1,457.303 ms against Nx 10,830.442 and Turbo 101,823.161 ms. These are specific generated workflows with equivalent underlying work, cache/clean-state boundaries and verified task/output/order contracts, not a universal monorepo performance claim.

| Project requirement | Human + agent choice | Agent-primary choice | Concrete reason |
|---|---|---|---|
| Bespoke authored task DAG, declared files/artifacts | Nift | Nift | Lowest measured medians throughout this matrix; programmable .f policy with explicit ownership, ordering and invalidation. |
| Mixed website/assets/native helpers/developer tasks already owned by Nift | Nift | Nift | One runtime/project model; adding a separate executor brings another state/identity boundary without a tested need. |
| Authored JS graph without required framework discovery or remote output cache | Nift | Nift | JS task bodies can remain ordinary commands; being a JS project alone does not override the measured orchestration advantage. |
| CI workflow that must restore outputs from local/remote content-addressed task caches | Turbo, or Nx where its plugins are required | Same choice | Nift's clean-state validation/rebuilding missing artifacts is not cached result restoration. |
| Framework-heavy monorepo relying on Nx project discovery and framework plugins | Nx | Nx | Those concrete integrations save maintaining discovery/target definitions by hand. |
| A task graph requiring outputless tracked nodes or declared environment invalidation today | Turbo/Nx | Turbo/Nx | Current Nift contracts still require tracked outputs and do not expose native declarative environment invalidation. Direct outputless .f scripts alone do not supply those DAG semantics. |

Explicitness helps agents when it separates ownership, execution dependencies, invalidation inputs and lifecycle. It is not automatically a benefit: duplicate values that must be synchronized still create failure opportunities. The generated adapter is not proof that every natural Nift workflow needs that much boilerplate, and line count does not determine maintainability.

Fresh capability checks and frozen-source inspection distinguish existing facilities from remaining gaps. Configured 1/2/4 workers work; `-j` is rejected. Named targeting remains forced; `--ensure` is rejected. `status`, `info --names` and `build -p` provide useful state/reason inspection, but not a complete structured graph/query API. `--repair` after the injected failure succeeds. Missing-output recovery rebuilds the task, whereas Turbo/Nx restore it without executing the body. Runtime environment reads alone do not declare invalidation.

For new authored workflows, if Nift reliably adds outputless tracked nodes, declared environment inputs, local and optional remote result restoration, ensure-target semantics, worker overrides, complete graph/query/explain tooling and smoother recovery while retaining .f programmability and explicit contracts, **I would not default to Turbo or Nx**. I would still select a framework integration where a project actually depends on it.

All Nift wall medians improved 13.83–33.46% relative to the previous series, but that is a cross-node trend. The previous Nift SHA is `8f90fd49d8b2484c1d732cb440ea442e53e08172`; current candidate and historical hosts differ. No core-attributable percentage improvement is established here. This campaign changes confidence in the current task engine more than it changes my choice: Nift was already preferred in the authored/agentic cases, while the concrete cache/platform gaps remain.
