#!/bin/bash
set -euo pipefail
# Run only after official timing PASS; no installation during timing.
test -f /opt/campaign/evidence/official-refresh/PASS
export GIT_TERMINAL_PROMPT=0
for spec in 'release c8d9c266518d115e4f289c5c6a2b94ddd7ee9968' 'original 7f7e487c47a87e871dfef53345e2b71288008bff'; do
 read -r name revision <<< "$spec"
 root=/opt/recovery-$name
 if test ! -d "$root/.git"; then git -c credential.helper= clone -q https://github.com/nift-dev/nift.git "$root"; fi
 git -C "$root" checkout -q "$revision"
 test -z "$(git -C "$root" status --porcelain)"
 (cd "$root"; make -j2 nift) >"/opt/recovery-$name-build.log" 2>&1
 test -z "$(git -C "$root" status --porcelain)"
 sha256sum "$root/nift"
done
g++ --version > /opt/recovery-compiler.txt
dpkg-query -W > /opt/recovery-packages.tsv
