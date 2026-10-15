# Provisional human and agent choices from complete shell evidence

I would choose Nift for authored Nift-owned automation and mixed website/assets/helper workflows when its APIs cover the requirements. Its explicit contracts and .f programmability are useful for both human review and agent edits. I would choose Bash/Zsh for existing POSIX-oriented compatibility/tooling, Fish for its interactive experience, or Nu for structured data/filesystem workflows where that model is the goal. The measured engine is credible; none of these choices is an overall shell-quality ranking.

For an agent-primary bespoke workflow, I prefer Nift when output ownership, declared dependencies and lifecycle semantics are the relevant contract. This preference does not erase task-specific deficits or justify migrating a stable compatible shell estate without a concrete benefit. Preserve useful explicitness; add concise helpers rather than collapse distinct semantics.

Same-host official strengths: prepared non-login prompt Nift1.986ms versus Bash2.089ms bare; empty/light/moderate Nift1.974/2.350/2.770ms versus Bash3.693/3.833/4.035ms. The prepared/fresh cohorts must remain separate. A tiny bare-prompt advantage is descriptive, not a significance claim. Arithmetic17.263ms versus Zsh26.402ms; calls21.956ms versus Nu43.813ms; Fibonacci4.069ms versus Zsh4.525ms.

Concrete peer gaps persist: traversal100k Nift1032.955ms versus Nu255.039ms (4.05×); metadata10k118.627 versus Fish40.653ms (2.92×); concatenation10k252.608 versus Zsh105.009ms (2.41×); small-file creation100k10823.532 versus Nu4769.209ms (2.27×). These are same-fixture end-to-end semantic comparisons with native/external implementation differences disclosed. Helper-only external-baseline is excluded from the league. No cross-scenario aggregate rank is meaningful.

Exact three-way calls/strings recovery remains pending; it must qualify release-engine conclusions independently of this peer league. No final engineering verdict or publication is made here.
