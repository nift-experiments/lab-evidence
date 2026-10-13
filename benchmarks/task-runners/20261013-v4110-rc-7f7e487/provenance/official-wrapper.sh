#!/bin/bash
set -euo pipefail
cd /opt/suite
export PATH=/opt/refresh-tools/node-v22.22.1-linux-x64/bin:$PATH
export NIFT=/opt/nift/nift
export NIFT_SOURCE_SHA=7f7e487c47a87e871dfef53345e2b71288008bff
test "$(git rev-parse HEAD)" = f37b63bd13cf71256607ba4652bcc911e270f94e
test -z "$(git status --porcelain)"
test "$(git -C /opt/nift rev-parse HEAD)" = "$NIFT_SOURCE_SHA"
test -z "$(git -C /opt/nift status --porcelain)"
echo '671e182ea31f3a23af92dadd738aba43edcb427670e7cf2f0d06b6362d28a606  /opt/nift/nift' | sha256sum -c -
taskset -c 0-3 python3 scripts/campaign-refresh.py --output /opt/results/task-runners-20261013-v4110-rc-7f7e487
python3 scripts/audit.py /opt/results/task-runners-20261013-v4110-rc-7f7e487
echo 'TASK-RUNNERS OFFICIAL COMPLETE AND AUDITED'
