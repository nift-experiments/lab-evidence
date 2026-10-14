from pathlib import Path
import json,importlib.util
b=Path('/home/nick/Repositories/nift/nift-experiments/agora-baseline');out=b/'measurements/final-optimized'
spec=importlib.util.spec_from_file_location('norm',b/'investigation/ssr-timestamp-proof/reproduce-proof.py')
# Load only the pure normalizer definition; reproduction script contains build actions.
s=(b/'investigation/ssr-timestamp-proof/reproduce-proof.py').read_text();ns={};exec('import re\n'+s.split('script=re.compile',1)[1].split('runs=[]',1)[0].join(['script=re.compile','']),ns)
report={}
for model in ['agora','agora-agent']:
 r={}
 for phase in ['warm','restoration']:
  raw=json.loads((out/(model+'-'+('warm-output-comparison' if phase=='warm' else 'restoration-comparison')+'.json')).read_text())
  normalized=json.loads((out/(model+'-'+phase+'-normalized-comparison.json')).read_text())
  nonhtml=[p for p in raw['changed'] if not p.endswith('.html')]
  assert not nonhtml,(model,phase,nonhtml)
  assert not any(normalized.values()),(model,phase,normalized)
  assert not raw['missing'] and not raw['extra']
  r[phase]={'rawChangedHtml':len(raw['changed']),'nonHtmlChanged':nonhtml,'normalizedComparison':normalized}
 counts={}
 for p in (b/'certification-optimized'/model/'public').rglob('*.html'):
  _,count=ns['normalize'](p.read_bytes());counts[str(count)]=counts.get(str(count),0)+1
 r['timestampReplacementCountDistribution']=counts;report[model]=r
(out/'restoration-certification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
