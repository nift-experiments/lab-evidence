package main
import("sync";"time";"fmt";"context")
func main(){for _,w:=range []int{1,2,4}{var mu sync.Mutex;var wg sync.WaitGroup;active,max:=0,0;for i:=0;i<w;i++{wg.Add(1);go func(){defer wg.Done();mu.Lock();active++;if active>max{max=active};mu.Unlock();time.Sleep(20*time.Millisecond);mu.Lock();active--;mu.Unlock()}()};wg.Wait();if max>w||active!=0{panic("bound")};fmt.Printf("{\"workers\":%d,\"max_active\":%d,\"remaining\":%d}\n",w,max,active)};ctx,cancel:=context.WithCancel(context.Background());cancel();<-ctx.Done();fmt.Printf("{\"cancel\":%q}\n",ctx.Err().Error())}
