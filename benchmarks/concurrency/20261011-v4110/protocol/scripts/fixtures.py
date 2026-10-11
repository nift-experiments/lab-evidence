from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parents[1]; dest=r/'work/fixtures';dest.mkdir(parents=True,exist_ok=True);manifest=[]
for i in range(10000):
 data=bytes((i*7+j*13)%128 for j in range(128));(dest/f'{i}.dat').write_bytes(data);manifest.append([f'{i}.dat',hashlib.sha256(data).hexdigest()])
(r/'work/fixtures-manifest.json').write_text(json.dumps(manifest,separators=(',',':'))+'\n')
print('10000 fixtures, 1280000 bytes; manifest sha256',hashlib.sha256((r/'work/fixtures-manifest.json').read_bytes()).hexdigest())
