---
title: "Vault Lint Report — 2026-06-16"
tags: [lint, vault-health, semester-1]
course: "General"
status: current
last_updated: 2026-06-16
---

# Vault Health Check — 2026-06-16

## Summary

| Metric | Count | Severity |
|--------|-------|----------|
| Total pages | 590 | — |
| Broken wikilinks | 81 | Medium (see categorization below) |
| Orphan pages | 48 | Low (mostly structural) |
| Large pages (>200 lines) | 12 | Low |
| Unsourced pages | 89 | Medium |
| Empty Open Questions | 0 | ✓ Clean |
| Log size | 531 lines | Medium (needs rotation) |

---

## 1. Broken Wikilinks (81 total)

### False Positives / Meta-Links (≈25)
These are wikilinks used as **examples** in documentation pages (`wikilinks.md`, `AGENTS.md`). They're not real broken links — they're illustrative.

**Examples:**
- `[[gradient-descent]]`, `[[backpropagation]]`, `[[note-name]]`, `[[My-Note]]`, `[[X]]`, `[[link]]`, `[[citations]]`, `[[updated]]`, `[[wikilink]]`, `[[bracket]]`, `[[gd]]`, `[[adam-optimizer]]`, `[[loss-function]]`, `[[neural-networks]]`, `[[optimization-algorithm]]`, `[[partial-derivatives]]`, `[[multivariable-calculus]]`, `[[stochastic-gradient-descent]]`, `[[my-note]]`

**Action:** None. These are intentional examples.

### Path-Based Links (≈30)
These use full paths like `[[study/flashcards/mmdb-ex01-flashcards]]` or `[[vault/concepts/band-theory]]`. The lint script only checks slugs (filenames without paths), so these appear broken but aren't — they're just using a different link format.

**Source:** Mostly `vault/study-materials-index.md`

**Action:** None. Obsidian resolves path-based links correctly.

### Real Broken Links (≈26)
These are genuine missing pages:

**High Priority (referenced from multiple files):**
- `[[electron hole]]` and `[[electron holes]]` — space in name, should be `[[electron-hole]]`
  - Referenced from: `valence-band.md`, `doping.md`, `p-type-semiconductor.md`, `intrinsic-semiconductor.md`
  - **Fix:** Update links to use hyphen: `[[electron-hole]]`

**Medium Priority (referenced from 1 file):**
- `[[experiment-vs-observation]]` — missing page (referenced from `confounding.md`)
- `[[kossinets-watts-2006]]` — missing citation page (referenced from `triadic-focal-membership-closure.md`)
- `[[latexmk]]` — missing page (referenced from `make-dependency-tracking.md`)
- `[[manski-reflection-problem]]` — missing page (referenced from `confounding.md`)
- `[[reproducibility-engineering-lecture-7]]` and `[[reproducibility-engineering-lecture-8]]` — missing lecture pages (referenced from `reproducibility-engineering-sheet-5.md`)

**Low Priority (course files using full titles):**
- IoT Security lecture links in `courses/iot-security/course.md` use full titles like `[[Lecture 1 — Introduction to IoT Security]]` instead of slugs
- **Fix:** Update to use slugs: `[[iot-security-l01]]`, etc.

**Image References (not real broken links):**
- `[[Pasted image 20260609110111.png]]`, `[[Pasted image 20260610105308.png]]` — these are image embeds, not wikilinks

**Action:** Fix `[[electron hole]]` → `[[electron-hole]]` (4 files). Create missing pages or remove links for the others.

---

## 2. Orphan Pages (48 total)

### Structural Files (≈15)
These aren't meant to be linked — they're structural or meta files:
- `AGENTS.md`, `log.md`, `index.md` (implied)
- Folder MOCs: `Algorithms.md`, `Concepts.md`, `Connections.md`, `Courses.md`, `Exams.md`, `Flashcards.md`, `Practice Problems.md`, `Projects.md`, `Study Materials.md`, `Topics.md`, `Vault.md`
- `SOUL.md` (if it exists)

**Action:** None. These are structural.

### Study Materials (≈28)
Flashcards and practice files that aren't linked from anywhere:
- `mmdb-ex01-flashcards.md` through `mmdb-ex07-flashcards.md`
- `network-science-e02.md` through `network-science-e06.md` (and flashcards)
- `reproducibility-engineering-sheet-1.md` through `sheet-6.md` (and flashcards)

