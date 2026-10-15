import json,hashlib,subprocess,os
from pathlib import Path
R=Path('/opt/website-publication');plan=json.loads((R/'PLAN.json').read_text());run=lambda cmd:subprocess.check_output(cmd,text=True).strip();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
for root,expected in [('/opt/nift',plan['candidate']),(str(R/'suite'),plan['suite_sha'])]:
 assert run(['git','-C',root,'rev-parse','HEAD'])==expected;assert not run(['git','-C',root,'status','--porcelain'])
assert sha('/opt/nift/nift')==plan['candidate_cli_sha256'];assert sha(R/'tools/bin/hugo')=='8f6ddd98ff4a21a27b86530eb2e40d305673c26f72b1d57734ef68505cd28f89'
assert run([str(R/'tools/bin/node'),'--version'])=='v24.21.0'
for package,version in [('astro','7.3.6'),('vitepress','1.6.4')]:assert json.loads((R/'suite/node_modules'/package/'package.json').read_text())['version']==version
for file,expected in plan['source_files'].items():assert sha(R/'suite'/file)==expected
assert not os.environ.get('GOMAXPROCS');d={'candidate':plan['candidate'],'suite':plan['suite_sha'],'plan_sha256':sha(R/'PLAN.json'),'tools':{name:{'sha256':sha(path),'version':run([str(path),flag])} for name,path,flag in [('Nift',Path('/opt/nift/nift'),'--version'),('Hugo',R/'tools/bin/hugo','version'),('Node',R/'tools/bin/node','--version')]},'worker_policy':plan['policy'],'source_clean':True}
(R/'evidence/identity.json').write_text(json.dumps(d,indent=2)+'\n');print('IDENTITY_PASS')
