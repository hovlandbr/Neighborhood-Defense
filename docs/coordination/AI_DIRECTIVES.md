# AI directive queue

Canonical record for cross-tool instructions. Read [AGENTS.md](../../AGENTS.md) first. Human statements in conversation records are evidence; only authenticated human intent or explicit delegated scope can authorize a directive. AI proposals remain proposed. Git history records revisions; do not silently change a directive's source or scope.

Statuses: Proposed -> Authorized -> In progress -> Completed; or Superseded/Cancelled by the owner. Standing instructions may remain Active. Link relevant tasks and the session containing the actual exchange.

## DIR-001 — Establish the repository documentation foundation

- Status: Completed.
- Date/source: 2026-10-06; [foundation conversation](../conversations/2026-10-06-foundation.md).
- Author/authority: Brent, direct user request; Codex is implementing it.
- Scope: Update `hovlandbr/Neighborhood-Defense` with README, license, development roadmap, and key Markdown files for consistent records, AI directives/conversations, continuity, and discovery by multiple tools.
- Constraints: Original code/content proprietary per license reply. Mark unresolved product/engine details as proposed. Preserve safe project conversations and avoid private credentials/account material.
- Tasks: ND-000.
- Acceptance: Repository contains linked entry points, product roadmap, status/decision/task/conversation records, templates, appropriate rights notice, and verified publication.
- Completion evidence: [Foundation session](../conversations/2026-10-06-foundation.md); 32 files published and content-verified at commit `d7f18e7eaddc459e319b32ceb45524e7dc8b8f5e`, followed by a completion-record reconciliation commit.

## DIR-002 — Markdown-first continuity for participating tools

- Status: Active standing owner instruction.
- Date/source: 2026-10-06; [foundation conversation](../conversations/2026-10-06-foundation.md).
- Author/authority: Brent, direct user request.
- Scope: All AI project directives and conversations use durable `.md` records; attached tools read the canonical start path and leave a handoff.
- Constraints: Chat/input surfaces are permitted, but actionable input and meaningful responses must be persisted. Never label historical summaries as complete transcripts. Never commit private secrets or hidden reasoning. No automatic collector is implemented.
- Tasks: Applies to all authorized tasks; does not authorize unrelated backlog execution.
- Acceptance: Each integrated session has a linked record, evidence, next action, and updated current status.

## DIR-003 — Install Unity on this Mac

- Status: Superseded by DIR-004 after interruption and owner's report that Unity was installed.
- Date/source: 2026-10-06; [Unity installation session](../conversations/2026-10-06-unity-installation.md).
- Author/authority: Brent, direct request.
- Scope: Install Unity Hub and an appropriate stable LTS Intel editor locally, verify outcomes, and preserve setup records under DIR-002.
- Constraints: No paid subscription, no game project creation, no assumption of final engine approval. Report any sign-in, activation, or administrator step that requires the owner.
- Tasks: ND-021.
- Acceptance: Actual installed versions and checks recorded; any remaining human step identified accurately.
- Outcome: Unity Hub 3.22.2 and editor 6000.6.4f1 verified on resumption; this assistant did not install them. The initially proposed LTS download was not completed, and the existing editor was preserved. License activation was not verified.

## DIR-004 — Install game and local AI development tools

- Status: Completed within local setup scope; documentation PR open for review.
- Date/source: 2026-10-06; [toolchain session](../conversations/2026-10-06-development-toolchain.md).
- Author/authority: Brent, direct request to install other tools needed for development and local AI.
- Scope: Verify Unity and existing tools; install a practical free development toolchain locally; record reproducible setup and limitations.
- Constraints: Preserve existing data/settings/models, no paid subscription or unrequested game implementation. Use Intel-compatible downloads and isolated Python environments. Do not represent local installation as setup of the separate desktop.
- Tasks: ND-021/022.
- Acceptance: Installed tool versions and functional smoke checks recorded, commands available in a new terminal, unresolved human/account/platform steps explicit, Markdown handoff published for review.
- Evidence: [Session](../conversations/2026-10-06-development-toolchain.md); [PR #1](https://github.com/hovlandbr/Neighborhood-Defense/pull/1). Initial 20 changed files verified against published commit `de9c5e814af40b433f46103c792f3d5b50124b7f`; completion records follow on the same branch.


## Proposed next directive

Ask the owners to define/confirm the product brief under ND-001. Do not activate a full game implementation directive by inference. Add new directives using [the template](../templates/DIRECTIVE.md) and link their human source.
