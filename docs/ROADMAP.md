# Product development roadmap

Planning baseline: 2026-10-06. Online-first novice family project. Treat estimates as allowances, not promises. At roughly 6–10 hours of project work per week, allow about 9–18 months for a very small online game, then revise using prototype evidence. Weekly availability is unconfirmed. Full active ragdolls, mixed local/online play, and broad content require new estimates.

The roadmap proposes work; only [active directives](coordination/AI_DIRECTIVES.md) authorize execution. Tasks are tracked in the [backlog](coordination/BACKLOG.md). Confirm the product concept before implementing a defense system.

## Milestones and gates

| Milestone | Outcome | Depends on | Gate |
| --- | --- | --- | --- |
| M0 — Foundation and concept | Shared records, license, one-page agreed game concept | Owner input | Instructions discoverable; key product choices recorded |
| M1 — Learning and setup | Both computers run the same tiny exported project | Engine/version decision | Both authors make and explain a small change |
| M2 — Network room | Two players can host/join and see one another on LAN | Basic player movement | Correct identities, spawn, failed-join and disconnect behavior |
| M3 — Online physics | One host-owned prop works on separate internet connections | M2 | Grab contention, release, loss/reset, and latency recovery work |
| M4 — Complete representative activity | One short objective with feedback, rewards, saving | M3 and approved gameplay loop | New tester understands and completes it |
| M5 — Four-player online | Four participants complete the activity | M4 | State/rewards stay consistent and performance is measured |
| M6 — Small-game alpha | One area and approved activities are playable end to end | M5 | Planned core systems complete; scope frozen |
| M7 — Beta and release | Tested distribution with controls, settings, credits | M6 | No known progress-destroying or core-blocking defects |
| M8 — Split-screen expansion | Approved local and online/local combinations | M7 or explicit reprioritization | Correct input, cameras, UI, shared progress, performance |
| M9 — Maintenance | Stable releases and evidence-based next scope | First release | Fixes, archive, retrospective, next decision |

## M0 — Product and working agreement

Confirm the central defense activity, audience, tone, player count meaning, camera, preferred engine, first operating systems, weekly time, and spending limit. Decide how each person owns creative and technical work. Preserve the decision source and an explicit first-release feature list.

Deliverables: approved brief, open-question priorities, chosen engine/version entry, first tasks, communication rules, and licensing notice. Exit when the owners can describe the game in one paragraph and the next contributor can find the current state without chat history.

## M1 — Learning through a tiny finished project

Learn variables, conditions, functions, input, scenes/nodes, signals, coordinates, collisions, cameras, and debugging. Use a coherent beginner course; finish a tiny goal/restart game before complex physics. Pair on one feature and let each person independently change another. Introduce Blender only when a custom prop is needed.

Set up the same stable engine version, repository workflow, imports, ignore rules, and an exported build. Document commands only after testing them. Compare a simple scene on both Macs and the desktop; record OS, GPU, resolution, settings, and engine version.

Exit: each person understands a small change, and the exported program runs on both Macs. Initial allowance: about 2–6 weeks after the product decisions, adjusted to available time.

## M2 — Multiplayer identity before world building

Prototype host/join, player spawning, movement, and clear connection messages on two physical computers. Distinguish connection ID, local player slot, player ID, and session ID. Design for later multiple local players without implementing split-screen UI yet.

Test failed joins, duplicate spawns, client departure, host departure, and restart. Decide whether the initial session ends when the host leaves. Create a written authority map for every synchronized system.

Exit: both players see consistent identities and recover from connection failure. Allow roughly 3–6 weeks for novice learning and implementation, then re-estimate.

## M3 — Physics plus a real internet test

Use a dedicated test area with slopes, steps, narrow openings, light/heavy props, a hinge, a pit, and reset points. Compare a reliable controlled character with visual wobble against any required ragdoll experiment. Tune one variable at a time. Use simple collision shapes and bounded forces.

Prototype exclusive ownership for a held object: the host validates grab distance and availability, simulates authoritative object state, and releases it when the holder disconnects. Clients display state smoothly. Do not assume independent physics simulations will remain identical.

Choose an actual internet connection method. LAN is not the internet gate. Test from separate networks, record latency conditions, and assess any relay/server cost. Do not open public matchmaking or create accounts just to prove a private session.

