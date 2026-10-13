# Candidate refresh readiness — 2026-10-13

Candidate: committed `main` SHA `7f7e487c47a87e871dfef53345e2b71288008bff`. Use a fresh independent core clone, exact detached checkout and empty pre-build porcelain status. Untracked local core material is excluded. Historical measurements and docs remain frozen. These are preparation instructions, not a certification claim; freeze the new suite SHA only after correctness/capability gates pass.

Build with the Makefile's normal `-O2` configuration, record compiler/version/flags, source SHA, CLI SHA-256 and embedded library/adapter hashes where applicable. No sanitizer/instrumentation flags in official timing. Installers accept `NIFT_SOURCE_SHA` (full lowercase 40-digit SHA); absent override preserves historical behavior. Capture `make -n`/build log and effective flags in the shared campaign receipt. Do not reuse a local old `work/nift-source` clone for this campaign.

Comparator policy: retain historical exact versions for direct contract comparison, verify download checksums/lockfiles, and disclose these are pinned versions rather than an unsupported claim of latest. Any comparator update requires its own recorded pin and historical-comparability caveat. New series metadata may be provided with `NIFT_BENCH_VERSIONS_JSON` to filesystem/template runners; historical `docs/VERSIONS.json` stays unchanged.

Baseline suite: `787fec146d975a69aea5f99a233b918388fcdc30`. Historical pins: Python 3.14.4 ordinary GIL, Node 24.21.0, Bun 1.4.3, Go 1.27.2, uv 0.13.0. CLI build: `NIFT_SOURCE_SHA=<candidate> bash scripts/install.sh`.

Full small certification (after tool install, in an isolated refresh clone):

```sh
python3 scripts/environment.py
python3 scripts/semantics.py
python3 scripts/run.py --certify --output work/refresh-certify
python3 scripts/audit.py work/refresh-certify --certify
```

This preserves 64 historical scenarios, both fresh/persistent boundaries, exact per-cell oracles, worker limits and failures. `--select` is a pilot only, not complete certification. Environment recorder obtains actual candidate SHA, version, compiler and binary hashes rather than historical docs.

Readiness gap: `run.unsupported` and independent audit retain Nift 10k held-futures outside 8GiB, and primitive/API exclusions. Re-evaluate with a bounded checkpoint before accepting exclusions unchanged. Newly feasible historical exclusions belong to a clearly separate supplement, with matching oracle/audit coverage. Never allow a 13.7GiB historical checkpoint to OOM the shared campaign host. Reused-runtime/scheduling-growth diagnostics stay separate from primary timings. RSS samples from `/proc` are boundary-specific; compare only matching definitions.

Official commands after suite freeze: `python3 scripts/run.py --output work/refresh-official`; `python3 scripts/audit.py work/refresh-official`. Use a fresh output path; runner currently permits existing paths and truncates observations, so orchestration must enforce path absence before invocation.
