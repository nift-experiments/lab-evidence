#!/bin/bash
set -euo pipefail
export PATH=/opt/campaign/tools/bin:/usr/local/bin:/usr/bin:/bin
cd /opt/campaign/shell-benchmark
E=/opt/campaign/evidence
python3 scripts/test_measurement.py
python3 scripts/test_workloads.py
taskset -c 0 python3 scripts/verify_rc.py --nift /opt/nift/nift --output "$E/rc-certification.json"
taskset -c 0 python3 scripts/benchmark.py --nift /opt/nift/nift --samples 5 --work-samples 5 --warmups 1 --output "$E/shell-repeated-pilot.json"
taskset -c 0 python3 scripts/benchmark.py --nift /opt/nift/nift --samples 5 --work-samples 5 --warmups 1 --state application-cold --output "$E/shell-fresh-pilot.json"
python3 scripts/summarize.py --input "$E/shell-repeated-pilot.json" --output "$E/shell-repeated-pilot-summary.json"
python3 scripts/summarize.py --input "$E/shell-fresh-pilot.json" --output "$E/shell-fresh-pilot-summary.json"
taskset -c 0 python3 scripts/workload_campaign.py --nift /opt/nift/nift --smoke --output "$E/shell-workloads-pilot.json"
python3 scripts/validate_workloads.py --input "$E/shell-workloads-pilot.json" --output "$E/shell-workload-pilot-validation.json"
python3 - <<'PY'
import json,hashlib
from pathlib import Path
r=Path('/opt/campaign/evidence');files=['rc-certification.json','shell-repeated-pilot.json','shell-fresh-pilot.json','shell-workloads-pilot.json','shell-workload-pilot-validation.json'];d={n:json.loads((r/n).read_text()) for n in files};assert d[files[0]]['all_state_valid'];assert len(d[files[0]]['cases'])==18
for f in files[1:3]:assert len(d[f]['jobs'])==76 and d[f]['publishable']
assert d[files[-1]]['jobs']==141
(r/'cloud-gates.json').write_text(json.dumps({'kind':'cloud-correctness-pilot-not-official-performance','all_gates_pass':True,'candidate_source_sha':'7f7e487c47a87e871dfef53345e2b71288008bff','prepared_jobs':76,'fresh_jobs':76,'rc_cases':18,'workload_jobs':141,'receipts':{n:hashlib.sha256((r/n).read_bytes()).hexdigest() for n in files}},indent=2)+'\n')
PY
echo CLOUD_SHELL_GATES_PASS
