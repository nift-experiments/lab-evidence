#!/bin/sh
set -eu
: "${OUTPUT:?fresh output directory required}"
export PATH=/opt/node-final/bin:$PATH
export NIFT=/opt/nift/nift NIFT_SOURCE_SHA=c14d06835bca515a5281e41da0e40219c2d60ef0
[ "$(git rev-parse HEAD)" = f37b63bd13cf71256607ba4652bcc911e270f94e ]
[ ! -e "$OUTPUT" ]
cc -O2 scripts/measure.c -o work/measure
cc -O2 scripts/tiny-body.c -o work/tiny-body
taskset -c 0-3 python3 scripts/campaign-refresh.py --output "$OUTPUT"
python3 scripts/audit.py "$OUTPUT"
