#!/usr/bin/env bash
set -euo pipefail
while kill -0 28729 2>/dev/null; do sleep 30; done
bash /root/filesystem-post-diagnostics.sh
