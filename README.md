# Neighborhood Defense

A first game built by Brent and Jax: an original 3D physics game inspired by the playful interactions and cooperative exploration of Wobbly Life.

**Stage:** planning and repository foundation. There is no playable game or engine project yet.

**Confirmed direction:** online co-op first; eventual four-player play and split-screen. The exact defense gameplay, engine selection, and split-screen combinations remain open.

## Start here

| Who you are | Read first | Then use |
| --- | --- | --- |
| Brent or Jax | [Current status](docs/STATUS.md) | [Product brief](docs/PRODUCT.md), [roadmap](docs/ROADMAP.md), [open questions](docs/QUESTIONS.md) |
| An AI assistant or coding agent | [AGENTS.md](AGENTS.md) | [AI directives](docs/coordination/AI_DIRECTIVES.md), [task queue](docs/coordination/BACKLOG.md), [conversation index](docs/conversations/README.md) |
| A developer | [Contribution workflow](CONTRIBUTING.md) | [Development setup](docs/DEVELOPMENT.md), [architecture proposal](docs/ARCHITECTURE.md), [testing](docs/TESTING.md) |
| An attached service or integration | [Integration register](docs/TOOLING.md) | [Documentation map](docs/README.md) and canonical file links |
| Someone checking reuse rights | [LICENSE](LICENSE) | [Licensing and asset register](docs/LICENSING.md) |

## What we are trying to prove first

Two players on separate computers can join one small test world, move around, pick up and drop a physical object, and recover from mistakes or disconnects. Test a real internet connection before building a neighborhood or a large set of missions.

The working title does not settle the gameplay. Enemies, waves, building, traps, combat, story, and progression require product decisions. A delivery exercise is only a possible physics test, not the agreed game concept.

## Project memory lives in Markdown

Repository Markdown is the durable source of truth for directives, project conversations, decisions, tasks, and handoffs. Git records their history. Linear can be a convenient task-board view, but important instructions and outcomes must be written back to the canonical Markdown files.

Chat is an input surface, not a substitute for project memory. Participating assistants must record actionable human requests and their project responses in a session file. Tools without repository access must return a Markdown handoff for an authorized writer to commit. No automatic chat capture or synchronization service has been implemented.

Keep credentials, private account information, and unrelated personal conversations out of this public repository. Record project-relevant conversation text with any necessary redactions; label summaries and redactions honestly.

## Initial scope and tools

- Online co-op first; design player identities for four total participants as a provisional limit.
- Eventual split-screen; mixed local/online sessions are not yet confirmed.
- Small, original 3D environment and understandable physics interactions.
- Godot with GDScript and a hybrid physics character is the current proposal, not an approved engine decision.
- Both Intel MacBooks are development/test targets; the desktop is an additional development/test machine.
- Prefer free/open-source development software. Using those tools does not make this game open source.

See [tool choices and connection status](docs/TOOLING.md). This repository does not yet have run, build, or gameplay-test commands.

## License

The owners chose to keep original game code and content proprietary for now. Rights are reserved under [LICENSE](LICENSE); third-party components retain their own licenses. Public visibility does not grant an additional open-source license.

## Next session

Start at [STATUS.md](docs/STATUS.md), resolve the first product questions in [QUESTIONS.md](docs/QUESTIONS.md), and work through task **ND-001** in the [backlog](docs/coordination/BACKLOG.md). Follow [AGENTS.md](AGENTS.md) before making changes.
