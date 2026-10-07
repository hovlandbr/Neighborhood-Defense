# Licensing and asset register

## Owner choice

On 2026-10-06 the owner chose: "Keep the game proprietary for now; reserve rights to code and content." See [the foundation conversation](conversations/2026-10-06-foundation.md) and DEC-002 in [DECISIONS.md](DECISIONS.md).

[LICENSE](../LICENSE) reserves rights to original materials while respecting applicable law, existing permissions, GitHub platform terms, and third-party licenses. Do not apply MIT/Creative Commons to the game's original code/assets without a new explicit rights-holder decision. Public visibility does not create an additional open-source license.

The notice does not transfer ownership between Brent, Jax, or other creators. Identify actual rights holders when publishing or accepting contributions. External contributions require agreed rights and permission; do not assume a public PR transfers copyright.

## Tool licenses versus output

Godot permits developers to choose the license for their games; distributed engine binaries require the relevant notices. Blender and Krita state that the artwork produced with them can be used as its creator chooses. Using an open-source authoring tool does not by itself open-source the game. Including third-party code or assets has separate obligations.

References checked 2026-10-06: [Godot license](https://godotengine.org/license/), [Blender license](https://www.blender.org/about/license/), [Krita license](https://krita.org/en/about/license/), [GitHub terms](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service).

## External asset/dependency register

No third-party game assets or runtime dependencies have been added to this documentation foundation. Suggested resources are not imported dependencies.

| ID | Asset/component and version | Creator/source URL | Exact license/evidence path | Changes | Required notices/credit | Game paths | Review status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| None | None imported | — | — | — | — | — | — |

For each import: retain its original terms, record source/version/date, verify distribution and modification rights, record required credit, and link actual paths. Register fonts, samples, plugins, code snippets, and AI-assisted assets too. Avoid relying on "free download" as license evidence.

CC0 resources can simplify asset use; CC BY adds attribution duties, and other CC variants may restrict commercial use or adaptations. Read the specific license. Software copyleft duties for incorporated code differ from using a GPL authoring application. Do not make blanket compatibility claims without reviewing what is included.

## Development tools and local model — 2026-10-06

Installed desktop/CLI applications are development tools, not included game components. The game remains proprietary. Unity and Microsoft editor/extension terms remain separate; confirm applicable Unity license eligibility in Hub before use. Review commercial/team use of extensions against their published terms rather than assuming all installed software is open source.

| Development component | Source/rights record | Inclusion |
| --- | --- | --- |
| Unity Hub/editor | [Unity legal terms](https://unity.com/legal); actual versions in DEVELOPMENT | Local application only; no game project created |
| Blender 4.5.14 LTS | [Blender licensing](https://www.blender.org/about/license/) | Local GPL authoring application; no imported artwork |
| VS Code and Microsoft extensions | [VS Code license](https://code.visualstudio.com/license), installed extensions' bundled license files | Local editing/debugging only |
| .NET SDK, Node, Git LFS, GitHub CLI, uv/Ruff | Official releases/installers; bundled license files retained with local installations | Development CLI tools only |
| Python notebook/API environment | [Manifest](../tools/local-ai/pyproject.toml) and [lock](../tools/local-ai/uv.lock); package license metadata retained in the local environment | Development-only dependencies, no game runtime integration |
| Qwen2.5-Coder 1.5B Q4_K_M, ID `d7372fd82851` | [Ollama model/license](https://ollama.com/library/qwen2.5-coder:1.5b), [original model card](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct); Apache-2.0 | Local Ollama cache, not committed or shipped |

No original project material was relicensed. Existing Ollama/gemma model terms were not changed; the existing model was not imported into the game. Register runtime packages, models, generated assets, and any redistribution separately before they enter a shipped product.


## Release check

Review original rights, imported notices, credits, store disclosures/requirements, and contribution permissions before distribution. Keep any private permission correspondence outside this public repository; record only the non-sensitive outcome and a secure reference. Keep source and evidence for the shipped version.
