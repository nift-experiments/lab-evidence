#!/usr/bin/env bash
set -euo pipefail
R=/opt/website-publication
for i in $(seq 1 300); do
 test ! -f "$R/CLOUD_GATE_PASS" || break
 sleep 2
done
test -f "$R/CLOUD_GATE_PASS"
cp "$R/evidence/website-correctness.json" "$R/evidence/website-correctness-attempt1-partial-receipt.json"
cp "$R/gate.py" "$R/gate-attempt1.py"
cp "$R/gate-fixed.py" "$R/gate.py"
export PATH=/opt/website-publication/tools/bin:/usr/local/bin:/usr/bin:/bin
unset GOMAXPROCS
taskset -c 0-3 python3 "$R/gate.py" > "$R/evidence/gate-complete-receipt.log" 2>&1
python3 - <<'PY'
import json
from pathlib import Path
d=json.loads(Path('/opt/website-publication/evidence/website-correctness.json').read_text());assert len(d['rows'])==24 and all(r['correct'] for r in d['rows'])
PY
echo GATE24_PASS > "$R/GATE24_PASS"
