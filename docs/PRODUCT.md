# Product brief

Version: initial planning brief, 2026-10-06. Requirements below distinguish human statements from AI proposals. See [decisions](DECISIONS.md) and [questions](QUESTIONS.md).

## Confirmed human direction

- Working repository/title: Neighborhood Defense.
- A first game built by Brent and Jax, both novice game programmers.
- Inspiration: the playful theme and physics interactions of Wobbly Life; create original characters, world, art, and identity.
- Brent has technical experience and uses AI assistance; Jax has basic starting coding knowledge.
- Online co-op multiplayer comes first. Four-player play and split-screen are eventual goals.
- Both use 2019 i9 MacBook Pros. An i9 14th-generation desktop with RTX 4090 and 128 GB RAM is available; its OS is not yet recorded.
- Prefer free/open-source tool licensing.
- Markdown is the durable project record for AI directives and conversations.
- Keep original game code and content proprietary for now.

## Proposed first playable

Two players join one compact test area, walk/jump, grab/drop a physics prop, perform a short shared objective, and recover from falls, lost objects, or disconnects. This is a technical learning milestone, not a final gameplay commitment.

Use a controlled character with visual wobble and physical props initially. Test active ragdoll movement early only if independently controlled limbs or physical climbing are essential to the owners' vision.

## Gameplay to decide

Do not infer a full design from the title. Ask whether neighborhood defense means protecting residents, building traps, repairing structures, fighting waves, cooperating on chores, or another idea. Define the target audience, tone, failure conditions, and the main 30-second action before designing enemies or progression.

Complete this sentence with the owners:

> Players are ______ who cooperate to ______ by ______. The enjoyable complication is ______. A round/session ends when ______.

Then define the core loop:

> Prepare/explore -> perform the central interaction -> face a complication -> recover or succeed -> receive feedback/reward -> choose the next action.

This loop is a worksheet, not an approved game mechanic.

## Proposed first-release envelope

| Area | Proposal | Approval needed |
| --- | --- | --- |
| World | One compact neighborhood area | Owners approve setting and size |
| Players | Two online first, then four total | Clarify total cap and mixed sessions |
| Camera | Third person online; split-screen later | Confirm camera comfort and local layouts |
| Activities | One complete objective, then about three reusable activities | Defense loop must be defined first |
| Art | Simple original cartoon shapes and a small palette | Agree visual direction |
| Physics | Hybrid character plus bounded movable props | Prove the intended feel |
| Saving | Host-owned progression and settings first | Decide shared versus individual rewards |
| Release | Private test builds first | Decide private/family versus eventual sale |

## Definition of success

Early success: Brent and Jax can explain, modify, and play the prototype together over the internet. Release success: a new tester can join, understand the objective, recover from mistakes, and complete the small game without developer intervention. Set measurable fun, readability, performance, and session-length targets after the first prototype.

## Scope boundaries

Keep large worlds, numerous vehicles, extensive character customization, public matchmaking, accounts, cloud persistence, AI-model integration, host migration, and console ports out of the first prototype. These are deferred recommendations, not a permanent prohibition. Do not add them without recording scope and revised effort.
