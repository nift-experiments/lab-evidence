#!/usr/bin/env bash
set -euo pipefail
R=/opt/website-publication
for i in $(seq 1 900); do
 test ! -f "$R/GATE24_PASS" || break
 sleep 2
done
test -f "$R/GATE24_PASS"
test ! -e "$R/evidence/official-allcore/start.txt"
export PATH=/opt/website-publication/tools/bin:/usr/local/bin:/usr/bin:/bin
unset GOMAXPROCS
python3 "$R/identity.py"
python3 - <<'PY'
import json,hashlib,datetime,os
from pathlib import Path
r=Path('/opt/website-publication');gate=json.loads((r/'evidence/website-correctness.json').read_text());assert len(gate['rows'])==24 and all(x['correct'] for x in gate['rows'])
d={'launched_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'host_id':108212898,'host_plan':'g6-standard-4','region':'us-east','controller_pid':os.getppid(),'plan_sha256':hashlib.sha256((r/'PLAN.json').read_bytes()).hexdigest(),'correctness_gate_sha256':hashlib.sha256((r/'evidence/website-correctness.json').read_bytes()).hexdigest(),'gate_cases':24,'gate_pass':True,'planned_observations':234,'official_output':'/opt/website-publication/evidence/official-allcore','candidate':json.loads((r/'evidence/identity.json').read_text())['candidate'],'authorization':'Root standing GO after exact identity/toolpins/24case gate PASS; no further approval needed','retention':'Retain after website collection+audit for separate15FSpostexecmetrics; root owns teardown'}
(r/'evidence/LAUNCH.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d),flush=True)
PY
exec bash "$R/controller.sh"
