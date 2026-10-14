import json,subprocess,hashlib,shutil,sys
from pathlib import Path
role=sys.argv[1];base=Path('/opt/campaign');tools=base/'tools/bin';out=base/'evidence';out.mkdir(exist_ok=True)
commands={'nift':(['--version'],tools/'nift'),'node':(['--version'],tools/'node')}
if role=='scripting-benchmark':
 for n,a in [('python3',['--version']),('ruby',['--version']),('lua5.4',['-v']),('luajit',['-v']),('bash',['--version'])]:commands[n]=(a,Path(shutil.which(n)))
elif role=='shell-benchmark':
 for n in ('bash','zsh'):commands[n]=(['--version'],Path(shutil.which(n)))
 for n in ('fish','nu'):commands[n]=(['--version'],tools/n)
else:commands['hugo']=(['version'],tools/'hugo')
rows={}
for name,(args,p) in commands.items():
 r=subprocess.run([str(p),*args],capture_output=True,text=True,check=True);rows[name]={'version':(r.stdout+r.stderr).strip(),'executable':str(p.resolve()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
if role=='website-generator-benchmark':
 project=base/role
 for n in ('astro','vitepress'):rows[n]={'version':json.loads((project/'node_modules'/n/'package.json').read_text())['version'],'lockfile_sha256':hashlib.sha256((project/'package-lock.json').read_bytes()).hexdigest()}
sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=base/role,text=True).strip();clean=not subprocess.check_output(['git','status','--porcelain'],cwd=base/role,text=True).strip();assert clean
candidate=json.loads(Path('/opt/candidate-built.json').read_text());assert candidate['candidate_sha']=='c14d06835bca515a5281e41da0e40219c2d60ef0';assert rows['nift']['sha256']==candidate['binary_sha256']
record={'kind':'frozen-comparator-inventory-not-performance','suite':role,'suite_sha':sha,'suite_clean':clean,'candidate':candidate,'comparators':rows,'policy':'historical comparator pins retained; exact installed Ubuntu package inventory frozen; no latest-version claim','dpkg_inventory_sha256':hashlib.sha256((out/'dpkg-versions.tsv').read_bytes()).hexdigest(),'download_inventory_sha256':hashlib.sha256((out/'download-sha256.txt').read_bytes()).hexdigest()}
(out/'refresh-readiness.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'suite':role,'suite_sha':sha,'clean':clean,'tools':{k:v['version'].splitlines()[0] for k,v in rows.items()}},indent=2))
