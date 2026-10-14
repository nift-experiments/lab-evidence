#!/usr/bin/env bash
set -euo pipefail
cd /opt/concurrency
mkdir -p work/tools
curl -fLsS https://nodejs.org/dist/v24.21.0/node-v24.21.0-linux-x64.tar.xz -o work/tools/node.tar
curl -fLsS https://go.dev/dl/go1.27.2.linux-amd64.tar.gz -o work/tools/go.tar
curl -fLsS https://github.com/oven-sh/bun/releases/download/bun-v1.4.3/bun-linux-x64.zip -o work/tools/bun.zip
tar -xf work/tools/node.tar -C work/tools
tar -xf work/tools/go.tar -C work/tools
unzip -qo work/tools/bun.zip -d work/tools
python3 -m pip install --target work/uv uv==0.13.0 --break-system-packages
work/uv/bin/uv python install 3.14.4 --install-dir work/tools/python
GOCACHE=/tmp/concurrency-go-cache work/tools/go/bin/go build -o work/go-adapter adapters/go.go
sha256sum work/tools/node.tar work/tools/go.tar work/tools/bun.zip > work/download-sha256.txt
sha256sum -c docs/DOWNLOAD-SHA256.txt
