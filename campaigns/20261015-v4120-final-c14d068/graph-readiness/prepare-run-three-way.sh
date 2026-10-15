#!/bin/bash
# ONLY after the official full collector and audits finish. No profiling/timing overlap.
set -euo pipefail
: "${DIAGNOSTIC_OUTPUT:?fresh diagnostic output}" "${DIAGNOSTIC_IDENTITY:?new identity file}" "${CPUS:?actual CPU IDs}"
export DIAGNOSTIC_OUTPUT DIAGNOSTIC_IDENTITY CPUS
export BUILD_SUITE=/opt/suites/build-systems
[ ! -e "$DIAGNOSTIC_OUTPUT" ]
[ ! -e "$DIAGNOSTIC_IDENTITY" ]
[ "$(git -C "$BUILD_SUITE" rev-parse HEAD)" = e95bfe88ac9e1eaf67cfeb8f67020fc3373ab81e ]
for pair in release:c8d9c266518d115e4f289c5c6a2b94ddd7ee9968 original:7f7e487c47a87e871dfef53345e2b71288008bff; do
 label=${pair%%:*}; sha=${pair#*:}; destination=/opt/nift-diagnostic-$label
 [ ! -e "$destination" ]
 git clone https://github.com/nift-dev/nift.git "$destination"
 git -C "$destination" checkout --detach "$sha"
 [ -z "$(git -C "$destination" status --porcelain)" ]
 make -C "$destination" -j2 nift
 [ -z "$(git -C "$destination" status --porcelain)" ]
done
python3 - <<'IDENTITY'
import os,json,subprocess,hashlib
from pathlib import Path
sources={'release':'c8d9c266518d115e4f289c5c6a2b94ddd7ee9968','original':'7f7e487c47a87e871dfef53345e2b71288008bff','final':'c14d06835bca515a5281e41da0e40219c2d60ef0'}
identity={'sources':sources,'binaries':{},'compiler':subprocess.check_output(['g++','--version'],text=True),'flags':'normal default Makefile release configuration; C++17 O2 pthread','post_official_only':True}
for label,sha in sources.items():
 root=Path('/opt/nift' if label=='final' else '/opt/nift-diagnostic-'+label)
 actual=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip();assert actual==sha
 status=subprocess.check_output(['git','status','--porcelain'],cwd=root,text=True);assert not status
 binary=root/'nift'
 identity['binaries'][label]={'source_sha':sha,'status':status,'path':str(binary),'sha256':hashlib.sha256(binary.read_bytes()).hexdigest(),'version':subprocess.check_output([str(binary),'--version'],text=True).strip(),'makefile_sha256':hashlib.sha256((root/'Makefile').read_bytes()).hexdigest(),'makefile':(root/'Makefile').read_text()}
Path(os.environ['DIAGNOSTIC_IDENTITY']).write_text(json.dumps(identity,indent=2)+'\n')
IDENTITY
export PATH=/opt/refresh-tools/bin:$PATH NINJA=/opt/refresh-tools/bin/ninja
python3 "$(dirname "$0")/run-build-three-way.py"
python3 "$(dirname "$0")/audit-build-three-way.py" "$DIAGNOSTIC_OUTPUT" > "$DIAGNOSTIC_OUTPUT/independent-audit.json"
