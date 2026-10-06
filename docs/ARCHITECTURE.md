# Architecture proposal

Status: proposed, not implemented. No engine project exists. Confirm the engine and gameplay before treating this as the build specification.

## Candidate stack

Godot stable + GDScript, built-in Jolt for 3D physics, simple cartoon rendering, hybrid controlled-character movement, and a host-authoritative online session. Record the exact engine version and renderer after approval and hardware testing. Do not install a separate Jolt extension by default; check the chosen version's built-in support and joint limitations.

## Proposed boundaries

| System | Responsibility | Proposed authority |
| --- | --- | --- |
| Session | Host/join, connection lifecycle, participant cap | Host |
| Player identity | Player ID, connection ID, local input slot | Host allocates identity; local device routes input |
| Character | Movement, interaction requests, fall/recovery | Host validates outcomes; local presentation may predict |
| Camera/UI | Player-specific camera, prompts, menus | Local per player |
| Physics prop | Grab state, motion, release/reset | Host |
| Activity/job | Objectives, failure, completion | Host |
| Rewards/progress | Completion and unlocks | Host, with duplicate-award protection |
| Save | Durable progression and versioning | Host-world save initially; local settings separate |
| Audio | Effects/music and volume | Local presentation of relevant events |

Movement prediction and correction are design work, not a free guarantee. Define how player movement behaves under latency before promising responsiveness.

## Player identity model

Keep network connection, local player slot, character identity, and session identity distinct. A single connection may later represent multiple local players. Do not key all game state solely by network peer ID. Proposed cap: four total participants, pending Q-002.

## First object interaction

Client sends a grab request -> host validates requester, range, object existence, and current holder -> host grants or rejects -> host simulates held object and sends state -> clients smooth presentation. Start with one holder per object. Release on holder disconnect, player reset, session end, or invalid object state.

Keep visual smoothing separate from authoritative collision/motion handling so remote presentation does not fight physics. Bound forces and update rates. Test contested grabs and repeated resets before adding two-person carrying.

## Networking deployment choices

1. LAN experiment on separate physical machines.
2. Private internet experiment using a chosen direct/relay/server connection strategy.
3. Four-player session and performance measurements.
4. Public distribution only after release requirements are understood.

Peer hosting is the first proposal, not a requirement for a dedicated cloud server. A 4090 is not a server requirement. If direct connectivity fails or exposes unacceptable setup burden, evaluate a relay/hosted alternative and record cost, permissions, and support needs. No provider, router change, or paid service has been authorized here.

## Scope of persistence

Save versioned progress, unlocks, and settings first. Define atomic write/backup recovery and missing/corrupt-save behavior before release. Exact world object poses, cloud sync, shared account inventories, host migration, and reconnect restoration are separate scope decisions.

## Proposed repository layout

- `game/`: future engine project, scenes, scripts, UI, game-ready assets.
- `assets/source/`: future original Blender/painting/audio authoring files.
- `assets/third_party/`: future external assets with original notices.
- `tests/`: future meaningful automated rules/save tests.
- `docs/`: existing project records.

These source directories have not been created. Keep responsibilities simple and document actual paths when implementation starts.

## References checked 2026-10-06

- [Godot networking](https://docs.godotengine.org/en/stable/tutorials/networking/high_level_multiplayer.html)
- [Godot physics](https://docs.godotengine.org/en/stable/tutorials/physics/physics_introduction.html)
- [Jolt backend and joint differences](https://docs.godotengine.org/en/stable/tutorials/physics/using_jolt_physics.html)

Documentation describes APIs, not proof that this project's multiplayer or physics works.
