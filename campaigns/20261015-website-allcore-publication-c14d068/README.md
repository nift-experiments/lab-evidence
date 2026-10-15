# Full all-core website publication campaign

Fresh dedicated g6-standard-4 (4 vCPU / 8 GiB), us-east, host 108212898. Exact candidate c14d06835bca515a5281e41da0e40219c2d60ef0; clean source build with native GCC13.3/Make -O2, expected CLI7dd42dcee5ca4a6965f0823c0ae59198282da1eb77e0fcd4cae93a537870a6fb. Frozen website suite a2890bc504cf7c55b77cd4fddae17403b7caf8ae.

This namespace contains newly collected measurements, never historical substitutions. The unchanged fixture/oracle/clock/ordering policy is executed with the documented worker-only adapter: Nift build-threads=-1, Hugo GOMAXPROCS unset, all products CPU0-3. Node24.21.0, Hugo0.167.0, Astro7.3.6, VitePress1.6.4 remain pinned. Frozen isolated_env PATH resolves through a directory alias to the new tools location.

`PLAN.json` freezes39jobs/234observations: three sizes × four products × fresh/warm full (24jobs), Nift three incremental cases at each size (9jobs), plus separate serial explicit-target/fresh-reference cohort (6jobs). Each job has1warmup+5measured. RSS remains waited-child highwater, never aggregate process-tree RSS. Full-corpus routes/title/h1/body and changed-input full-rebuild byte parity remain mandatory.

Prepare with setup.sh, then identity.py and CPU0-3 gate.py. Gate validates all four products at all three sizes plus Nift no-op/leaf/shared/target scenarios:24checks. `setup-original-executed.sh` preserves initial executed setup before the separately recorded tools alias operation. The first reused gate only persisted rows at Nift cases; it still validated its complete loop but omitted last3rows from its receipt. Its partial receipt/source/log are retained. `resume-gate.sh` runs the same correctness-only cases with fixed final receipt persistence; no official observation existed or was rerun because of this bookkeeping correction.

After exact identity, tool pins and24persisted gate checks pass, run `nohup bash /opt/website-publication/controller.sh` with output redirected to evidence/official.log. Root standing authorization is recorded in task coordination. Controller executes all234observations, separately saves adapter diff/hash/affinity receipts, rebuilds summaries, rechecks identity and runs independent audit.py. Do not install or profile concurrently.

Preserve this host after website timings/collection/audit for the separately authorized15filesystem post-exec memory cells. Runtime agent must wait for explicit timing-complete coordination; root owns final evidence push, local verification and teardown. No Labs changes until audited data is available.
