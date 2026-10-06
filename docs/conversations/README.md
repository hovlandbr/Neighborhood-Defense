# Conversation and handoff index

Project conversations belong in dated Markdown files here. Each independent writer owns a separate file. The index is reconciled serially, not edited concurrently as a shared chat buffer. See [AGENTS.md](../../AGENTS.md) and [the session template](../templates/SESSION.md).

| Date | Session | Writer | Directive/task | Outcome |
| --- | --- | --- | --- | --- |
| 2026-10-06 | [Foundation and earlier planning context](2026-10-06-foundation.md) | Codex with Brent's direct input | DIR-001/002; ND-000 | Documentation prepared; publication verification pending |

## Recording policy

- Record safe actionable human messages and meaningful AI project replies verbatim when available. Label progress notes, final responses, summaries, and redactions distinctly.
- Do not store private credentials/account URLs, hidden reasoning, unrelated conversations, or personal contact information.
- Historical sessions may use a clearly labeled context digest. Do not present that digest as a full transcript.
- Before another assistant acts on a message from Linear/chat/another service, import its relevant text/source and authorization here.
- Link active scope in [AI_DIRECTIVES.md](../coordination/AI_DIRECTIVES.md), tasks in [BACKLOG.md](../coordination/BACKLOG.md), and decisions in [DECISIONS.md](../DECISIONS.md).
- Preserve prior records. Append corrections and superseding links rather than rewriting a historical exchange.
- No automatic collector or cross-service conversation sync has been implemented. Participating writers follow this policy explicitly.

## Handoff to a new tool

Give the tool the repository URL, branch, `AGENTS.md`, and `docs/STATUS.md`. Ask it to identify the active directive, relevant task, and latest handoff before work. Give write access only through the appropriate service authorization. A disconnected assistant returns a Markdown record for an authorized writer to import.
