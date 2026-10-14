"""Private localhost model of retained Vercel rules; not deployed-provider certification."""
from pathlib import Path
import argparse,json,re,threading,hashlib,mimetypes
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlsplit,parse_qs,unquote
from urllib.request import build_opener,HTTPRedirectHandler,Request
from urllib.error import HTTPError

p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
base=Path(__file__).resolve().parents[2]
class NoRedirect(HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs):return None
opener=build_opener(NoRedirect)
receipts=[]
for model in ('agora','agora-agent'):
 repo=base/model;config=json.loads((repo/'vercel.json').read_text());upstream=json.loads((repo/'app/vercel.json').read_text());bulk=json.loads((repo/config['bulkRedirectsPath']).read_text());public=repo/'public'
 allowed={'buildCommand','outputDirectory','installCommand','framework'}
 assert {k:v for k,v in config.items() if k not in allowed}=={k:v for k,v in upstream.items() if k not in allowed}
 assert (repo/config['bulkRedirectsPath']).read_bytes()==(repo/'app'/upstream['bulkRedirectsPath']).read_bytes()
 def matching(source,path):
  expression=re.escape(source).replace(re.escape(':path*'),'(.*)');return re.fullmatch(expression,path)
 def conditions(rule,parsed,headers):
  query=parse_qs(parsed.query,keep_blank_values=True)
  for condition in rule.get('has',[]):
   value=headers.get(condition['key'],'') if condition['type']=='header' else query.get(condition['key'],[''])[0]
   if not re.fullmatch(condition.get('value','.*'),value):return False
  return True
 class Handler(BaseHTTPRequestHandler):
  def log_message(self,*args):pass
  def do_GET(self):
   parsed=urlsplit(self.path);path=parsed.path;destination=None;status=200;location=None;matched='filesystem'
   # Query-qualified regex redirects are preserved ahead of unconditional legacy redirects.
   for rule in config.get('routes',[]):
    hit=re.match(rule['src'],path)
    if hit and conditions(rule,parsed,self.headers):
     matched='routes'
     if 'Location' in rule.get('headers',{}):location=rule['headers']['Location'];status=rule['status'];break
     destination=rule.get('dest',path)
     for i,value in enumerate(hit.groups(),1):destination=destination.replace('$'+str(i),value or '')
     break
   if destination is None and location is None:
    for rule in config.get('redirects',[])+bulk:
     hit=matching(rule['source'],path)
     if not hit:continue
     matched='redirects/bulk';location=rule['destination'];status=rule.get('statusCode',308 if rule.get('permanent') else 307)
     if ':path*' in location:location=location.replace(':path*',hit.group(1))
     if rule.get('preserveQueryParams') and parsed.query:location+=('&' if '?' in location else '?')+parsed.query
     break
   if location:
    self.send_response(status);self.send_header('Location',location);self.send_header('X-Emulated-Rule',matched);self.end_headers();return
   target=(public/unquote((destination or path).lstrip('/'))).resolve()
   if not target.is_relative_to(public.resolve()):self.send_error(403);return
   if target.is_dir():target=target/'index.html'
   if not target.is_file() and target.suffix=='':target=target/'index.html'
   if not target.is_file():self.send_error(404);return
   data=target.read_bytes();content_type='text/markdown' if target.suffix=='.md' else mimetypes.guess_type(str(target))[0] or 'application/octet-stream'
   self.send_response(200);self.send_header('Content-Type',content_type);self.send_header('X-Emulated-Rule',matched);self.end_headers();self.wfile.write(data)
 server=ThreadingHTTPServer(('127.0.0.1',0),Handler);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();origin=f'http://127.0.0.1:{server.server_port}'
 cases=[('/doc/console/general/quickstart',{},308,'https://doc.shengwang.cn/doc/console/general/quickstart',None),('/skill.md',{},307,'https://raw.githubusercontent.com/AgoraIO/skills/main/skills/agora/SKILL.md',None),('/cn/whiteboard/whiteboard_file_conversion?platform=RESTful',{},301,'/en/api-reference/api-ref/whiteboard/file-conversion#query-the-progress-of-a-file-conversion-task',None),('/en/introduction/about-agora',{'Accept':'text/markdown'},200,None,'en/introduction/about-agora.md'),('/en/introduction/about-agora',{'Accept':'text/html'},200,None,'en/introduction/about-agora/index.html'),('/en/introduction/about-agora.md',{'Accept':'text/markdown'},200,None,'en/introduction/about-agora.md'),('/.well-known/mcp',{},200,None,'.well-known/mcp.json'),('/__certification_missing_route__',{},404,None,None)]
 asset=next((public/'assets').glob('*.js'));cases.append(('/'+str(asset.relative_to(public)),{},200,None,str(asset.relative_to(public))))
 if bulk:
  rule=bulk[0];cases.append((rule['source']+'?certification=1',{},rule['statusCode'],rule['destination']+'?certification=1',None))
 results=[]
 try:
  for path,headers,status,location,file in cases:
   try:response=opener.open(Request(origin+path,headers=headers),timeout=10)
   except HTTPError as error:response=error
   body=response.read();assert response.status==status,(model,path,response.status,status)
   if location is not None:assert response.headers.get('Location')==location,(path,response.headers.get('Location'),location)
   if file:assert hashlib.sha256(body).digest()==hashlib.sha256((public/file).read_bytes()).digest(),file
   results.append({'path':path,'requestHeaders':headers,'status':response.status,'location':response.headers.get('Location'),'contentType':response.headers.get('Content-Type'),'actualPublicationFile':file,'bytesVerified':bool(file)})
 finally:server.shutdown();server.server_close();thread.join()
 receipts.append({'model':model,'preservedRedirects':len(config.get('redirects',[])),'preservedConditionalRoutes':len(config.get('routes',[])),'preservedBulkRedirects':len(bulk),'passed':True,'cases':results})
a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps({'scope':'Local HTTP emulation of an explicitly tested subset of actual retained configuration. Not Vercel deployment, schema acceptance or exact provider precedence certification. No external redirect followed, credential used or mutation performed.','models':receipts},indent=2)+'\n');print(json.dumps({'models':len(receipts),'cases':sum(len(r['cases']) for r in receipts),'passed':True}))
