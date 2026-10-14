#!/usr/bin/env bash
set -euo pipefail
suite=$1
candidate=c14d06835bca515a5281e41da0e40219c2d60ef0
test "$(git -C /opt/nift rev-parse HEAD)" = "$candidate"
test -z "$(git -C /opt/nift status --porcelain)"
mkdir -p work
test -e work/nift-source || ln -s /opt/nift work/nift-source
export NIFT_SOURCE_SHA=$candidate
cli_before=$(sha256sum /opt/nift/nift | cut -d" " -f1)
python3 - <<'PY'
from pathlib import Path
import json
p=Path('docs/VERSIONS.json');v=json.loads(p.read_text());v['nift_source']='c14d06835bca515a5281e41da0e40219c2d60ef0';v['nift']='Nift v4.12.0 final candidate c14d068';v['nift_version']='Nift v4.12.0 final candidate c14d068';Path('work/final-versions.json').write_text(json.dumps(v,indent=2)+'\n')
PY
export NIFT_BENCH_VERSIONS_JSON=$PWD/work/final-versions.json
case "$suite" in
 template-engines)
  python3 -m venv .venv
  .venv/bin/pip install -r requirements.txt
  npm ci --ignore-scripts
  make -C /opt/nift -j2 embed > work/final-embedding-build.log 2>&1
  g++ -std=c++17 -O2 -pthread -I/opt/nift/include adapters/nift.cpp /opt/nift/libnift_c.a -ldl -o work/nift-adapter
  python3 scripts/certify.py > work/final-certification.log 2>&1
  python3 scripts/semantics.py > work/final-semantics.log 2>&1
  python3 scripts/variant_gates.py > work/final-variants.log 2>&1
 ;;
 concurrency)
  bash /root/concurrency-comparator-install.sh
  GOCACHE=/tmp/concurrency-go-cache work/tools/go/bin/go build -o work/go-adapter adapters/go.go
  cc -O2 -o work/helper adapters/helper.c
  python3 scripts/fixtures.py > work/final-fixture-generation.log
  python3 scripts/environment.py > work/final-actual-environment.log
  python3 scripts/semantics.py > work/final-semantics.log 2>&1
  python3 scripts/run.py --certify --output work/final-certify > work/final-certify.log 2>&1
 ;;
 filesystem-automation)
  FS_STANDALONE_TOOLS=1 python3 scripts/local.py 20 > work/final-certify.log 2>&1
  python3 scripts/semantics.py > work/final-semantics.log 2>&1
  python3 - <<'PY'
import sys
from pathlib import Path
sys.path.insert(0,str(Path('scripts').resolve()))
s=Path('scripts/refresh_semantic_gates.py').read_text().replace("candidate='7f7e487c47a87e871dfef53345e2b71288008bff'","candidate='c14d06835bca515a5281e41da0e40219c2d60ef0'")
exec(compile(s,'final-identity-only-semantic-wrapper','exec'))
PY
 ;;
 *) echo 'Unknown suite' >&2; exit 2;;
esac
git status --porcelain
sha256sum /opt/nift/nift

python3 /root/cloud-actual-provenance.py "$suite"

test "$(sha256sum /opt/nift/nift | cut -d" " -f1)" = "$cli_before"
