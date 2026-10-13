# PRE-RELEASE DIAGNOSTIC SWEEP — NO LABS PUBLICATION

Candidate remains frozen; release recommendation held. Current Labs must remain unchanged. Teardown gates are completed measurement, independent audit, safely pushed evidence and completed required diagnostics; no live-publication requirement. See [full brief](DIAGNOSTIC-SWEEP-BRIEF.md).

# Campaign dashboard

Preparation checkpoint COMPLETE. Candidate7f7e487; all8CLIhashes identical. Five suites measuring; template/concurrency completed with cloud audits and local collection in progress; scripting independently accepted. All eight local/cloud certification gates pass.

| Benchmark | Linode | Frozen suite | Planned observations | State | Audit | Labs/live | Teardown |
|---|---:|---|---:|---|---|---|---|
| build-systems | 108024443 | e95bfe8 | 9,348 | official_measurement | pending | pending | retained |
| concurrency | 108024477 | d6d0cac | 11,506 | complete; collecting | cloud pass | pending | retained |
| filesystem-automation | 108024451 | 75e77bb | 15,016 | official_measurement | pending | pending | retained |
| scripting-benchmark | 108024446 | f889fff | 2,256 | accepted; same-node diagnostic pending | pass | pending | retained |
| shell-benchmark | 108024467 | aec1349 | 8,566 | official_measurement | pending | pending | retained |
| task-runners | 108024433 | f37b63b | 1,527 | official_measurement | pending | pending | retained |
| template-engines | 108024438 | 3c0dcdd | 18,700 | complete; collecting | cloud pass | pending | retained |
| website-generator-benchmark | 108024456 | a2890bc | 234 | official_measurement | pending | pending | retained |

## Scripting diagnostic follow-up

User requested same-node old/new A/B and focused regression investigation. Official accepted bytes remain immutable. Prior exact core SHA: `2eaec7d70e9ce2e698d0ba23a605fb9cf85317ff`; current candidate remains frozen. Scripting host retained; publication and release recommendation await findings. Other seven campaigns continue. Historical ranking, scenario peer ratios and read-only source hypotheses are under `scripting-regression-diagnostics/`.

Same-node scripting diagnostic independently audited: all 720 observations correct, 13 higher / 17 lower medians. Large function calls +145.76%, small +65.63%; sort/index large −30.71%. Source attribution awaits separated instrumentation. Release recommendation remains held.
