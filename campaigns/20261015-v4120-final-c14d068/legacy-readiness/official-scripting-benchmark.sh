#!/bin/bash
set -euo pipefail
export PATH=/opt/campaign/tools/bin:/usr/local/bin:/usr/bin:/bin
cd /opt/campaign/scripting-benchmark
E=/opt/campaign/evidence/official-refresh
mkdir -p "$E"
test "$(git rev-parse HEAD)" = f889fff4af94658259932f611d4b0ad681c1eebf
test -z "$(git status --porcelain)"
test "$(git -C /opt/nift rev-parse HEAD)" = c14d06835bca515a5281e41da0e40219c2d60ef0
test -z "$(git -C /opt/nift status --porcelain)"
python3 - <<'VERIFY'
import json,hashlib
from pathlib import Path
d=json.loads(Path('/opt/campaign/evidence/refresh-readiness.json').read_text())
assert d['suite_sha']=='f889fff4af94658259932f611d4b0ad681c1eebf'
for k,v in d['comparators'].items():
 if 'executable' in v:assert hashlib.sha256(Path(v['executable']).read_bytes()).hexdigest()==v['sha256']
VERIFY
NIFT_CANDIDATE_VERSION=4.12.0
: "${NIFT_CANDIDATE_BINARY_SHA256:?frozen cloud CLI hash required}"
test "$(sha256sum /opt/campaign/tools/bin/nift | cut -d' ' -f1)" = "$NIFT_CANDIDATE_BINARY_SHA256"
test "$(/opt/campaign/tools/bin/nift --version)" = "Nift v4.12.0"
date -u +%FT%TZ > "$E/start.txt"
taskset -c 0 python3 scripts/campaign.py --nift /opt/campaign/tools/bin/nift --families sanity/noop,sanity/output,sanity/loops,sanity/function-calls,arrays-strings-hash/scan,arrays-strings-hash/frequency-count,arrays-strings-hash/sliding-window,arrays-strings-hash/sort-index,arrays-strings-hash/map-set,dynamic-programming/fibonacci,graphs-trees-search/bfs,structured-data/json-parse,structured-data/json-transform,structured-data/json-traverse,filesystem/traverse --samples 10 --warmups 2 --timeout 180 --output "$E"/scripting.json
python3 scripts/summarize.py --input "$E"/scripting.json --output "$E"/scripting-summary.json
test -z "$(git status --porcelain)"
test -z "$(git -C /opt/nift status --porcelain)"
date -u +%FT%TZ > "$E/end.txt"
echo OFFICIAL_REFRESH_PASS > "$E/PASS"
echo OFFICIAL_REFRESH_PASS
