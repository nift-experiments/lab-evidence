#!/usr/bin/env bash
set -euo pipefail
while kill -0 1279 2>/dev/null; do sleep 30; done
cd /opt/filesystem/suite
test -f work/official/complete.json
git fetch origin main
git checkout 5af31b2
python3 scripts/filter_supplement.py
python3 work/filter-suite/scripts/run.py > work/filter-campaign.log 2>&1
python3 work/filter-suite/scripts/audit.py work/filter-suite/work/official
python3 scripts/audit_distributions.py work/official
python3 scripts/audit_distributions.py work/filter-suite/work/official
printf 'FILTER SUPPLEMENT COMPLETE\n'
