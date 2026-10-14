"""Small serialized source-model campaign. All receipts remain outside implementation repos."""
from pathlib import Path
import subprocess,json,hashlib,time,re
BASE=Path('/home/nick/Repositories/nift/nift-experiments/agora-baseline');OUT=BASE/'measurements/final-optimized';OUT.mkdir(parents=True,exist_ok=True)
script=re.compile(rb'(<script\b[^>]*\bid="\$tsr-stream-barrier"[^>]*>)([\s\S]*?)(</script>)')
field=re.compile(rb'(\{i:"(?:\\.|[^"\\])*",u:)\d{13}(,s:)')
def normalize(data):
 count=0
 def replace(m):
  nonlocal count
  body,n=field.subn(lambda x:x.group(1)+b'0'+x.group(2),m.group(2));count+=n
  return m.group(1)+body+m.group(3)
 return script.sub(replace,data),count
def hashes(root):return {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*')) if p.is_file()}
def normalized_hashes(root):return {str(p.relative_to(root)):hashlib.sha256(normalize(p.read_bytes())[0]).hexdigest() for p in sorted(root.rglob('*.html')) if p.is_file()}
def compare(a,b):return {'missing':sorted(a.keys()-b.keys()),'extra':sorted(b.keys()-a.keys()),'changed':sorted(p for p in a.keys()&b.keys() if a[p]!=b[p])}
def measure(repo,scenario,args=()):
 label=repo.name+'-'+scenario
 print('START '+label,flush=True)
 subprocess.run(['python3',str(BASE/'tools/measure.py'),'--cwd',str(repo),'--output',str(OUT),'--label',label,'--','/home/nick/.bun/bin/bun','tools/build.ts',*args],check=True)
 phases=json.loads((repo/'.generated/last-phases.json').read_text());report=json.loads((OUT/(label+'.json')).read_text());report['componentPhases']=phases
 (OUT/(label+'.json')).write_text(json.dumps(report,indent=2)+'\n')
 print('DONE '+label+' '+json.dumps({k:report[k] for k in ['wallSeconds','sampledPeakTreeRssMiB','maxIndividualProcessRssMiB']}),flush=True)
for model in ('agora','agora-agent'):
 repo=BASE/'certification-optimized'/model
 if (repo/'.generated/pipeline-state.json').exists():raise RuntimeError('Fresh sample requires source-only checkout: '+str(repo))
 measure(repo,'fresh')
 original=hashes(repo/'public');(OUT/(model+'-fresh-output-hashes.json')).write_text(json.dumps(original,sort_keys=True)+'\n')
 canonical=normalized_hashes(repo/'public');(OUT/(model+'-fresh-normalized-html-hashes.json')).write_text(json.dumps(canonical,sort_keys=True)+'\n')
 measure(repo,'warm-forced',('--all',))
 (OUT/(model+'-warm-normalized-comparison.json')).write_text(json.dumps(compare(canonical,normalized_hashes(repo/'public')),indent=2)+'\n')
 warm=hashes(repo/'public');(OUT/(model+'-warm-output-comparison.json')).write_text(json.dumps({'missing':sorted(original.keys()-warm.keys()),'extra':sorted(warm.keys()-original.keys()),'changed':[p for p in original.keys()&warm.keys() if original[p]!=warm[p]]},indent=2)+'\n')
 measure(repo,'unchanged')
 backups={}
 phrase='Agora is a real-time platform';replacement='Agora is an interactive real-time platform'
 if model=='agora':
  path=repo/'app/content/docs/en/introduction/about-agora.mdx';backups[path]=path.read_bytes();assert phrase.encode() in backups[path];path.write_bytes(backups[path].replace(phrase.encode(),replacement.encode()))
 else:
  path=repo/'maintained/__nift/content-metadata.json';backups[path]=path.read_bytes();metadata=json.loads(backups[path]);key='en/introduction/about-agora.mdx';entry=metadata[key]
  def update(value):
   if isinstance(value,str):return value.replace(phrase,replacement)
   if isinstance(value,list):return [update(x) for x in value]
   if isinstance(value,dict):return {k:update(v) for k,v in value.items()}
   return value
  assert phrase in entry['_raw'];metadata[key]=update(entry);path.write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
  manifest=json.loads((repo/'maintained/__nift/content-manifest.json').read_text());module=repo/'maintained'/manifest[key].lstrip('/');backups[module]=module.read_bytes();assert phrase.encode() in backups[module];module.write_bytes(backups[module].replace(phrase.encode(),replacement.encode()))
 try:measure(repo,'docs-edit')
 finally:
  for path,bytes_ in backups.items():path.write_bytes(bytes_)
 # Restore production products before shared change; this is correctness work,
 # not an additional benchmark sample.
 subprocess.run(['/home/nick/.bun/bin/bun','tools/build.ts'],cwd=repo,check=True,stdout=(OUT/(model+'-restore-doc.log')).open('w'),stderr=subprocess.STDOUT)
 style=repo/'app/src/styles/app.css';old=style.read_bytes();style.write_bytes(old+b'\n/* Temporary shared-layout measurement, restored after capture. */\nbody { letter-spacing: 0.001px; }\n')
 try:measure(repo,'shared-layout')
 finally:style.write_bytes(old)
 subprocess.run(['/home/nick/.bun/bin/bun','tools/build.ts'],cwd=repo,check=True,stdout=(OUT/(model+'-restore-layout.log')).open('w'),stderr=subprocess.STDOUT)
 (OUT/(model+'-restoration-normalized-comparison.json')).write_text(json.dumps(compare(canonical,normalized_hashes(repo/'public')),indent=2)+'\n')
 final=hashes(repo/'public');comparison={'missing':sorted(original.keys()-final.keys()),'extra':sorted(final.keys()-original.keys()),'changed':[p for p in original.keys()&final.keys() if original[p]!=final[p]]};(OUT/(model+'-restoration-comparison.json')).write_text(json.dumps(comparison,indent=2)+'\n')
 subprocess.run(['git','status','--porcelain'],cwd=repo,check=True,stdout=(OUT/(model+'-clean-status.txt')).open('w'))
 print('MODEL COMPLETE '+model+' '+json.dumps({k:len(v) for k,v in comparison.items()}),flush=True)
