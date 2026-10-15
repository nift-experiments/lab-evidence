#!/usr/bin/env bash
set -euo pipefail
# Local COLLECTION-PASS and accounting acceptance are checked by the operator before upload.
test -f /opt/website-publication/evidence/official-allcore/PASS
test -f /opt/website-publication/evidence/work-accounting/PASS
cd /opt/filesystem-postexec
mkdir -p collected
bash setup-after-website.sh >collected/setup.log 2>&1
python3 record-identity.py >collected/identity.stdout.json 2>collected/identity.stderr
cp suite/work/postexec-identity.json collected/postexec-identity.json
# Bound diagnostic lifetime without changing per-request measurement boundaries.
timeout --signal=TERM --kill-after=15s 1800s python3 collect-final.py >collected/postexec-memory.json 2>collected/collector.stderr
cp suite/work/fixture-{1000,10000,100000}.json collected/
python3 independent-audit.py collected >collected/audit.stdout.json 2>collected/audit.stderr
sha256sum /opt/nift/nift >collected/cli-after.sha256
test -z "$(git -C /opt/nift status --porcelain)"
printf 'FS_POSTEXEC_15_PASS\n' > collected/PASS
