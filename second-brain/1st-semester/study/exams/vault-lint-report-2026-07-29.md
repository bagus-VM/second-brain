---
title: "Vault Lint Report — 2026-07-29"
tags: [vault-health, lint, semester-1]
status: current
last_updated: 2026-07-29
---

# Vault Lint Report — 2026-07-29

> Full vault scan. 769 .md files across 6 courses.

---

## Summary

| Metric | Value |
|--------|-------|
| Total .md files (excl raw/) | 769 |
| Files with frontmatter | 704 (91.4%) |
| Files without frontmatter | 65 (node_modules/.venv/project files) |
| Unique slugs | 723 |
| Status: current | 697 |
| Status: stale | 0 |
| Status: draft | 0 |
| Broken wikilinks | 0 |
| Orphan pages (no inbound links) | 5 (all Obsidian placeholder files) |
| Vault pages not in index.md | 5 (same placeholders) |
| Unsourced pages (source_count: 0) | 17 |
| Pages last_updated >90 days ago | 0 |
| Open Questions (non-trivial) | ~1657 (by design — AGENTS.md: "The open question is sacred") |
| Duplicate slugs | 4 (all from node_modules/.venv — not real content) |

**Overall health: EXCELLENT.** Zero broken wikilinks, zero stale pages, zero drafts, zero old pages. The vault is exam-ready.

---

## Course Distribution

| Course | Pages |
|--------|-------|
| Network Science | 157 |
| Multimedia Databases | 122 |
| Software Analyse | 115 |
| IoT Security | 104 |
| Reproducibility Engineering | 99 |
| Introduction to Microelectronics | 71 |
| Microelectronics (legacy tag) | 10 |
| General / Other | 3 |

---

## P0 — Broken Wikilinks: NONE

Initial scan flagged 3 links in `vault/concepts/community-detection.md` as broken:
- `[[girvan-newman-algorithm\|Girvan–Newman]]`
- `[[louvain-algorithm\|Louvain]]`
- `[[leiden-algorithm\|Leiden]]`

These are FALSE POSITIVES. The `\|` is standard Obsidian escaped-pipe syntax for wikilink aliases inside table cells. All 3 target pages exist on disk. No fix needed.

---

## P1 — Unsourced Pages (17 pages with source_count: 0)

These vault concept pages have `source_count: 0` in their frontmatter, meaning no raw source has been formally linked. Most are early-built pages from initial vault construction. The pages themselves are fine — they lack provenance tracking only.

**IoT Security (6 pages):**
- `vault/concepts/actuators.md`
- `vault/concepts/authentication.md`
- `vault/concepts/digital-signatures.md`
- `vault/concepts/iot-security-overview.md`
- `vault/concepts/non-repudiation.md`
- `vault/concepts/sensors.md`

**Microelectronics (7 pages):**
- `vault/concepts/digital-circuit-design.md`
- `vault/concepts/diode-applications.md`
- `vault/concepts/doping-and-extrinsic-semiconductors.md`
- `vault/concepts/mos-transistors.md`
- `vault/concepts/p-n-junction-overview.md`
- `vault/concepts/semiconductor-physics.md`
- `vault/concepts/vlsi-design.md`

**Network Science (2 pages):**
- `vault/concepts/six-degrees-of-separation.md`
- `vault/concepts/pagerank-algorithm.md`

**Software Analyse (1 page):**
- `vault/concepts/visitor-pattern.md`

**Machine Learning (1 page):**
- `vault/concepts/machine-learning-basics.md`

**Recommendation:** Low priority. After exams, bump source_count to 1 and add a `sources:` field pointing to the relevant lecture.

---

## P2 — Orphan Pages / Not in Index (5 pages, all placeholder files)

These are Obsidian auto-generated folder placeholder files, not real content:

