#!/usr/bin/env python3
"""SZZ on the exercise-5 appendix.

Compares the line-level answer (what SZZ is defined to do) with the file-level
substitute the sheet permits, and shows what a naive "fix" keyword detector adds.

Run: python szz-exercise-05.py
"""

import re
from collections import Counter

HISTORY = [
    {
        "sha": "160f0625", "date": "01.01.2023", "author": "lukas",
        "msg": "Initial commit for Project0815",
        "lines": ["import version", "VERSION = version(0.0001)"],
    },
    {
        "sha": "24f914fd", "date": "02.01.2023", "author": "lukas",
        "msg": "ISSUE-0001: add option to perform multiplication",
        "lines": ["import version", "import math", "VERSION = version(0.0001)",
                  "def multiply(a, b):", "    return math.divide(a, b)"],
    },
    {
        "sha": "3f5b0912", "date": "05.01.2023", "author": "alex",
        "msg": "ISSUE-0003: Change version to fix value 0.0002",
        "lines": ["import math", "import version", "VERSION = version(0.0002)",
                  "def multiply(a, b):", "    return math.divide(a, b)"],
    },
    {
        "sha": "42d921a2", "date": "06.01.2023", "author": "lukas",
        "msg": "Fixes ISSUE-0002: replace division by multiplication",
        # the sheet's context line prints VERSION 0.0001; commit 3 set 0.0002 and
        # no diff line changes it, so 0.0002 is used and the defect is reported.
        "lines": ["import version", "VERSION = version(0.0002)",
                  "def multiply(a, b):", "    return a * b"],
    },
    {
        "sha": "56682e28", "date": "08.01.2023", "author": "lukas",
        "msg": "ISSUE-0004: bump to 1.0 for major release",
        "lines": ["import version", "VERSION = version(1.0)",
                  "def multiply(a, b):", "    return a * b"],
    },
]

ISSUES = {
    "ISSUE-0001": ("add option to perform multiplication", "feature"),
    "ISSUE-0002": ("multiplication actually performs division", "bug"),
    "ISSUE-0003": ("increase prototype version", "feature"),
    "ISSUE-0004": ("bump version to 1.0 for bug-free release", "feature"),
    "ISSUE-0005": ("add option to perform division", "feature"),
}


def build_states(history):
    """Line -> introducing commit, carrying origins through every commit."""
    states, prev_pairs = [], []
    for commit in history:
        pool = Counter(prev_pairs)
        pairs = []
        for line in commit["lines"]:
            origin = None
            for pair in prev_pairs:
                if pair[0] == line and pool[pair] > 0:
                    _, origin = pair
                    pool[pair] -= 1
                    break
            pairs.append((line, origin or commit["sha"]))
        states.append(pairs)
        prev_pairs = pairs
    return states


def multiset_diff(prev_lines, cur_lines):
    pc, cc = Counter(prev_lines), Counter(cur_lines)
    return list((pc - cc).elements()), list((cc - pc).elements())


def refs(msg):
    return re.findall(r"ISSUE-\d{4}", msg)


def issue_linked_fixes(history):
    return [c["sha"] for c in history
            if any(ISSUES.get(r, ("", ""))[1] == "bug" for r in refs(c["msg"]))]


def keyword_fixes(history):
    return [c["sha"] for c in history if re.search(r"\bfix", c["msg"], re.I)]


def index_of(history, sha):
    return next(i for i, c in enumerate(history) if c["sha"] == sha)


def line_level_szz(history, states, fix_shas):
    rows = []
    for fix in fix_shas:
        i = index_of(history, fix)
        if i == 0:
            continue
        prev_lines = [line for line, _ in states[i - 1]]
        cur_lines = [line for line, _ in states[i]]
        removed, _ = multiset_diff(prev_lines, cur_lines)
        origins = dict(states[i - 1])
        for line in removed:
            rows.append((fix, line, origins.get(line)))
    return rows


def file_level_szz(history, fix_shas):
    return [(fix, history[index_of(history, fix) - 1]["sha"]) for fix in fix_shas]


def main():
    states = build_states(HISTORY)
    fixes = issue_linked_fixes(HISTORY)

    print("== issue-linked bug fixes ==")
    for sha in fixes:
        print(f"  {sha}  {next(c['msg'] for c in HISTORY if c['sha'] == sha)}")

    print("\n== line-level SZZ (the definition) ==")
    line_rows = line_level_szz(HISTORY, states, fixes)
    for fix, line, origin in line_rows:
        print(f"  fix {fix} removes {line!r} -> introduced by {origin}")

    print("\n== file-level SZZ (this sheet's substitute) ==")
    file_rows = file_level_szz(HISTORY, fixes)
    for fix, origin in file_rows:
        print(f"  fix {fix} -> last commit touching the file: {origin}")

    print("\n== naive 'fix' keyword detector ==")
    kw = keyword_fixes(HISTORY)
    for sha in kw:
        print(f"  {sha}  {next(c['msg'] for c in HISTORY if c['sha'] == sha)}")
    kw_rows = line_level_szz(HISTORY, states, kw)
    print("  line-level candidates:",
          sorted({origin for _, _, origin in kw_rows if origin}))

    print("\n== validation table ==")
    print("candidate,fix,issue,changed_line,label")
    for _, line, origin in line_rows:
        print(f'{origin},{fixes[0]},ISSUE-0002,"{line.strip()}",true_positive')
    for _, origin in file_rows:
        print(f"{origin},{fixes[0]},ISSUE-0002,file-level,false_positive")

    assert fixes == ["42d921a2"], fixes
    assert line_rows[0][2] == "24f914fd", line_rows
    assert file_rows[0][1] == "3f5b0912", file_rows
    assert line_rows[0][2] != file_rows[0][1]
    assert set(kw) == {"3f5b0912", "42d921a2"}, kw
    print("\nself-checks: PASS")
    print("line-level = 24f914fd; file-level = 3f5b0912; the approximation blames the wrong commit")


if __name__ == "__main__":
    main()