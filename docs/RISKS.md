# Risk register

These are current planning risks, not claims that failures have occurred. Reassess using prototype evidence.

| ID | Risk and trigger | Mitigation | Review gate |
| --- | --- | --- | --- |
| RISK-001 | World/content expands before core interactions are fun | One test room, one prop, one complete activity; revise scope explicitly | M3/M4 |
| RISK-002 | Online physics disagrees or feels poor under latency | Early host-authority experiment, contested-grab and internet tests | M3 |
| RISK-003 | Full active ragdoll dominates learning time | Hybrid baseline; separate time-boxed feasibility experiment if essential | M1/M3 |
| RISK-004 | AI-generated changes are too large to debug | Small tasks, plain explanations, tested increments, rollback points | Every task |
| RISK-005 | 4090-only tests mask poor Mac performance | Benchmark both Macs and multiple-player worst case | M1/M5/M8 |
| RISK-006 | Multiple tools overwrite shared records or act on stale scope | Latest-head reads, writer-specific sessions, advisory claims, serial index reconciliation | Every handoff |
| RISK-007 | One connection is assumed to equal one player | Separate identities/local slots before networking implementation | M2/M8 |
| RISK-008 | Missing asset rights or incompatible imported code | Register license/version/evidence before import; release review | Every import/M7 |
| RISK-009 | Family project becomes frustrating or one person has no ownership | Short demonstrations, rotated ownership, weekly fun/workload review | Every milestone |
| RISK-010 | Internet connectivity requires unexpected setup or recurring cost | Test separate networks early; evaluate direct/relay/server tradeoffs | M3 |
| RISK-011 | Markdown policy is mistaken for automated synchronization | Explicit onboarding and manual import; verify each tool's access | Tool onboarding |

For each material issue, link a reproducible test/session and create a task. Do not treat a risk entry as authority to purchase services or widen access.
