The handover is clear: the repaired **v4.12.0 candidate is exactly `342287696eaf619d942054826e43b8565639c83b`**, pushed to `main`, with the known call-path, website-build, tiny-build memory/time and shell-string regressions targeted in core before this recertification. Pasted text The whole point of this pass is now to independently verify that those repairs hold across the complete eight-suite matrix and that nothing else broke. Pasted text

I’d give Codex this:

> # Nift v4.12.0 — full independent eight-suite benchmark recertification
>
> We are ready to rerun the complete Nift benchmark suite against the repaired, pushed v4.12 candidate.
>
> This is intended to be the **independent release-candidate recertification campaign**.
>
> The exact Nift candidate is:
>
> ```text
> 342287696eaf619d942054826e43b8565639c83b
> ```
>
> Repository:
>
> `https://github.com/nift-dev/nift`
>
> Branch:
>
> `main`
>
> Version:
>
> `Nift v4.12.0` — unreleased
>
> Do **not** benchmark latest `main` implicitly.
>
> On every benchmark host:
>
> 1. clone/fetch `nift-dev/nift`;
> 2. checkout exact SHA `342287696eaf619d942054826e43b8565639c83b`;
> 3. verify clean checkout;
> 4. build using the established campaign toolchain;
> 5. record source SHA;
> 6. record executable/library SHA-256;
> 7. use that exact build for the suite.
>
> No benchmark may silently move to a later `main`.
>
> ---
>
> # 1. Benchmark workspace layout
>
> The benchmark repositories are now local under:
>
> `/home/nick/Repositories/nift/nift-benchmarks/`
>
> including:
>
> - `build-systems`
> - `concurrency`
> - `filesystem-automation`
> - `scripting-benchmark`
> - `shell-benchmark`
> - `task-runners`
> - `template-engines`
> - `website-generator-benchmark`
> - `lab-evidence`
>
> Nift core remains:
>
> `/home/nick/Repositories/nift/nift`
>
> Labs remains:
>
> `/home/nick/Repositories/nift/lab`
>
> Use the existing accepted campaign infrastructure, fixtures, sample plans, correctness gates and evidence formats.
>
> Do not invent a simplified replacement campaign.
>
> ---
>
> # 2. Eight authoritative suites
>
> Run all eight:
>
> 1. `build-systems`
> 2. `concurrency`
> 3. `filesystem-automation`
> 4. `scripting-benchmark`
> 5. `shell-benchmark`
> 6. `task-runners`
> 7. `template-engines`
> 8. `website-generator-benchmark`
>
> No selective rerun.
>
> Include scenarios where Nift previously:
>
> - won;
> - lost;
> - regressed;
> - remained badly uncompetitive.
>
> ---
>
> # 3. Provision one fresh Linode per benchmark
>
> Provision **eight fresh cheap Linodes**, one dedicated host per suite.
>
> Run them concurrently.
>
> Prefer the same established host class/region used in the previous campaign where available:
>
> - g6-standard-4
> - 4 vCPU
> - 8 GiB
> - us-east
> - Ubuntu 24.04
>
> Record actual:
>
> - Linode ID;
> - plan;
> - region;
> - CPU model;
> - RAM;
> - kernel;
> - filesystem;
> - compiler/runtime versions.
>
> The Linode CLI API key has **changed** and is available at the **end of `~/.bashrc`** on the local machine.
>
> Use it securely for provisioning/inspection/teardown.
>
> **Do not print, echo, dump, log, commit, upload or include the API key in evidence.**
>
> Do not dump the whole `.bashrc`.
>
> Read only what is needed to configure the CLI/environment.
>
> Clean temporary CLI configuration, SSH keys and known-host state at the end.
>
> ---
>
> # 4. Check CI for the exact SHA
>
> Before or while preparing the hosts, check GitHub Actions for:
>
> `342287696eaf619d942054826e43b8565639c83b`
>
> The core handover only established that workflows had started; it did not establish that they had all passed. Pasted text
>
> Record:
>
> - passed;
> - failed;
> - pending;
> - skipped;
>
> for relevant workflows.
>
> If a CI failure looks release-blocking:
>
> - preserve it;
> - report it;
> - do not silently change candidate SHA.
>
> Benchmark preparation may continue where independent validity is unaffected.
>
> ---
>
> # 5. Historical comparison identities
>
> Preserve three distinct Nift identities:
>
> ## Previous release baseline
>
> ```text
> v4.11
> c8d9c266518d115e4f289c5c6a2b94ddd7ee9968
> ```
>
> ## Original regression-bearing v4.12 candidate
>
> ```text
> 7f7e487c47a87e871dfef53345e2b71288008bff
> ```
>
> ## Repaired v4.12 candidate
>
> ```text
> 342287696eaf619d942054826e43b8565639c83b
> ```
>
> Do not overwrite or reinterpret previous evidence.
>
> The new campaign is a new accepted series.
>
> ---
>
> # 6. Primary questions
>
> The campaign must answer two independent questions:
>
> ## A. Did we recover the known v4.12 regressions?
>
> Especially:
>
> - scripting function calls;
> - shell function calls;
> - shell string transforms;
> - website fresh full builds;
> - tiny 10k full builds;
> - tiny-build child RSS.
>
> ## B. Did the repairs introduce new regressions elsewhere?
>
> Run the whole matrix precisely because targeted core testing cannot answer this.
>
> ---
>
> # 7. Keep previous methodology intact
>
> For every suite preserve the accepted:
>
> - warmup counts;
> - measured sample counts;
> - workload ordering;
> - participant ordering/interleaving;
> - affinity;
> - timeouts;
> - memory accounting;
> - correctness checks;
> - fixture restoration;
> - output hashes;
> - raw samples;
> - distribution summaries.
>
> No outlier deletion.
>
> No adaptive stopping.
>
> No reducing samples to finish early.
>
> No workload modifications after seeing results.
>
> ---
>
> # 8. Build Systems
>
> Preserve:
>
> - Make;
> - Ninja;
> - Nift;
> - native graphs;
> - tiny-action graphs;
> - 1/2/4 workers;
> - no-op;
> - incremental;
> - full;
> - light/heavy profiles;
> - all established graph sizes.
>
> Mandatory recovery checks:
>
> - tiny 10k full time;
> - tiny 10k peak-child RSS;
> - native heavy no-op;
> - large no-op/incremental scanning.
>
> Previous diagnostic regression:
>
> ```text
> tiny 10k full +21.25%
> peak child RSS ~+63%
> ```
>
> Core targeted evidence suggests these are recovered, but the official benchmark must prove it under the original definitions. Pasted text
>
> Keep parent/child/aggregate memory boundaries distinct.
>
> ---
>
> # 9. Scripting
>
> Run the complete accepted scripting matrix.
>
> Mandatory attention:
>
> - large/small function calls;
> - loops;
> - sort/index;
> - scan;
> - frequency count;
> - BFS;
> - JSON parse;
> - JSON transform;
> - JSON traverse;
> - filesystem traversal;
> - map/set;
> - sliding window;
> - Fibonacci.
>
> Known regression to verify:
>
> ```text
> large calls +145.76%
> small calls +65.63%
> ```
>
> The core repair claims major recovery while preserving exactly-once evaluation and value/reference semantics. Pasted text
>
> This is one of the main release gates.
>
> ---
>
> # 10. Shell
>
> Run the entire accepted shell matrix:
>
> - startup;
> - external commands;
> - function calls;
> - strings;
> - traversal;
> - files;
> - arithmetic;
> - process scenarios;
> - existing Bash/Zsh/Fish/Nushell comparisons.
>
> Verify:
>
> ```text
> previous shell calls regression: +119.68%
> previous string transform regression: +15.32%
> ```
>
> Core targeted testing suggests string transformation may now be dramatically faster than v4.11. Pasted text
>
> Do not change the workload to amplify that result.
>
> ---
>
> # 11. Website Generator
>
> Run the accepted website-generator matrix:
>
> - fresh application/project state;
> - warm full;
> - unchanged;
> - incremental;
> - targeted;
> - all existing site sizes;
> - existing competitor matrix.
>
> Keep state boundaries separate.
>
> Known previous regression:
>
> ```text
> fresh 10k +38.29%
> ```
>
> Core targeted recovery suggests fresh build time and memory are close to v4.11 again, but the official benchmark must establish this independently. Pasted text
>
> Do not let improved warm/no-op paths hide a fresh-build regression.
>
> ---
>
> # 12. Task Runners
>
> Preserve:
>
> - Nift;
> - Turbo;
> - Nx;
> - mixed graphs;
> - tiny graphs;
> - no-op;
> - one dirty leaf;
> - fanout/shared input;
> - all dirty;
> - worker scaling;
> - targeting;
> - failure/recovery;
> - cache-disabled semantics.
>
> Reassess current missing capabilities:
>
> - outputless tracked nodes;
> - env invalidation;
> - local/remote result restoration;
> - ensure target;
> - worker override;
> - graph/query/explain.
>
> Do not invent parity if those still do not exist.
>
> ---
>
> # 13. Template Engines
>
> Preserve full accepted matrix:
>
> - fresh invocation;
> - source render;
> - loops;
> - article;
> - nested data;
> - partials;
> - repeated source;
> - prepared reuse where peers support it.
>
> We want to know whether the previous huge gains remain:
>
> ```text
> source-render loop +71.82%
> fresh loop +54.91%
> article source-render +38.05%
> ```
>
> Also verify whether Nift still lacks a public prepared-template artifact.
>
> Do not relabel source reuse as prepared reuse.
>
> ---
>
> # 14. Concurrency
>
> Run the entire accepted concurrency matrix:
>
> - scheduling;
> - tiny tasks;
> - queues;
> - waits;
> - CPU scaling;
> - mutex;
> - subprocess;
> - files;
> - held-task memory;
> - retained-runtime diagnostics;
> - failure semantics.
>
> Preserve the previous queue improvement while checking whether any new regressions appeared.
>
> Do not hide the fact that Nift may remain orders of magnitude behind Go/Bun on lightweight concurrency.
>
> ---
>
> # 15. Filesystem Automation
>
> Run the complete accepted filesystem matrix:
>
> - walk;
> - stat;
> - filtering;
> - reads;
> - writes;
> - checksums;
> - copy;
> - mirror;
> - change detection;
> - generation;
> - mixed project workflow.
>
> We especially want to verify that the enormous previous gains survive:
>
> ```text
> stat 10k  ~91% improvement
> size filter 10k ~86%
> walk 10k ~86%
> ```
>
> Do not assume they do.
>
> Also report remaining gaps:
>
> - checksum/read;
> - mirror;
> - hashing;
> - metadata APIs;
> - recursive removal;
> - any unsupported cells.
>
> ---
>
> # 16. Correctness gates first
>
> Every sample must prove the expected work happened.
>
> If:
>
> - output differs;
> - task set differs;
> - filesystem state differs;
> - hash differs;
> - process result differs;
> - graph action count differs;
>
> reject that sample.
>
> Never treat an unexpectedly fast failed/skipped workload as a valid improvement.
>
> ---
>
> # 17. Same-node old/repaired diagnostic policy
>
> The primary campaign is current-candidate vs current peers.
>
> In addition, for historical regression recovery use same-node old/repaired diagnostics where valuable.
>
> Prioritize:
>
> - scripting calls;
> - shell calls;
> - shell strings;
> - fresh website build;
> - tiny full build;
> - tiny child RSS.
>
> Use exact v4.11 and/or original v4.12 candidate where the existing diagnostic methodology already supports it.
>
> Keep these runs separate from official peer comparison samples.
>
> ---
>
> # 18. Evidence storage
>
> Canonical evidence goes in:
>
> `/home/nick/Repositories/nift/nift-benchmarks/lab-evidence`
>
> Create a new v4.12 repaired-candidate campaign namespace.
>
> Preserve:
>
> - raw samples;
> - warmups;
> - machine manifests;
> - suite SHAs;
> - Nift SHA;
> - binary hashes;
> - comparator versions;
> - correctness audit;
> - rejected attempts;
> - diagnostics;
> - lifecycle receipts.
>
> Do not overwrite the previous diagnostic campaign.
>
> ---
>
> # 19. Do not publish Labs yet
>
> Prepare publication-ready data if useful.
>
> But:
>
> **do not publish lab.nift.dev benchmark refreshes without explicit user approval.**
>
> Also do not:
>
> - create the `v4.12.0` tag;
> - publish GitHub release;
> - publish packages;
> - update downloads.
>
> The handover explicitly retains this boundary. Pasted text
>
> ---
>
> # 20. Campaign dashboard
>
> Maintain:
>
> ```text
> Benchmark              Host    Local cert  Cloud  Audit  Diagnostics  Evidence  Deleted
> Build systems
> Concurrency
> Filesystem automation
> Scripting
> Shell
> Task runners
> Template engines
> Website generator
> ```
>
> Update continuously.
>
> ---
>
> # 21. Report best improvements — ordered best to worst
>
> This is mandatory.
>
> Produce:
>
> `BEST-IMPROVEMENTS.md`
>
> plus JSON.
>
> Use same-node old→repaired candidate comparisons where valid.
>
> Sort descending by percentage improvement.
>
> Format:
>
> ```text
> Rank
> Benchmark/scenario
> v4.11
> original v4.12
> repaired v4.12
> % improvement vs v4.11
> % recovery vs broken v4.12
> confidence
> ```
>
> Keep separate rankings for:
>
> - wall time;
> - memory;
> - throughput;
> - new capabilities.
>
> Do not mix incomparable metrics.
>
> ---
>
> # 22. Report regressions — worst to least bad
>
> Produce:
>
> `WORST-REGRESSIONS.md`
>
> plus JSON.
>
> Sort descending by same-node regression percentage.
>
> Include:
>
> ```text
> Rank
> Benchmark/scenario
> v4.11
> repaired v4.12
> % regression
> original broken-v4.12 value
> evidence confidence
> likely subsystem
> ```
>
> Explicitly distinguish:
>
> - confirmed same-node regression;
> - descriptive small increase;
> - cross-node trend only.
>
> Do not suppress small regressions simply because the known major regressions were fixed.
>
> ---
>
> # 23. Report where Nift still sucks — worst first
>
> Produce:
>
> `WORST-COMPETITIVE-GAPS.md`
>
> plus JSON.
>
> Use the repaired candidate vs best valid same-node competitor.
>
> For lower-is-better:
>
> ```text
> deficit = Nift / best peer
> ```
>
> Sort descending.
>
> Format:
>
> ```text
> Rank
> Benchmark/scenario
> Nift
> Best peer
> Deficit multiple
> Previous deficit
> Improved/flat/worse
> Product importance
> ```
>
> Separate:
>
> - wall time;
> - memory;
> - throughput;
> - capability gaps.
>
> This should plainly answer:
>
> > Where is Nift still embarrassing itself most?
>
> Use professional wording in public-facing drafts, but do not soften the internal analysis.
>
> ---
>
> # 24. “Improved massively but still bad” table
>
> Produce a fourth explicit table:
>
> ```text
> Scenario
> % improvement
> previous deficit
> current deficit
> verdict
> ```
>
> This is important because:
>
> - a 90% improvement can still leave Nift 4× behind;
> - a 70% improvement can still leave it 15× behind;
> - a huge recovery does not necessarily mean competitive.
>
> ---
>
> # 25. “Regression recovered?” table
>
> Create one targeted release table:
>
> ```text
> Prior blocker
> v4.11
> broken v4.12
> repaired v4.12
> recovered?
> residual difference
> release impact
> ```
>
> Include at minimum:
>
> - scripting calls large;
> - scripting calls small;
> - shell calls;
> - shell string transform;
> - website fresh full;
> - tiny 10k full;
> - tiny peak child RSS.
>
> This should be the first table in the final release assessment.
>
> ---
>
> # 26. Revisit all practitioner conclusions
>
> For every benchmark, update Codex’s opinion from scratch based on repaired v4.12.
>
> Explicitly give two choices:
>
> ## Human + agent
>
> What would Codex choose?
>
> ## Agent-primary
>
> What would Codex choose?
>
> Use direct language:
>
> - Nift
> - Python
> - Go
> - Bash/Zsh
> - Turbo
> - Nx
> - Hugo
> - Ninja
> - etc.
>
> Do not write vague:
>
> > “Nift is compelling.”
>
> Say:
>
> > “For agent-primary authored workflows, I choose Nift.”
>
> or:
>
> > “For standalone high-fanout concurrency, I still choose Go.”
>
> State the concrete reason.
>
> ---
>
> # 27. Track preference changes
>
> Produce:
>
> `PREFERENCE-CHANGES.md`
>
> Format:
>
> ```text
> Benchmark/category
> Previous human+agent choice
> New human+agent choice
> Previous agent-primary choice
> New agent-primary choice
> Why it changed
> Remaining blocker
> ```
>
> This is one of the most valuable outputs.
>
> ---
>
> # 28. Cross-benchmark shared bottlenecks
>
> Track repeated subsystem evidence:
>
> - call/runtime staging;
> - scalar/value execution;
> - filesystem metadata/path handling;
> - allocation churn;
> - task creation/retention;
> - prepared-template reuse;
> - build no-op scanning;
> - hashing/mtime;
> - channels/cancellation;
> - cache/result restoration.
>
> Do not infer one root cause merely because multiple symptoms have similar names.
>
> Only connect evidence-supported relationships.
>
> ---
>
> # 29. Release readiness rules
>
> The repaired candidate should only receive a positive technical recommendation if:
>
> - major known regressions are recovered;
> - no new severe regressions appear;
> - correctness remains green;
> - memory regressions are recovered;
> - CI state is acceptable;
> - all eight suites audit successfully.
>
> A candidate can still have known longstanding weaknesses and be releasable.
>
> Distinguish:
>
> > old known weakness
>
> from:
>
> > new release regression.
>
> That distinction is essential.
>
> ---
>
> # 30. If a new major regression is found
>
> Do not modify Nift core from benchmark workspaces.
>
> Preserve:
>
> - reproducer;
> - exact candidate;
> - same-node comparison;
> - profile/syscalls/allocations where useful.
>
> Report it to the core workspace.
>
> If core must change candidate SHA, the campaign is no longer the final release campaign.
>
> Do not silently continue under a new binary.
>
> ---
>
> # 31. Linode teardown
>
> As each suite completes:
>
> - collect evidence;
> - audit locally;
> - push evidence;
> - complete required same-node diagnostics;
> - then delete that suite’s Linode.
>
> Verify:
>
> - CLI absence;
> - authenticated API 404;
> - SSH/known-host cleanup;
> - temporary per-host access cleanup.
>
> Do not retain completed nodes unnecessarily.
>
> Do not delete before required diagnostics are safely captured.
>
> ---
>
> # 32. Final report
>
> Produce:
>
> **NIFT v4.12.0 — INDEPENDENT EIGHT-SUITE RECERTIFICATION**
>
> Lead with:
>
> ### Regression recovery
>
> Did each previous blocker disappear?
>
> ### Best improvements
>
> Sorted best→worst by %.
>
> ### Remaining regressions
>
> Sorted worst→least bad.
>
> ### Worst competitive deficits
>
> Sorted most embarrassing→least.
>
> ### Improved hugely but still behind
>
> ### Human+agent preferences
>
> ### Agent-primary preferences
>
> ### Remaining capability gaps
>
> ### Release recommendation
>
> Then:
>
> - candidate identity;
> - environment;
> - observations;
> - audits;
> - evidence;
> - lifecycle;
> - CI;
> - teardown.
>
> ---
>
> # 33. No publication/release without approval
>
> At campaign completion:
>
> - stop;
> - report everything;
> - prepare Labs data if useful;
> - do **not** publish;
> - do **not** tag;
> - do **not** release.
>
> Wait for user approval.
>
> ---
>
> # 34. Autonomy
>
> Proceed through:
>
> - inspection;
> - suite freeze;
> - provisioning;
> - certification;
> - cloud execution;
> - diagnostics;
> - audits;
> - evidence push;
> - teardown;
> - consolidated reporting
>
> autonomously.
>
> Do not ask for approval between ordinary campaign stages.
>
> Only stop early for:
>
> - candidate identity mismatch;
> - correctness failure;
> - genuine methodology ambiguity;
> - serious CI/core defect that invalidates measurement.
>
> Otherwise complete the campaign end-to-end.

The most important addition relative to the previous run is that the final report should have **four separate ranked views**, because each answers a different question:

1. **What did we fix best?**
2. **What did we still make worse?**
3. **Where are we still getting absolutely smoked by competitors?**
4. **What improved enormously but is still nowhere near good enough?**

And the release-specific recovery table should make it instantly obvious whether the repaired v4.12 actually fixed the things that blocked the first candidate.