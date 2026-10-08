# Nift benchmark campaign — working outline

Authorized scope: audit and improve scripting-benchmark and
website-generator-benchmark; build shell-benchmark; validate locally; run a
reproducibly provisioned inexpensive Linode; retain evidence; destroy and verify
node removal; publish individually designed Labs reports. No Nift source changes.

1. Audit existing suites before changes (committed in both repositories).
2. Correct per-sample correctness, cache terminology, run isolation, fixture
   parity and short-duration measurement; validate failure gates.
3. Shell: Bash/Zsh/Fish/Nushell/Nift, bare/empty/light/moderate RC scenarios,
   isolated HOME/XDG with allowlisted environment, login distinctions where
   supported, startup distributions and native/process workloads. Never subtract
   RC timing. Inspect system configuration and test contamination explicitly.
4. Freeze tool versions, binary checksums and suite revisions; record exact
   commands, raw samples, OS/kernel, CPU/RAM and concurrency. Prepare outside
   timing. Direct fresh-process timing is not machine-cold timing.
5. Clean Linode pilot, then official samples; correctness on every run; investigate
   surprises. Save evidence before teardown; verify destruction.
6. Labs: inspect Capgo, Cloudflare and Omarchy report sources/designs first.
   Treat this as one publication with three feature articles, not three copies
   of a report template. Preserve dark Labs identity and its no-blue palette.
   - Scripting: code/profiler character, runtime lanes and workload/result
     pairings; separate startup, computation, filesystem/data and external work.
   - Website generation: architectural source/build/output motifs, corpus scale,
     full/incremental distinction and paired latency/memory; scaling where measured.
   - Shell: stronger readable cyberpunk/CLI character; startup distributions and
     RC matrix prominent; explain process → runtime → RC → prompt boundaries.
     Do not fabricate phase durations from total latency measurements.
   Share navigation/status, machine/version/evidence and caveat conventions.
   Cross-link as the Nift Benchmarks family with a small landing page.
   Choose charts by metric, label absolute values, use colour-independent cues,
   honour reduced motion, and keep tables usable on mobile.
7. Deliberate joint design review: visually recognizable subjects, coherent Labs
   identity, obvious headline findings, useful methodological visuals, desktop
   and mobile QA. Push apart cloned layouts; reconcile unrelated branding.
8. Reproduce from clean committed sources, regenerate tables, validate links,
   build Labs, inspect rendered pages, scan for credentials/temporary paths,
   commit/push suites and source/deployment repos, verify published URLs.
9. Final report: changes, comparability, versions/machine, headline observations,
   caveats/surprises, URLs/SHAs and external defensibility for each suite.

Completed state: official serial CPU-0 measurements, independent raw-summary checks,
clean-checkout reproduction and full RC certification passed. Bash and Zsh are
included alongside Fish/Nu/Nift. The disposable Linode was deleted and its absence
verified by API HTTP 404. Historical evidence is retained separately.

Presentation review: numeric headers align with values; scripting exposes all
seven languages across every workload and both sizes. Eight standalone measured
figures cover distributions, configuration, orchestration, scripting workloads,
corpus scaling and memory. All three reports pass desktop and 320/390 px checks;
wide tables and figures scroll within their own keyboard-accessible regions.

Follow-up presentation: scope exclusions use compact accessible dashes to preserve numeric-column widths. Corpus scaling includes original no-op, changed-leaf and shared-template incremental curves. A separate explicitly targeted one-page series is measured on another same-plan node, with its own full-build reference and complete-output gates; it is never pooled with original observations.
