---
title: "Vault Lint Report — 2026-07-08"
tags: [lint, meta]
date: 2026-07-08
---

# Vault Lint Report — 2026-07-08

**Scan scope:** 681 .md files (excluding raw/, .obsidian/, .git/, _archive/)
**Real vault pages (excluding project submodule noise):** ~640
**Project submodule noise:** 656 dirs under RepEng/ (.venv, benchbase vendored .md)

---

## Findings

### P0 — Fixed during lint

**Broken wikilinks in index.md (3):** Wikilinks inside table summary cells had unescaped `|` aliases eaten as column delimiters, truncating the slug.
- `[[graph-lap` → `[[graph-laplacian\|graph Laplacian]]` (L320)
- `[[closeness-centralit` → `[[closeness-centrality\|closeness centrality]]` (L342)
- `[[physical-unclonab` → `[[physical-unclonable-functions\|PUFs]]` (L788)
- **Status: FIXED.** Post-fix scan: 0 broken targets in index.

### P1 — New raw materials not yet ingested (7 files)

| Source | Course | Status |
|--------|--------|--------|
| Ex09_solutions.pdf | MMDB | NOT INGESTED — no vault page, not in index |
| Sheet_8.pdf | RepEng | Sheet-8 page EXISTS, but PDF may have been processed from sibling. Verify content. |
| Sheet_9.pdf | RepEng | NOT INGESTED — no vault page, not in index |
| SoSe_2026_RepEng_IC_9___LLMs.pdf | RepEng | NOT INGESTED — no lecture-9 page, not in index. Index says "8/8 lectures" |
| 11_AgenticCoding_and_SoftwareQuality.pdf | Software Analyse | NOT INGESTED — no lecture-11 page, not in index. Index says "10/10 lectures" |
| Microelectronics7_2026.pdf | Microelectronics | NOT INGESTED — no lecture-7 page, not in index. Index says "6/6 lectures" |
| Microelectronics8_2026.pdf | Microelectronics | NOT INGESTED — no lecture-8 page, not in index. Index says "6/6 lectures" |

**Impact:** 4 courses have new unprocessed material. RepEng and Software Analyse each have a new lecture. Microelectronics has 2 new lectures. MMDB has Ex09 solutions.

### P2 — Structural

**Duplicate slugs (3):** All in RepEng project submodule:
- `README` (14 copies across benchbase/.venv) — vendored, not vault content
- `LICENSE` (10 copies in .venv numpy) — vendored, not vault content
- `course` (2 copies: microelectronics, iot-security) — legitimate, different courses

**Orphan pages (28):** All structural/MOC files (AGENTS, README, LICENSE, folder MOCs, lint reports, project prompts). Acceptable floor — these don't need inbound links.

**Missing Open Questions sections (84):** These are mostly MOC files, exam prep pages, practice files, and folder-level docs. Concept/algorithm pages all have OQ sections.

**Empty Open Questions: 0** — good tracking discipline.

**Stale pages (>90 days): 0** — vault is actively maintained.

**Drafts: 0** — all pages promoted to current.

**Raw source drift: 0** — no sha256 mismatches.

**Large pages (>200 lines): 15** — only 2 genuine split candidates:
- `java-for-software-analysis.md` (472 lines)
- `sign-analysis.md` (382 lines)
Others are exercise sheets, exam prep, index, log — acceptable at their size.

**Unsourced "current" concept pages: ~20** — IoT and Microelectronics concept pages with source_count: 0. Verification risk for exam prep, not a structural failure.

**RepEng project submodule noise:** The `projects/reproducibility-engineering/RepEng/` directory contains a cloned benchbase repo and .venv with 656 subdirectories of vendored .md files. These inflate the page count and slug namespace. Consider adding to .gitignore or excluding from vault scans.

---

## Vault Health Score: A-

**Strengths:** Zero broken wikilinks in active content, zero drafts, zero stale pages, zero empty OQs, 100% index completeness, zero source drift. The vault is structurally sound.

**Weaknesses:** 7 new raw files awaiting ingest across 4 courses. ~20 unsourced concept pages. RepEng submodule noise.

---

## Top 3 Actions

1. **INGEST the 7 new raw files** — RepEng L9 (LLMs), SA L11 (Agentic Coding), Microelectronics L7+L8, MMDB Ex09 solutions, RepEng Sheet 9. These are exam-relevant material.
2. **Update index exam calendar** — RepEng should be 9/9, SA should be 11/11, Microelectronics should be 8/8 after ingest.
3. **Address RepEng submodule noise** — add `.gitignore` for .venv/benchbase or exclude from vault scans.

---

*"The vault held. Zero broken links, zero drafts, zero stale pages. The three truncated index slugs were the only structural flaw, and they're fixed. The real work now is ingestion — seven new sources across four courses, all exam-relevant. The vault is ready to receive them."*
