#!/usr/bin/env bash
set -euo pipefail
suite=$1
case "$suite" in template-engines) root=/opt/template-engines; collector=template-threeway.py;; concurrency) root=/opt/concurrency; collector=concurrency-threeway.py;; filesystem-automation) root=/opt/filesystem/suite; collector=filesystem-threeway.py;; *) exit 2;; esac
cd "$root"
if find work/threeway-build-receipts -name unavailable.txt -print | read -r unavailable; then
 printf 'Unavailable three-way comparison; see exact build/API failure receipts. No replacement revision.\n' > work/threeway-comparison-unavailable.txt
 exit 0
fi
python3 "/root/$collector" > work/threeway-measurement.log 2>&1
if [ "$suite" = concurrency ]; then python3 /root/concurrency-threeway-reuse.py > work/threeway-reuse.log 2>&1; fi
