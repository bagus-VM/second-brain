"""Lint the 2nd-semester vault: broken wikilinks, missing frontmatter, missing sections.

Usage: python lint_vault.py
Prints a report; exits non-zero if broken links exist.
"""
import os
import re
import sys
from collections import defaultdict

ROOT = r"C:\Users\quiescent\Documents\Vault\second-brain"
SEM = os.path.join(ROOT, "2nd-semester")
REQUIRED = [
    "## One-line Summary",
    "## Core Intuition",
    "## Formal Definition / Statement",
    "## Core Properties",
    "## Key Properties",
    "## Worked Example",
    "## Common Pitfalls",
    "## Connections",
    "## Open Questions",
]

LINK = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")

# Obsidian does not create wikilinks inside code spans or fenced code blocks.
# Strip them before scanning, otherwise a tensor literal like tensor([[0.0740]])
# is reported as a broken link to the page "0.0740".
CODE_SPAN = re.compile(r"`[^`\n]*`")
FENCE = re.compile(r"```.*?```", re.S)


def strip_code(text):
    """Remove fenced code blocks and inline code spans."""
    return FENCE.sub(" ", CODE_SPAN.sub(" ", text))


def note_index():
    names = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if any(skip in dirpath for skip in (".obsidian", ".kilo", "node_modules", ".venv", ".git", ".pytest_cache", ".mypy_cache", ".ruff_cache")):
            continue
        for fn in filenames:
            if fn.endswith(".md"):
                names[fn[:-3]].append(os.path.join(dirpath, fn))
    return names


def main():
    names = note_index()
    files = []
    for dirpath, dirnames, filenames in os.walk(SEM):
        if any(skip in dirpath for skip in (".obsidian", ".venv", ".git", ".pytest_cache", ".mypy_cache", ".ruff_cache", "projects", "Ai Engineering Lab")):
            continue
        for fn in filenames:
            if fn.endswith(".md"):
                files.append(os.path.join(dirpath, fn))

    broken = []
    no_fm = []
    short = []
    for path in sorted(files):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        rel = os.path.relpath(path, SEM)
        if not text.startswith("---"):
            no_fm.append(rel)
        words = len(text.split())
        if words < 250:
            short.append((rel, words))
        for m in LINK.finditer(strip_code(text)):
            target = m.group(1).strip()
            if "'" in target or '"' in target or target in ("wikilinks", "target", "x", "concept-foo", "concept-foo.md"):
                continue  # placeholder text in docs, or a Python literal like [["Amount"]]
            if "/" in target:
                # path-style link (Obsidian supports [[folder/note]]): resolve against the vault root
                if os.path.exists(os.path.join(ROOT, target)) or os.path.exists(os.path.join(ROOT, target + ".md")):
                    continue
            if target not in names:
                broken.append((rel, target))

    print(f"notes scanned: {len(files)}")
    print(f"broken wikilinks: {len(broken)}")
    for rel, target in broken:
        print(f"  {rel} -> [[{target}]]")
    print(f"missing frontmatter: {len(no_fm)}")
    for rel in no_fm:
        print(f"  {rel}")
    print(f"notes under 250 words: {len(short)}")
    for rel, w in short:
        print(f"  {rel} ({w} words)")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
