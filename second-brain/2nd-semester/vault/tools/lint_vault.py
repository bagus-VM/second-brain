"""Lint the 2nd-semester vault: broken wikilinks, duplicate note names, template sections,
missing frontmatter, stubs.

Usage: python lint_vault.py
Prints a report; exits non-zero if broken links, duplicate note names or missing concept
sections are found.
"""
import os
import re
import sys
from collections import defaultdict

ROOT = r"C:\Users\quiescent\Documents\Vault\second-brain"
SEM = os.path.join(ROOT, "2nd-semester")
# The 8-section concept template. Only vault/concepts pages owe all of it: topic overview pages,
# course pages and homework solutions follow templates of their own.
REQUIRED = [
    "One-line Summary",
    "Core Intuition",
    "Formal Definition / Statement",
    "Key Properties",
    "Worked Example",
    "Common Pitfalls",
    "Connections",
    "Open Questions",
]

# headings this vault has used for the same section
ALIASES = {
    "Core Properties": "Key Properties",
    "Key Properties / Complexity": "Key Properties",
    "Formal Definition": "Formal Definition / Statement",
    "Formal Statement": "Formal Definition / Statement",
}

SOURCE_DIRS = ("raw", "projects")


def in_source_tree(path):
    """True for immutable source material or a project workspace, i.e. not a vault note."""
    return any(part in SOURCE_DIRS for part in os.path.normpath(path).split(os.sep))


def headings_of(text):
    """The ## headings of a page, alias-normalised and with any ' — subtitle' stripped.

    Pages legitimately title a section '## Worked Example — the runtime path of one line';
    an exact-match check would report those as missing sections.
    """
    body = text[text.find("\n---", 3) + 4:] if text.startswith("---") else text
    out = []
    for h in re.findall(r"^##\s+(.+?)\s*$", body, re.M):
        h = re.split(r"\s+[—–-]\s+", h)[0].strip()
        out.append(ALIASES.get(h, h))
    return out

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
        # "raw" is immutable source material (PDFs, harvested HTML, agent plan files), not vault
        # notes: its .md files have no frontmatter by design and must not be linted as notes.
        if any(skip in dirpath for skip in (".obsidian", ".venv", ".git", ".pytest_cache", ".mypy_cache", ".ruff_cache", "projects", "Ai Engineering Lab", "raw")):
            continue
        for fn in filenames:
            if fn.endswith(".md"):
                files.append(os.path.join(dirpath, fn))

    broken = []
    no_fm = []
    short = []
    missing_sec = []
    for path in sorted(files):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        rel = os.path.relpath(path, SEM)
        if not text.startswith("---"):
            no_fm.append(rel)
        words = len(text.split())
        if words < 250:
            short.append((rel, words))
        if rel.startswith("vault" + os.sep + "concepts"):
            heads = headings_of(text)
            for want in REQUIRED:
                if want not in heads:
                    missing_sec.append((rel, want))
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

    # A name shared by two notes makes every [[wikilink]] to that name ambiguous, and Obsidian
    # resolves it silently — a page can end up pointing at the wrong course or concept with no
    # visible error. raw/ and projects/ are excluded: they carry many same-named READMEs by design.
    # Two classes are deliberately not errors:
    #   - the per-semester registries (index.md, log.md, Courses.md, Topics.md), which exist once per
    #     semester by design — link them path-style when the target semester matters;
    #   - pairs that live entirely outside 2nd-semester: reported, but not counted against this run.
    REGISTRIES = {"index.md", "log.md", "Courses.md", "Topics.md"}
    dupes = {name: [p for p in paths if not in_source_tree(p)] for name, paths in names.items()}
    dupes = {name: paths for name, paths in dupes.items() if len(paths) > 1}
    registry_dupes = {n: p for n, p in dupes.items()
                      if all(os.path.basename(x) in REGISTRIES for x in p)}
    other_semester = {n: p for n, p in dupes.items()
                      if n not in registry_dupes and not any(
                          os.path.normpath(x).startswith(os.path.normpath(SEM) + os.sep) for x in p)}
    dupes = {n: p for n, p in dupes.items() if n not in registry_dupes and n not in other_semester}

    print(f"notes scanned: {len(files)}")
    print(f"broken wikilinks: {len(broken)}")
    for rel, target in broken:
        print(f"  {rel} -> [[{target}]]")
    print(f"duplicate note names: {len(dupes)}")
    for name, paths in sorted(dupes.items()):
        print(f"  {name}")
        for p in paths:
            print(f"    {os.path.relpath(p, ROOT)}")
    print(f"per-semester registries sharing a name (expected): {len(registry_dupes)}")
    for name, paths in sorted(registry_dupes.items()):
        print(f"  {name}: " + ", ".join(os.path.relpath(p, ROOT) for p in paths))
    print(f"duplicate names outside 2nd-semester (reported, not counted): {len(other_semester)}")
    for name, paths in sorted(other_semester.items()):
        print(f"  {name}: " + ", ".join(os.path.relpath(p, ROOT) for p in paths))
    print(f"concept pages missing a template section: {len(missing_sec)}")
    for rel, want in missing_sec:
        print(f"  {rel} :: {want}")
    print(f"missing frontmatter: {len(no_fm)}")
    for rel in no_fm:
        print(f"  {rel}")
    print(f"notes under 250 words: {len(short)}")
    for rel, w in short:
        print(f"  {rel} ({w} words)")
    print("not linted as notes (excluded by design): raw*, projects*, "
          "vault/topics/Ai Engineering Lab/report/")
    return 1 if (broken or dupes or missing_sec) else 0


if __name__ == "__main__":
    sys.exit(main())
