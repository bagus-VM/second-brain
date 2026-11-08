---
title: "Vault Lint Report — 2026-06-22"
tags: [lint, vault-health, meta]
course: "General"
source_count: 0
status: current
last_updated: 2026-06-22
prerequisites: []
---

# Vault Lint Report — 22 June 2026

> Professor White. Full-scan health check. Method: programmatic walk of all 628 `.md` files; wikilink graph, frontmatter parse, open-question scan, duplication/drift check.

**Vault state:** 618 vault pages (628 `.md` total incl. structural/raw). 6 active courses, all lectures ingested.
**Exam horizon:** MMDB 21 Jul (29d) · NetSci 28 Jul (36d) · RepEng 30 Jul (38d) · SoftAnal 31 Jul (39d) · IoT 05 Aug (44d) · Microelectronics 06 Aug (45d).

---

## Health Score: B+ → A (after fixes applied 2026-06-22)

> **POST-FIX UPDATE:** All 9 issue classes resolved. See log.md [2026-06-22] FIX for details.
> Duplicate slugs: 7→0. Drafts: 74→0. Index dupes: 5→0. Broken content links: 0. YAML errors: 0.
> 18 files deleted, 4 pages created, 64 drafts promoted, 30 links redirected, 15 index entries added.

| Metric | 2026-06-16 | 2026-06-22 | Trend |
|--------|-----------|-----------|-------|
| Stale pages | some | **0** | ✅ improved |
| Empty Open Questions | 0 | **0** | ✅ held |
| Broken wikilinks (real) | ~26 | **6 targets / 5 files** | ✅ improved |
| Orphan pages | 17 | 16 (14 structural) | ✅ stable |
| Draft pages | — | **74 (12%)** | ⚠️ backlog |
| Unsourced "current" pages | ~20 | **26** | ⚠️ up |
| Duplicate drifted pages | — | **7** | ⚠️ new |
| Abandoned draft cluster | — | **14** | ⚠️ new |

**Strengths:** Zero stale pages. Zero empty Open Questions (540 pages track OQs, all substantive). Broken-link count down to a handful. Full lecture coverage across all 6 courses. Linking discipline solid.

**Weaknesses:** A 74-page draft backlog (concentrated in IoT Security and Microelectronics — the two latest-exam courses). 26 "current" pages with `source_count: 0` (verification risk). 7 concept pages exist as drifted duplicates (root + concepts/). 14 orphaned-from-index network-science drafts that duplicate current pages. One junk meta page.

---

## Findings

### 1. Duplicate drifted concept pages — 7 (HIGH)
Same slug exists in BOTH `vault/<slug>.md` AND `vault/concepts/<slug>.md`. The `concepts/` copy is consistently the richer/fuller version; the root copy is a stale smaller leftover. Obsidian resolves `[[slug]]` ambiguously — the two copies will diverge further. All 7 are drifted (different content):

- `abstract-interpretation` (root 3.8KB vs concepts 9.4KB)
- `balance-theorem` (4.7KB vs 6.3KB)
- `balanced-triads` (3.9KB vs 6.3KB)
- `c-preprocessor` (5.6KB vs 8.8KB)
- `content-based-retrieval` (3.6KB vs 7.4KB)
- `structural-balance-theory` (4.4KB vs 7.2KB)
- `weak-structural-balance` (4.0KB vs 7.4KB)

**Fix:** Delete the 7 root copies; keep `vault/concepts/` versions as canonical.

### 2. Abandoned network-science draft cluster — 14 (HIGH)
14 draft pages, none referenced in `index.md`, each duplicating a concept already covered by a *current* page. An abandoned alternate page-generation pass. Dead weight that inflates the page count and confuses the graph.

| Draft (orphaned, unsourced) | Duplicates current page |
|---|---|
| `network-science-l01-overview` | `network-intro` |
| `network-science-graph-fundamentals` | `graph-fundamentals` |
| `network-centrality-l04` | `centrality` |
| `weak-ties-and-bridges` | `weak-ties-hypothesis` / `bridges-and-local-bridges` |
| `network-community-structure-l06` | `community-structure` |
| `spectral-clustering` | `graph-partitioning-cut-spectral` |
| `network-navigation-small-worlds-l07` | `small-world-property` / `watts-strogatz-model` |
| `small-world-networks` | `small-world-property` |
| `hierarchical-navigable-small-world` | (no current equiv — keep/finish or delete) |
| `network-dynamics-l08` | `network-diffusion` |
| `sis-model` | `network-diffusion` / `sir-model-network-epidemics` |
| `sirs-model` | `sir-model-network-epidemics` |
| `scale-free-epidemic-threshold-vanishes` | `basic-reproduction-number-r0` |
| `word2vec-skip-gram` | `deepwalk` / `node2vec` |

