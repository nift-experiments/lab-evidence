#!/bin/bash
set -euo pipefail
export PATH=/opt/campaign/tools/bin:/usr/local/bin:/usr/bin:/bin
cd /opt/campaign/shell-benchmark
E=/opt/campaign/evidence/official-refresh
mkdir -p "$E"
test "$(git rev-parse HEAD)" = aec1349fd0ba986108d9c851944e41e5ed330b6f
test -z "$(git status --porcelain)"
test "$(git -C /opt/nift rev-parse HEAD)" = 7f7e487c47a87e871dfef53345e2b71288008bff
test -z "$(git -C /opt/nift status --porcelain)"
python3 - <<'VERIFY'
import json,hashlib
from pathlib import Path
d=json.loads(Path('/opt/campaign/evidence/refresh-readiness.json').read_text())
assert d['suite_sha']=='aec1349fd0ba986108d9c851944e41e5ed330b6f'
for k,v in d['comparators'].items():
 if 'executable' in v:assert hashlib.sha256(Path(v['executable']).read_bytes()).hexdigest()==v['sha256']
VERIFY
NIFT_CANDIDATE_VERSION=4.11.0
NIFT_CANDIDATE_BINARY_SHA256=671e182ea31f3a23af92dadd738aba43edcb427670e7cf2f0d06b6362d28a606
date -u +%FT%TZ > "$E/start.txt"
taskset -c 0 python3 scripts/verify_rc.py --nift /opt/campaign/tools/bin/nift --output "$E"/rc-before.json
taskset -c 0 python3 scripts/benchmark.py --nift /opt/campaign/tools/bin/nift --samples 100 --work-samples 10 --warmups 3 --output "$E"/shell-repeated.json
taskset -c 0 python3 scripts/benchmark.py --nift /opt/campaign/tools/bin/nift --samples 30 --work-samples 10 --warmups 3 --state application-cold --output "$E"/shell-application-cold.json
taskset -c 0 python3 scripts/workload_campaign.py --nift /opt/campaign/tools/bin/nift --output "$E"/shell-workloads.json
python3 scripts/validate_workloads.py --input "$E"/shell-workloads.json --output "$E"/workload-validation.json
taskset -c 0 python3 scripts/verify_rc.py --nift /opt/campaign/tools/bin/nift --output "$E"/rc-after.json
python3 scripts/summarize.py --input "$E/shell-repeated.json" --output "$E/shell-repeated-summary.json"
python3 scripts/summarize.py --input "$E/shell-application-cold.json" --output "$E/shell-fresh-summary.json"
test -z "$(git status --porcelain)"
test -z "$(git -C /opt/nift status --porcelain)"
date -u +%FT%TZ > "$E/end.txt"
echo OFFICIAL_REFRESH_PASS > "$E/PASS"
echo OFFICIAL_REFRESH_PASS
