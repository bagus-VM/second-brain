"""Generate 2nd-semester/index.md from note frontmatter.

Groups pages by course, keeps counts honest. Re-runnable.
"""
import os
import re
from collections import OrderedDict

SEM = r"C:\Users\quiescent\Documents\Vault\second-brain\2nd-semester"
OUT = os.path.join(SEM, "index.md")

COURSE_ORDER = [
    "Energy Informatics I",
    "Introduction to Deep Learning",
    "Machine Learning for Cybersecurity",
    "Scaling Database Systems",
    "Virtual Machines and Runtime Systems",
    "Advanced IT Security",
    "AI Engineering Lab (Block Seminar)",
]


def parse(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    fm = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        block = text[3:end]
        for line in block.splitlines():
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
    # first paragraph after the summary heading
    summary = ""
    m = re.search(r"## One-line Summary\s*\n+(.+?)(?:\n\n|\n##)", text, re.S)
    if m:
        summary = " ".join(m.group(1).split())
    else:
        # meta pages have no One-line Summary: fall back to the first sentence after the H1
        body = re.sub(r"^---.*?---", "", text, flags=re.S)
        m2 = re.search(r"^#\s+.*?\n+(.+?)(?:\n\n|\n#)", body, re.S | re.M)
        if m2:
            summary = " ".join(m2.group(1).split())
    return fm, summary


def collect(subdir):
    rows = []
    d = os.path.join(SEM, subdir)
    if not os.path.isdir(d):
        return rows
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(d, fn)
        fm, summary = parse(path)
        rows.append(
            {
                "slug": fn[:-3],
                "title": fm.get("title", fn[:-3]),
                "course": fm.get("course", "—"),
                "status": fm.get("status", "—"),
                "sources": fm.get("source_count", "—"),
                "summary": summary,
            }
        )
    return rows


concepts = collect(os.path.join("vault", "concepts"))
topics = collect(os.path.join("vault", "topics"))
courses = collect("courses")
courses = [c for c in courses if c["slug"] != "Courses"]

by_course = OrderedDict((c, []) for c in COURSE_ORDER)
for row in concepts:
    by_course.setdefault(row["course"], []).append(row)

lines = []
lines.append("---")
lines.append('title: "Semester 2 — Master Index"')
lines.append("tags: [meta, index, semester-2]")
lines.append("status: current")
lines.append("last_updated: 2026-10-20")
lines.append("---")
lines.append("")
lines.append("# Semester 2 — Master Index")
lines.append("")
lines.append("> Maintained by Professor White. Generated from note frontmatter; re-run `vault/tools/generate_index.py` after an ingest.")
lines.append("")
lines.append(f"**Courses:** {len(courses)} registered · **Concept pages:** {len(concepts)} · **Topic pages:** {len(topics)}")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Courses")
lines.append("")
lines.append("| Course | Professor | Exam | Page |")
lines.append("|--------|-----------|------|------|")
exam = {
    "Energy Informatics I": "17.02.2027 / 24.03.2027",
    "Introduction to Deep Learning": "TBD",
    "Machine Learning for Cybersecurity": "portfolio",
    "Scaling Database Systems": "TBD",
    "Virtual Machines and Runtime Systems": "11.02.2027 / 01.04.2027",
    "Advanced IT Security": "05.04.2027",
    "AI Engineering Lab (Block Seminar)": "report-based",
}
prof = {
    "Energy Informatics I": "de Meer",
    "Introduction to Deep Learning": "Lemmerich",
    "Machine Learning for Cybersecurity": "Reiser",
    "Scaling Database Systems": "Scherzinger",
    "Virtual Machines and Runtime Systems": "Größlinger",
    "Advanced IT Security": "Posegga",
    "AI Engineering Lab (Block Seminar)": "—",
}
for c in courses:
    t = c["title"]
    lines.append(f"| [[{c['slug']}]] | {prof.get(t, '—')} | {exam.get(t, '—')} | {c['status']} |")
lines.append("")
lines.append("## Concept Pages by Course")
lines.append("")
for course, rows in by_course.items():
    if not rows:
        continue
    lines.append(f"### {course}")
    lines.append("")
    lines.append("| Page | Summary | Sources | Status |")
    lines.append("|------|---------|---------|--------|")
    for r in rows:
        s = r["summary"].replace("|", "\\|")
        if len(s) > 140:
            s = s[:137].rstrip() + "…"
        lines.append(f"| [[{r['slug']}]] | {s} | {r['sources']} | {r['status']} |")
    lines.append("")
if topics:
    lines.append("## Topic Pages")
    lines.append("")
    lines.append("| Page | Summary | Sources | Status |")
    lines.append("|------|---------|---------|--------|")
    for r in topics:
        s = r["summary"].replace("|", "\\|")
        if len(s) > 140:
            s = s[:137].rstrip() + "…"
        lines.append(f"| [[{r['slug']}]] | {s} | {r['sources']} | {r['status']} |")
    lines.append("")
lines.append("## Gaps")
lines.append("")
lines.append("- Bitcoin and Cryptocurrencies Technologies: `raw/` folder empty, no page.")
lines.append("- Dropped on 2026-10-20: Hardware-Oriented Security and Reverse- and Reengineering — all pages and raw sources removed.")
lines.append("- Advanced IT Security: lecture 0 (Basics) is ingested; lectures 1-6 have no slides in `raw/` yet.")
lines.append("- Scaling Database Systems: new course. Only organisational sheets in `raw/` - `raw/lectures/Scaling Database Systems/Vorlesung/` is empty, so no lecture slides have been ingested and the technical content is not yet in the vault.")
lines.append("- Exam formats/dates marked TBD were not in the source material and are not guessed.")
lines.append("")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"wrote {OUT}: {len(concepts)} concepts, {len(topics)} topics, {len(courses)} courses")
