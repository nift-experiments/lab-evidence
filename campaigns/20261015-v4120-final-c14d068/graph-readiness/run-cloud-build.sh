#!/bin/sh
set -eu
: "${OUTPUT:?fresh output directory required}" "${CPUS:?inventory CPU ids required}"
export PATH=/opt/refresh-tools/bin:$PATH
export NINJA=/opt/refresh-tools/bin/ninja
export NIFT=/opt/nift/nift NIFT_SOURCE_SHA=c14d06835bca515a5281e41da0e40219c2d60ef0
[ "$(git rev-parse HEAD)" = e95bfe88ac9e1eaf67cfeb8f67020fc3373ab81e ]
[ ! -e "$OUTPUT" ]
python3 scripts/campaign.py --plan docs/refresh-7f7e487-20261013/plan.json --output "$OUTPUT" --cpus "$CPUS"
python3 scripts/validate_campaign.py "$OUTPUT" --official
python3 scripts/summarize.py "$OUTPUT"
python3 scripts/audit_campaign.py "$OUTPUT"
