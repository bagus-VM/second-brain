---
title: "Seminar on Hardware Security Solutions for the Internet of Things"
tags: [course, semester-2, seminar, hardware-security, iot]
professor: "Dr. Nikolaos Athanasios Anagnostopoulos (kick-off deck, slide 1)"
semester: "WS 2026/27"
exam_date: "04.01.2027 (blind paper) / 18.01.2027 (reviews) / 01.02.2027 (final) / 15.02.2027 (talk)"
credits: "5 ECTS"
language: "English"
source_count: 2
status: active
last_updated: 2026-11-03
prerequisites: []
---

## One-line Summary

Course 6234S with Dr. Nikolaos Athanasios Anagnostopoulos: no lectures and no exam — you write one
6-page IEEE paper (70%), review two peers' papers (10%) and present it (20%), through OpenConf, and
the deck states twice that AI-generated text is not allowed.

## Course facts

- **Course:** 6234S, Seminar on Hardware Security Solutions for the Internet of Things.
- **Supervisor:** Dr. Nikolaos Athanasios Anagnostopoulos, Faculty of Computer Science and
  Mathematics, University of Passau (also the Semester 1 `[[internet-of-things]]` lecturer).
- **Grading:** Paper 70% + Reviews 10% + Presentation 20%. **5 ECTS.**
- **Tooling:** LaTeX in Overleaf, IEEE double-column conference template.
- **Work steps:** topic selection and registration → discussion with the assigned supervisor →
  writing → blind submission → reviewer registration → review phase → final submission → talk.
- There are **no lecture slides** for this course; the only teaching input is the kick-off deck.

## Fixed dates (from the kick-off deck)

| Date | What |
|------|------|
| 04.01.2027 | First version submitted **blind** (no name, no affiliation) |
| 18.01.2027 | Review phase deadline (reviews you owe others) |
| 01.02.2027 | Final version, **non-blind** (name + affiliation back in) |
| 15.02.2027 | Final presentation, **in person, offline** |

Registration is **in person**: fill in the form, sign it, send it back. After registering you cannot
be unregistered; if you then fail to finish, you are graded **5,0**. Attending **all** colleague
presentations is mandatory.

## Paper requirements

- IEEE double-column conference template, LaTeX/Overleaf.
- **6 pages, and the 6th page must carry adequate content** — padding does not count.
- Structure the deck asks for: Title + author/affiliation (hidden while blind) · Abstract with
  keywords · Introduction · Related Work (surveys/reviews of similar work, not ordinary papers) ·
  Implementation — for the seminar this is the *State of the Art / Overview* section ·
  Discussion/Evaluation — for the seminar your own assessment of that literature · Conclusion ·
  References in IEEE BibTeX style.
- Sections may be renamed or split (e.g. "Introduction and Motivation", "Related Work and
  Background", "Conclusion and Future Work"); the own-contribution sections (Implementation,
  Discussion/Evaluation) get the most attention.
- The deck's own honesty note: novelty in a seminar paper is low, you are mostly recycling other
  people's work — what matters is finding an interesting way to evaluate it.

## Submission and review mechanics (OpenConf)

`https://openconf.hardwaresecurity.eu/openconf.php`

1. **First submission:** "Make Submission" (form → e-mail gives a submission ID), then "Upload
   File" with that ID + password. Unlimited re-uploads until the deadline; only the last counts.
   The e-mail address you enter is the one the organisers use to contact you.
2. **Reviewer registration:** "Review Cmt. Sign Up", opens after the first deadline.
3. **Reviews:** "Review Cmt. Sign In" → assigned papers → online review form, or download the PDF.
   Reviews can be reopened and amended after submission.
4. **Review structure:** restate the manuscript's main idea in two sentences (proof you read it),
   judge how well the authors presented it, then propose concrete improvements. Author-facing
   comments go in the author box; only technical remarks (plagiarism, overlength, deanonymised
   author) go to the programme committee box.
5. **Final submission:** "Edit Submission" with your submission ID → "Upload File" again.

A commented PDF may be shared via a semi-private link (Dropbox-style), never by uploading the
unpublished manuscript to a public site — reviewing unpublished work carries an explicit
confidentiality duty.

## Presentation

15 min talk + 5 min questions, **10–15 slides, not 50**. Focus on the main idea, ≤7 bullets per
slide, no reading from the slides, practise beforehand.

## Integrity rules (stated twice in the deck, treat as hard constraints)

- **"You are not allowed to use ChatGPT or anything else to automatically generate text."** This
  appears on the general-information slide *and* on the registration slide. Any prose submitted for
  grading must be the student's own writing.
- **NO PLAGIARISM.** Anything not from your own knowledge or common sense needs a citation.
  Significant plagiarism is graded **5,0**.
- **Blind review:** the first submission must not contain name or affiliation; the final one must.
  Author identity leaking into a blind submission is a technical comment routed to the programme
  committee.

## Bonus

With the supervisor's agreement, a practical implementation related to the topic adds up to
**+1,0** to the final grade; it must not interfere with the normal seminar work.

## Sources ingested

| Source | What it is |
|--------|------------|
| `raw/lectures/Seminar on Hardware Security Solutions for the Internet of Things/task/Seminar_2026-2027.pptx` | 17-slide kick-off deck: rules, dates, OpenConf and review procedure, presentation rules, bonus (extracted 2026-11-02) |
| `raw/lectures/Seminar on Hardware Security Solutions for the Internet of Things/task/Overleaf_Guide.pdf` | LaTeX/Overleaf setup walkthrough, IEEE template download steps |

Not teaching material, kept as project artifacts: `task/` template files, `template/`, and the
`paper/` folder described below.

## Project state (two locations — do not confuse them)

- **`2nd-semester/projects/Seminar/`** — the active git repo (commits `a0f6e6e`, `835d174`).
  Skeleton `main.tex` (title, abstract, keywords, six empty `\section` TODOs, `\nocite{*}`),
  compiled `main.pdf`, `references.bib` with 30 entries, six source PDFs in `resources/`, IEEE
  template pack in `template/`. Title: *Zero-Days in Your Pocket: Comparing Android and iOS Under
  Real-World Exploitation*.
- **`raw/lectures/.../paper/`** — a complete 6-page draft of the same title: `main.tex` (~4000
  words, all sections written, two tables + a pgfplots chart), 30-entry `references.bib`, compiled
  `main.pdf`, `sources/` with 17 harvested PDFs/HTML sources, and `.zcode/plans/` holding the
  section-by-section plan. This draft exists in `raw/`, which is read-only.
- **Open point:** whether the `raw/paper` text is reused, rewritten or abandoned is undecided, and
  it interacts directly with the AI-generation prohibition above. Not decided here.

## Connections

- `[[internet-of-things]]` — Semester 1 course by the same supervisor; the seminar's subject matter
  is adjacent to it.
- `[[ai-engineering-lab]]` — the other project-shaped (exam-free) course in this semester; same
  pattern of "deliverable, not written exam".

## Open Questions

- Is the Android-vs-iOS zero-day topic **registered** with the supervisor, and who the assigned
  supervisor is? The deck requires in-person topic registration before work starts; nothing in the
  ingested material records it.
- Whether 5 ECTS and the dates above are confirmed anywhere outside the kick-off deck (Stud.IP) —
  not stated in the ingested material.
- Whether the bonus practical work has been agreed with the supervisor — not stated.
- The blind submission needs author and affiliation stripped from `main.tex`; not yet done in the
  active repo.