# Verification and playtesting

Keep evidence proportional to the change. Documentation checks cannot establish playable behavior. Use [the playtest template](templates/PLAYTEST.md) for game observations and session records for development checks.

## Documentation foundation

- Run `python3 scripts/validate_docs.py` and whitespace checks from [DEVELOPMENT.md](DEVELOPMENT.md).
- Confirm README navigation, adapter paths, and the canonical document map agree.
- Confirm each accepted requirement has a human source and each proposal is labeled.
- Confirm task/directive/decision references resolve and license notices agree.
- Confirm no private emails, credentials, auth URLs, keys, or unrelated conversations were committed.
- Verify the published GitHub branch and file tree after integration.

## First gameplay matrix

| Test | Expected result | Gate |
| --- | --- | --- |
| Export and launch on both Macs | Game starts outside editor with readable controls | M1 |
| Host and join on LAN | Correct distinct player identities | M2 |
| Failed connection | Clear failure and retry; no duplicate player | M2 |
| Client leaves | Character and held object resolve safely | M2/M3 |
| Host leaves | Session ends with clear return to menu | M2/M3 |
| Repeated grab/drop | Stable objects and recoverable movement | M3 |
| Simultaneous grab | One holder or explicit shared-grab rule, never ambiguous state | M3 |
| Player/object out of bounds | Host resets essential state | M3 |
| Internet from separate networks | Connection strategy works and latency is assessed | M3 |
| Complete/fail/retry activity | Objectives and rewards stay consistent | M4 |
| Save, quit, reopen | Progress/settings restore; missing/corrupt save handled | M4/M7 |
| Simultaneous completion | Reward awarded once according to policy | M4/M5 |
| Four participants | Stable state, readable feedback, measured performance | M5 |
| Controller disconnect/reconnect | Inputs recover without switching characters unexpectedly | M7/M8 |
| Multiple local players | Correct inputs, cameras, prompts, pause/save rules | M8 |
| Mixed local/online | Test only if this combination is approved | M8 |

## Record test conditions

Record build/commit, date with time-zone offset, engine version, OS, machine/GPU, resolution, settings, player count, connection method, and observed network conditions. Separate a measured result from an estimate. Desktop-only testing cannot establish Mac performance.

## Automated tests to introduce

Prioritize meaningful rules: reward idempotency, objective state transitions, save-version/missing-file recovery, and authority validation. Do not add tests that merely mirror a trivial implementation. Physics feel, camera comfort, and online play require representative manual testing even with automated checks.

## Defect severity and release gate

Block release for known lost-progress defects, crashes on supported paths, impossible core objectives, or unrecoverable session failures. Prioritize frequent input/camera/readability problems next. Cosmetic issues can be deferred with a recorded task.

Have several new testers try the exported build without developer narration. Observe what they do, not only what they say. Record findings and create specific tasks. Do not claim a test passed unless it ran; record not-run limitations explicitly.
