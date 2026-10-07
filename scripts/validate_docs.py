#!/usr/bin/env python3
"""Check the Markdown record map without external dependencies.

Run from any directory with Python 3. Does not verify network links, prose,
anchors, licensing interpretation, or gameplay. No files are modified.
"""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "LICENSE", "AGENTS.md", "CLAUDE.md", "GEMINI.md",
    "CONTRIBUTING.md", "CHANGELOG.md", ".github/copilot-instructions.md",
    "docs/README.md", "docs/STATUS.md", "docs/PRODUCT.md", "docs/ROADMAP.md",
    "docs/ARCHITECTURE.md", "docs/DEVELOPMENT.md", "docs/TESTING.md",
    "docs/TOOLING.md", "docs/LICENSING.md", "docs/DECISIONS.md",
    "docs/QUESTIONS.md", "docs/RISKS.md", "docs/coordination/AI_DIRECTIVES.md",
    "docs/coordination/BACKLOG.md", "docs/conversations/README.md",
    "docs/conversations/2026-10-06-foundation.md",
    "docs/templates/SESSION.md", "docs/templates/DIRECTIVE.md",
    "docs/templates/TASK.md", "docs/templates/DECISION.md",
    "docs/templates/PLAYTEST.md",
)


def main():
    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append("Missing required record: " + name)

    paths = sorted(
        p for p in ROOT.rglob("*.md")
        if not any(part in {".git", "work", "outputs", ".venv", ".ipynb_checkpoints"}
                   for part in p.relative_to(ROOT).parts)
    )
    links = 0
    for path in paths:
        relative = str(path.relative_to(ROOT))
        content = path.read_text(encoding="utf-8")
        if not content.strip():
            errors.append("Empty Markdown file: " + relative)
        if not content.endswith("\n"):
            errors.append("Missing final newline: " + relative)
        body = re.sub(r"```[^\n]*\n.*?```", "", content, flags=re.S)
        ids = re.findall(r"^##\s+((?:DIR|DEC)-\d+)\b", body, flags=re.M)
        if len(ids) != len(set(ids)):
            errors.append("Duplicate record heading ID in: " + relative)
        for match in re.finditer(r"\[[^\]\n]+\]\(([^)\n]+)\)", body):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            links += 1
            local = (path.parent / unquote(parsed.path)).resolve()
            try:
                local.relative_to(ROOT)
            except ValueError:
                errors.append(relative + ": link leaves repository: " + target)
                continue
            if not local.exists():
                errors.append(relative + ": missing link target: " + target)

    if errors:
        for error in errors:
            print("ERROR: " + error)
        print("Documentation validation failed: " + str(len(errors)) + " error(s).")
        return 1
    print("PASS: " + str(len(paths)) + " Markdown files; " + str(links)
          + " relative links; required records and heading IDs checked.")
    print("Scope: documentation structure only; no game or network behavior verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
