#!/bin/bash
set -euo pipefail
export PATH=/opt/campaign/tools/bin:/usr/local/bin:/usr/bin:/bin
cd /opt/campaign/shell-benchmark
[ "$(git status --porcelain)" = "" ]
[ "$(nift version)" = "Nift v4.10.0" ]
python3 scripts/test_measurement.py
python3 scripts/test_workloads.py
taskset -c 0 python3 scripts/verify_rc.py --nift /opt/campaign/tools/bin/nift --output /opt/campaign/evidence/rc-certification.json
taskset -c 0 python3 scripts/calibrate.py --output /opt/campaign/evidence/calibration.json
taskset -c 0 python3 scripts/diagnose_rc.py --output /opt/campaign/evidence/rc-body.json
taskset -c 0 python3 scripts/benchmark.py --nift /opt/campaign/tools/bin/nift --samples 5 --work-samples 5 --warmups 1 --output /opt/campaign/evidence/smoke-shell-repeated.json
taskset -c 0 python3 scripts/benchmark.py --nift /opt/campaign/tools/bin/nift --samples 5 --work-samples 5 --warmups 1 --state application-cold --output /opt/campaign/evidence/smoke-shell-fresh.json
taskset -c 0 python3 scripts/workload_campaign.py --nift /opt/campaign/tools/bin/nift --smoke --output /opt/campaign/evidence/smoke-shell-workloads.json
python3 scripts/validate_workloads.py --input /opt/campaign/evidence/smoke-shell-workloads.json --output /opt/campaign/evidence/smoke-workload-validation.json
python3 - <<'SCHEMA'
import json,jsonschema
from pathlib import Path
jsonschema.validate(json.loads(Path('/opt/campaign/evidence/smoke-shell-workloads.json').read_text()),json.loads(Path('schemas/shell-workloads.schema.json').read_text()))
SCHEMA
df -h /opt/campaign > /opt/campaign/evidence/disk-after-smoke.txt
printf 'SMOKE_PASS\n'
