import readline from 'node:readline';
import {Worker,isMainThread,parentPort,workerData} from 'node:worker_threads';
import {readFile} from 'node:fs/promises';
import {spawn} from 'node:child_process';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
function kernel(i,it){let x=i+1;for(let j=0;j<it;j++)x=x*48271%2147483647;return x;}
async function job(k,i,it,e){
 if(['wait','memory','stagger','mixed-wait'].includes(k)){await sleep(k==='stagger'?1+i%20:k==='mixed-wait'?(i%10===0?20:1):e);return i;}
 if(k==='files'){let h=0;for(const b of await readFile(`work/fixtures/${i}.dat`))h=(h*31+b)%1000000007;return h;}
 if(k.startsWith('process')||k==='mixed'){
  if(k==='mixed')await sleep(e);
  let ms=k==='process-mixed'?i%5:0,code=k==='process-fail'&&i<e?7:0;
  let child=spawn('work/helper',[String(i),String(ms),String(code)]),chunks=[];child.stdout.on('data',b=>chunks.push(b));let exit=await new Promise((r,j)=>{child.on('error',j);child.on('close',r)});
  return {value:Number(Buffer.concat(chunks).toString().trim())+(k==='mixed'?kernel(i,it):0),exit};
 }
 if(k==='failure'&&i<e)throw new Error('task.failure');
 return kernel(i,it);
}
class BoundedQueue{
 constructor(cap){this.cap=cap;this.items=[];this.readers=[];this.writers=[];}
 async put(v){while(this.items.length===this.cap)await new Promise(r=>this.writers.push(r));this.items.push(v);this.readers.shift()?.();}
 async get(){while(!this.items.length)await new Promise(r=>this.readers.push(r));const v=this.items.shift();this.writers.shift()?.();return v;}
}
let input;
async function execute(k,n,w,it,e){
 if(k==='memory'){let release;let gate=new Promise(r=>release=r);let tasks=Array.from({length:n},async(_,i)=>{await gate;await sleep(e);return [i,i]});await Promise.resolve();console.log('READY');await input.next();release();return await Promise.all(tasks);}

 if(k==='atomic'){
  const sab=new SharedArrayBuffer(4);const workers=Array.from({length:w},()=>new Worker(new URL(import.meta.url),{workerData:{kind:'atomic',sab,count:n/w}}));
  await Promise.all(workers.map(x=>new Promise((r,j)=>{x.on('error',j);x.on('exit',c=>c?j(Error('worker exit '+c)):r())})));return [[0,Atomics.load(new Int32Array(sab),0)]];
 }
 if(k==='queue'){
  const q=new BoundedQueue(64),rows=[];
  const consumers=Array.from({length:e},async()=>{while(true){const i=await q.get();if(i===null)return;rows.push([i,i*17+3]);}});
  await Promise.all(Array.from({length:w},async(_,p)=>{for(let i=p;i<n;i+=w)await q.put(i);}));
  for(let j=0;j<e;j++)await q.put(null);await Promise.all(consumers);return rows;
 }
 if(k==='cpu'||k==='pool'){
  const out=[],workers=[];let next=0;
  await Promise.all(Array.from({length:w},()=>new Promise((resolve,reject)=>{
   const worker=new Worker(new URL(import.meta.url));workers.push(worker);worker.on('error',reject);
   worker.on('message',msg=>{out.push(msg);dispatch()});worker.on('exit',code=>code?reject(Error('worker exit '+code)):resolve());
   function dispatch(){if(next<n)worker.postMessage({kind:k,id:next++,it,extra:e});else worker.postMessage({stop:true});}dispatch();
  })));return out;
 }
 if(['files','mixed'].includes(k)||k.startsWith('process')){
  let next=0;const out=[];await Promise.all(Array.from({length:w},async()=>{while(next<n){const id=next++;out.push([id,await job(k,id,it,e)]);}}));return out;
 }
 if(k==='nested'){const groups=await Promise.all(Array.from({length:n},(_,i)=>Promise.all(Array.from({length:it},(_,j)=>Promise.resolve().then(()=>[i*it+j,kernel(i*it+j,8)])))));return groups.flat();}
 const settled=await Promise.allSettled(Array.from({length:n},(_,i)=>Promise.resolve().then(()=>job(k,i,it,e))));return settled.map((r,i)=>[i,r.status==='fulfilled'?r.value:{error:r.reason.message}]);
}
if(!isMainThread){
 if(workerData?.kind==='atomic'){let a=new Int32Array(workerData.sab);for(let i=0;i<workerData.count;i++)Atomics.add(a,0,1);parentPort.close();}
 else parentPort.on('message',async p=>{if(p.stop){parentPort.close();return;}parentPort.postMessage([p.id,await job(p.kind,p.id,p.it,p.extra)]);});
}else{
 console.log('BOOT');input=readline.createInterface({input:process.stdin,crlfDelay:Infinity})[Symbol.asyncIterator]();while(true){const row=await input.next();if(row.done)break;let [k,n,w,it,e]=row.value.split('|');console.log(JSON.stringify(await execute(k,+n,+w,+it,+e)));}
}
