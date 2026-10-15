#!/usr/bin/env bash
set -euo pipefail
export PATH=/opt/website-publication/tools/bin:/usr/local/bin:/usr/bin:/bin
unset GOMAXPROCS
cd /opt/website-publication/suite
E=/opt/website-publication/evidence/official-allcore
mkdir -p "$E"
test -f /opt/website-publication/SETUP_PASS
python3 /opt/website-publication/identity.py
python3 - <<'PY'
import json
from pathlib import Path
d=json.loads(Path('/opt/website-publication/evidence/website-correctness.json').read_text());assert len(d['rows'])==24 and all(r['correct'] for r in d['rows'])
PY
date -u +%FT%TZ > "$E/start.txt"
for pages in 100 1000 10000; do
 taskset -c 0-3 python3 /opt/website-publication/allcore.py campaign --nift /opt/nift/nift --hugo /opt/website-publication/tools/bin/hugo --node-project /opt/website-publication/suite --pages "$pages" --samples 5 --warmups 1 --timeout 1200 --output "$E/website-$pages.json"
 python3 scripts/summarize.py --input "$E/website-$pages.json" --output "$E/website-$pages-summary.json"
done
taskset -c 0-3 python3 /opt/website-publication/allcore.py targeted_campaign --nift /opt/nift/nift --expected-nift-version 4.12.0 --expected-nift-sha256 7dd42dcee5ca4a6965f0823c0ae59198282da1eb77e0fcd4cae93a537870a6fb --same-host-serial --samples 5 --warmups 1 --output "$E/targeted-builds.json"
python3 scripts/summarize.py --input "$E/targeted-builds.json" --output "$E/targeted-builds-summary.json"
python3 /opt/website-publication/identity.py
python3 /opt/website-publication/audit.py "$E"
date -u +%FT%TZ > "$E/end.txt"
echo FULL_ALLCORE_PASS > "$E/PASS"
