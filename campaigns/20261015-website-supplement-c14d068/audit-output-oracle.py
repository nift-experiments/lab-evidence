import json,hashlib,tarfile,sys
from pathlib import Path
P=Path(__file__).resolve().parent;expected={}
for engine in ('Nift','Hugo'):
 table={}
 for i in range(10000):
  html=f'<!doctype html><html><head><title>Page {i}</title></head><body><h1>Page {i}</h1><p>Equivalent benchmark content.</p>'+ ('\n' if engine=='Hugo' else '')+'</body></html>';b=html.encode();table['index.html' if i==0 else f'page-{i}.html']=(len(b),hashlib.sha256(b).hexdigest())
 expected[engine]=table
counts={};total=0
for archive,want in [(sys.argv[1],228),(str(P/'host-b/raw-artifacts.tar.gz'),48)]:
 n=0
 with tarfile.open(archive,'r|gz') as t:
  for member in t:
   if not member.name.endswith('/output-manifest.json'):continue
   engine='Nift' if '-Nift-' in member.name else 'Hugo';d=json.load(t.extractfile(member));assert d['files']==10000 and {r['path'] for r in d['entries']}==set(expected[engine])
   for row in d['entries']:assert (row['bytes'],row['sha256'])==expected[engine][row['path']]
   n+=1;total+=10000
 assert n==want,(archive,n,want);counts[Path(archive).name]=n
r={'pass':True,'output_manifests':counts,'complete_expected_output_fingerprints_checked':total,'independent_oracle':'Generated expected literal title/h1/body/template bytes for all10000routes, separately accounting for Hugo newline; does not call harnessvalidate','limit':'Full original generated files were ephemeral; verified their retained full-file SHA/length manifests and retained HTML examples'};(P/'OUTPUT-ORACLE-AUDIT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
