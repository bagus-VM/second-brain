---
title: "Vault Lint Report — 2026-07-20"
tags: [meta, lint, vault-health]
status: current
last_updated: 2026-07-20
---

## Vault Lint Report — 2026-07-20

**Scan scope:** 718 .md files (597 vault, 74 study, 47 other). Excludes raw/, .git/, RepEng submodule.

---

### 1. INDEX COMPLETENESS — 323 pages missing from index.md (CRITICAL)

The biggest finding. 323 pages in vault/ and study/ are not linked from index.md. These are invisible to any index-first search.

**Breakdown by course:**
| Course | Missing pages | Notes |
|--------|--------------|-------|
| IoT Security | ~80 | All lecture topics (L01-L09) + ~65 concept pages |
| Microelectronics | ~55 | All lecture topics (L01-L09) except L09 + ~45 concept pages |
| Software Analyse | ~45 | All lecture topics (L01-L11) + ~30 concept pages |
| Reproducibility Engineering | ~20 | Practice sheets 1-9 + flashcards 1-7 |
| Network Science | ~8 | Lecture topics L01-L08 |
| Cross-cutting / other | ~115 | Exam prep, flashcards, misc |

**Root cause:** The index was last rebuilt on 2026-07-02 (log entry claims 254 entries added). But pages created or promoted after that date — especially the bulk Microelectronics, IoT, and SA concept pages from the 06-22 FIX — were never added. The index claims 657 pages but only links ~335.

**Impact:** HIGH. A student using index.md as their navigation hub cannot find 46% of the vault.

---

### 2. BROKEN WIKILINKS — 3 missing concept pages (MODERATE)

| Missing target | Referenced by | Course |
|---------------|--------------|--------|
| `[[negative-feedback]]` | opamp-integrator, opamp-differentiator, weighted-summer, voltage-follower | Microelectronics |
| `[[opamp-basics]]` | microelectronics-lecture-9 | Microelectronics |
| `[[impedance-matching]]` | voltage-follower | Microelectronics |

All 3 are Microelectronics concept pages that were never created. The student needs these for exam prep (exam Aug 6).

---

### 3. ESCAPED BACKSLASH WIKILINKS — 10 in active content (MODERATE)

These use `\|` inside wikilinks in a way that Obsidian doesn't resolve:

| File | Broken links |
|------|-------------|
| index.md:325 | `[[graph-laplacian\|graph Laplacian]]` |
| index.md:347 | `[[closeness-centrality\|closeness centrality]]` |
| vault/concepts/distributive-framework.md | reaching-definitions, available-expressions, live-variable-analysis, very-busy-expressions |
| vault/concepts/graph-representations.md | breadth-first-search, depth-first-search, sparse-dense-and-random-graphs |
| vault/concepts/pixel-formats-and-bit-depth.md | color-lookup-table |

**Fix:** Replace `\|` with `|` in wikilink alias syntax. Obsidian uses `[[slug|alias]]` not `[[slug\|alias]]`.

---

### 4. UNSOURCED CURRENT PAGES — 18 pages (LOW)

Pages marked `status: current` with `source_count: 0`:

vault/concepts/: actuators, authentication, digital-circuit-design, digital-signatures, diode-applications, doping-and-extrinsic-semiconductors, iot-security-overview, machine-learning-basics, mos-transistors, non-repudiation, p-n-junction-overview, pagerank-algorithm, semiconductor-physics, sensors, six-degrees-of-separation, visitor-pattern, vlsi-design, Vault.md

Most are from bulk promotions on 2026-06-22. Content is substantive (not stubs) but hasn't been verified against a source.

---

### 5. DRAFT PAGE — 1 page (LOW)

- `vault/concepts/Vault.md` — status: draft. Appears to be a meta/overview page, not a study concept.

---

### 6. ORPHAN PAGES — 61 total (acceptable)

**Structural/MOC files (28):** AGENTS.md, SOUL.md, Courses.md, Projects.md, etc. — expected.

**Historical lint reports (3):** vault-lint-report-2026-06-{16,22}, 2026-07-08 — acceptable.

**Study materials not linked from index (30):** These overlap with finding #1. Once added to index, they're no longer orphans.

**True orphans requiring attention:** 0.

---

### 7. STALE PAGES — 0 ✅

### 8. EMPTY OPEN QUESTIONS — 0 ✅

### 9. DUPLICATE SLUGS — 0 ✅

### 10. CONTRADICTION FLAGS — 0 detected

---

## Top 3 Actions (priority order)

1. **REBUILD INDEX.md** — Add 323 missing entries. This is the single highest-impact fix. Takes ~30 min with a script.

2. **FIX 10 ESCAPED BACKSLASH WIKILINKS** — Replace `\|` with `|` in 5 files. Takes 5 min.

3. **CREATE 3 MISSING MICROELECTRONICS PAGES** — `negative-feedback`, `opamp-basics`, `impedance-matching`. Exam is Aug 6. Takes 15 min.

---

## Vault Health Score: B+

**Strengths:**
- 0 stale pages, 0 empty OQs, 0 duplicate slugs
- All 6 courses have complete lecture coverage
- Content quality is high — pages are substantive, well-structured
- Practice sheets and flashcards cover all exercises

**Weaknesses:**
- Index is 46% incomplete (structural debt from bulk page creation)
- 3 missing Microelectronics concept pages
- 10 broken wikilinks from escaped backslashes
- 18 unsourced current pages (verification risk)

*"The vault has 718 pages of real content and a 335-entry index. That's like having a library with no catalog. Fix the index first — everything else is secondary."*
