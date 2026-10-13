# PRE-RELEASE DIAGNOSTIC SWEEP — NO LABS PUBLICATION

Candidate remains frozen; release recommendation held. Current Labs must remain unchanged. Teardown gates are completed measurement, independent audit, safely pushed evidence and completed required diagnostics; no live-publication requirement. See [full brief](DIAGNOSTIC-SWEEP-BRIEF.md).

# Campaign dashboard

Six suites are independently audited and closed with verified host deletion. Build remains in its final matrix; filesystem primary passed cloud audit and both collectors completed; local collection/audits in progress. Candidate and Labs remain unchanged.

| Benchmark | Linode | Frozen suite | Planned observations | State | Audit | Labs/live | Teardown |
|---|---:|---|---:|---|---|---|---|
| build-systems | 108024443 | e95bfe8 | 9,348 | official_measurement | pending | pending | retained |
| concurrency | 108024477 | d6d0cac | 11,506 | closed diagnostic series | independent pass | pending | deleted; CLI/API verified |
| filesystem-automation | 108024451 | 75e77bb | 15,016 | official_measurement | pending | pending | retained |
| scripting-benchmark | 108024446 | f889fff | 2,256 | closed diagnostic series | pass | pending | deleted; CLI/API verified |
| shell-benchmark | 108024467 | aec1349 | 8,566 | closed diagnostic series | independent pass | pending | deleted; CLI/API verified |
| task-runners | 108024433 | f37b63b | 1,527 | closed diagnostic series | independent pass | pending | deleted; CLI/API verified |
| template-engines | 108024438 | 3c0dcdd | 18,700 | closed diagnostic series | independent pass | pending | deleted; CLI/API verified |
| website-generator-benchmark | 108024456 | a2890bc | 234 | closed diagnostic series | independent pass | pending | deleted; CLI/API verified |

## Scripting diagnostic follow-up

User requested same-node old/new A/B and focused regression investigation. Official accepted bytes remain immutable. Prior exact core SHA: `2eaec7d70e9ce2e698d0ba23a605fb9cf85317ff`; current candidate remains frozen. Scripting host is now deleted after retained audits/diagnostics. Release recommendation remains held; remaining campaigns continue. Historical ranking, scenario peer ratios and read-only source hypotheses are under `scripting-regression-diagnostics/`.

Same-node scripting diagnostic independently audited: all 720 observations correct, 13 higher / 17 lower medians. Large function calls +145.76%, small +65.63%; sort/index large −30.71%. Separated instrumentation identifies extra call-path allocation churn; exact root-cause attribution remains provisional. Release recommendation remains held.

Scripting closeout: official accepted results and720-observation paired A/B plus24instrumented runs safely pushed at2b98e06. Node108024446 deleted; CLIabsence/API404 verified; per-host temporary access removed. Shared temporary access remains only for the build host.

Latest collector checkpoint: build9,348/9,348; timing complete; postprocessing/local audit pending; shellfull8,566observations independently audited; targeted A/B/profiles complete; host deleted; filesystem15,016observations independently accepted; targeted stat/walk/filter A/B pending. No failures reported; no new audited engineering conclusions. Partial timing values are excluded from synthesis/rankings. Seven completed hosts remain CLI/API-confirmed absent. Labs source/public trees remain clean.

All eight full measurement plans completed. Build audit/collection and filesystem targetedsame-nodecontrols remain beforefinaldiagnosticcloseout. Do not confuse completionofmeasurement withreleaseapproval.

Filesystemclosed:primary/filter15,016observationsindependentlyaccepted;24-observationmatched-nodegaincontrolsretained/pushed4206b47. Host108024451deletedandCLIabsence/API404verified. Onlybuildaudit/collection/diagnosticdecisionremainsbeforefinalcloseout.

All eight official series independently audited. Completepeerleague520cells nowincludesbuild;463matchedhistoricalNifttrendsremaincross-node. Buildsame-nodecontrols stillrunning; holdlastnodeuntilaudit/evidence/diagnosticscomplete.
