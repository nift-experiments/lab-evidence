#!/bin/bash
set -euo pipefail
export PATH=/opt/campaign/tools/bin:/usr/local/bin:/usr/bin:/bin
cd /opt/campaign/website-generator-benchmark
E=/opt/campaign/evidence/official-refresh
mkdir -p "$E"
test "$(git rev-parse HEAD)" = a2890bc504cf7c55b77cd4fddae17403b7caf8ae
test -z "$(git status --porcelain)"
test "$(git -C /opt/nift rev-parse HEAD)" = c14d06835bca515a5281e41da0e40219c2d60ef0
test -z "$(git -C /opt/nift status --porcelain)"
python3 - <<'VERIFY'
import json,hashlib
from pathlib import Path
d=json.loads(Path('/opt/campaign/evidence/refresh-readiness.json').read_text())
assert d['suite_sha']=='a2890bc504cf7c55b77cd4fddae17403b7caf8ae'
for k,v in d['comparators'].items():
 if 'executable' in v:assert hashlib.sha256(Path(v['executable']).read_bytes()).hexdigest()==v['sha256']
VERIFY
NIFT_CANDIDATE_VERSION=4.12.0
: "${NIFT_CANDIDATE_BINARY_SHA256:?frozen cloud CLI hash required}"
test "$(sha256sum /opt/campaign/tools/bin/nift | cut -d' ' -f1)" = "$NIFT_CANDIDATE_BINARY_SHA256"
test "$(/opt/campaign/tools/bin/nift --version)" = "Nift v4.12.0"
date -u +%FT%TZ > "$E/start.txt"
taskset -c 0 python3 scripts/campaign.py --nift /opt/campaign/tools/bin/nift --hugo /opt/campaign/tools/bin/hugo --node-project /opt/campaign/website-generator-benchmark --pages 100 --samples 5 --warmups 1 --timeout 1200 --output "$E"/website-100.json
taskset -c 0 python3 scripts/campaign.py --nift /opt/campaign/tools/bin/nift --hugo /opt/campaign/tools/bin/hugo --node-project /opt/campaign/website-generator-benchmark --pages 1000 --samples 5 --warmups 1 --timeout 1200 --output "$E"/website-1000.json
taskset -c 0 python3 scripts/campaign.py --nift /opt/campaign/tools/bin/nift --hugo /opt/campaign/tools/bin/hugo --node-project /opt/campaign/website-generator-benchmark --pages 10000 --samples 5 --warmups 1 --timeout 1200 --output "$E"/website-10000.json
taskset -c 0 python3 scripts/targeted_campaign.py --nift /opt/campaign/tools/bin/nift --expected-nift-version "$NIFT_CANDIDATE_VERSION" --expected-nift-sha256 "$NIFT_CANDIDATE_BINARY_SHA256" --same-host-serial --samples 5 --warmups 1 --output "$E"/targeted-builds.json
python3 scripts/summarize.py --input "$E/website-100.json" --output "$E/website-100-summary.json"
python3 scripts/summarize.py --input "$E/website-1000.json" --output "$E/website-1000-summary.json"
python3 scripts/summarize.py --input "$E/website-10000.json" --output "$E/website-10000-summary.json"
python3 scripts/summarize.py --input "$E/targeted-builds.json" --output "$E/targeted-builds-summary.json"
test -z "$(git status --porcelain)"
test -z "$(git -C /opt/nift status --porcelain)"
date -u +%FT%TZ > "$E/end.txt"
echo OFFICIAL_REFRESH_PASS > "$E/PASS"
echo OFFICIAL_REFRESH_PASS