| File | Status |
|------|--------|
| `vault/algorithms/Algorithms.md` | Obsidian folder placeholder |
| `vault/concepts/Concepts.md` | Obsidian folder placeholder |
| `vault/concepts/Vault.md` | Obsidian folder placeholder |
| `vault/connections/Connections.md` | Obsidian folder placeholder |
| `vault/topics/Topics.md` | Obsidian folder placeholder |

**Recommendation:** Safe to delete. They serve no purpose in the vault structure.

---

## P3 — Tag Taxonomy Health

298 unique tags across the vault. No SCHEMA.md taxonomy file exists (the vault uses AGENTS.md conventions instead, which is fine for a study vault).

Potential tag sprawl (synonyms/duplicates):
- `build` vs `builds` vs `build-system` vs `build-systems` vs `build-tools` — 5 variants
- `compiler` vs `compilers` — 2 variants
- `databases` vs `database` vs `database-architecture` — 3 variants
- `cheat-sheet` vs `cheatsheet` — 2 variants
- `iot-2.0` vs `iot-2-0` — 2 variants of same concept
- `microelectronics` vs `introduction-to-microelectronics` — 2 variants

**Recommendation:** Low priority. Tag consolidation after exams. Does not affect exam readiness.

---

## Open Questions Inventory

~1657 open questions across all vault and topic pages. This is BY DESIGN — the vault tracks what the student hasn't fully understood yet (AGENTS.md: "The open question is sacred"). These are NOT lint issues.

**Exam-relevant open questions (from exam prep pages):**
- `software-analyse-codebase-defense.md`: "Verify IASTORE stack layout — does the code check the right stack position?"
- `software-analyse-exam-prep.md`: "Verify stack calculation coverage in java-for-software-analysis page"
- `software-analyse-exam-prep.md`: "Verify method call instrumentation coverage in dynamic-analysis page"
- `iot-security-exam-format.md`: "Which specific security solutions are in scope?"
- `iot-security-exam-format.md`: "Are there past exam papers available for practice?"

---

## Coverage Gaps

**FOUND AND FIXED:** `vault/topics/reproducibility-engineering-lecture-11.md` was missing. RepEng had lectures 1-10 in vault/topics/ but not 11 (FAIR Principles & Legal Aspects). The raw source (IC 11 PDF) was in `raw/lectures/reproducibility_engineering/Vorlesung/` and the exercise was already processed at `study/practice/repeng-prof-ic11.md`.

**Fixed:** Created `vault/topics/reproducibility-engineering-lecture-11.md` with full vault template.

**Lesson:** The lint coverage check was too coarse. Future lints should compare raw/lectures file counts against vault/topics lecture page counts per course.

All other courses: complete lecture coverage confirmed.

---

## Comparison to Previous Lints

| Metric | 2026-06-16 | 2026-07-20 | 2026-07-29 | Delta (last) |
|--------|-----------|-----------|-----------|-------------|
| Total pages | ~590 | ~740 | 769 | +29 |
| Broken wikilinks | 81 | 12 | 0 | -12 |
| Orphan pages | 48 | 5 | 5 | 0 |
| Unsourced pages | 89 | 17 | 17 | 0 |
| Stale pages | ? | 0 | 0 | 0 |

Vault has been stable and clean since 2026-07-20. Growth of +29 pages from the last lint, mostly from exam prep materials (cheatsheets, mock exams, condensed prep). All broken wikilinks from previous lints have been resolved.

---

## Top 3 Actions

1. **NOTHING URGENT.** The vault is exam-ready. Zero broken links, zero stale pages, zero drafts.
2. **DELETE (low priority):** Remove the 5 Obsidian placeholder files after exams.
3. **SOURCE (after exams):** Add source_count to the 17 unsourced pages. Do not touch during exam prep.

---

## Connections

- [[vault-lint-report-2026-07-20]] — Previous lint report
- [[vault-lint-report-2026-07-08]] — Earlier lint
- [[vault-lint-report-2026-06-22]] — Earlier lint
- [[vault-lint-report-2026-06-16]] — First lint

---

## Open Questions

- None — all issues identified and prioritized. Vault is healthy.
