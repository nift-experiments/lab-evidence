#!/usr/bin/env bash
# Run on the suite's dedicated host only after its official timing has completed.
set -euo pipefail
suite=$1
case "$suite" in template-engines) root=/opt/template-engines;; concurrency) root=/opt/concurrency;; filesystem-automation) root=/opt/filesystem/suite;; *) exit 2;; esac
cd "$root"
test -f work/final-official/complete.json || test -f work/final-official/acceptance.json || test -f work/final-official/audit.json || test -f work/refresh-series-complete.txt || { echo 'Missing audited completion marker; do not build during timing' >&2; exit 3; }
# Parent additionally verifies audits and collector absence before dispatching.
mkdir -p work/threeway-build-receipts /opt/recert-threeway
for item in prior:c8d9c266518d115e4f289c5c6a2b94ddd7ee9968 checkpoint:7f7e487c47a87e871dfef53345e2b71288008bff candidate:c14d06835bca515a5281e41da0e40219c2d60ef0; do
 label=${item%%:*}; revision=${item#*:}; source=/opt/recert-threeway/$label; receipt=$PWD/work/threeway-build-receipts/$label
 mkdir -p "$receipt"
 if [ ! -d "$source/.git" ]; then git clone https://github.com/nift-dev/nift.git "$source" > "$receipt/clone.log" 2>&1; fi
 git -C "$source" checkout --detach "$revision" > "$receipt/checkout.log" 2>&1
 test "$(git -C "$source" rev-parse HEAD)" = "$revision"
 test -z "$(git -C "$source" status --porcelain)"
 git -C "$source" rev-parse HEAD > "$receipt/source-sha.txt"
 g++ --version > "$receipt/compiler.txt"
 make -C "$source" -n nift > "$receipt/build-plan.txt"
 if ! make -C "$source" -j2 nift > "$receipt/build.log" 2>&1; then
  printf 'unavailable: exact historical source failed normal build\n' > "$receipt/unavailable.txt"; continue
 fi
 test -z "$(git -C "$source" status --porcelain)"
 "$source/nift" version > "$receipt/version.txt"
 sha256sum "$source/nift" > "$receipt/cli-sha256.txt"
 if [ "$suite" = template-engines ]; then
  if ! make -C "$source" -j2 embed > "$receipt/embedding-build.log" 2>&1; then
   printf 'unavailable: exact historical embedding target failed\n' > "$receipt/unavailable.txt"; continue
  fi
  if ! g++ -std=c++17 -O2 -pthread -I"$source/include" adapters/nift.cpp "$source/libnift_c.a" -ldl -o "work/threeway-$label-adapter" > "$receipt/adapter-build.log" 2>&1; then
   printf 'unavailable: frozen adapter incompatible with historical public API\n' > "$receipt/unavailable.txt"; continue
  fi
  sha256sum "$source/libnift_c.a" "$source/libnift_c.so" "work/threeway-$label-adapter" > "$receipt/library-adapter-sha256.txt"
  printf 'adapter: -std=c++17 -O2 -pthread -ldl; library: normal Makefile embed\n' > "$receipt/adapter-flags.txt"
 fi
 test -z "$(git -C "$source" status --porcelain)"
 printf 'PASS exact clean normal source build\n' > "$receipt/complete.txt"
done
python3 /root/runtime-threeway-build-receipt.py "$suite"
