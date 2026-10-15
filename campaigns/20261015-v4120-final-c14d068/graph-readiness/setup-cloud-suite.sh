#!/bin/bash
set -euo pipefail
: "${SUITE:?build-systems or task-runners}" "${PREPARATION:?absolute preparation receipts directory}"
mkdir -p "$PREPARATION" /opt/suites
case "$SUITE" in
 build-systems) SUITE_SHA=e95bfe88ac9e1eaf67cfeb8f67020fc3373ab81e ;;
 task-runners) SUITE_SHA=f37b63bd13cf71256607ba4652bcc911e270f94e ;;
 *) exit 2 ;;
esac
export NIFT=/opt/nift/nift NIFT_SOURCE_SHA=c14d06835bca515a5281e41da0e40219c2d60ef0
[ "$(git -C /opt/nift rev-parse HEAD)" = "$NIFT_SOURCE_SHA" ]
[ -z "$(git -C /opt/nift status --porcelain)" ]
[ ! -e "/opt/suites/$SUITE" ]
git clone "https://github.com/nift-experiments/$SUITE.git" "/opt/suites/$SUITE"
cd "/opt/suites/$SUITE"
git checkout --detach "$SUITE_SHA"
[ "$(git rev-parse HEAD)" = "$SUITE_SHA" ]
[ -z "$(git status --porcelain)" ]
if [ "$SUITE" = task-runners ]; then
 mkdir -p /opt/node-final
 curl -fL https://nodejs.org/dist/v22.22.1/SHASUMS256.txt -o "$PREPARATION/node-SHASUMS256.txt"
 curl -fL https://nodejs.org/dist/v22.22.1/node-v22.22.1-linux-x64.tar.xz -o "$PREPARATION/node.tar.xz"
 (cd "$PREPARATION" && grep ' node-v22.22.1-linux-x64.tar.xz$' node-SHASUMS256.txt | sed 's/node-v22.22.1-linux-x64.tar.xz/node.tar.xz/' | sha256sum -c -)
 tar -xJf "$PREPARATION/node.tar.xz" --strip-components=1 -C /opt/node-final
 export PATH=/opt/node-final/bin:$PATH
 npm install --global npm@9.2.0 --no-audit --no-fund
 [ "$(node --version)" = v22.22.1 ]
 [ "$(npm --version)" = 9.2.0 ]
fi
bash "$(dirname "$0")/prepare-cloud-comparators.sh" > "$PREPARATION/comparator-install.log" 2>&1
export PATH=/opt/refresh-tools/bin:${PATH}
export NINJA=/opt/refresh-tools/bin/ninja
mkdir -p work
ln -s /opt/nift work/nift-source
{ git rev-parse HEAD; git -C /opt/nift rev-parse HEAD; "$NIFT" --version; sha256sum "$NIFT"; g++ --version; uname -a; lscpu; } > "$PREPARATION/identity.txt"
if [ "$SUITE" = build-systems ]; then
 { make --version; "$NINJA" --version; sha256sum "$(command -v make)" "$NINJA"; } > "$PREPARATION/comparators.txt"
 for profile in light heavy; do
  for jobs in 1 2 4; do
   python3 scripts/certify.py --size 100 --profile "$profile" --jobs "$jobs" --results "$PREPARATION/native-$profile-j$jobs"
  done
 done
 for jobs in 1 2 4; do
  python3 scripts/certify.py --kind tiny --size 100 --jobs "$jobs" --scenarios noop leaf batch10 batch10pct full --results "$PREPARATION/tiny-j$jobs"
 done
else
 { node --version; npm --version; work/tools/node_modules/.bin/turbo --version; work/tools/node_modules/.bin/nx --version; sha256sum "$(command -v node)" "$(command -v npm)"; sha256sum docs/tools-package-lock.json; sha256sum "$(readlink -f work/tools/node_modules/.bin/turbo)" "$(readlink -f work/tools/node_modules/.bin/nx)"; find work/tools/node_modules -type f \( -path '*/@turbo/linux-64/bin/turbo' -o -name 'nx.linux-x64-gnu.node' \) -exec sha256sum {} \;; } > "$PREPARATION/comparators.txt"
 TASK_RUNNER_PROBE_OUTPUT="$PREPARATION/semantic-probe.json" python3 scripts/probe.py
 python3 scripts/campaign-refresh.py --smoke --output "$PREPARATION/full-smoke"
 python3 scripts/audit.py "$PREPARATION/full-smoke"
fi
