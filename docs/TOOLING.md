# Tool and integration register

This register distinguishes an available tool from a verified connection. Each participant needs its own valid permissions; Markdown cannot grant access or automatically configure an application.

## Current services

| Service | Role | Verified state as of 2026-10-06 | Canonical record |
| --- | --- | --- | --- |
| GitHub | Repository, history, code review | `hovlandbr` connection reports push/admin access to this repository | Git commits and these Markdown files |
| Linear | Optional planning/task board | Owner considered it; no project/issue mapping configured here | [Backlog](coordination/BACKLOG.md) |
| Codex | Current assistant | Used for foundation; future sessions must re-read latest state | [AGENTS.md](../AGENTS.md) |
| Claude | Potential additional assistant | Connection not verified; adapter added | [CLAUDE.md](../CLAUDE.md) |
| Gemini | Potential additional assistant | Connection not verified; adapter added | [GEMINI.md](../GEMINI.md) |
| GitHub Copilot | Potential additional assistant | Use repository instructions; settings/support vary | [Copilot adapter](../.github/copilot-instructions.md) |
| Other AI/editor | Future integration | Manually attach root instructions if not auto-discovered | [AGENTS.md](../AGENTS.md) |

Use the `hovlandbr` account for this repository when multiple GitHub connections exist. A public read does not verify write access. Do not store link credentials or personal emails in this register.

## Proposed software

| Tool | Purpose | License/cost category | Selection |
| --- | --- | --- | --- |
| Godot | Engine, scripting, levels, UI | Free/open source, MIT | Proposed |
| Blender | 3D authoring and animation | Free/open source, GPL application | Installed on current Mac; see DEVELOPMENT |
| Krita | Painting and textures | Free/open source, GPL application | Proposed |
| Audacity | Audio recording/editing | Free/open source, GPL application | Proposed |
| Git | Version control | Free/open-source software | Repository workflow |
| GitHub | Hosted repository | Proprietary service with free options | Confirmed hosting |
| Linear | Planning view | Proprietary service with free options and limits | Optional |
| Inkscape / OBS | Vector art / gameplay recordings | Free/open-source applications | Optional |

Keep application licensing separate from asset and game licensing. Verify current terms when adopting a tool/service; avoid paid hosting or broad permissions without owner direction.

## Installed software for evaluation

The owner's setup requests installed VS Code/Unity C# extensions, Blender LTS, .NET SDK, Git LFS, GitHub CLI, Node LTS, uv/Python/Ruff, and an isolated Jupyter/local AI environment on the current Mac. Unity and Ollama were already present when the setup resumed. Exact versions and verification live in [DEVELOPMENT.md](DEVELOPMENT.md) and [LOCAL_AI.md](LOCAL_AI.md); these records supersede any assumption that every tool is merely proposed.

Unity, VS Code's distributed binaries, and Microsoft extensions have their own proprietary terms; Blender/Git LFS/Node/uv/.NET are open-source tools. No paid account or service was configured. Desktop installation is not a game runtime dependency or proof of an external integration. GitHub CLI is installed but not signed in; the existing GitHub connector remains separate. Linear and Docker applications were observed locally, but their project configuration/runtime was not tested or changed.

Official setup references: [Unity Hub](https://docs.unity.com/en-us/hub/install-hub-win-mac), [VS Code Unity support](https://code.visualstudio.com/docs/other/unity), [.NET on macOS](https://learn.microsoft.com/en-us/dotnet/core/install/macos), [uv installation](https://docs.astral.sh/uv/getting-started/installation/), [Node downloads](https://nodejs.org/en/download), [Git LFS](https://git-lfs.com/), [GitHub CLI](https://cli.github.com/), [Blender release downloads](https://download.blender.org/release/Blender4.5/).


## Markdown-first synchronization contract

1. Read the current directive/task/session records from the repository.
2. Map one task ID to one external issue if a planning integration is adopted.
3. Put the external URL in that task and the canonical Markdown path in the issue.
4. Import substantive external comments/requests into a dated Markdown conversation record before dependent implementation.
5. Update canonical task status and evidence when external work completes; then mirror it to the board.
6. On conflict, retain both records and reconcile using their source timestamps/authorization. A board status cannot approve a product decision.

No bidirectional sync, webhook, scheduled automation, or transcript collector exists. Initial synchronization is manual. An automated integration requires a separate directive, design, permissions review, and test. Do not promise automatic capture across every tool.

## Discovery support

Root adapters provide a common starting path, but tools vary in whether they read links or instruction files automatically. Verify onboarding with a simple test: ask the attached tool to report the current stage, active directive, next task, and handoff path. Correct configuration if it cannot find them.

[GitHub's repository instruction documentation](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) describes Copilot discovery support. Adapters are entry points, not proof that a tool is connected.
