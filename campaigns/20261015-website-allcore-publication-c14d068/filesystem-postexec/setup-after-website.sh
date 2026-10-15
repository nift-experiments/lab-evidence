#!/usr/bin/env bash
# Parent must verify website official timing+audits COMPLETE before running this.
set -euo pipefail
candidate=c14d06835bca515a5281e41da0e40219c2d60ef0
core=/opt/nift
test "$(git -C "$core" rev-parse HEAD)" = "$candidate"
test -z "$(git -C "$core" status --porcelain)"
cli_before=$(sha256sum "$core/nift" | cut -d' ' -f1)
git clone https://github.com/nift-experiments/filesystem-automation.git /opt/filesystem-postexec/suite
cd /opt/filesystem-postexec/suite
git checkout --detach 75e77bb4bb6fb0b8c49920f641c77b394aec5985
test -z "$(git status --porcelain)"
mkdir -p work/tools; ln -s "$core" work/nift-source
curl -fLsS https://nodejs.org/dist/v24.21.0/node-v24.21.0-linux-x64.tar.xz -o work/tools/node.tar
curl -fLsS https://go.dev/dl/go1.27.2.linux-amd64.tar.gz -o work/tools/go.tar
curl -fLsS https://github.com/oven-sh/bun/releases/download/bun-v1.4.3/bun-linux-x64.zip -o work/tools/bun.zip
sha256sum -c docs/DOWNLOAD-SHA256.txt
tar -xf work/tools/node.tar -C work/tools; tar -xf work/tools/go.tar -C work/tools; unzip -qo work/tools/bun.zip -d work/tools
python3 -m pip install --target work/uv uv==0.13.0 --break-system-packages
work/uv/bin/uv python install 3.15.0 --install-dir work/tools/python
GOCACHE=/tmp/filesystem-postexec-go-cache work/tools/go/bin/go build -o work/go-adapter adapters/go.go
python3 - <<'PY'
import sys,json
from pathlib import Path
sys.path.insert(0,'scripts');import fixtures
for n in [1000,10000,100000]:
 root=Path('work/fixtures')/str(n);m=fixtures.generate(root,n);Path('work/fixture-'+str(n)+'.json').write_text(json.dumps(m,separators=(',',':'))+'\n')
PY
test "$(sha256sum "$core/nift" | cut -d' ' -f1)" = "$cli_before"
test -z "$(git -C "$core" status --porcelain)"
