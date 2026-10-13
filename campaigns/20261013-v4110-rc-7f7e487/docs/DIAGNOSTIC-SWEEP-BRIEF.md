Agreed — better to let the full refresh finish so we get a complete regression/improvement map before touching core again.

I’d send Codex this:

> Continue all currently running benchmark campaigns to completion.
>
> Do **not** publish the refreshed Labs results yet.
>
> The purpose of this pass is now diagnostic:
>
> > establish exactly what improved, what regressed, and what still performs badly in the current release candidate before we make another round of Nift core changes.
>
> The scripting same-node A/B has already confirmed a real focused regression, especially function-call overhead, so this candidate is **not yet approved for release publication**.
>
> However, do not stop the other suites. We want the full picture first.
>
> ---
>
> # 1. Finish every benchmark
>
> Complete:
>
> - build-systems
> - concurrency
> - filesystem-automation
> - scripting-benchmark
> - shell-benchmark
> - task-runners
> - template-engines
> - website-generator-benchmark
>
> Keep the current candidate frozen at:
>
> `7f7e487c47a87e871dfef53345e2b71288008bff`
>
> Do not patch Nift mid-campaign.
>
> ---
>
> # 2. Preserve all accepted evidence
>
> For every suite:
>
> - complete measurements;
> - run independent audits;
> - retain raw samples;
> - retain warmups;
> - retain diagnostics;
> - retain correctness receipts;
> - retain rejected attempts;
> - retain machine/environment identities.
>
> Push canonical evidence into:
>
> `/home/nick/Repositories/nift/nift-benchmarks/lab-evidence`
>
> using a clearly marked **pre-release diagnostic refresh** campaign identity.
>
> Do not overwrite previous accepted evidence.
>
> ---
>
> # 3. Do not publish to lab.nift.dev yet
>
> Do not update:
>
> - current benchmark headline values;
> - charts;
> - practitioner conclusions;
> - homepage current-series labels;
> - benchmark collection current-series labels.
>
> Do not publish these results as the new canonical Labs generation.
>
> The current candidate has a confirmed scripting regression and may still change.
>
> Labs publication waits until:
>
> - core regressions are addressed;
> - a new candidate SHA is frozen;
> - the benchmark refresh is rerun against that final candidate.
>
> You may prepare local draft summaries if useful, but do not push/publish refreshed benchmark pages.
>
> ---
>
> # 4. Finish same-node old-vs-candidate checks where useful
>
> Scripting already has a same-node A/B.
>
> For other suites, if historical cross-node results suggest a major regression or surprising improvement, add a **same-node old-vs-candidate diagnostic** where practical.
>
> Use the exact previous accepted Nift SHA for that benchmark.
>
> Build both old and candidate on the current Linode and compare under the current suite where semantics remain compatible.
>
> Keep these A/B runs:
>
> - diagnostic only;
> - separate from accepted current-vs-peer results.
>
> Do not do this for every cell automatically.
>
> Prioritize scenarios where:
>
> - historical trend is large;
> - peer/node drift could plausibly explain it;
> - the result would materially affect release decisions.
>
> ---
>
> # 5. Produce a cross-benchmark regression report
>
> Create:
>
> `CROSS-BENCHMARK-REGRESSIONS.md`
>
> plus machine-readable JSON.
>
> Rank all confirmed or strongly supported Nift regressions.
>
> Prefer same-node A/B where available.
>
> Include:
>
> ```text
> rank
> benchmark
> scenario
> old Nift
> candidate Nift
> % regression
> confidence/basis
> likely subsystem
> notes
> ```
>
> Separate:
>
> - confirmed same-node regressions;
> - cross-node suspected regressions;
> - capability regressions;
> - correctness regressions.
>
> Put the worst first.
>
> ---
>
> # 6. Produce a cross-benchmark improvements report
>
> Create:
>
> `CROSS-BENCHMARK-IMPROVEMENTS.md`
>
> plus machine-readable JSON.
>
> Rank by percentage improvement where directly comparable.
>
> Include:
>
> ```text
> rank
> benchmark
> scenario
> old Nift
> candidate Nift
> % improvement
> comparison basis
> notes
> ```
>
> Keep separate sections for:
>
> - wall time;
> - memory;
> - throughput;
> - newly supported capabilities.
>
> Preserve the scripting wins already observed, such as sort/index and scan improvements, rather than allowing the function-call regression to obscure them.
>
> ---
>
> # 7. Produce a “what still sucks” report
>
> Create:
>
> `CROSS-BENCHMARK-COMPETITIVE-GAPS.md`
>
> This is the current-candidate competitive deficit ranking.
>
> For lower-is-better metrics:
>
> ```text
> deficit = Nift / fastest valid peer
> ```
>
> Rank the largest deficits first.
>
> Include:
>
> ```text
> rank
> benchmark/scenario
> Nift result
> best peer
> deficit multiple
> practical importance
> likely subsystem
> previous deficit if known
> ```
>
> Keep separate:
>
> - wall-time deficits;
> - memory deficits;
> - throughput deficits;
> - unsupported capabilities.
>
> This should answer:
>
> > Where is Nift still embarrassing itself most?
>
> Internally that wording is fine; public-facing docs can call them “largest remaining competitive gaps.”
>
> ---
>
> # 8. Add a product-priority ranking
>
> Raw deficit alone is not enough.
>
> Also rank gaps by product importance:
>
> - how large the gap is;
> - how central the workload is to Nift;
> - how often it affects real projects;
> - whether it appears across multiple benchmarks;
> - whether it prevents Codex preferring Nift.
>
> Example categories to watch:
>
> - function-call/runtime dispatch;
> - scalar interpreter/value-path overhead;
> - filesystem metadata/path handling;
> - task/future allocation;
> - prepared-template reuse;
> - concurrency waits/channels/cancellation;
> - build-system no-op/incremental scanning.
>
> Do not infer shared root causes without evidence.
>
> ---
>
> # 9. Track cross-benchmark shared signals
>
> Maintain:
>
> `CROSS-BENCHMARK-SUBSYSTEMS.md`
>
> Example:
>
> ```text
> subsystem
> benchmarks affected
> evidence
> improved/regressed
> confidence
> ```
>
> Specifically check whether the new candidate changed:
>
> - runtime/value execution;
> - call frames/captures;
> - path/stat handling;
> - allocation churn;
> - JSON/object handling;
> - process launch;
> - async state/task retention.
>
> ---
>
> # 10. Revisit practitioner opinions — but do not publish them yet
>
> After each suite finishes, draft an updated practitioner verdict locally.
>
> For each benchmark explicitly answer:
>
> ## Human + agent use
>
> Would Codex choose Nift or an alternative?
>
> ## Agent-primary use
>
> Would Codex choose Nift or an alternative?
>
> Use direct language:
>
> - “I would choose Nift.”
> - “I would still choose Go.”
> - “For agent-primary workflows I prefer Nift.”
> - etc.
>
> Name the concrete reason.
>
> Do not use vague “ecosystem” language.
>
> Save these as draft conclusions only.
>
> Do **not** push them to Labs yet.
>
> ---
>
> # 11. Build a before/after preference table
>
> Create:
>
> `CROSS-BENCHMARK-PREFERENCES.md`
>
> With:
>
> ```text
> benchmark
> previous human+agent preference
> candidate human+agent preference
> previous agent-primary preference
> candidate agent-primary preference
> what changed
> remaining blocker
> ```
>
> This should show whether the current candidate actually moved Codex’s opinion.
>
> ---
>
> # 12. Keep release recommendation on hold
>
> Current candidate:
>
> `7f7e487c47a87e871dfef53345e2b71288008bff`
>
> is not release-approved while the scripting regression remains unresolved.
>
> Do not recommend release merely because other benchmarks improve.
>
> Finish the campaign first, then summarize:
>
> - blockers;
> - severe regressions;
> - worthwhile wins;
> - unchanged weak spots.
>
> ---
>
> # 13. Teardown policy
>
> Once each benchmark has:
>
> - finished measurements;
> - passed audit;
> - had evidence collected locally and pushed;
> - completed any required diagnostics;
>
> its Linode can be deleted.
>
> Since we are **not publishing Labs yet**, do not keep finished nodes alive waiting for publication.
>
> Before deleting each:
>
> - verify evidence is safely retained;
> - record machine identity;
> - record teardown receipt;
> - verify CLI absence;
> - verify API 404;
> - remove temporary SSH/CLI state.
>
> Do not delete a node still needed for a same-node diagnostic.
>
> ---
>
> # 14. Final diagnostic closeout
>
> When all eight are finished, return one consolidated report containing:
>
> ## Regressions
>
> - top confirmed regressions;
> - same-node evidence;
> - likely subsystem clusters.
>
> ## Improvements
>
> - top improvements ranked by %;
> - new capabilities;
> - scenarios where Nift became competitive/preferred.
>
> ## Still weak
>
> - biggest competitive deficits ranked by multiple;
> - biggest missing capabilities;
> - highest-priority product gaps.
>
> ## Preferences
>
> - human+agent verdict per benchmark;
> - agent-primary verdict per benchmark;
> - where Codex changed its mind.
>
> ## Release blockers
>
> - issues that must be fixed before the next candidate.
>
> ## Infrastructure
>
> - evidence commits;
> - experiment commits;
> - all Linode teardown receipts.
>
> Do not publish current-candidate benchmark pages.
>
> ---
>
> # 15. Next step after closeout
>
> Once this diagnostic campaign is complete:
>
> 1. we will address the confirmed regressions in Nift core;
> 2. freeze a new candidate SHA;
> 3. rerun the entire benchmark refresh;
> 4. only that final clean candidate gets published to lab.nift.dev.
>
> The current campaign is therefore a **release-candidate diagnostic sweep**, not the final public benchmark generation.

That’s a better move than tearing them down now. We’ve already paid the setup cost, and this is probably the best chance we’ll get to identify every regression before the next candidate rather than fixing scripting, rerunning everything, and discovering a second unrelated regression later.