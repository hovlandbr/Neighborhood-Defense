# Development and local AI toolchain session

## Metadata

- Date: 2026-10-06 (America/Chicago).
- Participants: Brent and Codex.
- Tasks/directives: ND-021/022; DIR-003/004, standing DIR-002.
- Branch: `codex/development-toolchain`, renamed from `codex/unity-installation` for this continuing setup task.
- Base revision: `4b415e30c6f910f8254805066bd5681ebbc5ab47`.
- Read: root instructions, README/documentation map, status, directives, backlog, decisions, prior session, development, tooling, licensing, testing.
- Claimed paths: setup/tooling/status/directive/task/conversation records, and small setup support files if needed.

## Human request — verbatim

> unity should be installed, can you install any other thinkgs we will need for development and local ai development,

The owner also supplied the standing AGENTS.md instructions in chat; they match the repository workflow. No new game implementation or paid service was requested.

## Conversation

AI progress — verbatim:

> I’ll verify Unity’s installation, then set up the core tools for game development and local AI. I’ll check what is already installed and record versions and any remaining setup steps in the project’s Markdown files.

Optional clarification asked:

> For local AI, what should this Mac focus on? I can install the general development tools while you decide.

Choices: run local models/build AI apps; train/fine-tune; both with heavy work on the RTX 4090 desktop. No answer recorded yet.

AI progress — verbatim:

> Unity Hub and Unity Editor **6000.6.4f1** are now present. Ollama is also installed, and this Mac has 64 GB of RAM.
>
> I’m adding VS Code with Unity/C# support, Blender for 3D assets, Git LFS for large files, and Python tools for local AI work. Ollama uses the CPU on Intel Macs, so your RTX 4090 desktop will be better suited to heavier model work.

## Initial evidence and scope

Intel x86_64 Mac, macOS 26.7.1, 64 GiB RAM; Apple Command Line Tools and Git exist. Unity Hub reports 3.22.2; editor folder 6000.6.4f1 exists. Ollama application reports 0.40.0. Verify functional checks before treating these as working. VS Code, Blender, uv, and Node were not found in the initial standard paths/PATH. Homebrew is absent, and the system CLI directory is not writable; prefer official user-local CLI downloads rather than requiring administrator access for a package manager.

Plan: VS Code and Unity/Python extensions, a supported Intel Blender LTS, .NET SDK for C# tooling, Git LFS, uv with isolated Python/Jupyter/AI API tooling, and Node LTS for development integrations. Preserve existing Ollama models/settings. Avoid installing CUDA on this Intel Mac or assuming training libraries support it. No engine project or external integrations will be created by this setup task.

AI progress — verbatim:

> The downloads are complete. I’m finishing installation and checking that the tools run from a new terminal.
>
> For local AI, I’m setting up an isolated Python environment with Jupyter and a small coding model for quick experiments. Your existing Ollama model and settings are being preserved.

AI progress — verbatim:

> The core checks passed: C# compiled and ran, Blender launched successfully, the Python libraries imported, and the new local coding model answered through Ollama.
>
> I’m recording the setup and publishing the handoff files. Unity project creation and debugging are still untested because the game project has not been created yet.

## Changes and decisions

