# AI directive queue

Canonical record for cross-tool instructions. Read [AGENTS.md](../../AGENTS.md) first. Human statements in conversation records are evidence; only authenticated human intent or explicit delegated scope can authorize a directive. AI proposals remain proposed. Git history records revisions; do not silently change a directive's source or scope.

Statuses: Proposed -> Authorized -> In progress -> Completed; or Superseded/Cancelled by the owner. Standing instructions may remain Active. Link relevant tasks and the session containing the actual exchange.

## DIR-001 — Establish the repository documentation foundation

- Status: In progress; local preparation underway, remote verification pending.
- Date/source: 2026-10-06; [foundation conversation](../conversations/2026-10-06-foundation.md).
- Author/authority: Brent, direct user request; Codex is implementing it.
- Scope: Update `hovlandbr/Neighborhood-Defense` with README, license, development roadmap, and key Markdown files for consistent records, AI directives/conversations, continuity, and discovery by multiple tools.
- Constraints: Original code/content proprietary per license reply. Mark unresolved product/engine details as proposed. Preserve safe project conversations and avoid private credentials/account material.
- Tasks: ND-000.
- Acceptance: Repository contains linked entry points, product roadmap, status/decision/task/conversation records, templates, appropriate rights notice, and verified publication.
- Completion evidence: To be recorded in the foundation session after remote verification.

## DIR-002 — Markdown-first continuity for participating tools

- Status: Active standing owner instruction.
- Date/source: 2026-10-06; [foundation conversation](../conversations/2026-10-06-foundation.md).
- Author/authority: Brent, direct user request.
- Scope: All AI project directives and conversations use durable `.md` records; attached tools read the canonical start path and leave a handoff.
- Constraints: Chat/input surfaces are permitted, but actionable input and meaningful responses must be persisted. Never label historical summaries as complete transcripts. Never commit private secrets or hidden reasoning. No automatic collector is implemented.
- Tasks: Applies to all authorized tasks; does not authorize unrelated backlog execution.
- Acceptance: Each integrated session has a linked record, evidence, next action, and updated current status.

## Proposed next directive

Ask the owners to define/confirm the product brief under ND-001. Do not activate a full game implementation directive by inference. Add new directives using [the template](../templates/DIRECTIVE.md) and link their human source.
