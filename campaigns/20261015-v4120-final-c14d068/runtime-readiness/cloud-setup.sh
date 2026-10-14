#!/usr/bin/env bash
set -euo pipefail
suite=$1
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq build-essential git python3-venv python3-pip curl xz-utils unzip ca-certificates autoconf automake libtool pkg-config
case "$suite" in
 template-engines) repo=template-engines; sha=3c0dcdd1aad3cbb0a0c638c9041233b1e329dc6f; root=/opt/template-engines;;
 concurrency) repo=concurrency; sha=d6d0cac9e7dd65d12b5bbccd0ec5b542d187c0a6; root=/opt/concurrency;;
 filesystem-automation) repo=filesystem-automation; sha=75e77bb4bb6fb0b8c49920f641c77b394aec5985; root=/opt/filesystem/suite;;
 *) exit 2;;
esac
git clone "https://github.com/nift-experiments/$repo.git" "$root"
cd "$root"; git checkout --detach "$sha"; test -z "$(git status --porcelain)"
mkdir -p work; ln -s /opt/nift work/nift-source
if [ "$suite" = template-engines ]; then
 mkdir -p /opt/node; cd /opt/node
 curl -fLsS https://nodejs.org/dist/v22.22.1/node-v22.22.1-linux-x64.tar.xz -o node.tar.xz
 curl -fLsS https://nodejs.org/dist/v22.22.1/SHASUMS256.txt -o SHASUMS256.txt
 expected=$(awk '$2=="node-v22.22.1-linux-x64.tar.xz"{print $1}' SHASUMS256.txt)
 test "${#expected}" = 64; printf '%s  node.tar.xz\n' "$expected" | sha256sum -c -
 tar -xf node.tar.xz --strip-components=1
 ln -sf /opt/node/bin/node /usr/local/bin/node; ln -sf /opt/node/bin/npm /usr/local/bin/npm
 cd "$root"
elif [ "$suite" = filesystem-automation ]; then
 bash /root/filesystem-comparator-install.sh
 git clone https://github.com/nift-experiments/filesystem-automation.git /opt/filesystem/filter-supplement
 git -C /opt/filesystem/filter-supplement checkout --detach 1ab31488eb949eb8f8cd6d50b0eb9fd59e1ad78e
 mkdir -p /opt/filesystem/filter-supplement/work
 ln -s /opt/nift /opt/filesystem/filter-supplement/work/nift-source
 ln -s "$root/work/tools" /opt/filesystem/filter-supplement/work/tools
 GOCACHE=/tmp/filesystem-filter-go-cache work/tools/go/bin/go build -o /opt/filesystem/filter-supplement/work/go-adapter /opt/filesystem/filter-supplement/adapters/go.go
fi
bash /root/cloud-gates.sh "$suite"
# Preserve actual tool provenance without changing historical version locks.
uname -a > work/final-kernel.txt; df -T . > work/final-filesystem.txt; dpkg-query -W > work/final-packages.txt
