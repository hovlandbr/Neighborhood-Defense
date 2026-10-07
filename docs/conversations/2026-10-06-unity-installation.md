# Unity installation session

- Date: 2026-10-06 (America/Chicago).
- Participants: Brent and Codex.
- Directive/task: DIR-003; ND-021.
- Branch: `codex/unity-installation`.
- Base revision: `4b415e30c6f910f8254805066bd5681ebbc5ab47`.

## Human request — verbatim

> can you install unity on this computer

## AI progress — verbatim

> I’ll check this Mac and any existing Unity installation, then install Unity Hub and a stable LTS editor. I’ll record the setup in the project’s Markdown files so future tools can find it.

> This is an Intel Mac with plenty of free disk space, and Unity is not installed yet. I’m installing Unity Hub first, then using its release list to choose an LTS editor for this Mac.

## Scope and initial evidence

Install Unity locally for evaluation. This request does not authorize creating a game project or settle the final product engine choice. Current Mac: x86_64, macOS 26.7.1 (25G241), about 831 GiB available. No Unity Hub/editor installation was found in the standard Applications paths. Homebrew was not found on PATH. Applications is writable.

## Handoff

The installation attempt was interrupted before an application was installed by this assistant. The legacy Unity download URL returned HTTP 404. On resumption the owner reported Unity should be installed; Unity Hub 3.22.2 and an editor folder for 6000.6.4f1 were found. This session continues in [the development toolchain session](2026-10-06-development-toolchain.md); activation and editor execution still need verification. The local branch was renamed to `codex/development-toolchain` to cover the owner's expanded setup request.
