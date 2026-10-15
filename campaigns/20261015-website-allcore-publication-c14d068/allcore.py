"""Guarded execution adapter: no workload, measurement-clock or oracle changes."""
import sys,json,hashlib,difflib,os
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=Path('/opt/website-publication/suite');plan=json.loads((HERE/'PLAN.json').read_text())
for file,expected in plan['source_files'].items():assert hashlib.sha256((ROOT/file).read_bytes()).hexdigest()==expected,file
mode=sys.argv.pop(1);assert mode in ('campaign','targeted_campaign');file=ROOT/'scripts'/f'{mode}.py';source=file.read_text();adapted=source
needle="c['config']['build-threads']=1";assert adapted.count(needle)==(1 if mode=='campaign' else 2);adapted=adapted.replace(needle,"c['config']['build-threads']=-1")
if mode=='campaign':
 assert adapted.count("env['GOMAXPROCS']='1'")==1;adapted=adapted.replace("env['GOMAXPROCS']='1'","env.pop('GOMAXPROCS',None)")
 adapted=adapted.replace('One CPU affinity recommended; Nift build threads=1; GOMAXPROCS=1.','All-core publication: CPU affinity0-3; Nift build threads=-1; Hugo GOMAXPROCS unset.')
else:adapted=adapted.replace('one CPU, one build thread','CPU0-3, build threads=-1')
os.environ.pop('GOMAXPROCS',None)
output=Path(sys.argv[sys.argv.index('--output')+1]);output.parent.mkdir(parents=True,exist_ok=True)
receipt={'plan_sha256':hashlib.sha256((HERE/'PLAN.json').read_bytes()).hexdigest(),'original_sha256':hashlib.sha256(source.encode()).hexdigest(),'adapted_sha256':hashlib.sha256(adapted.encode()).hexdigest(),'diff':''.join(difflib.unified_diff(source.splitlines(True),adapted.splitlines(True),fromfile=str(file),tofile='allcore-memory-adapter')),'affinity':sorted(os.sched_getaffinity(0)),'GOMAXPROCS':'unset'}
assert receipt['affinity']==[0,1,2,3];output.with_suffix('.adapter.json').write_text(json.dumps(receipt,indent=2)+'\n')
sys.path.insert(0,str(ROOT/'scripts'));sys.argv[0]=str(file);exec(compile(adapted,str(file),'exec'),{'__name__':'__main__','__file__':str(file)})
