# Website workflows and AI-DX verdict — unpublished qualitative review

AI-DX is a separate primary axis, not a footnote to fresh throughput. Normal Nift development/publishing may use `nift build`; `--all` is forced full work, not a mandatory synonym for publish. Confidence depends on complete declared/discovered dependencies and the project's actual validation/deployment contract. The fixture tests do not certify arbitrary production content/assets/helper graphs.

## Workflow boundaries (10k pages, median ms)

| Workflow | Nift | Hugo | Comparable? | Performance-only result |
|---|---:|---:|---|---|
| Fresh fixture full | 3015.980 | 2623.337 | Yes, equivalent minimal-page intent, native implementations; CPU0 | Hugo takes less time in this cell |
| Warm forced full | 2613.877 | 2723.813 | Yes, matching full boundary | Nift takes less time in this cell |
| No changes | 842.446 | Not measured | No matched Hugo cell | No cross-tool winner established |
| One-page content edit | 858.452 | Not measured | No matched Hugo cell | Nift supported/validated; no relative claim |
| Shared-template edit | 3488.225 | Not measured | No matched Hugo cell | Nift supported/validated; global invalidation can be expensive |
| Explicit targeted changed leaf | 151.855 | Not measured | Separate supplemental cohort | Nift supported/validated; no relative claim |
| Publish after small edit | Build leg as above; deployment not timed | Not measured | No end-to-end publish comparison | Do not call forced full the normal publish boundary |
| Multiple edits/assets/helper changes | Not measured here | Not measured here | Not covered by this minimal fixture | Must validate project contracts separately |

The practical Nift loop for the measured leaf case is edit→`nift build`→about0.858s build→inspect; inspection and deployment latency are not included. No-op is about0.842s; explicit changed-leaf target about0.152s in its distinct cohort. A global template edit rebuilt/validated affected outputs; it is not represented by the leaf latency. First clones, state loss, clean CI and reproducibility checks still need the fresh/full measurements.

## AI-DX evidence assessment

| Dimension | Nift | Hugo | Evidence limit |
|---|---|---|---|
| Project structure | Fixture declares content/output dirs and tracked page name/title/template mapping | Fixture uses content/frontmatter, hugo.toml and layout lookup conventions | Source-inspected fixture affordances, not measured editing difficulty |
| Ownership/dependencies | Explicit tracked outputs and template associations are inspectable; order and invalidation remain distinct | Native content/layout model supplies conventional relationships | Full comparative graph inspection not exercised |
| Targeted edits | Named changed-leaf command tested | No matching targeted test | Not proof Hugo cannot support targeted workflows |
| Incremental semantics | No-op/leaf/shared tested against full output snapshot parity | Only fresh/warm full measured | Cannot infer Hugo incremental correctness from full builds |
| Rebuild explanation | Exact c14 CLI source exposes status/why-rebuild text | Not evaluated here | No comprehensive comparative explain test |
| Structured feedback | JSON config/tracking; structured benchmark records are harness-generated | TOML/frontmatter fixture; benchmark records also harness-generated | Product-native general build-status JSON not established for either |
| Mixed content/assets/helper logic | Programmable .f/lifecycle model offers one project policy | Conventional site model; custom orchestration not audited | Nift advantage is design judgment, not timed authoring success |
| Hidden conventions | More explicit associations reduce inference, but tracking can become inconsistent | Familiar conventional layouts may simplify ordinary sites but require lookup knowledge | Neither minimum files nor human familiarity is a safety metric |
| Failures/debugging | Core BUILD-SCRIPTS docs describe propagation, checks and repair | Not comparatively injected/tested | No blanket superiority claim |
| Autonomous edits | Explicit ownership/inputs/targets can constrain an agent's edit surface | Conventional templates can be simple when requirements fit | No controlled agent task trial; knowledge of APIs matters |
| Intended output changes | Harness checks changed leaf, unaffected snapshot and full parity | Route/content oracle for full builds | Harness proof is not automatic production enforcement |
| Partial-state recovery | Documented build-script repair mechanisms | Not tested comparatively | Neither fully certified by website fixture |
| Operational simplicity | One runtime/project model for mixed work; metadata requires disciplined maintenance | Site conventions may reduce custom policy for ordinary content | Requirements determine which is simpler |

Evidence: frozen benchmark.py fixture construction; campaign.py105–127 incremental/full parity; targeted_campaign.py25–45 unchanged-output and full parity checks. Exact candidate docs/BUILD-SCRIPTS.md describes lifecycle/output ownership/order/invalidation/failure constraints; src/CLI.cpp status why-rebuild path. These source observations are not additional timed results.

## Direct practitioner choices

| Site category | Human + agent | Agent-primary | Rationale and condition |
|---|---|---|---|
| Human-authored conventional content/theme site | Hugo when standard conventions/theme fit; preserve an established estate | Hugo for an existing Hugo estate with no need for mixed policy | Convention fit and low custom policy, not a claimed universal speed win |
| Human + agent actively authoring templates/assets/helpers | Nift | Nift | Inspectable contracts and programmable integrated policy, assuming the agent understands the APIs |
| New agent-primary authored site | Nift | Nift | Explicit artifact ownership, native targets and project policy aid bounded automated edits |
| Mixed procedural publishing project | Nift | Nift | One model for content/assets/helpers/tasks; strong AI-DX fit |

Across these categories weigh clean speed, steady-state edits, publish build leg, output correctness, AI-DX, ecosystem requirements and operational simplicity separately. For an objective restricted solely to current fresh10k throughput choose Hugo; for current warm-full throughput choose Nift. Missing incremental peer cells are unknown, not Hugo losses. No measured total quality score or universal preference follows.

## Additional diagnostic ideas from the attached brief

The first attachment proposes all-core/scaling profiles, thread/syscall counts, fixture byte/work accounting and new host-sensitivity experiments. Those are a separate supplemental experiment design, not measurements already performed. Current evidence does not establish why the same Hugo binary improved47.59% across hosts, actual OS thread counts, or default/all-core scaling. GOMAXPROCS1 limits Go execution parallelism, not the number of OS threads. CPU0 affinity restricts available CPU execution; it does not prove either process creates only one thread. No host is provisioned or frozen official plan changed by this qualitative scorecard. Read-only fixture accounting can proceed; new timings must remain separately labeled and must not overlap the two ongoing official hosts.
