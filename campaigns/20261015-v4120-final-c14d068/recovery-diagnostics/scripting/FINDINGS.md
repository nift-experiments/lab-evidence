# Exact same-node scripting recovery

All 72 observations pass correctness; independent audit verifies complete 60 measured/12 warmups, exact adjacent three-version ordering, frozen source/oracle hashes and every distribution. Exact clean builds compare release c8d9c266518d115e4f289c5c6a2b94ddd7ee9968, original 7f7e487 and final c14d068. The same host GCC 13.3/default Make flags and runtime library identities are recorded. CPU 0; no installations or profiles during timing. Official raw hashes remain unchanged.

Small call median: release 4.710201 ms, original 7.374958 ms, final 4.678490 ms. Final gains 2.696468 ms (36.56%) over original, with all ten matched pairs faster and disjoint observed ranges. Final/release differs −0.031711 ms (−0.67%), overlapping ranges; no meaningful remaining slowdown is established.

Large call median: release 193.600459 ms, original 469.418897 ms, final 198.619789 ms. Final gains 270.799109 ms (57.69%) over original, all ten matched pairs faster and disjoint ranges. Final/release differs +5.019330 ms (+2.59%), overlapping ranges; eight of ten matched pairs final slower. This small residual does not justify claiming exact equality or a significant population regression. The large original-candidate regression is substantially recovered to near release latency in this specimen.

This is a focused calls diagnostic, not a claim that all language performance is solved. It does not identify the causal commit or establish allocation-count parity. No additional profile campaign is justified by the tiny residual alone. Full suites and peer gaps remain separate evidence. No release recommendation or Labs publication is made here.
