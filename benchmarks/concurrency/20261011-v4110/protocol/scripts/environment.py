from pathlib import Path
import subprocess,json,os,sys,hashlib,platform,time
sys.path.insert(0,str(Path(__file__).resolve().parent));import run
commands={e:run.command(e) for e in run.ENGINES};versions={}
for e in run.ENGINES:
 cmd=[commands[e][0],'version' if e in ['nift','go'] else '--version']
 if e=='go':cmd=[str(run.R/'work/tools/go/bin/go'),'version']
 p=subprocess.run(cmd,capture_output=True,text=True);versions[e]=p.stdout.strip()+p.stderr.strip()
x={'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'suite_sha':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'nift_sha':subprocess.check_output(['git','-C','work/nift-source','rev-parse','HEAD'],text=True).strip(),'uname':platform.uname()._asdict(),'affinity':run.AFFINITY,'cpu':subprocess.check_output(['lscpu'],text=True),'os_release':Path('/etc/os-release').read_text(),'memory':Path('/proc/meminfo').read_text(),'versions':versions,'commands':commands,'binary_sha256':{e:hashlib.sha256(Path(c[0]).read_bytes()).hexdigest() for e,c in commands.items()},'python_gil':subprocess.check_output([commands['python'][0],'-c','import sys;print(sys._is_gil_enabled())'],text=True).strip(),'compiler':subprocess.check_output(['g++','--version'],text=True),'go_compiler':subprocess.check_output([str(run.R/'work/tools/go/bin/go'),'version'],text=True)}
Path('work/environment.json').write_text(json.dumps(x,indent=2)+'\n');print(json.dumps({'suite_sha':x['suite_sha'],'nift_sha':x['nift_sha'],'affinity':x['affinity'],'versions':versions}))
