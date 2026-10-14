#!/bin/bash
set -euo pipefail
export GIT_TERMINAL_PROMPT=0
export PATH=/opt/campaign/tools/bin:/usr/local/bin:/usr/bin:/bin
mkdir -p /opt/campaign/evidence
if test ! -d /opt/campaign/shell-benchmark/.git; then
 git -c credential.helper= clone --quiet https://github.com/nift-dev/shell-benchmark.git /opt/campaign/shell-benchmark
fi
git -C /opt/campaign/shell-benchmark checkout --quiet aec1349fd0ba986108d9c851944e41e5ed330b6f
test "$(git -C /opt/campaign/shell-benchmark rev-parse HEAD)" = aec1349fd0ba986108d9c851944e41e5ed330b6f
test -z "$(git -C /opt/campaign/shell-benchmark status --porcelain)"
NIFT_BINARY=/opt/nift/nift bash /opt/provision-pinned-comparators.sh
python3 /opt/capture-comparators.py shell-benchmark
