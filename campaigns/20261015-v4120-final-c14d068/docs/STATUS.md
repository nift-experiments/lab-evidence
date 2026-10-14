# Final v4.12 recertification — c14d068

Candidate: `c14d06835bca515a5281e41da0e40219c2d60ef0`, unreleased Nift v4.12.0.

The observed interrupted preparation failures pass unchanged on the clean final candidate. All nine exact-SHA CI workflows passed. The available interrupted evidence contains CI/preparation failures, with no official suite launches or measurements. Sanitized CLI/API inspection found no campaign-owned hosts; the unrelated account instance is untouched.

Local gates passed: scripting (188), website (18), shell (RC 18; startup 76 prepared and 76 fresh; expanded 141), build (324), template (393 supported plus semantic and variant checks). Concurrency also passed all 608 supported cells and semantic gates (32 explicitly excluded cells retained). Filesystem also passed all 662 primary and 90 filter cells with independent fixture/distribution audits. Task full smoke also passed all 186 observations and its independent audit. All eight suites are green. Eight fresh dedicated hosts are provisioned; clean exact-candidate build launch is in progress. All eight local gates passed; all eight fresh g6-standard-4 hosts are provisioned in us-east. Official timing has not started.

The complete frozen sample plans total 67,153 observations. Three-way same-node recovery diagnostics remain separate. New cloud tooling uses an isolated namespace and an explicit all-eight preflight gate. The previously approved 20-minute follow-up now tracks this final candidate.

No Labs, tags, releases, packages or download publication is authorized.

All eight official builds independently verified clean exact source, GCC 13 and Nift v4.12.0. Common CLI SHA256: `7dd42dcee5ca4a6965f0823c0ae59198282da1eb77e0fcd4cae93a537870a6fb`. Full frozen timing is authorized per suite only after its pinned-comparator and cloud correctness gates pass. Scripting, website and filesystem gates have passed; other cloud gates remain running. Actual suite affinity is recorded in cloud-affinity-clarification.json.

Six full official collectors are running: build, concurrency, filesystem, scripting, template and website. Shell and task-runner cloud correctness gates remain running; they start official timing only after acceptance. No performance conclusion or release recommendation is issued from partial samples.

Scripting and template official evidence and all required same-node diagnostics are complete. Major original scripting call regressions recovered; large final/release residual+2.59% is retained as descriptive. Controlled template gains versus release:72.19%10k source-loop,51.21%fresh-loop,38.09%article-source. Both hosts become teardown-eligible after combined evidence push. Other six full collectors remain active. Task first attempt is rejected for preflight-cache contamination; all153partial observations +failed154/cache preserved, no accepted reuse, unchanged full1527 restart uses a fresh exact-suite workspace.

Scripting Linode108162749 and template Linode108162740 are deleted after all evidence/diagnostics were pushed at3521529. Both CLI absence and API404 verified; their temporary known-host entries removed. Shared temporary access is retained only for six remaining active campaign hosts. Lifecycle receipts are under lifecycle/.
