# Regression recovery — interim

Exact clean same-node releases: prior `c8d9c266518d115e4f289c5c6a2b94ddd7ee9968`, original `7f7e487c47a87e871dfef53345e2b71288008bff`, final `c14d06835bca515a5281e41da0e40219c2d60ef0`. Version names are shorthand; the original measured CLI reports v4.11.0 even though the user calls it the broken v4.12 candidate.

| Prior blocker | Release ms | Original ms | Final ms | Recovered? | Residual vs release |
|---|---:|---:|---:|---|---:|
| sanity/function-calls/small | 4.710201 | 7.374958 | 4.678490 | Yes, major original regression recovered | -0.67% |
| sanity/function-calls/large | 193.600459 | 469.418897 | 198.619788 | Yes, major original regression recovered | +2.59% |
| shell calls | 20.989496 | 44.971487 | 21.655463 | Partial: major original regression recovered | +3.17% |
| shell strings | 59.695733 | 66.950305 | 18.680012 | Yes; substantially faster than release | -68.71% |
| website fresh 10k | 2871.544599 | 3278.509241 | 2951.495366 | Partial: near-release recovery | +2.78% |
| tiny10k full | pending | pending | pending | Pending | pending |
| tiny child RSS | pending | pending | pending | Pending | pending |

All 72 scripting observations and exact rotation/source/oracles passed independent audit. Final is faster than original in all 10 paired blocks for both sizes, with disjoint ranges. Final/release ranges overlap. Large calls remain +5.01933 ms (+2.59%) and are slower in 8/10 pairs; this residual is retained as a descriptive increase, not dismissed as zero or treated as a formal significance result. Small is −0.031711 ms (−0.67%), with 6/10 final pairs slower: near-flat. Original→final recovery: 36.56% small and 57.69% large.

Template controlled gains versus release remain: 72.19% source-render 10k loop,51.21% fresh 10k loop,38.09% article source. Checkpoint→final fresh loop +4.90% and article source +0.35% have overlapping ranges and remain listed as descriptive increases. Memory floor controls prove raw inherited-floor values unsuitable for runtime-memory ranking.

Website: all 18 diagnostic observations independently audited. Final is 9.97% faster than original, all five paired blocks faster with disjoint ranges. Final remains +79.950767 ms (+2.78%) versus release, overlapping ranges and three of five slower; no exact parity claim. Child peaks release/original/final are 17468/39872/17596 KiB.

Shell all72 diagnostic observations independently audited. Original/final calls disjoint ranges and all10 final faster; release residual+0.665967ms,+3.17%,8/10 slower with overlapping ranges. Strings all10 final faster with disjoint ranges against both baselines; final−72.10% versus original.
