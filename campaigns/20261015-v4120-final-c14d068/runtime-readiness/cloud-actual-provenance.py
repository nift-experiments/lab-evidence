from pathlib import Path
import sys,json,subprocess,hashlib,importlib.metadata
suite=sys.argv[1];core=Path('/opt/nift');run=lambda args:subprocess.check_output(args,text=True).strip();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert run(['git','-C',str(core),'rev-parse','HEAD'])=='c14d06835bca515a5281e41da0e40219c2d60ef0';assert not run(['git','-C',str(core),'status','--porcelain'])
meta={'suite':suite,'source_sha':run(['git','rev-parse','HEAD']),'candidate_sha':run(['git','-C',str(core),'rev-parse','HEAD']),'nift_version':run([str(core/'nift'),'version']),'cli_sha256':sha(core/'nift'),'compiler':run(['g++','--version']),'tools':{}}
if suite=='template-engines':
 node=run(['node','--version']);assert node=='v22.22.1';meta['tools']['node']=node;meta['tools']['node_sha256']=sha('/opt/node/bin/node');packages=json.loads(run(['.venv/bin/python','-c','import importlib.metadata,json;print(json.dumps({x:importlib.metadata.version(x) for x in ["Jinja2","MarkupSafe"]}))']));assert packages=={'Jinja2':'3.1.6','MarkupSafe':'3.0.4'};meta['tools']['python_packages']=packages;meta['tools']['python']=run(['.venv/bin/python','--version']);npm=json.loads(run(['node','-e','console.log(JSON.stringify(Object.fromEntries(["nunjucks","handlebars","liquidjs"].map(x=>[x,require(x+"/package.json").version]))))']));assert npm=={'nunjucks':'3.2.4','handlebars':'4.7.10','liquidjs':'10.30.0'};meta['tools']['npm_packages']=npm
 for f in ['libnift_c.a','libnift_c.so']:meta[f+'_sha256']=sha(core/f)
 meta['adapter_sha256']=sha('work/nift-adapter')
else:
 tools=Path('work/tools');python=next((tools/'python').glob('*/bin/python3'));node=tools/'node-v24.21.0-linux-x64/bin/node';bun=tools/'bun-linux-x64/bun';go=tools/'go/bin/go';versions={'python':run([str(python),'--version']),'node':run([str(node),'--version']),'bun':run([str(bun),'--version']),'go':run([str(go),'version'])};assert versions['node']=='v24.21.0' and versions['bun']=='1.4.3' and 'go1.27.2' in versions['go'];assert versions['python']=='Python '+('3.14.4' if suite=='concurrency' else '3.15.0');meta['tools']['versions']=versions;meta['tools']['binary_sha256']={k:sha(v) for k,v in {'python':python,'node':node,'bun':bun,'go_compiler':go,'go_adapter':Path('work/go-adapter')}.items()}
Path('work/final-actual-provenance.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta))