**Action:** These should be linked from:
1. `index.md` (under each course's "Practice" or "Flashcards" section)
2. Course pages (e.g., `courses/mmdb.md`)
3. `vault/study-materials-index.md` (already has some, but using path-based links)

**Priority:** Medium. These are high-value study materials that should be discoverable.

### Project Files (≈5)
- `SOFTWARE_ANALYSE_PROJECTS.md`, `prompt.md`, `initial prompt.md`, `course.md`, `prompt.md`

**Action:** None. These are project-specific files, not meant to be linked from the vault.

---

## 3. Large Pages (>200 lines, 12 total)

| Lines | Page | Action |
|-------|------|--------|
| 472 | `vault/concepts/java-for-software-analysis.md` | Split into sub-pages (Maven, JavaParser, ASM, WEKA, picocli) |
| 402 | `projects/software-analyse/SOFTWARE_ANALYSE_PROJECTS.md` | Already has dedicated vault pages; this is a project overview, acceptable |
| 385 | `study/practice/network-science-e02.md` | Acceptable (exercise sheet with solutions) |
| 382 | `vault/concepts/sign-analysis.md` | Split into sub-pages (lattice, transfer functions, inter-procedural) |
| 346 | `projects/software-analyse/ss26sareadability-practice-putra01/LLM/prompt.md` | Project file, acceptable |
| 296 | `study/exams/software-analyse-codebase-defense.md` | Acceptable (exam prep) |
| 265 | `vault/topics/iot-lecture-6.md` | Acceptable |
| 249 | `vault/concepts/readability-classifier.md` | Acceptable |
| 237 | `vault/topics/iot-lecture-3.md` | Acceptable |
| 222 | `study/practice/mmdb-ex07.md` | Acceptable |
| 219 | `study/exams/network-science-exercise-prep.md` | Acceptable |
| 209 | `vault/topics/iot-lecture-5.md` | Acceptable |

**Priority:** Low. Only `java-for-software-analysis.md` and `sign-analysis.md` are candidates for splitting.

---

## 4. Unsourced Pages (89 total)

Pages with `source_count: 0`. Many are legitimate:
- Meta pages: `Vault.md`, `study-materials-index.md`
- Exam prep: `software-analyse-codebase-defense.md`, `network-science-exercise-prep.md`, `mmdb-exam-prediction.md`
- Overview pages: `software-analyse-projects-overview.md`

**Concept pages that should have sources (≈20):**
- `iot-communication-protocols.md`, `iot-data-lifecycle.md`, `iot-device-fundamentals.md`, `iot-network-architecture.md`
- `signed-networks.md`, `word2vec-skip-gram.md`, `spectral-clustering.md`, `network-science-graph-fundamentals.md`
- And 11 more

**Action:** These should either:
1. Be linked to a raw source (lecture, paper, textbook)
2. Have `source_count` bumped if they were created from a source
3. Be marked as `status: draft` if they're incomplete

**Priority:** Medium. Unsourced concept pages are risky — they might contain errors that can't be verified.

---

## 5. Log Rotation

**Current size:** 531 lines (exceeds 500-line threshold)

**Action:** Rotate log:
```bash
mv log.md log-2026.md
# Start fresh log.md with header
```

**Priority:** Medium. The log is getting large and will slow down orientation reads.

---

## 6. Top 3 Actions (Priority Order)

### 1. Fix `[[electron hole]]` links (High Priority)
**Files:** `valence-band.md`, `doping.md`, `p-type-semiconductor.md`, `intrinsic-semiconductor.md`
**Fix:** Replace `[[electron hole]]` and `[[electron holes]]` with `[[electron-hole]]`
**Time:** 2 minutes

### 2. Link study materials from index (Medium Priority)
**Files:** 28 orphan flashcards/practice files
**Fix:** Add to `index.md` under each course's "Practice" and "Flashcards" sections
**Time:** 15 minutes

### 3. Rotate log (Medium Priority)
**Fix:** `mv log.md log-2026.md`, create fresh `log.md`
**Time:** 1 minute

---

## 7. Vault Health Score

**Overall:** **B+** (Good)

**Strengths:**
- No empty Open Questions sections (good tracking discipline)
- Most pages are well-linked (only 48 orphans out of 590 pages)
- Large pages are mostly acceptable (exercise sheets, exam prep)

**Weaknesses:**
- 89 unsourced pages (15% of vault) — verification risk
- Log needs rotation
- Some broken links in Microelectronics course (electron hole)

**Recommendation:** Focus on linking study materials and fixing the electron-hole links. The unsourced pages can be addressed incrementally as you re-ingest sources.

---

## Related

- [[index]] — Master catalog
- [[log]] — Session log
