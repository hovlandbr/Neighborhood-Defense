# Contribution and handoff workflow

The repository is proprietary. Public visibility is not an invitation to contribute or permission to reuse the game. External contributions require agreement with the owners; do not submit third-party work whose rights are unclear. Authorized collaborators follow this workflow.

## Start a session

Read [AGENTS.md](AGENTS.md) and [STATUS.md](docs/STATUS.md). Confirm the current human request or active directive authorizes the task. Check the latest backlog claim and branch state. Make a task branch such as `docs/nd-001-product-brief` or `feat/nd-006-player-movement`.

Create a unique file under `docs/conversations/` using [the session template](docs/templates/SESSION.md). Use `YYYY-MM-DD-HHMMSS-tool-task.md`; include an offset in the timestamp field and an extra suffix if needed to avoid collisions. Record the safe request and link its source.

## Work in small increments

- Define acceptance criteria before implementation.
- Give one change a clear outcome; keep learning experiments separate from production systems.
- Discuss overlapping edits through a session/handoff record, and link it in the queue.
- Keep original authoring files when game exports are introduced.
- Register dependencies/assets before adding them.
- Use pull/read, focused commit, and push habits. Do not merge others' uncommitted work into your task.

## Finish a session

Run applicable checks from [TESTING.md](docs/TESTING.md). Record results and uncertainty. Update the task, concise current status, impacted product/technical docs, conversation index, and changelog where applicable. Open a PR using the repository template and link the session record. Record a direct commit only when authorized by the owner.

## Shared indexes and recovery

Session files are writer-specific. Shared indexes are edited serially against the latest branch head. Task claims are advisory. If simultaneous changes occur, compare both versions, retain both histories, and reconcile the current state explicitly. Never force push to resolve a documentation conflict.

## Communication through Markdown

Use the conversation file for the exchange, the directive queue for authorization/scope, the decision log for outcomes, and the backlog for executable tasks. GitHub/Linear/chat comments may link to these records; important new information must be imported before another tool acts on it. A tool that cannot write must provide a Markdown handoff to an authorized writer.

## Learning together

Explain changed code in plain language. Include reproduction steps Jax and Brent can perform. Rotate ownership of design, props, small code changes, and testing. A working AI-generated change is not complete until its essential behavior and failure cases can be explained.
