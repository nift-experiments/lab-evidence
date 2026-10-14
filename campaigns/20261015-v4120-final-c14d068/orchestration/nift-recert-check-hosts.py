from pathlib import Path
import json,subprocess,concurrent.futures
R=Path('/home/nick/Repositories/nift/nift-benchmarks/lab-evidence/campaigns/20261015-v4120-final-c14d068');state=json.loads(Path('/tmp/nift-recert-c14d068-state.json').read_text())
def check(name):
 command="if test -f /opt/candidate-built.json; then cat /opt/candidate-built.json; elif test -f /opt/candidate-checkout.json; then cat /opt/candidate-checkout.json; else echo '{}'; fi"
 p=subprocess.run(['python3','/tmp/nift-recert-cloud.py','ssh',name,command],capture_output=True,text=True)
 try:x=json.loads(p.stdout)
 except: return name,{'stage':'connection_pending','returncode':p.returncode}
 if x:
  assert x['candidate_sha']==state['candidate'];(R/(name+'-candidate.json')).write_text(json.dumps(x,indent=2)+'\n')
 return name,{'stage':'candidate_built' if x.get('binary_sha256') else 'candidate_checkout_verified' if x else 'installing_dependencies','candidate_sha':x.get('candidate_sha'),'binary_sha256':x.get('binary_sha256'),'cpu':x.get('cpu_model')}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:result=dict(pool.map(check,state['nodes']))
(R/'host-stage.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
