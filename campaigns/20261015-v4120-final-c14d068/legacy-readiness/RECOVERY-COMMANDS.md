# Separate recovery execution

After official PASS and parent authorization, upload build-recovery-versions.sh and recovery-three-way.py to /opt. Run `bash /opt/build-recovery-versions.sh` once on each of the three suite hosts. Fresh clean exact-source versions are built using the same host compiler/default flags as final; build logs and package/compiler receipts are outside samples. No installed Nift is used.

Then run the appropriate command:

- `taskset -c 0 python3 /opt/recovery-three-way.py scripting --output /opt/campaign/evidence/recovery-three-way-scripting`
- `taskset -c 0 python3 /opt/recovery-three-way.py shell --output /opt/campaign/evidence/recovery-three-way-shell`
- `taskset -c 0 python3 /opt/recovery-three-way.py website --output /opt/campaign/evidence/recovery-three-way-website`

Counts: scripting 72 observations (60 measured/12 warmups); shell 72 (60/12); website 18 (15/3). Six permutations cycle through adjacent three-version blocks; 10 and 5 measured rounds cannot perfectly balance six permutations, so audit checks the exact declared schedule rather than claiming perfect balance. Output/source/scenario/clock/oracles are frozen. Preserve all raw, stdout/stderr, failures, summary, controller, build logs and inventory. Run `python3 audit-recovery-three-way.py COLLECTED_DIRECTORY` locally independently. Profiling is a separate subsequent step only if justified. Official raw hashes are checked unchanged after diagnostics.
