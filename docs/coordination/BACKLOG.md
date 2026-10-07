# Task queue

Canonical task state. The roadmap proposes work; an active directive or current human request authorizes execution. A Ready task is eligible to plan, not blanket permission to execute. Use [TASK.md](../templates/TASK.md) for detailed tasks as needed.

Statuses: Backlog, Ready, In progress, Playtest/Review, Done, Blocked. Claims identify writer, branch, time, and affected files; they are advisory, not locks. Work against the latest revision and reconcile shared indexes serially.

## Initial tasks

| ID | Outcome | Dependency | Status | Acceptance criteria |
| --- | --- | --- | --- | --- |
| ND-000 | Publish the documentation foundation | DIR-001 | Done | Linked records, proprietary license, validation, verified GitHub publication; see foundation session |
| ND-001 | Agree on the product brief | ND-000 | Ready | Q-001/002/003/005 prioritized; approved central loop and first scope recorded |
| ND-002 | Confirm tools, versions, target machines | ND-001 | Backlog | Engine/version, OS/GPU details, renderer benchmark plan, actual setup recorded |
| ND-003 | Finish/export a tiny learning project | ND-002 | Backlog | Runs on both Macs; both authors explain a small independent change |
| ND-004 | Build physics test area | ND-003 | Backlog | Slopes/steps/props/pit/reset and measurable interaction trials |
| ND-005 | Separate player identities and input slots | ND-003 | Backlog | Connection/local slot/player identity remain distinct; documented authority map |
| ND-006 | Implement understandable movement/camera | ND-004 | Backlog | Walking/jumping/visibility/recovery pass manual trials |
| ND-007 | Implement host/join and player lifecycle | ND-005/006 | Backlog | Two physical clients spawn correctly; join failures/disconnects handled |
| ND-008 | Implement host-owned crate interaction | ND-007 | Backlog | Grab/drop/contention/range validation pass repeated tests |
| ND-009 | Recover held objects and session state | ND-008 | Backlog | Client/host loss and out-of-bounds reset are predictable |
| ND-010 | Test actual internet connectivity | ND-009 | Backlog | Separate-network session works; latency/cost/setup evidence recorded |
| ND-011 | Choose character physics approach | ND-006/010 | Backlog | Owners assess hybrid versus required ragdoll evidence and record decision |
| ND-012 | Complete one approved game activity | ND-010/011 | Backlog | Start/objective/fail/retry/success/reward all work in online session |
| ND-013 | Save progression and settings | ND-012 | Backlog | Reload/missing-save recovery and duplicate reward behavior verified |
| ND-014 | Test four online participants | ND-013 | Backlog | Shared state consistent, new-player feedback and Mac performance recorded |
| ND-015 | Produce one custom prop and sound | ND-011 | Backlog | Art/audio pipeline works in-game; source/rights registered |
| ND-016 | Playtest with a new participant | ND-012/015 | Backlog | Confusion/defects recorded with reproducible follow-up tasks |
| ND-017 | Build approved small-game content | ND-014/016 | Backlog | One compact area and agreed activities playable end to end |
| ND-018 | Polish and validate release | ND-017 | Backlog | Export/controller/save/network/accessibility/license gates met |
| ND-019 | Package the first release | ND-018 | Backlog | Download/launch/join/finish/reload tested on promised platforms |
| ND-020 | Add approved split-screen combinations | ND-014 plus owner scheduling decision | Backlog | Distinct inputs/cameras/UI and all approved combinations tested |

## Claims

ND-021 — Verify Unity on the current Mac: Done under DIR-004 after interruption and owner's installation. Hub/editor versions recognized and executable checked; activation remains unverified. Original DIR-003 superseded. See [initial session](../conversations/2026-10-06-unity-installation.md) and [continuation](../conversations/2026-10-06-development-toolchain.md).

ND-022 — Install game/local AI toolchain: Done within current-Mac setup scope; authorized by DIR-004 independently of ND-001. Compatible tools installed and smoke-tested; handoff published in [PR #1](https://github.com/hovlandbr/Neighborhood-Defense/pull/1), awaiting owner review/merge. This does not complete broader ND-002 product/tool selection or desktop training.

| Task | Writer/tool | Branch | Intended scope | Claimed on | Handoff |
| --- | --- | --- | --- | --- | --- |
| None | — | — | — | — | — |

No claims exist for game implementation. On completion move a claim to the completed-claims history below; do not erase another writer's work. Exact branch revisions are available in Git and should be recorded in future sessions when known.

## Completed claims

ND-021/022: Codex, `codex/development-toolchain`, 2026-10-06. Continued after owner's Unity installation and expanded setup request. Local tools checked; 20 changed files verified against published commit `de9c5e814af40b433f46103c792f3d5b50124b7f`; completion records follow. [Session](../conversations/2026-10-06-development-toolchain.md), [PR #1](https://github.com/hovlandbr/Neighborhood-Defense/pull/1). No claim transferred to game implementation.

ND-000: Codex, initial bootstrap on main, completed 2026-10-06. All 32 foundation files verified against GitHub commit `d7f18e7eaddc459e319b32ceb45524e7dc8b8f5e`; see [foundation session](../conversations/2026-10-06-foundation.md). No game implementation claim transferred or opened.
