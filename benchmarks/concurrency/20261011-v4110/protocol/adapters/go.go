package main
import("bufio";"os";"fmt";"strings";"strconv";"encoding/json";"time";"sync";"sync/atomic";"os/exec")
var input *bufio.Scanner
type Pair struct{ID int; Value any}
func kernel(id,it int)int64{x:=int64(id+1);for j:=0;j<it;j++{x=x*48271%2147483647};return x}
func job(k string,id,it,extra int)any{
 if k=="wait"||k=="memory"||k=="stagger"||k=="mixed-wait"{ms:=extra;if k=="stagger"{ms=1+id%20};if k=="mixed-wait"{ms=1;if id%10==0{ms=20}};time.Sleep(time.Duration(ms)*time.Millisecond);return id}
 if k=="files"{b,e:=os.ReadFile(fmt.Sprintf("work/fixtures/%d.dat",id));if e!=nil{panic(e)};h:=int64(0);for _,x:=range b{h=(h*31+int64(x))%1000000007};return h}
 if strings.HasPrefix(k,"process")||k=="mixed"{ms,code:=0,0;if k=="process-mixed"{ms=id%5};if k=="process-fail"&&id<extra{code=7};if k=="mixed"{time.Sleep(time.Duration(extra)*time.Millisecond)};cmd:=exec.Command("work/helper",strconv.Itoa(id),strconv.Itoa(ms),strconv.Itoa(code));b,e:=cmd.Output();exit:=0;if e!=nil{if ee,ok:=e.(*exec.ExitError);ok{exit=ee.ExitCode()}else{panic(e)}};v,e:=strconv.ParseInt(strings.TrimSpace(string(b)),10,64);if e!=nil{panic(e)};if k=="mixed"{v+=kernel(id,it)};return map[string]any{"value":v,"exit":exit}}
 if k=="failure"&&id<extra{return fmt.Errorf("task.failure")};return kernel(id,it)
}
func execute(k string,n,w,it,extra int)[][]any{
 out:=[][]any{};cap:=n;if k=="nested"{cap=n*it};collect:=make(chan Pair,cap)
 if k=="memory"{gate:=make(chan struct{});var ready,done sync.WaitGroup;for id:=0;id<n;id++{ready.Add(1);done.Add(1);go func(id int){defer done.Done();ready.Done();<-gate;collect<-Pair{id,job("memory",id,it,extra)}}(id)};ready.Wait();fmt.Println("READY");input.Scan();close(gate);done.Wait();close(collect);for p:=range collect{out=append(out,[]any{p.ID,p.Value})};return out}
 if k=="atomic"||k=="mutex"{var a atomic.Int64;var m sync.Mutex;v:=int64(0);var wg sync.WaitGroup;for j:=0;j<w;j++{wg.Add(1);go func(){defer wg.Done();for i:=0;i<n/w;i++{if k=="atomic"{a.Add(1)}else{m.Lock();for z:=0;z<it;z++{v++};m.Unlock()}}}()};wg.Wait();if k=="atomic"{v=a.Load()};return [][]any{{0,v}}}
 if k=="queue"{q:=make(chan int,64);var producers,consumers sync.WaitGroup;for c:=0;c<extra;c++{consumers.Add(1);go func(){defer consumers.Done();for id:=range q{collect<-Pair{id,id*17+3}}}()};for p:=0;p<w;p++{producers.Add(1);go func(p int){defer producers.Done();for id:=p;id<n;id+=w{q<-id}}(p)};producers.Wait();close(q);consumers.Wait()
 }else if k=="pool"||k=="cpu"||k=="files"||strings.HasPrefix(k,"process")||k=="mixed"{jobs:=make(chan int,w);var wg sync.WaitGroup;for j:=0;j<w;j++{wg.Add(1);go func(){defer wg.Done();for id:=range jobs{collect<-Pair{id,job(k,id,it,extra)}}}()};for id:=0;id<n;id++{jobs<-id};close(jobs);wg.Wait()
 }else{var wg sync.WaitGroup;for id:=0;id<n;id++{wg.Add(1);go func(id int){defer wg.Done();if k=="nested"{var inner sync.WaitGroup;for z:=0;z<it;z++{inner.Add(1);go func(x int){defer inner.Done();collect<-Pair{x,kernel(x,8)}}(id*it+z)};inner.Wait()}else{collect<-Pair{id,job(k,id,it,extra)}}}(id)};wg.Wait()}
 close(collect);for p:=range collect{v:=p.Value;if e,ok:=v.(error);ok{v=map[string]any{"error":e.Error()}};out=append(out,[]any{p.ID,v})};return out
}
func main(){fmt.Println("BOOT");s:=bufio.NewScanner(os.Stdin);input=s;e:=json.NewEncoder(os.Stdout);for s.Scan(){p:=strings.Split(s.Text(),"|");n,_:=strconv.Atoi(p[1]);w,_:=strconv.Atoi(p[2]);it,_:=strconv.Atoi(p[3]);x,_:=strconv.Atoi(p[4]);if err:=e.Encode(execute(p[0],n,w,it,x));err!=nil{panic(err)}}}
