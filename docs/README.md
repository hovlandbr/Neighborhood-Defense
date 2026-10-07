# Documentation map

Start with [current status](STATUS.md). This table defines which document owns each kind of information; link to the owner instead of maintaining competing copies.

| Canonical file | Owns | Update when |
| --- | --- | --- |
| [../README.md](../README.md) | Public entry point and navigation | Scope/stage/navigation changes |
| [../AGENTS.md](../AGENTS.md) | Standing AI workflow | Owners change collaboration policy |
| [STATUS.md](STATUS.md) | Present state, next action, latest handoff | Each integrated session |
| [PRODUCT.md](PRODUCT.md) | Confirmed requirements and proposed gameplay | Product scope changes |
| [ROADMAP.md](ROADMAP.md) | Milestones, dependencies, completion gates | Milestone plan changes |
| [coordination/AI_DIRECTIVES.md](coordination/AI_DIRECTIVES.md) | Human-authorized scope and proposed AI directives | New directive/status/authorization |
| [coordination/BACKLOG.md](coordination/BACKLOG.md) | Tasks, dependencies, acceptance criteria, claims | Task work or handoff |
| [DECISIONS.md](DECISIONS.md) | Decision status, sources, supersession | A decision is proposed or accepted |
| [QUESTIONS.md](QUESTIONS.md) | Unanswered questions and answer routing | Human input is needed or received |
| [RISKS.md](RISKS.md) | Concrete risks and mitigation triggers | Evidence changes a risk |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Technical design and ownership boundaries | Design changes |
| [DEVELOPMENT.md](DEVELOPMENT.md) | Setup, versions, actual commands | Setup/build workflow is implemented |
| [LOCAL_AI.md](LOCAL_AI.md) | Local model/notebook development and hardware limits | AI toolchain or local workflow changes |
| [TESTING.md](TESTING.md) | Verification strategy and reproducible checks | Test workflow changes |
| [TOOLING.md](TOOLING.md) | Tools, integrations, permissions evidence | A connection/tool is added or changes |
| [LICENSING.md](LICENSING.md) | Rights policy, external asset/dependency register | A license or external asset changes |
| [conversations/README.md](conversations/README.md) | Index of conversations and handoffs | A session record is created/integrated |
| [../CHANGELOG.md](../CHANGELOG.md) | Significant changes by date | User-facing/project milestone changes |

## Templates

- [Session and conversation](templates/SESSION.md)
- [Directive](templates/DIRECTIVE.md)
- [Task](templates/TASK.md)
- [Decision](templates/DECISION.md)
- [Playtest report](templates/PLAYTEST.md)

## Path policy

Use repository-relative paths and relative Markdown links inside committed documentation so the project works on both computers and in cloud tools. Do not commit machine-specific absolute paths, account tokens, or private contact information. Use dated conversation files rather than one indefinitely growing transcript.

## Planned source directories

`game/`, `assets/source/`, `assets/third_party/`, and `tests/` are proposed locations. They are not present and must not be described as existing until created by an authorized implementation task. Add a directory-specific README when each is introduced.
