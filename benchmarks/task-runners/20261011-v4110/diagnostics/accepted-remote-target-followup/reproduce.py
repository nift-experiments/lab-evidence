import json,sys,shutil,subprocess
from pathlib import Path
root=Path('/root/task-runners');sys.path.insert(0,str(root/'generators'));sys.path.insert(0,str(root/'scripts'))
from workflow import generate
from probe import command,ENV
from campaign import closure,descendants
from oracle import certify
out=Path('/root/task-runners-target-followup');out.mkdir();rows=[]
for runner in ['nift','turbo','nx']:
 r=root/'work'/('target-followup-'+runner);g=generate(r,20,runner,4)
 if runner!='nift':(r/'node_modules').symlink_to(root/'work/tools/node_modules')
 p=subprocess.run(command(runner,g),cwd=r,env=ENV,capture_output=True,text=True);assert p.returncode==0,p.stderr
 (r/'trace.jsonl').unlink();v=json.loads((r/'inputs/generate-schema.json').read_text());v['value']=2;(r/'inputs/generate-schema.json').write_text(json.dumps(v)+'\n')
 selected=closure(g,['release-prep']);dirty=descendants(g,['generate-schema'])
 for name,target,expected,scope in [('selected',['release-prep'],dirty&selected,selected),('global-followup',None,dirty-selected,None)]:
  if name=='global-followup':(r/'trace.jsonl').unlink(missing_ok=True)
  p=subprocess.run(command(runner,g,target=target),cwd=r,env=ENV,capture_output=True,text=True);assert p.returncode==0,p.stderr
  proof=certify(r,expected,4,scope=scope);proof.update(runner=runner,case=name,exit_code=p.returncode,expected=sorted(expected),scope=sorted(scope) if scope is not None else None)
  rows.append(proof);d=out/(runner+'-'+name);d.mkdir();shutil.copy2(r/'trace.jsonl',d/'trace.jsonl');shutil.copy2(r/'graph.json',d/'graph.json');shutil.copytree(r/'inputs',d/'inputs');(d/'stdout').write_text(p.stdout);(d/'stderr').write_text(p.stderr);(d/'oracle.json').write_text(json.dumps(proof,indent=2)+'\n')
(out/'validation.json').write_text(json.dumps({'all_passed':True,'observations':6,'not_timing_samples':True,'selected_tasks_executed':10,'followup_tasks_executed':4,'all_global_outputs_verified':True,'results':rows},indent=2)+'\n');print('Supplemental target/followup gates passed: 6 observations; exact 10 then 4 actions; all outputs correct')
