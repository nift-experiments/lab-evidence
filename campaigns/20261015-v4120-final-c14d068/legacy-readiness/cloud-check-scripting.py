import sys,json,subprocess,hashlib,shutil,tempfile
from pathlib import Path
root=Path('/opt/campaign/scripting-benchmark');sys.path.insert(0,str(root/'scripts'))
from campaign import equivalent
from campaign_measure import isolated_env
candidate='/opt/nift/nift'
plan=json.loads((root/'docs/REFRESH-20261013-READINESS.json').read_text());families=plan['commands'][0].split('--families ')[1].split(' --samples')[0].split(',');manifest=json.loads((root/'benchmarks/manifest.json').read_text());rows=[]
with tempfile.TemporaryDirectory(prefix='legacy-refresh-script-home-') as td:
 for lang in manifest['languages']:
  cmd=lang['command'].copy();cmd=[candidate,'{source}'] if lang['id']=='nift' else [shutil.which(cmd[0]),*cmd[1:]]
  for family in families:
   cat,bench=family.split('/')
   if cat in lang.get('excluded_categories',[]):continue
   for size in manifest['sizes']:
    src=root/'benchmarks/sources'/cat/bench/(size+'.'+lang['extension']);gold=root/'benchmarks/golden'/f'{cat}__{bench}__{size}.txt';command=[x.replace('{source}',str(src)) for x in cmd]
    row={'id':family+'/'+size+'/'+lang['id'],'command':command,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'oracle_sha256':hashlib.sha256(gold.read_bytes()).hexdigest()}
    try:
     p=subprocess.run(command,cwd=root,env=isolated_env(td),capture_output=True,timeout=180);row.update(exit_code=p.returncode,correct=p.returncode==0 and equivalent(p.stdout,gold.read_bytes()),stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode(errors='replace')[:1000])
    except subprocess.TimeoutExpired:row.update(correct=False,timeout=True)
    rows.append(row);Path('/opt/campaign/evidence/scripting-correctness.json').write_text(json.dumps({'candidate':'c14d06835bca515a5281e41da0e40219c2d60ef0','kind':'cloud-correctness-only','rows':rows,'complete':len(rows)==188,'all_correct':all(x['correct'] for x in rows)},indent=2)+'\n')
    print(row['id'],row['correct'],flush=True)
print('COMPLETE',len(rows),all(x['correct'] for x in rows));sys.exit(0 if len(rows)==188 and all(x['correct'] for x in rows) else 1)
