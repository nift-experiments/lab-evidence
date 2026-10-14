#!/bin/bash
set -euo pipefail
export GIT_TERMINAL_PROMPT=0
export PATH=/opt/campaign/tools/bin:/usr/local/bin:/usr/bin:/bin
mkdir -p /opt/campaign/evidence
if test ! -d /opt/campaign/scripting-benchmark/.git; then
 git -c credential.helper= clone --quiet https://github.com/nift-dev/scripting-benchmark.git /opt/campaign/scripting-benchmark
fi
git -C /opt/campaign/scripting-benchmark checkout --quiet f889fff4af94658259932f611d4b0ad681c1eebf
test "$(git -C /opt/campaign/scripting-benchmark rev-parse HEAD)" = f889fff4af94658259932f611d4b0ad681c1eebf
test -z "$(git -C /opt/campaign/scripting-benchmark status --porcelain)"
NIFT_BINARY=/opt/nift/nift bash /opt/provision-pinned-comparators.sh
python3 /opt/capture-comparators.py scripting-benchmark
