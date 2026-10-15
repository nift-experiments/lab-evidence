# Controlled build recovery: all measured metrics

Independent audits pass all 180 observations (165 measured + 15 warmups). Exact source identities: release `c8d9c266518d115e4f289c5c6a2b94ddd7ee9968`, original `7f7e487c47a87e871dfef53345e2b71288008bff`, final `c14d06835bca515a5281e41da0e40219c2d60ef0`.

| Workload | Source | Measured n | Wall median ms | CPU median ms | Maximum-child RSS median KiB |
|---|---|---:|---:|---:|---:|
| native 1000 / noop / j1 | final | 30 | 218.274221 | 213.345 | 6784 |
| native 1000 / noop / j1 | original | 30 | 195.062514 | 190.742 | 8064 |
| native 1000 / noop / j1 | release | 30 | 406.815025 | 402.150 | 6832 |
| tiny 10000 / full / j4 | final | 5 | 14976.488604 | 46060.919 | 17572 |
| tiny 10000 / full / j4 | original | 5 | 20975.957026 | 62165.804 | 33312 |
| tiny 10000 / full / j4 | release | 5 | 16676.004755 | 51727.417 | 17952 |
| tiny 10000 / noop / j4 | final | 20 | 586.915060 | 1736.128 | 12576 |
| tiny 10000 / noop / j4 | original | 20 | 603.387523 | 1692.026 | 21542 |
| tiny 10000 / noop / j4 | release | 20 | 754.151091 | 2309.891 | 12452 |

Heavy native no-op final/original wall ranges overlap: final 206.565–258.114 ms; original 179.331–230.221 ms. The marginal median increase is 11.90% (+23.212 ms). Round-matched final wall and CPU are higher in 28/30 pairs; RSS is lower in 30/30. Median within-round wall increase is 12.83% (+25.934 ms), with individual changes −8.28% to +32.71%. The paired statistic is distinct from the headline ratio of marginal medians.

This supports a consistent slowdown in the tested cohort, rather than dismissing it as noise. It does not provide a confidence interval or a cross-machine guarantee. Against the released baseline, all 30 matched wall/CPU pairs improve and wall median is 46.35% lower.

**Build-only release recommendation: bounded non-blocker with an explicit remaining latency/CPU tradeoff.** Targeted tiny10k full time/memory recovery passes; release-relative no-op gains remain. Do not claim every original-best median was retained. AI-DX benefits do not erase the remaining native executor latency gap. Global publication/release authority remains the parent’s all-eight assessment.

All distributions, paired counts, source/build identities and original observations are retained. The five-sample full-build cells remain descriptive; no significance test was performed. No samples were removed.
