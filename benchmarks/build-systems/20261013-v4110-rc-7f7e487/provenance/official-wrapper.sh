#!/bin/bash
set -euo pipefail
cd /opt/suite
export PATH=/opt/refresh-tools/bin:$PATH
export NIFT=/opt/nift/nift
export NINJA=/opt/refresh-tools/bin/ninja
export NIFT_SOURCE_SHA=7f7e487c47a87e871dfef53345e2b71288008bff
test "$(git rev-parse HEAD)" = e95bfe88ac9e1eaf67cfeb8f67020fc3373ab81e
test -z "$(git status --porcelain)"
test "$(git -C /opt/nift rev-parse HEAD)" = "$NIFT_SOURCE_SHA"
test -z "$(git -C /opt/nift status --porcelain)"
echo '671e182ea31f3a23af92dadd738aba43edcb427670e7cf2f0d06b6362d28a606  /opt/nift/nift' | sha256sum -c -
python3 scripts/campaign.py --plan docs/refresh-7f7e487-20261013/plan.json --output /opt/results/build-systems-20261013-v4110-rc-7f7e487 --cpus 0,1,2,3
python3 scripts/validate_campaign.py /opt/results/build-systems-20261013-v4110-rc-7f7e487 --official
python3 scripts/audit_campaign.py /opt/results/build-systems-20261013-v4110-rc-7f7e487
python3 scripts/summarize.py /opt/results/build-systems-20261013-v4110-rc-7f7e487
echo 'BUILD-SYSTEMS OFFICIAL COMPLETE AND AUDITED'
