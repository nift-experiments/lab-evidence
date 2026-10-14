#!/usr/bin/env bash
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive LC_ALL=C
apt-get update -qq
apt-get install -y -qq build-essential git curl ca-certificates autoconf automake libtool pkg-config python3 python3-venv python3-pip xz-utils unzip jq > /opt/refresh-packages.log 2>&1
[ ! -e /opt/nift ] || { echo 'Candidate checkout already exists; inspect before restarting'; exit 1; }
git clone https://github.com/nift-dev/nift.git /opt/nift
git -C /opt/nift checkout --detach c14d06835bca515a5281e41da0e40219c2d60ef0
test "$(git -C /opt/nift rev-parse HEAD)" = c14d06835bca515a5281e41da0e40219c2d60ef0
test -z "$(git -C /opt/nift status --porcelain)"
python3 - <<'PY'
import json,subprocess,os
from pathlib import Path
p=Path('/opt/nift');g=lambda *a:subprocess.check_output(['git',*a],cwd=p,text=True).strip()
r={'candidate_sha':g('rev-parse','HEAD'),'branch':'detached exact main candidate','clean_before_build':not g('status','--porcelain'),'compiler':subprocess.check_output(['g++','--version'],text=True).splitlines()[0],'cc':subprocess.check_output(['gcc','--version'],text=True).splitlines()[0],'build_command':'make -C /opt/nift -j2 nift','cxxflags':'-std=c++17 -O2 -Wall -Wextra -pedantic -pthread','cflags':'-std=c99 -O2 -Wall -Wextra -pedantic','libffi_cflags':'-O2 -fPIC -Wno-deprecated-declarations','cpu_model':next(x.split(':',1)[1].strip() for x in Path('/proc/cpuinfo').read_text().splitlines() if x.startswith('model name')),'logical_cpus':os.cpu_count(),'kernel':subprocess.check_output(['uname','-r'],text=True).strip(),'os':Path('/etc/os-release').read_text(),'memory_kib':int(Path('/proc/meminfo').read_text().splitlines()[0].split()[1]),'filesystem':subprocess.check_output(['findmnt','-J','-o','FSTYPE,OPTIONS,TARGET','/'],text=True),'affinity_policy':'0-3 during official measurements','release_intended_unchanged':True}
Path('/opt/candidate-checkout.json').write_text(json.dumps(r,indent=2)+'\n')
PY
make -C /opt/nift -j2 nift > /opt/nift-build.log 2>&1
python3 - <<'PY'
import json,hashlib,subprocess
from pathlib import Path
p=Path('/opt/nift');r=json.loads(Path('/opt/candidate-checkout.json').read_text());r['version']=subprocess.check_output([str(p/'nift'),'--version'],text=True).strip();assert r['version']=='Nift v4.12.0';assert r['compiler'].startswith('g++ (Ubuntu 13.');r['binary_sha256']=hashlib.sha256((p/'nift').read_bytes()).hexdigest();r['clean_after_build']=not subprocess.check_output(['git','status','--porcelain'],cwd=p,text=True).strip();assert r['clean_after_build'];Path('/opt/candidate-built.json').write_text(json.dumps(r,indent=2)+'\n')
PY
echo 'CANDIDATE BUILD COMPLETE'
