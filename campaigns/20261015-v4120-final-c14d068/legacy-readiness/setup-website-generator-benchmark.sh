#!/bin/bash
set -euo pipefail
export GIT_TERMINAL_PROMPT=0
export PATH=/opt/campaign/tools/bin:/usr/local/bin:/usr/bin:/bin
mkdir -p /opt/campaign/evidence
if test ! -d /opt/campaign/website-generator-benchmark/.git; then
 git -c credential.helper= clone --quiet https://github.com/nift-dev/website-generator-benchmark.git /opt/campaign/website-generator-benchmark
fi
git -C /opt/campaign/website-generator-benchmark checkout --quiet a2890bc504cf7c55b77cd4fddae17403b7caf8ae
test "$(git -C /opt/campaign/website-generator-benchmark rev-parse HEAD)" = a2890bc504cf7c55b77cd4fddae17403b7caf8ae
test -z "$(git -C /opt/campaign/website-generator-benchmark status --porcelain)"
NIFT_BINARY=/opt/nift/nift bash /opt/provision-pinned-comparators.sh
cd /opt/campaign/website-generator-benchmark
npm ci --ignore-scripts --no-audit --no-fund
python3 /opt/capture-comparators.py website-generator-benchmark