- Verified Unity Hub 3.22.2 and editor 6000.6.4f1, preserved the installed version; no new Unity download was necessary after the owner installed it between turns.
- Installed VS Code 1.140.0 x64, Blender 4.5.14 LTS x64, .NET 10.0.401 x64, Git LFS 3.8.0, GitHub CLI 2.102.0, Node 24.21.0 LTS/npm 11.19.0, uv 0.12.23, Python 3.12.15, and Ruff 0.16.10.
- Installed VS Code extensions: Unity 1.3.2, C# 2.160.4, C# Dev Kit 3.40.210, .NET runtime acquisition 3.2.0, Python 2026.8.0, Python environments 1.38.0, Pylance 2026.4.1, debugpy 2026.6.0, Jupyter 2025.9.1/renderers 1.3.0/keymap 1.1.2/cell-tags 0.1.9/slideshow 0.1.6, Ruff 2026.84.0.
- Added isolated notebook/API environment, manifest and lock under `tools/local-ai/`; 102 packages installed locally. Private environments/scratch excluded from Git. Updated validator exclusions to avoid scanning vendor Markdown inside `.venv/`.
- Retained Ollama 0.40.0 and existing gemma4:26b; added qwen2.5-coder:1.5b (986 MB, ID d7372fd82851) for quick CPU experiments.
- Created user-local CLI launchers/path setup. Existing shell profiles preserved, with a small marked source block added. Git LFS initialized only in this repository; no tracking patterns/uploads added. Git author identity left unset.
- DEC-007 accepts installation scope only. Final game engine, game concept, and training workflow remain open. The optional AI preference question received no answer during this work; inference/notebook setup is the stated default.
- Updated README, development/local AI/tooling/licensing records, directive/task/status/conversation indexes, changelog, and validator. No game source or third-party game content added.

## Verification

| Check | Command/condition | Result |
| --- | --- | --- |
| Unity recognized | Hub `-- --headless editors -i`; editor `-version` | Hub recognized the standard installation; editor returned 6000.6.4f1 |
| Download integrity | Official checksum files for Blender, Node, Git LFS, GitHub CLI | SHA256 matches |
| Desktop application signing | `spctl --assess --type execute --verbose` on VS Code and Blender | Both accepted, Notarized Developer ID |
| New terminal paths | `zsh -lic` tool paths/versions and Node expression | User-local tools resolve and Node runtime prints confirmation |
| C# compiler/runtime | `dotnet new console` and `dotnet run` in ignored scratch | Printed `Hello, World!` |
| Blender | Background factory-startup with `bpy.app.version_string` | Printed 4.5.14 LTS and exited normally |
| Python environment | Frozen uv sync, imports, `uv pip check` | 102 packages compatible; imports passed |
| Notebook kernel | nbclient executed a NumPy cell | Result `3`; JupyterLab version 4.6.4 |
| Ollama API | Loopback version endpoint; one local generation request | 0.40.0; response `READY`, two tokens; model unloaded afterward |
| GitHub CLI | `gh --version`, `gh auth status` | CLI runs; terminal not logged in, owner login remains |
| Documentation | `python3 scripts/validate_docs.py`; `git diff --check` | 33 Markdown files and 136 relative links passed before publication; whitespace clean |

The smoke prompt was: `Reply with exactly the word READY.` The local model reply was: `READY`. This was a setup check, not a product directive or coding-quality evaluation.

Initial Blender CLI check failed because a symlink made bundled Python/resource discovery use the wrong directory. Replaced that newly created symlink with a wrapper that executes the actual application binary; the subsequent check passed. Initial documentation validation inspected vendor Markdown in `.venv/`; added generated-environment exclusions and reran successfully. Hub headless listing printed database-lock warnings while the existing GUI was running but returned the installation; no Hub data was deleted. Unity activation, graphical game execution, game debugging/export/networking, second-Mac setup, desktop training, and Docker/Linear configuration were not tested.

## Final handoff

- Local installation complete; repository records prepared on `codex/development-toolchain` for PR publication.
- Task/claim: ND-021 verification complete; ND-022 tools complete, publication reconciliation pending.
- Human follow-up: Open Unity Hub and finish sign-in/license activation if prompted. Terminal GitHub uses `gh auth login --hostname github.com --web`; connected GitHub access does not sign the terminal in.
- Next action: Review this setup PR, then resolve ND-001 product/engine questions before creating a game project. For local experiments, use [LOCAL_AI.md](../LOCAL_AI.md).
- Publication evidence and final response are appended after GitHub verification. No game behavior is claimed.
