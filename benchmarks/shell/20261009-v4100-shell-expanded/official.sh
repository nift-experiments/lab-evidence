#!/bin/bash
set -euo pipefail
export PATH=/opt/campaign/tools/bin:/usr/local/bin:/usr/bin:/bin
cd /opt/campaign/shell-benchmark
[ "$(git status --porcelain)" = "" ]
[ "$(git -C /opt/campaign/nift status --porcelain)" = "" ]
date -u +%FT%TZ > /opt/campaign/evidence/official-start.txt
taskset -c 0 python3 scripts/benchmark.py --nift /opt/campaign/tools/bin/nift --samples 100 --work-samples 10 --warmups 3 --output /opt/campaign/evidence/shell-repeated.json
taskset -c 0 python3 scripts/benchmark.py --nift /opt/campaign/tools/bin/nift --samples 30 --work-samples 10 --warmups 3 --state application-cold --output /opt/campaign/evidence/shell-application-cold.json
python3 scripts/summarize.py --input /opt/campaign/evidence/shell-repeated.json --output /opt/campaign/evidence/shell-repeated-summary.json
python3 scripts/summarize.py --input /opt/campaign/evidence/shell-application-cold.json --output /opt/campaign/evidence/shell-fresh-summary.json
taskset -c 0 python3 scripts/workload_campaign.py --nift /opt/campaign/tools/bin/nift --output /opt/campaign/evidence/shell-workloads.json
python3 scripts/validate_workloads.py --input /opt/campaign/evidence/shell-workloads.json --output /opt/campaign/evidence/workload-validation.json
taskset -c 0 python3 scripts/verify_rc.py --nift /opt/campaign/tools/bin/nift --output /opt/campaign/evidence/rc-certification-after.json
python3 scripts/test_measurement.py
python3 scripts/test_workloads.py
[ "$(git status --porcelain)" = "" ]
[ "$(git -C /opt/campaign/nift status --porcelain)" = "" ]
date -u +%FT%TZ > /opt/campaign/evidence/official-end.txt
printf 'OFFICIAL_PASS\n'