Exit: repeated grab/drop cycles, simultaneous grab attempts, falls, object loss, client loss, and host loss work without unrecoverable states. Allow roughly 4–10 weeks; make a new plan if physics/networking cannot meet the gate.

## M4 — One complete activity

Implement one activity from the approved defense loop. Define start, objective, complication, failure/retry, completion, reward, and replay. Temporary delivery/sorting can exercise interactions only if useful to the chosen design.

Include representative art, sound, UI, saving, and controller feedback. Store progression/settings first; saving every physical object pose is optional. Introduce meaningful tests for reward duplication and save restoration. Observe at least one new tester without explaining every step.

Exit: a 5–10 minute representative experience works independently of the editor, its save reloads, and a new player understands success. Allow about 4–8 weeks.

## M5 — Four-player online

Test four clients, preferably four human participants on representative machines. Additional instances on the desktop can exercise logic but are not evidence of a four-person experience. Test object contention, simultaneous objective completion, unequal latency, reconnect behavior, and shared-versus-individual progress.

Measure worst-case physics and rendering on the Macs. Recheck host CPU/network work, memory, object counts, and update frequency. Use evidence to limit active props or effects.

Exit: a four-player session completes the representative activity with consistent outcomes. Allow about 3–6 weeks, subject to M3 evidence.

## M6 — Content and alpha

Expand by reusing verified mechanics. Target one compact area and approximately three activities only after owner approval. Estimate asset volume from measured production time, not imagined output speed. Add optional carts/vehicles only after the core loop is stable.

Build landmarks, short onboarding, cosmetic rewards, a few secrets, and reliable resets. Track time per model, animation, activity, and playtest fix. Freeze major features when the planned game is playable end to end.

Exit: all core systems and approved content are present. Allow roughly 6–12 weeks. If content grows, revise scope and calendar before adding it.

## M7 — Beta, packaging, and release

Test with people outside development. Prioritize crashes, lost saves, blocked objectives, stuck players/objects, confusing controls, camera discomfort, and poor performance. Add readable text, camera sensitivity, volume controls, reduced shake, and hold/toggle choices where appropriate.

Validate host/join across networks, exported builds on promised OS versions, controller unplug/replug, restart, save reload, and clean-machine download/install. Set measured minimum hardware and a performance target. Include third-party notices and credit/license verification.

For private release, package build, controls, version, and bug-report instructions. For commercial release, confirm adult-managed store/payout requirements, store fees, applicable ratings/privacy/signing requirements, screenshots, trailer, and support channel. Do not announce a public date before checking the chosen store's current requirements.

Exit: new testers can download, join, complete, quit, and resume. Allow about 4–10 weeks for testing and release work; commercial administration may add time.

## M8 — Split-screen

First resolve whether the target is four local players, two local players, or mixed local/online sessions. Add device assignment, join/leave UI, separate cameras/viewports, per-player prompts, pause rules, and shared progress. Profile multiple views on the Macs; do not infer performance from the desktop.

Test each supported combination explicitly, including one computer with multiple local players joining an online host if that is in scope. Fix assumptions linking one network peer to one character. Estimate this milestone after four-player online evidence, not now.

## M9 — Maintenance and future scope

Tag releases, preserve source and builds, fix severe issues, and record reproducible bug reports. Hold a retrospective on fun, learning, workload, and the collaboration process. Choose expansion, a new small game, or one advanced physics experiment deliberately. Record migrations and superseded decisions instead of resetting project memory.

## Cross-cutting work

| Area | Work throughout development |
| --- | --- |
| Design | Define the central action; playtest clarity and recovery; record scope changes |
| Art/animation | Simple consistent style, common scale/orientation, source assets, bounded production count |
| Audio | Clear action feedback, restrained repetition, separate volumes, licensed/original recordings |
| Engineering | Small scenes/components, authority map, data-driven activity definitions, reproducible setup |
| QA/accessibility | Exported-build checks, controller/camera/readability tests, novice-friendly failure recovery |
| Production | One active task per writer; milestone evidence; realistic time; family enjoyment |
| Licensing | Record each external asset/dependency and preserve third-party notices |
| Continuity | Record requests/results in Markdown; update current state and handoff each integrated session |

## First four work blocks

These are outcomes, not fixed calendar weeks: (1) approved concept and exported scene; (2) understandable movement/camera; (3) host/join with distinct players; (4) one synchronized physical object. Do not skip concept/learning gates to match a date. Then test the internet connection before investing in town production.
