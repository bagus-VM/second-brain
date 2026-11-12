"""Generate 2nd-semester/index.md from note frontmatter.

Groups pages by course, keeps counts honest. Re-runnable.
"""
import os
import re
from collections import OrderedDict

SEM = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(SEM, "index.md")

COURSE_ORDER = [
    "Search-Based Software Engineering",
    "Introduction to Deep Learning",
    "Machine Learning for Cybersecurity",
    "Dependable Distributed Systems",
    "Virtual Machines and Runtime Systems",
    "Advanced IT Security",
    "Reverse- and Reengineering",
    "Mining Software Repositories",
    "AI Engineering Lab (Block Seminar)",
    "Seminar on Hardware Security Solutions for the Internet of Things",
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
lines.append("last_updated: 2026-11-12")
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
    "Introduction to Deep Learning": "TBD",
    "Machine Learning for Cybersecurity": "portfolio",
    "Dependable Distributed Systems": "TBD",
    "Virtual Machines and Runtime Systems": "11.02.2027 / 01.04.2027",
    "Advanced IT Security": "05.04.2027",
    "Reverse- and Reengineering": "two dates via Campus Portal (90 points / 90 min)",
    "Mining Software Repositories": "10.02.2027 / 22.03.2027 (preliminary)",
    "Search-Based Software Engineering": "written or oral, depends on participants; registration closed 03.11.2026",
    "AI Engineering Lab (Block Seminar)": "report-based",
    "Seminar on Hardware Security Solutions for the Internet of Things": "04.01.2027 paper / 15.02.2027 talk",
}
prof = {
    "Introduction to Deep Learning": "Lemmerich",
    "Machine Learning for Cybersecurity": "Reiser",
    "Dependable Distributed Systems": "Reiser",
    "Virtual Machines and Runtime Systems": "Größlinger",
    "Advanced IT Security": "Posegga",
    "Reverse- and Reengineering": "Hammer",
    "Mining Software Repositories": "Herbold",
    "AI Engineering Lab (Block Seminar)": "—",
    "Seminar on Hardware Security Solutions for the Internet of Things": "Anagnostopoulos",
    "Search-Based Software Engineering": "Fraser",
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
lines.append("- Search-Based Software Engineering (new registration, first ingested 2026-11-07, replacing Energy Informatics 1): organisation deck + lecture 1 (introduction, search spaces and fitness landscapes), lecture 2 (hill climbing, tabu search, simulated annealing, statistical evaluation) and the two Jupyter lab notebooks; lecture 3 is the evolutionary-algorithms deck, its Part 1 stopping at the history of evolutionary computation. Registration closed 2026-11-03 and is binding. Four Java assignments (Artemis, individual work) and a written-or-oral exam are the assessment.")
lines.append("- Dropped on 2026-11-07: Energy Informatics 1 — course page, 6 concept pages, 1 lecture page, 1 tutorial page and the 4 raw PDFs removed (raw was git-tracked, so recoverable).")
lines.append("- Introduction to Deep Learning: lectures 1-3 and exercise sets 1-3 ingested; lecture 3 (single-layer networks) arrived 2026-11-07.")
lines.append("- Dropped on 2026-10-20: Hardware-Oriented Security — all pages and raw sources removed.")
lines.append("- Reverse- and Reengineering was dropped on 2026-10-20 and has since been re-registered; lectures 1-5 and homework 1-5 are ingested (lecture 5 and homework 5 arrived 2026-11-12). The Term 2 exam timeframe is printed as '22.03.-09.04.2025' and is flagged as a typo on the course page.")
lines.append("- Mining Software Repositories (new registration, ingested 2026-10-22): 9 lecture decks and 5 exercise sheets (exercise 5 arrived 2026-11-12 and is solved; the student overruled the sheets' no-AI instruction on 2026-11-12 because they are ungraded).")
lines.append("- Dropped on 2026-10-21: Scaling Database Systems — all pages and raw sources removed.")
lines.append("- Advanced IT Security: lectures 0, 0b, 1-3 and exercise sheets 0-3 are ingested. The 2026-11-10 continuation covers security games, symmetric ciphers and the one-time pad; public-key cryptography, signatures, key establishment and later agenda topics remain absent.")
lines.append("- Virtual Machines and Runtime Systems: lectures 0-3, the `s02` example programs, and exercise sheets 1-3 are ingested. Lecture 3 introduces C abstract-machine semantics and the Prolog/WAM execution model.")
lines.append("- Dependable Distributed Systems: lectures 1-5 and exercises 1-5 ingested; official exercise-3 solutions cross-checked (their 3.3(a) arithmetic is wrong: the mean is 04:00, not 05:00). The semester plan is preliminary, so topics 6-12 have no slides in `raw/` yet; lecture 5 introduces broadcast and consensus but the separately announced consensus/failure-detectors topic is still forthcoming.")
lines.append("- The five Mining Software Repositories exercise sheets carry an instruction from their owner against AI assistance; the student overruled it for this course on 2026-11-12 (ungraded), so exercise 5 is solved and 1-4 remain task notes.")
lines.append("- Seminar on Hardware Security Solutions for the Internet of Things (ingested 2026-11-02): no lecture slides exist, only the kick-off deck and Overleaf guide. The deck forbids ChatGPT or any other automatic text generation, twice, and grades significant plagiarism 5,0. Whether the complete draft in `raw/.../paper/` is reused is undecided; the active repo is `projects/Seminar/` (skeleton only).")
lines.append("- Exam formats/dates marked TBD were not in the source material and are not guessed.")
lines.append("")

with open(OUT, "w", encoding="utf-8", newline="\r\n") as f:
    f.write("\n".join(lines))
print(f"wrote {OUT}: {len(concepts)} concepts, {len(topics)} topics, {len(courses)} courses")
