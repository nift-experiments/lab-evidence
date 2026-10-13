# Interim top10 core priorities

1. **Fix function-call regression.** Confirmed+145.76%; central policy-language path. Investigate extra argument parsing/classification/allocation; preserve exactly-once and ownership.

2. **Fix fresh website full-build regression.** Confirmed+38.29%; strategically central product. Extra filesystem probes merit investigation independent of call cause.

3. **Resolve retained-runtime state/time growth.** Ten scheduling requests grow7.17×; prior also grows. Blocks long-lived embedding/service preference; prove lifetime cause before calling it a leak.

4. **Reduce lightweight task creation/retention cost.** 10k scheduling1376.9×Go and held1k memory26.7×Go. Tiny work is infeasible despite queue wins.

5. **Improve scalar/value execution throughput.** 4-worker CPU186.5×Go despite useful parallel scaling; large calls289.1×LuaJIT. Separate interpreter cost from scheduling.

6. **Add nonblocking waits/timers.** 1k wait2576ms vsGo14.484ms; historical Nift2659.6ms shows little movement. Blocking workers remain the architectural/API boundary to address.

7. **Add public prepared-template artifacts.** Missing today; source-render cannot be relabelled prepared reuse. High-volume rendering still selects prepared peers.

8. **Reduce remaining collection/JSON costs.** BFS/frequency/transform paired medians increase; BFS allocations rise39.8%, frequency counts barely change. Investigate independently; keep sorting wins.

9. **Add channels/cancellation with explicit lifetime contracts.** Queue polling/mutex value copies persist; native bounded channel/condition and public cancellation remain absent. Do not replace semantic safety with terseness.

10. **Close task-runner contract/cache ergonomics gaps.** Outputless nodes, env invalidation, restoration, ensure,-j,structured graph remain incomplete. Existing repair works; Nift is already preferred for authored tasks.
