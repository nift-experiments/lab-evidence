# Current Labs data audit

PASS. All eight current reports match final c14 evidence; no unlabeled stale current series found. The CPU0 website numbers were current, but their prominence obscured the separately audited all-core result.

| Page | Old data found? | Updated? | Historical retained? | Validation |
|---|---|---|---|---|
| website-generator | No | True | Explicitly labeled | PASS |
| build-systems | No | False | Explicitly labeled | PASS |
| task-runners | No | False | Explicitly labeled | PASS |
| filesystem-automation | No | False | Explicitly labeled | PASS |
| shell | No | False | Explicitly labeled | PASS |
| scripting | No | False | Explicitly labeled | PASS |
| template-engines | No | False | Explicitly labeled | PASS |
| concurrency | No | False | Explicitly labeled | PASS |
| benchmark index / homepage / shared cards | No | False | Explicitly labeled | PASS |

Source: 973e6fbb1aa3b4708ed1a0abe332cb108f3e671b

Publication: 5294d4889bcfbc86f33c7d0152fc101ae7a36ce6

Data pin: `19e390183b9bcb039abe6aa553ad88a2305b49ee`. Full per-page checks and live hashes are in CURRENT-DATA-AUDIT.json.

All-core results now appear in the hero and first detailed section `#parallel`; official controlled results follow at `#results`. CPU utilization, workload audit, historical host sensitivity and incremental workflow remain separate and qualified. No static graph data changed. No unrelated reports changed. Desktop 1440px and mobile 390/320px passed with loaded images and no horizontal overflow. All ten live HTML routes match local bytes; links and storage guard passed.

Scripting 198.620ms is the recovery diagnostic, not the official current peer-series median of 193.726ms; these valid cohorts remain explicitly separated.
