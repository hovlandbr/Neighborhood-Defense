# Decision register

Accepted decisions require a direct human source or an explicitly delegated decision scope. Proposed entries are planning recommendations only. Append superseding entries; preserve history. Use [the decision template](templates/DECISION.md).

## DEC-001 — Markdown as durable project memory

- Status: Accepted.
- Date: 2026-10-06.
- Authority: Owner's direct repository-organization request in [foundation session](conversations/2026-10-06-foundation.md).
- Decision: Keep AI directives, conversations, handoffs, decisions, and task state in canonical Markdown files committed to Git.
- Implementation: AGENTS.md, documentation map, directives/backlog, indexed per-session records, and adapters. Linear may mirror tasks, with important information imported back.
- Limit: This is a workflow requirement; it does not automatically capture unrelated software chats or grant repository access.

## DEC-002 — Proprietary code and content

- Status: Accepted.
- Date: 2026-10-06.
- Authority: Owner's explicit license answer in [foundation session](conversations/2026-10-06-foundation.md).
- Decision: Reserve rights to original code and content for now; preserve separate third-party licensing.
- Consequence: Add LICENSE and an import register; no open-source license grant for original game materials.

## DEC-003 — Online co-op first; four-player and split-screen goals

- Status: Accepted at direction level; exact player combinations unresolved.
- Date: 2026-10-06.
- Authority: Owner's gameplay follow-up in [foundation session](conversations/2026-10-06-foundation.md).
- Decision: Prove online co-op early. Plan eventual four-player play and split-screen.
- Open detail: Four total versus more; four-local versus two-local; mixed local/online sessions. See Q-002.

## DEC-004 — Godot/GDScript and hybrid physics

- Status: Proposed.
- Author: AI planning recommendation.
- Date: 2026-10-06.
- Proposal: Stable Godot + GDScript, built-in Jolt, controlled character with visual wobble and physical props.
- Why: Free/open-source tool preference and manageable novice scope.
- Required evidence: Owner confirmation, exact version, Mac benchmark, and intended physics interactions. See Q-003 and Q-007.
- Consequence: No engine project should be created based solely on this proposal.

## DEC-005 — Host-authoritative private sessions

- Status: Proposed.
- Author: AI architecture recommendation.
- Date: 2026-10-06.
- Proposal: Host owns shared physics, activity completion, and progression; clients submit validated requests; session ends when host quits initially.
- Required evidence: Owner scope confirmation and LAN/internet prototype results.
- Alternatives: Dedicated server, relay-backed hosting, stronger prediction, host migration; evaluate when justified.

## DEC-006 — Linear as optional planning view

- Status: Proposed implementation of owner interest.
- Date: 2026-10-06.
- Source: Owner considered Linear; later explicitly requested Markdown-based continuity.
- Proposal: Keep Markdown canonical and mirror tasks to Linear with reciprocal links.
- Current state: No Linear project or sync created. A tool connection alone is not a configured project.

## DEC-007 — Local development tools for evaluation

- Status: Accepted within installation scope.
- Date: 2026-10-06.
- Authority: Brent's direct Unity installation and subsequent development/local AI setup requests in [the toolchain session](conversations/2026-10-06-development-toolchain.md).
- Decision: Install/verify Unity and supporting game/local AI development tools on this Mac, preserving existing settings/models and proprietary project rights.
- Implementation: [Development register](DEVELOPMENT.md), [local AI workflow](LOCAL_AI.md), locked Python environment.
- Limit: Does not accept Unity as the final engine, create a game, configure the separate desktop, or approve a training project. DEC-004 remains a historical proposal.
