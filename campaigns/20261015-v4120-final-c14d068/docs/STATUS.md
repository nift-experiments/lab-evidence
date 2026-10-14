# Final v4.12 recertification — current checkpoint

Candidate: `c14d06835bca515a5281e41da0e40219c2d60ef0`, unreleased Nift v4.12.0. All eight fresh clean source builds and pinned suite/comparator inventories are verified. Common official CLI SHA256: `7dd42dcee5ca4a6965f0823c0ae59198282da1eb77e0fcd4cae93a537870a6fb`. Official GCC 13.3/O2; local GCC 15 receipts are correctness preparation only. Nine exact-SHA CI workflows passed.

## Engineering findings

Scripting is fully audited: 1,880 measured and 376 warmups. Its separate 72-observation exact-source same-node comparison substantially recovers the major original call regressions. Small calls: release 4.710201 → original 7.374958 → final 4.678490 ms. Large: release193.600459 → original 469.418897 → final 198.619789 ms. Large retains +2.59% (+5.01933ms) versus release and 8/10 final pairs slower; overlapping ranges do not prove equality. Current official competitor deficits still reach 137.83× for frequency-count and 136.53× for large calls versus LuaJIT.

Template is fully audited: 17,950 measured and 750 warmups. Separate 78 diagnostic/control rows retain release improvements 72.19% 10k source-loop,51.21% fresh-loop and38.09% article-source. Checkpoint fresh-loop+4.90% and article-source+0.35% remain descriptive increases. The official 10k source-loop is still15.16× behind Handlebars. Inherited memory floor controls confirm raw launch RSS is retained/unranked.

Complete current interim leagues, confidence qualifications and recovery table are in INTERIM-RECERTIFICATION.md/JSON and REGRESSION-RECOVERY.md. Other blocker recovery and practitioner/release conclusions remain pending the full sweep. No cross-node trend substitutes for controlled same-node evidence.

## Lifecycle and remaining work

Scripting host 108162749 and template host 108162740 are closed after official evidence, audits and all required diagnostics were pushed at 3521529. CLI absence/API404 and per-host known-host removal verified; lifecycle receipts pushed 84656a4. Shared private access remains only for six active campaign hosts.

Full collectors active: build 108162775, concurrency 108162758, filesystem 108162735, shell 108162738, task 108162743 and website 108162733. Frozen total plan 67,153 observations. Task's first 153 observations and failed 154/cache are rejected and preserved for preflight-cache contamination: Turbo restored valid prior outputs but the benchmark required action execution. The authoritative unchanged full 1,527-observation restart uses a fresh exact-suite workspace; no rejected samples reused. Both build and other collectors remain unaffected.

Timing must finish before any per-host installation, profiling or old-version diagnostic. Collect/audit/push complete raw/warmup/log identities, run required separated diagnostics, then delete each owned host and verify CLI absence/API404. Cleanup shared temporary state only after all eight close. The approved 20-minute follow-up remains active.

No Labs, tags, releases, packages or download publication is authorized. Labs' 193 baseline files remain unchanged. Historical evidence and interrupted 342 preparation failures are preserved; that available interrupted namespace had no evidenced official suite launches or campaign hosts. All final local/cloud preflight gates passed before official collection.
