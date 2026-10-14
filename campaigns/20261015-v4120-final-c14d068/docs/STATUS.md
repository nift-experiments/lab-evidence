# Final v4.12 recertification — c14d068

Candidate: `c14d06835bca515a5281e41da0e40219c2d60ef0`, unreleased Nift v4.12.0.

The observed interrupted preparation failures pass unchanged on the clean final candidate. All nine exact-SHA CI workflows passed. The available interrupted evidence contains CI/preparation failures, with no official suite launches or measurements. Sanitized CLI/API inspection found no campaign-owned hosts; the unrelated account instance is untouched.

Local gates passed: scripting (188), website (18), shell (RC 18; startup 76 prepared and 76 fresh; expanded 141), build (324), template (393 supported plus semantic and variant checks). Task full smoke, concurrency certification, and full filesystem/filter certification remain in progress. No fresh cloud spend until all eight local gates pass.

The complete frozen sample plans total 67,153 observations. Three-way same-node recovery diagnostics remain separate. New cloud tooling uses an isolated namespace and an explicit all-eight preflight gate. The previously approved 20-minute follow-up now tracks this final candidate.

No Labs, tags, releases, packages or download publication is authorized.