**Fix:** Delete the 13 clear duplicates. `hierarchical-navigable-small-world` has no current equivalent — finish it or delete.

### 3. Draft backlog by course — 74 total (MEDIUM-HIGH)
| Course | Draft | Current | % draft | Exam |
|--------|-------|---------|---------|------|
| IoT Security | 37 | 59 | 38% | 05 Aug |
| Network Science | 14 (abandoned, see #2) | — | — | 28 Jul |
| Microelectronics | 14 | 52 | 21% | 06 Aug |
| Software Analyse | 7 | — | — | 31 Jul |

IoT Security is the critical risk: 38% of its pages are draft stubs, many `source_count: 0`, and its exam is 05 Aug. The index claims "7/7 lectures ✅ (~70 pages)" but the page *quality* lags the coverage claim. Microelectronics (21% draft, exam 06 Aug) is the next concern — its drafts are foundational concepts (`capacitor`, `conductor`, `electricity`, `cmos-inverter`, `band-theory`, `electron-hole`) that other pages depend on.

### 4. Unsourced "current" pages — 26 (MEDIUM)
Pages marked `status: current` but `source_count: 0`. Includes 6 Software Analyse pages created 2026-06-19 (SSA/PDG/slicing family — never got source_count bumped) and ~10 Microelectronics concept pages. Verification risk: "current" implies vetted, but no source is recorded. Either attach a source or downgrade to `draft`.

### 5. Missing prerequisite pages — 6 targets in 5 files (MEDIUM)
Vault concept pages link to pages that don't exist:

| Source file | Missing target |
|---|---|
| `confounding.md` | `experiment-vs-observation`, `manski-reflection-problem` |
| `dynamic-slicing.md` | `debugging` |
| `make-dependency-tracking.md` | `latexmk` |
| `triadic-focal-membership-closure.md` | `kossinets-watts-2006` |

**Fix:** Create stub pages (per AGENTS.md "no half-measures" — only if you'll finish them) or remove the links.

### 6. Index/file contradictions & duplicate index entries (LOW-MEDIUM)
- **Status contradiction:** `index.md` lists `[[signed-networks]]` as *current*; the file's frontmatter says `status: draft`. Reconcile.
- **Duplicate index entries (5):** `ei-index`, `triadic-focal-membership-closure`, `confounding` each listed twice (L05 + L06 Network Science); `c-preprocessor` twice (L05 + L06 RepEng); `abstract-interpretation` twice (L01 + L06 SoftAnal). Legitimate cross-lecture pages, but deduplicate to one row.

### 7. Junk / redundant files (LOW)
- `vault/concepts/wikilinks.md` — 80-line meta page documenting Obsidian's wikilink *syntax*. Not study material. Draft, unsourced, orphan, contains broken example links. **Delete.**
- `vault/study-materials-index.md` — a second study-materials index, zero inbound links, full of path-based broken links (`[[study/flashcards/...]]`, `[[vault/concepts/band-theory]]`, MOC folder links). Redundant with `index.md`. **Delete or repair.**

### 8. Broken links in course/structural files (LOW)
- `courses/iot-security/course.md` — 5 title-case lecture links (`[[Lecture 1 — Introduction to IoT Security]]` etc.) that don't resolve. Should be slug links to the actual lecture pages.
- `raw/lectures/iot_security/IoT_Security_Lectures_Extraction.md` — 53 title-case auto-extraction links (immutable raw/, noted not fixed).

### 9. Large pages — split candidates (LOW)
Only 2 concept pages are genuinely large: `java-for-software-analysis.md` (472 lines), `sign-analysis.md` (382 lines). Same as 2026-06-16. Acceptable unless they grow.

---

## Top 3 priorities (do now)

1. **Delete the 7 drifted duplicate root pages** — integrity fix, 5 minutes. Keeps `vault/concepts/` as canonical, removes ambiguity.
2. **Delete the 13 abandoned network-science draft duplicates** + decide on `hierarchical-navigable-small-world` — removes 14 pages of dead weight and de-confuses the graph.
3. **Triage the IoT Security draft backlog** — 37 draft pages, exam in 44 days. Either promote to current (finish + source) or explicitly mark as out-of-scope. Don't let "7/7 lectures ✅" mask that 38% of pages are stubs.

*Deferred:* unsourced-current cleanup (#4), missing-prereq stubs (#5), index dedup + signed-networks reconciliation (#6), junk-file deletion (#7), course.md link fixes (#8).

---

*"A lint is a diagnostic, not a verdict. The bones are strong — zero stale, zero empty open questions, every lecture covered. The disease is accumulated cruft: 74 draft stubs, 7 drifted duplicates, 14 abandoned ghosts. The vault didn't rot; it accumulated unfinished work. Cut the dead weight, finish what the exams need, and the compound effect holds."*
