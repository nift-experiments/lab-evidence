# Final v4.12 recertification — c14d068

Candidate: `c14d06835bca515a5281e41da0e40219c2d60ef0`, unreleased Nift v4.12.0.

The observed interrupted preparation failures pass unchanged on the clean final candidate. All nine exact-SHA CI workflows passed. The available interrupted evidence contains CI/preparation failures, with no official suite launches or measurements. Sanitized CLI/API inspection found no campaign-owned hosts; the unrelated account instance is untouched.

Local gates passed: scripting (188), website (18), shell (RC 18; startup 76 prepared and 76 fresh; expanded 141), build (324), template (393 supported plus semantic and variant checks). Concurrency also passed all 608 supported cells and semantic gates (32 explicitly excluded cells retained). Filesystem also passed all 662 primary and 90 filter cells with independent fixture/distribution audits. Task full smoke also passed all 186 observations and its independent audit. All eight suites are green. Eight fresh dedicated hosts are provisioned; clean exact-candidate build launch is in progress. All eight local gates passed; all eight fresh g6-standard-4 hosts are provisioned in us-east. Official timing has not started.

The complete frozen sample plans total 67,153 observations. Three-way same-node recovery diagnostics remain separate. New cloud tooling uses an isolated namespace and an explicit all-eight preflight gate. The previously approved 20-minute follow-up now tracks this final candidate.

No Labs, tags, releases, packages or download publication is authorized.
