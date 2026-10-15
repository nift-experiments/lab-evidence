import json,re,shlex,sys,tarfile,zipfile,gzip,lzma
from pathlib import Path
root=Path(__file__).resolve().parents[1]
f=Path.home()/'.bashrc'
with f.open('rb') as h:
 h.seek(max(0,f.stat().st_size-16384));tail=h.read().decode()
tokens=[shlex.split(x)[0].encode() for x in re.findall(r'(?m)^\s*(?:export\s+)?LINODE_CLI_TOKEN\s*=\s*(.+)$',tail)]
del tail
markers=tokens+[b'-----BEGIN '+b'OPENSSH PRIVATE KEY-----',b'-----BEGIN '+b'RSA PRIVATE KEY-----']
def scan(stream):
 carry=b''
 while True:
  chunk=stream.read(1048576)
  if not chunk:return
  chunk=carry+chunk
  assert not any(t and t in chunk for t in markers),'Private material detected; contents suppressed'
  carry=chunk[-max(map(len,markers)):]
count=0
for folder in [root,*[Path(x) for x in sys.argv[1:]]]:
 for p in folder.rglob('*'):
  if not p.is_file() or '__pycache__' in p.parts:continue
  with p.open('rb') as h:scan(h)
  count+=1
  if p.name.endswith(('.tar.gz','.tgz','.tar.xz','.tar')):
   with tarfile.open(p) as archive:
    for member in archive:
     if member.isfile():
      with archive.extractfile(member) as h:scan(h)
  elif p.suffix=='.zip':
   with zipfile.ZipFile(p) as archive:
    for member in archive.infolist():
     if not member.is_dir():
      with archive.open(member) as h:scan(h)
  elif p.suffix in ('.gz','.xz'):
   with (gzip.open if p.suffix=='.gz' else lzma.open)(p,'rb') as h:scan(h)
r={'files_scanned':count,'credential_or_private_key_matches':0,'archives_scanned_decompressed':True}
(root/'ci/private-material-scan.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
