from pathlib import Path
import json,hashlib,datetime
root=Path('/opt/campaign/evidence');data=[json.loads((root/x).read_text()) for x in ('shell-repeated.json','shell-application-cold.json','shell-workloads.json')];work=data[-1];rows=[]
for name,tool in work['tools'].items():
 hashes=[d['tools'][name]['sha256'] for d in data];actual=hashlib.sha256(Path(tool['executable']).read_bytes()).hexdigest();assert all(x==actual for x in hashes),name
 rows.append({'participant':name,'sha256':actual,'all_three_official_runs_and_final_binary_match':True})
for name,tool in work['external_tools'].items():
 actual=hashlib.sha256(Path('/usr/bin',name).read_bytes()).hexdigest();assert actual==tool['sha256'],name;rows.append({'utility':name,'sha256':actual,'start_and_final_binary_match':True})
(root/'final-tool-identity-validation.json').write_text(json.dumps({'all_match':True,'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':rows},indent=2)+'\n')
print('Final participant and GNU binary identities unchanged')
