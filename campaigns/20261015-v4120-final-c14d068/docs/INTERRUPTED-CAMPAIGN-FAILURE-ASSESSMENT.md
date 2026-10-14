# Interrupted campaign failure assessment

Superseded candidate: 342287696eaf619d942054826e43b8565639c83b. Final candidate: c14d06835bca515a5281e41da0e40219c2d60ef0.

## Available campaign evidence

The local interrupted namespace records all eight suites at inspection, with no host creation receipts, suite command launch receipts, official samples or cloud state. Preparation stopped while CI failures were being investigated. Thus no official suite is evidenced as started here. If additional interrupted-run material exists elsewhere, it has not been supplied; no failure commands or partial measurements are invented.

| Suite | Started official jobs | Passed/failed official jobs | Source used | Pending |
|---|---|---|---|---|
| build-systems | none evidenced | none | no official executable built/deployed | full certification/measurement |
| concurrency | none evidenced | none | no official executable built/deployed | full certification/measurement |
| filesystem-automation | none evidenced | none | no official executable built/deployed | full certification/measurement |
| scripting-benchmark | none evidenced | none | no official executable built/deployed | full certification/measurement |
| shell-benchmark | none evidenced | none | no official executable built/deployed | full certification/measurement |
| task-runners | none evidenced | none | no official executable built/deployed | full certification/measurement |
| template-engines | none evidenced | none | no official executable built/deployed | full certification/measurement |
| website-generator-benchmark | none evidenced | none | no official executable built/deployed | full certification/measurement |

## Recorded failures were CI, not official benchmark jobs

1. Linux behavioural corpus, workflow 38607076815 / job 116000601945: the full aggregate Make invocation (retained exactly in `ci/interrupted-exact-command-receipt.json`), failing at `test-v410-filesystem-recipe-guard` exited 2. Guard line 19 expected recipes 0/fallbacks 1/backends 1/operands 2, received recipes 0/fallbacks 0/backends 1/operands 2. The preceding probe checks process success and exact output before this assertion. Classification: core instrumentation/contract-counter mismatch; no benchmark output error established by this log. Full stdout/stderr retained in the original ci/linux-behavioural-failure.log.
2. Linux complete FFI wall, workflow 38607077638 / job 116000604708: `make warnings-check` exited 2 before subsequent FFI walls. Compiler treated misleading indentation at ParserExpression.cpp:2180 and unused ordinary_arguments parameter at :1538 as errors. Classification:strict core build / CI hygiene failure, not evidence of failed FFI execution. Full log retained in original ci/linux-libffi-warnings-failure.log.
3. The same workflows report macOS/Windows failures; original workflow status / job receipts are retained, and platform logs will remain separate if deeper inspection is needed.

Partial CI successes may support their own correctness/build contracts; they are not official benchmark timings. No sample is salvaged into final candidate evidence.

## Infrastructure

Current CLI/API inventories agree on one account instance and zero campaign-labelled instances. No old 342 campaign host inventory/state exists in the available workspace. The unrelated instance is left untouched. The preceding 7f7 campaign has eight verified CLI absence / API 404 receipts. No fresh provisioning occurred before this review.

## Required preflight

Build a clean exact-c14 checkout, reproduce `warnings-check` and `test-v410-filesystem-recipe-guard` unchanged, then independently certify all prior frozen suite jobs. Retain logs, exit codes and identities. No core patches or weakened gates; only documented harness compatibility corrections if necessary. No fresh Linodes before preflight is green.

## Final-candidate reproduction

Unchanged `warnings-check`, `test-v410-filesystem-recipe-guard`, and `test-call-semantics` commands pass on the clean exact final checkout. Logs and identity are retained. Counts: 35/35 call contracts, 10/10 nested-index, 10/10 method-error; negative replay control detected. This establishes recovery of the observed preparation failures, not performance recertification.

The local reproduction executes the failing targets unchanged; it is not represented as a rerun of every target in the original aggregate Make invocation. The full original invocation is preserved separately. Final exact-SHA CI status is independently verified.
