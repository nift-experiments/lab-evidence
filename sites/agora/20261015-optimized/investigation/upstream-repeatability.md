# Initial upstream repeatability diagnostic

Two successful untouched-source global publications retained identical file count (7136) and total bytes (653751888), but are not byte-identical. Eleven content-hashed JavaScript asset paths changed; 2018 common files changed (2016 HTML plus search JSON and llms-full.txt). No route removal was observed; removed paths are replaced hashed assets.

Search JSON contains the same 678 complete entries after order-independent comparison, but array ordering differs. LLM text shows reordered document sections. One compiled C++ example changed a Shiki light-theme token colour (#24292E to #D73A49); this is an actual rendered difference, not solely a timestamp/hash change. Its downstream chunk names then propagate into HTML.

Keep the original frozen first publication as the parity reference. Retain both raw output manifests. Do not claim byte-for-byte determinism, discard render differences as metadata, or normalize benchmark artifacts silently. Distinguish route/content completeness from exact bytes and account for observed upstream variability in browser parity review. No upstream source patch has been made.
