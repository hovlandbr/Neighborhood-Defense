# Development setup and commands

Status: local development tools installed on one Mac; no Unity/Godot game project, game build pipeline, or playable source yet. Toolchain smoke checks do not establish game behavior.

## Available hardware

Two 2019 i9 MacBook Pros and one i9 14th-generation/RTX 4090/128 GB desktop, as reported by the owner. The current Mac was verified as Intel x86_64, 64 GiB RAM, macOS 26.7.1 (25G241) on 2026-10-06. The second Mac's details, current Mac GPU, and desktop OS remain unrecorded. Use Mac performance evidence to set the initial budget; the desktop can mask inefficiency.

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
| Unity Hub | 3.22.2 | Already present when resumed; editor recognized |
| Unity Editor | 6000.6.4f1, Intel | Already present when resumed; `-version` passed; license activation/project debugging not verified; not recorded as an LTS release |
| Language | GDScript proposed | Not implemented |
| Physics | Built-in Jolt proposed | Not tested |
| Renderer | Compatibility proposed for first benchmark | Not tested |
| Source project | `game/` proposed | Directory absent |
| Git hosting | GitHub, `hovlandbr/Neighborhood-Defense` | Repository confirmed |
| Planning view | Linear considered | No project connection verified |
| Documentation validator | Python 3 standard library | Local workflow provided below |

## Installed local tools — 2026-10-06

| Tool | Version | Location/verification |
| --- | --- | --- |
| VS Code | 1.140.0 x64 | Applications; CLI works; notarization assessment accepted |
| Unity extension | 1.3.2 | `visualstudiotoolsforunity.vstuc`; installed with C# 2.160.4 and C# Dev Kit 3.40.210 |
| Python/Jupyter/Ruff extensions | Python 2026.8.0, Jupyter 2025.9.1, Ruff 2026.84.0 | Installed; full extension inventory in the session |
| Blender | 4.5.14 LTS x64 | Applications; background factory-startup/Python check passed; notarization assessment accepted |
| .NET SDK | 10.0.401 x64 | `~/.dotnet`; independent C# console compiled and printed `Hello, World!` |
| Apple developer tools | Clang 21.0.0, Git 2.50.1 | Existing Command Line Tools; retained |
| Git LFS | 3.8.0 amd64 | `~/.local/bin/git-lfs`; repository-local hooks initialized; no asset patterns or LFS uploads yet |
| GitHub CLI | 2.102.0 amd64 | `~/.local/bin/gh`; installed, terminal login still required |
| Node / npm | 24.21.0 LTS / 11.19.0 | `~/.local/bin`; official binaries and checksum verified |
| uv / Python | 0.12.23 / 3.12.15 | `~/.local/bin`; isolated [AI environment](LOCAL_AI.md) |
| Ruff CLI | 0.16.10 | `~/.local/bin/ruff`; installed with `uv tool` |
| Ollama | 0.40.0 | Existing application and loopback API retained; local generation passed |

Official installers were used without Homebrew. CLI binaries/packages live under the user's local directories; shell path setup is in `~/.config/neighborhood-dev/env.zsh`, sourced by `.zprofile` and `.zshrc`. Existing profiles were preserved; any backups/installers are ignored local scratch. Open a new terminal to pick up the paths. These home-relative locations are conventions, not hardcoded account paths in the repository.

Run from the repository root:

```sh
code .
dotnet --version
blender --background --factory-startup --python-expr 'import bpy; print(bpy.app.version_string)'
git lfs version
uv sync --project tools/local-ai --frozen
```

Open Unity Hub from Applications to complete sign-in/license activation if prompted. In a future authorized Unity project, select VS Code in Unity Preferences > External Tools and use the **Visual Studio Editor** package version 2.0.20 or newer. The older **Visual Studio Code Editor** package is deprecated; see [Microsoft's Unity setup guide](https://code.visualstudio.com/docs/other/unity). The standalone .NET SDK supports editor tooling; it does not change Unity's scripting runtime.

Terminal GitHub authentication is separate from the connected GitHub service. Run `gh auth login --hostname github.com --web` and select the intended account when terminal pushes are needed. This session used the existing authorized connector for publication. No terminal credentials or Git author identity were invented.

The second Mac and desktop have not been configured by this session. Training frameworks/CUDA, art-painting/audio applications, and engine plugins remain future choices tied to actual tasks.

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
| Open editor | Unity Hub/VS Code/Blender installed; no game project to open yet |
| Run game | Not available |
| Export macOS | Not available |
| Export desktop OS | Not available; OS also unresolved |
| Gameplay/rules tests | Not available |
| Network simulation tests | Not available |

Add tested commands and prerequisites after ND-002/ND-003; never replace unknown entries with guessed success.
