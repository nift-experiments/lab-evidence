# Capability / implementation matrix

| Requirement | Nift | Python 3.14 GIL | Node/Bun | Go |
|---|---|---|---|---|
| Wait many tasks | native async pool; blocking sleep occupies worker | asyncio timers | promise/event-loop timers | goroutine timers |
| CPU parallel | native threads | spawn process pool | worker_threads isolates | goroutines on four CPUs |
| Native shared threads | yes, snapshots ordinary captured values | yes, GIL limits Python bytecode | workers with isolated heaps; explicit shared buffers | yes, runtime scheduler |
| Futures/results | async/await; thread join values | asyncio tasks/executor futures | promises/worker messages | channels and explicit collection |
| Bounded queue | authored mutex ring + backoff | queue.Queue | authored cooperative promise queue | native buffered channel |
| Atomics | shared atomic handles | no comparable std public integer here | SAB/Atomics | sync/atomic |
| Mutex | owner checked protected-value handle | threading.Lock | no standard native mutex cell | sync.Mutex |
| Cancellation | cooperative stop token; no public future/thread cancel found | asyncio cancel; pending executor future cancel (running process separate) | AbortSignal where API supports; Worker terminate separate | cooperative context cancellation |
| Worker limit | explicit native worker loops | executor max_workers | explicit worker/async loops | explicit worker loops |
| Join/lifecycle | join/await explicit, owned task cleanup | futures/context manager/async gather | promises + worker exit join | WaitGroup/channel close |
| Subprocess | run argv, captured streams/status | subprocess.run argv | child_process.spawn argv | exec.Command argv |

These are alternative semantics, not equivalent checkboxes. Timed failure collection is all-settled; cancellation probes are separate. Worker limits tested at 1/2/4, exact IDs/results checked for every workload. Nift held tasks can be queued rather than all actively running. Go is compiled and is explicitly a reference, not described as the same scripting deployment model.

Selection sources: frozen local Nift source/tests at docs/VERSIONS.json SHA; Python https://docs.python.org/3.14/library/concurrent.futures.html and https://docs.python.org/3.14/library/asyncio-task.html; Node https://nodejs.org/api/worker_threads.html; Bun https://bun.sh/docs/api/workers; Go https://pkg.go.dev/sync and https://pkg.go.dev/context. Runtime release indices: https://nodejs.org/dist/index.json, https://go.dev/dl/?mode=json, https://github.com/oven-sh/bun/releases/tag/bun-v1.4.3.
