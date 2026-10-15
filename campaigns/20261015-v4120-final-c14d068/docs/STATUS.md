# Final v4.12 recertification — current checkpoint

Candidate: `c14d06835bca515a5281e41da0e40219c2d60ef0`, unreleased Nift v4.12.0. All eight fresh clean source builds and pinned suite/comparator inventories are verified. Common official CLI SHA256: `7dd42dcee5ca4a6965f0823c0ae59198282da1eb77e0fcd4cae93a537870a6fb`. Official GCC 13.3/O2; local GCC 15 receipts are correctness preparation only. Nine exact-SHA CI workflows passed.

## Engineering findings

Five official suites are independently audited: scripting, template, concurrency, website and task. Four hosts are verified closed. Task diagnostics are complete and awaiting pushed evidence and teardown. Build, filesystem and shell continue their frozen full collections.

Scripting is fully audited: 1,880 measured and 376 warmups. Its separate 72-observation exact-source same-node comparison substantially recovers the major original call regressions. Small calls: release 4.710201 → original 7.374958 → final 4.678490 ms. Large: release193.600459 → original 469.418897 → final 198.619789 ms. Large retains +2.59% (+5.01933ms) versus release and 8/10 final pairs slower; overlapping ranges do not prove equality. Current official competitor deficits still reach 137.83× for frequency-count and 136.53× for large calls versus LuaJIT.

Template is fully audited: 17,950 measured and 750 warmups. Separate 78 diagnostic/control rows retain release improvements 72.19% 10k source-loop,51.21% fresh-loop and38.09% article-source. Checkpoint fresh-loop+4.90% and article-source+0.35% remain descriptive increases. The official 10k source-loop is still15.16× behind Handlebars. Inherited memory floor controls confirm raw launch RSS is retained/unranked.

Complete current interim leagues, confidence qualifications and recovery table are in INTERIM-RECERTIFICATION.md/JSON and REGRESSION-RECOVERY.md. Other blocker recovery and practitioner/release conclusions remain pending the full sweep. No cross-node trend substitutes for controlled same-node evidence.

## Lifecycle and remaining work

Five hosts are closed after complete official evidence, independent audits and required diagnostics were pushed: scripting108162749 and template108162740 (evidence3521529, teardown84656a4); concurrency108162758 and website108162733 (evidence0785ec0, teardownb0ccb36); task108162743 (evidence55cae88, teardowne5dafd0). Every deletion verified CLI absence, API404 and per-host known-host removal. Do not contact these closed hosts.

Only build108162775, filesystem108162735 and shell108162738 remain collecting. Frozen official total remains67,153 observations. Task's first153 observations and failed154/cache are rejected and preserved for preflight-cache contamination: Turbo restored valid prior outputs but the benchmark required action execution. The unchanged fresh-workspace full restart passed1,527 observations; none reused from rejection.

Timing must finish before any per-host installation, profiling or old-version diagnostic. Collect/audit/push complete raw/warmup/log identities, run required separated diagnostics, then delete each owned host and verify CLI absence/API404. Cleanup shared temporary state only after all eight close. The approved 20-minute follow-up remains active.

No Labs, tags, releases, packages or download publication is authorized. Labs' 193 baseline files remain unchanged. Historical evidence and interrupted 342 preparation failures are preserved; that available interrupted namespace had no evidenced official suite launches or campaign hosts. All final local/cloud preflight gates passed before official collection.

Latest audited competitive results: persistent tiny10k Nift30,949.017ms versusGo17.781ms (1,740.60×); persistent schedule10k28,018.832ms versusGo17.989ms (1,557.52×). These are current same-node deficits, not claims of a new version regression. Website10k fresh3,015.980ms versusHugo2,623.337ms; warm2,613.877ms versusHugo2,723.813ms. Website controlled recovery: release2871.545/original3278.509/final2951.495ms; final−9.97% versus original and +2.78% versus release (overlapping ranges). Required website diagnostics and verified teardown complete. Complete current wall deficit league now contains171rows; memory/capabilities and cross-node trends remain separate.

## Latest closeout

Task full series independently audited: 1,434 measured +93 warmups; targeted tiny100 full same-node diagnostic queued. Concurrency queue improves69.48% versus release; schedule retains descriptive+8.70% with overlapping ranges. Retained runtime slowdown remains8.07x over ten requests; no root cause established. Held10k timed out beforeREADY and is excluded from rankings. Website and concurrency official+required diagnostic evidence pushed0785ec0; both hosts deleted with CLI absence/API404 and known-host cleanup verified. Four of eight hosts now closed. Build, filesystem and shell continue timing; task remains for its bounded diagnostic. No publication authorized.

Latest task control: release138.333/original129.031/final134.851ms; final−2.52% versus release, +4.51% versus original, overlapping five-sample ranges. All18 diagnostic observations audited. Build checkpoint1998/9348; shell expanded checkpoint423; filesystem rename10000 healthy. These partial counts are not accepted final results.

Task evidence and controlled diagnostic pushed55cae88; host108162743 deleted, CLI absent/API404 and known-host cleanup verified. Five of eight hosts closed. Only build108162775, filesystem108162735 and shell108162738 remain.

Shell official complete and independently audited:293jobs,7855measured+711warmups=8566. Arithmetic17.263ms and calls21.956ms lead their peer workloads. Remaining traversal4.05xNu,metadata2.92xFish,concatenation2.41xZsh deficits now in complete sorted leagues. External helper-only baselines excluded; startup prepared/fresh distinct. Separate72-observation exact three-way recovery running on idle shell host. Six official suites audited, five hosts closed; build/filesystem continue timing.

Shell recovery independently audited72observations: stringsrelease59.696/original66.950/final18.680ms,−68.71% versus release; callsrelease20.989/original44.971/final21.655ms,−51.85% versus original but+3.17% release residual (8/10 slower, overlap). All required shell work complete; push then teardown.

Shell complete evidence pushed8630bd0; host108162738 deleted with CLI absent/API404 and per-host known-host cleanup verified. Six hosts now closed. Only build108162775 and filesystem108162735 remain active. Complete leagues:17 baseline-explicit improvements,7positive version changes,205current peer deficits. No publication authorized.

Filesystem official15016 and36 exactthreeway diagnostic observations independently audited. Release improvements stat90.80%,sizefilter88.58%,walk87.02%; stat+1.63% versus original is descriptive3samples. Portable hash detection still49.89xGo. Sevenofficialsuites nowaudited; pushandFS teardownnext. Build9250/9348 remains collecting; website supplementalplanv3 default-only is separate.
