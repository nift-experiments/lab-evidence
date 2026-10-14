from pathlib import Path
import json,hashlib,subprocess,sys
suite=sys.argv[1];R=Path({'template-engines':'/opt/template-engines','concurrency':'/opt/concurrency','filesystem-automation':'/opt/filesystem/suite'}[suite]);sources={'prior':'c8d9c266518d115e4f289c5c6a2b94ddd7ee9968','checkpoint':'7f7e487c47a87e871dfef53345e2b71288008bff','candidate':'c14d06835bca515a5281e41da0e40219c2d60ef0'};rows=[]
for label,sha in sources.items():
 root=Path('/opt/recert-threeway')/label;p=R/'work/threeway-build-receipts'/label;unsupported=p/'unavailable.txt';row={'version':label,'source_sha':sha,'supported':not unsupported.exists(),'normal_build_flags':'Makefile normal -std=c++17 -O2 -Wall -Wextra -pedantic -pthread','compiler':(p/'compiler.txt').read_text()}
 if unsupported.exists():row['reason']=unsupported.read_text()
 else:
  assert (p/'complete.txt').exists();assert subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()==sha;assert not subprocess.check_output(['git','-C',str(root),'status','--porcelain'],text=True).strip();row['cli_sha256']=hashlib.sha256((root/'nift').read_bytes()).hexdigest()
  if suite=='template-engines':row['libraries']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in ['libnift_c.a','libnift_c.so']};row['adapter_sha256']=hashlib.sha256((R/'work'/('threeway-'+label+'-adapter')).read_bytes()).hexdigest()
 row['receipt_hashes']={x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(p.iterdir()) if x.is_file()};rows.append(row)
(R/'work/threeway-build-receipts/identity.json').write_text(json.dumps({'suite':suite,'scope':'same-node exact fresh builds after official timings; incompatible build/API unavailable; no substituted source','versions':rows},indent=2)+'\n')
