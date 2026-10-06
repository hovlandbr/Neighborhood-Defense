# Development setup and commands

Status: documentation only. There is no `project.godot`, dependency installation, build pipeline, or playable source yet. Do not invent a run command.

## Available hardware

Two 2019 i9 MacBook Pros and one i9 14th-generation/RTX 4090/128 GB desktop, as reported by the owner. Exact Mac GPUs/RAM/OS and desktop OS are unrecorded. Use Mac performance evidence to set the initial budget; the desktop can mask inefficiency.

## Proposed setup order

1. Resolve product and engine decisions through ND-001.
2. Choose one stable engine version and record it below.
3. Install the same version on both development Macs and download matching export templates.
4. Start with a simple renderer and compare a representative scene on both Macs.
5. Establish Git pull/commit/push habits and confirm repository access separately for each human/tool.
6. Create the engine project under the agreed source path, then document actual editor/run/export steps.
7. Test an exported build outside the editor on both Macs and the desktop OS when known.
8. Introduce art/audio applications only as needed; register external content before importing it.

## Version register

| Component | Selection/version | Status |
| --- | --- | --- |
| Engine | Godot proposed; exact version unset | Awaiting owner decision |
| Language | GDScript proposed | Not implemented |
| Physics | Built-in Jolt proposed | Not tested |
| Renderer | Compatibility proposed for first benchmark | Not tested |
| Source project | `game/` proposed | Directory absent |
| Git hosting | GitHub, `hovlandbr/Neighborhood-Defense` | Repository confirmed |
| Planning view | Linear considered | No project connection verified |
| Documentation validator | Python 3 standard library | Local workflow provided below |

## Useful Git checks

From the repository root, inspect `git status --short --branch`, `git remote -v`, and `git log -5 --oneline`. An empty repository has no log until its first commit. Validate permissions through the authenticated tool rather than assuming a public clone can push. Pull/fetch before integration; never force push to overwrite another agent's work.

Configure commit identity using the authorized human/tool identity if needed; do not invent a person's email or commit as Jax. Keep credentials in approved credential storage, never Markdown.

## Documentation validation

Run from repository root:

```sh
python3 scripts/validate_docs.py
git diff --check
```

The validator checks required records, safe relative links, and duplicate record headings. It does not validate remote web availability, all Markdown anchor syntax, prose accuracy, code, or game behavior. Review those separately. `git diff --check` checks changed tracked/staged text, so use `git diff --cached --check` after staging initial files.

## Commands to add later

| Operation | Command/evidence |
| --- | --- |
| Open editor | Not available until engine approval and project creation |
| Run game | Not available |
| Export macOS | Not available |
| Export desktop OS | Not available; OS also unresolved |
| Gameplay/rules tests | Not available |
| Network simulation tests | Not available |

Add tested commands and prerequisites after ND-002/ND-003; never replace unknown entries with guessed success.
