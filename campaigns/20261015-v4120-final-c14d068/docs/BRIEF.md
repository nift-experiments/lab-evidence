The key change is that the authoritative candidate is now **`c14d06835bca515a5281e41da0e40219c2d60ef0`**, not `3422876`, and the previous stopped benchmark run has to be treated as an interrupted campaign that needs forensic review before any fresh spend. The handover also says the final candidate has now passed **9/9 GitHub Actions workflows plus the local release-certification suite**, so the benchmark workspace can focus on performance rather than continuing Nift development. Pasted text Pasted text

I’d give Codex this updated brief:

> # Nift v4.12.0 — resume and rerun independent eight-suite recertification
>
> The previous benchmark attempt was intentionally stopped after jobs began failing.
>
> We are now good to proceed again, but **do not blindly restart the old campaign**.
>
> First inspect the interrupted campaign and preserve its failure evidence. Then run a fresh eight-suite campaign against the **final authoritative candidate**:
>
> ```text
> c14d06835bca515a5281e41da0e40219c2d60ef0
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
> This SHA supersedes:
>
> ```text
> 342287696eaf619d942054826e43b8565639c83b
> ```
>
> Do not mix measurements from the old interrupted candidate with final-candidate results.
>
> ---
>
> # 1. First task — forensic inspection of the interrupted campaign
>
> Before provisioning new Linodes:
>
> inspect the latest interrupted campaign state and answer:
>
> - which of the eight suites had started;
> - which jobs passed;
> - which failed;
> - which were pending/interrupted;
> - exact source SHA used by each;
> - exact failure command;
> - exit status;
> - stderr/stdout;
> - whether failure was:
>   - Nift correctness;
>   - benchmark harness;
>   - CLI/API compatibility;
>   - fixture;
>   - dependency/toolchain;
>   - timeout;
>   - resource exhaustion;
>   - infrastructure/orchestration;
> - which partial results are valid;
> - whether any Linodes remain running.
>
> Preserve all original failure logs and evidence.
>
> Do not delete failed-job material merely to create a clean campaign.
>
> Produce a short:
>
> **`INTERRUPTED-CAMPAIGN-FAILURE-ASSESSMENT.md`**
>
> before fresh measurement begins.
>
> ---
>
> # 2. Check for leftover Linodes immediately
>
> Use the Linode CLI/API and the campaign inventory to identify any campaign-owned instances still running.
>
> Do not assume stopping Codex deleted them.
>
> The Linode CLI API key has changed and is available at the **end of `~/.bashrc`**.
>
> Use it securely.
>
> Do not:
>
> - print it;
> - echo it;
> - dump `.bashrc`;
> - commit it;
> - include it in evidence/logs.
>
> Only inspect enough shell state to configure the CLI.
>
> Do not delete unrelated Linodes.
>
> If old campaign nodes have uncertain state/isolation, preserve any needed evidence and delete them rather than reusing them for official measurement.
>
> ---
>
> # 3. Final candidate identity
>
> Every official host must:
>
> 1. clone/fetch `nift-dev/nift`;
> 2. checkout detached:
>
> ```text
> c14d06835bca515a5281e41da0e40219c2d60ef0
> ```
>
> 3. verify:
>
> ```text
> git rev-parse HEAD
> git status --porcelain
> ```
>
> 4. build using the established benchmark toolchain;
> 5. record:
>    - Git SHA;
>    - executable SHA-256;
>    - library SHA-256 where relevant;
>    - compiler;
>    - flags;
>    - host information.
>
> Do not use local installed Nift.
>
> Do not use an earlier A13/B1 scratch build.
>
> Do not silently follow a newer `main`.
>
> ---
>
> # 4. CI/correctness baseline
>
> Record that the final candidate has:
>
> - **9/9 GitHub Actions workflows passing**
> - 35/35 corrected function-call semantic contracts
> - 10/10 nested-index tests
> - 10/10 method-error tests
> - 26/26 mandatory local release-certification suites
>
> This is useful provenance, but **does not replace performance recertification**. Pasted text
>
> ---
>
> # 5. Preflight previously failing benchmark jobs
>
> Before launching thousands of samples:
>
> reproduce the previously failing jobs against `c14d068`.
>
> Check:
>
> - command syntax;
> - working directory;
> - fixture paths;
> - environment variables;
> - expected output;
> - exit status;
> - measurement parser;
> - timeouts;
> - parent/child metrics;
> - comparator availability.
>
> If the failure was a **harness defect**, apply the smallest justified harness correction.
>
> Distinguish:
>
> **compatibility correction**
>
> from:
>
> **methodology change**.
>
> Do not:
>
> - alter workloads to make Nift pass;
> - weaken correctness gates;
> - modify Nift core.
>
> If a harness correction changes measurement semantics, document comparability impact before continuing.
>
> ---
>
> # 6. Fresh official campaign only
>
> Once preflight is green, provision **eight fresh cheap Linodes**, one per benchmark suite.
>
> Run all eight concurrently.
>
> Suites:
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
> Benchmark repos live under:
>
> `/home/nick/Repositories/nift/nift-benchmarks/`
>
> Evidence:
>
> `/home/nick/Repositories/nift/nift-benchmarks/lab-evidence`
>
> Labs:
>
> `/home/nick/Repositories/nift/lab`
>
> Core:
>
> `/home/nick/Repositories/nift/nift`
>
> ---
>
> # 7. Host strategy
>
> Prefer the established campaign configuration where practical:
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
> - CPU model;
> - RAM;
> - kernel;
> - filesystem;
> - compiler/runtime versions.
>
> One suite per host.
>
> No unrelated workloads on the same host.
>
> ---
>
> # 8. Preserve accepted methodologies exactly
>
> Reuse:
>
> - existing scenario matrices;
> - participant versions;
> - sample counts;
> - warmups;
> - interleaving;
> - affinity;
> - timeouts;
> - correctness gates;
> - RSS definitions;
> - raw-sample retention.
>
> No cherry-picking.
>
> No outlier deletion.
>
> No adaptive stopping.
>
> No shortened campaign because expected repairs “look good.”
>
> ---
>
> # 9. Explicit recovery targets
>
> The previous independent campaign found:
>
> ```text
> scripting calls large      +145.76%
> shell calls                +119.68%
> scripting calls small       +65.63%
> website fresh full          +38.29%
> tiny 10k full               +21.25%
> tiny peak child RSS         +63%
> shell string transform      +15.32%
> ```
>
> The final campaign must explicitly establish whether each is recovered. Pasted text
>
> Create:
>
> **`REGRESSION-RECOVERY.md`**
>
> with:
>
> | Prior blocker | v4.11 | broken v4.12 | final v4.12 | Recovered? | Residual |
> |---|---:|---:|---:|---|---:|
>
> ---
>
> # 10. Function calls
>
> Pay particular attention to:
>
> - scripting large calls;
> - scripting small calls;
> - shell function calls;
> - zero-arg calls where available;
> - indexed-reference calls;
> - method chains.
>
> The final CI fixes included recursion-depth and named-call spread/evaluation changes, so performance must be independently rechecked. Pasted text
>
> ---
>
> # 11. Website generation
>
> Preserve:
>
> - fresh;
> - warm full;
> - unchanged/no-op;
> - incremental;
> - targeted;
> - time;
> - peak RSS.
>
> Do not conflate boundaries.
>
> We need to know whether the fresh-build regression and RSS growth are truly recovered in the official campaign.
>
> ---
>
> # 12. Build systems
>
> Preserve:
>
> - Make;
> - Ninja;
> - Nift;
> - native/tiny graphs;
> - 1/2/4 workers;
> - no-op;
> - incremental;
> - full;
> - light/heavy.
>
> Explicitly recheck:
>
> - tiny 10k full time;
> - tiny 10k peak child RSS;
> - heavy native no-op;
> - no-op metadata/path behavior.
>
> ---
>
> # 13. Shell
>
> Run full accepted matrix:
>
> - startup;
> - calls;
> - strings;
> - files;
> - traversal;
> - process work;
> - Bash/Zsh/Fish/Nushell.
>
> Verify whether the repaired method-chain/string improvement survives the official workload.
>
> ---
>
> # 14. Scripting
>
> Run full historical matrix.
>
> Do not focus only on calls.
>
> Include:
>
> - loops;
> - calls;
> - sort/index;
> - scan;
> - frequency;
> - BFS;
> - JSON;
> - filesystem traversal;
> - collections.
>
> Check that recovering calls did not regress:
>
> - sorting;
> - template-related scalar paths;
> - JSON;
> - collection operations.
>
> ---
>
> # 15. Template engines
>
> Verify previous gains remain:
>
> - 10k source-render loop;
> - fresh loop;
> - article source-render.
>
> Still distinguish:
>
> - source reuse;
> - prepared reuse.
>
> Do not invent a prepared-template result if public prepared API is still absent.
>
> ---
>
> # 16. Concurrency
>
> Run full matrix:
>
> - scheduling;
> - tiny tasks;
> - queues;
> - waits;
> - CPU;
> - mutex;
> - held memory;
> - reuse diagnostic.
>
> Previous improvements do not excuse existing huge competitive gaps.
>
> ---
>
> # 17. Filesystem
>
> Verify the large gains remain:
>
> - stat 10k;
> - size filter 10k;
> - walk 10k.
>
> Also retain bad workloads:
>
> - checksum/read;
> - mirror;
> - bulk processing;
> - unsupported native SHA/mtime/removal where applicable.
>
> ---
>
> # 18. Task runners
>
> Run full Nift/Turbo/Nx campaign.
>
> Recheck:
>
> - no-op;
> - one dirty;
> - all dirty;
> - worker scaling;
> - failure;
> - targeting.
>
> Do not invent capability parity for:
>
> - outputless nodes;
> - env invalidation;
> - result restoration;
> - ensure targeting;
> - `-j`;
> - graph explain.
>
> ---
>
> # 19. Correctness-first rule
>
> Every sample must pass its correctness contract.
>
> Invalid:
>
> - wrong output;
> - missing output;
> - wrong task set;
> - wrong graph state;
> - wrong hash;
> - failed process;
> - incomplete filesystem mutation.
>
> Never treat an unexpectedly fast incorrect sample as an improvement.
>
> ---
>
> # 20. Ranked final reporting — mandatory
>
> The final report must lead with **three full league tables**.
>
> ## A. Best improvements — best → worst
>
> Same-node valid old→final comparisons.
>
> Sort descending by percentage improvement.
>
> Include:
>
> ```text
> rank
> suite/scenario
> v4.11
> broken v4.12
> final v4.12
> % improvement vs v4.11
> % recovery vs broken v4.12
> confidence
> ```
>
> Keep wall/memory/throughput separate.
>
> ---
>
> ## B. Regressions — worst → least bad
>
> Sort descending by regression percentage.
>
> Include every measured increase.
>
> Separate:
>
> - confirmed same-node regression;
> - descriptive increase;
> - cross-node-only trend.
>
> Do not hide small regressions.
>
> ---
>
> ## C. Remaining competitive deficits — worst → best
>
> Use final v4.12 vs best valid same-node peer.
>
> For lower-is-better:
>
> ```text
> deficit = Nift / best peer
> ```
>
> Sort descending.
>
> This should plainly show where Nift still sucks most.
>
> Separate:
>
> - wall time;
> - memory;
> - throughput;
> - unsupported capability.
>
> ---
>
> # 21. Fourth league table — huge gains but still bad
>
> Produce:
>
> | Scenario | % improvement | Old deficit | New deficit | Verdict |
> |---|---:|---:|---:|---|
>
> This avoids declaring victory when something improves 80% but is still 10×/100× behind.
>
> ---
>
> # 22. Track recovered blockers explicitly
>
> First section of final report:
>
> **“Did v4.12 recover the blocked regressions?”**
>
> Must include:
>
> - scripting calls large;
> - scripting calls small;
> - shell calls;
> - shell strings;
> - website fresh;
> - tiny 10k full;
> - tiny child RSS.
>
> Answer each:
>
> - yes;
> - partial;
> - no;
>
> with exact values.
>
> ---
>
> # 23. Practitioner opinions
>
> Re-evaluate from scratch after final candidate data.
>
> For every category report:
>
> ## Human + agent
>
> What does Codex choose?
>
> ## Agent-primary
>
> What does Codex choose?
>
> Use direct names:
>
> - Nift
> - Python
> - Go
> - Bash/Zsh
> - Hugo
> - Make/Ninja
> - Turbo/Nx
> etc.
>
> Do not say only:
>
> > “Nift is compelling.”
>
> Say which tool wins and why.
>
> ---
>
> # 24. Track preference changes
>
> Produce:
>
> `PREFERENCE-CHANGES.md`
>
> with:
>
> - prior choice;
> - final choice;
> - human+agent;
> - agent-primary;
> - reason;
> - remaining blocker.
>
> ---
>
> # 25. Cross-benchmark “still embarrassing” list
>
> Produce:
>
> `WORST-COMPETITIVE-GAPS.md`
>
> sorted by deficit multiple.
>
> Also produce a **product-priority ranking**, because:
>
> - a 1000× concurrency microgap may be less central than a 20% website regression;
> - both matter, but for different reasons.
>
> Rank by:
>
> - gap size;
> - product centrality;
> - frequency;
> - cross-benchmark impact;
> - whether it changes Codex’s preference.
>
> ---
>
> # 26. Evidence
>
> Create a new final-candidate namespace in:
>
> `/home/nick/Repositories/nift/nift-benchmarks/lab-evidence`
>
> Preserve:
>
> - raw samples;
> - warmups;
> - source/binary identities;
> - comparator versions;
> - audits;
> - failure logs;
> - harness-fix evidence;
> - diagnostics;
> - host inventory;
> - teardown receipts.
>
> Do not overwrite the interrupted campaign.
>
> ---
>
> # 27. No Labs publication yet
>
> Prepare publication-ready summaries if useful.
>
> But:
>
> - do not publish Labs;
> - do not tag v4.12;
> - do not publish packages;
> - do not release.
>
> Wait for user review.
>
> ---
>
> # 28. Teardown
>
> As each suite completes:
>
> - collect evidence;
> - audit;
> - push evidence;
> - complete necessary diagnostics;
> - delete its Linode.
>
> Verify:
>
> - CLI absence;
> - API 404;
> - per-host SSH cleanup;
> - known-host cleanup.
>
> Do not leave eight hosts running after completion.
>
> ---
>
> # 29. Stop conditions
>
> Proceed autonomously unless one of these occurs:
>
> - candidate SHA mismatch;
> - genuine Nift correctness defect;
> - harness correction would materially change methodology;
> - required comparator cannot be installed/reproduced;
> - evidence integrity cannot be established.
>
> Otherwise complete the whole campaign without asking for routine approvals.
>
> ---
>
> # 30. Final deliverable
>
> Return one consolidated:
>
> **NIFT v4.12.0 — INDEPENDENT EIGHT-SUITE RECERTIFICATION**
>
> containing:
>
> - interrupted-campaign failure assessment;
> - final candidate SHA and binary hashes;
> - CI status;
> - all eight suites;
> - observations/warmups;
> - correctness/audits;
> - regression-recovery table;
> - best improvements ranking;
> - worst regressions ranking;
> - worst competitive deficits ranking;
> - huge gains/still-behind table;
> - memory changes;
> - capability gaps;
> - human+agent preference matrix;
> - agent-primary preference matrix;
> - product-priority issues;
> - evidence commits;
> - all eight teardown receipts;
> - technical release-readiness recommendation.
>
> Then stop and wait for user authorization before public release or Labs publication.

The big operational difference from the last outline is: **first explain why the stopped campaign failed, then start fresh against `c14d068`**. The file is explicit that those failures were not diagnosed and should not simply be assumed to have been fixed by the newer Nift revision. Pasted text

And since the final candidate includes genuine call-evaluation changes after `3422876`, I’d absolutely require fresh official measurements for every suite rather than trying to salvage earlier numbers as final-candidate evidence. Pasted text