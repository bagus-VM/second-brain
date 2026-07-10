# Copilot Instructions for `second-brain`

## Build, test, and lint commands

Repository docs define vault workflows, not a code test/build toolchain.

- **INGEST:** `ingest [filename]` (process new source from `raw/`)
- **QUERY:** ask conceptual questions against the vault
- **DRILL:** `drill me on [topic]` / `quiz me`
- **PREP:** `exam prep for [course/topic]`
- **LINT:** `lint the vault` / `check the vault`

Useful maintenance command documented in logs:

```bash
grep "^\#\# \[" log.md | tail -10
```

## High-level architecture

This repository is an Obsidian study vault with a strict pipeline:

1. **Root control files**
   - `index.md` is the master catalog for discoverability and exam tracking.
   - `log.md` (plus rotated `log-YYYY.md`) is the append-only operation history.

2. **Immutable source layer**
   - `raw/` stores source materials (lectures, papers, textbooks, assets).
   - Treat as read-only source-of-truth.

3. **Compiled knowledge layer**
   - `vault/` contains synthesized knowledge:
     - `concepts/` (atomic concepts)
     - `algorithms/` (algorithm pages)
     - `topics/` (lecture/topic overviews)
     - `connections/` (cross-topic synthesis)

4. **Active exam-prep layer**
   - `study/flashcards/`, `study/practice/`, `study/exams/` are derived outputs generated from vault knowledge.

5. **Course/project overlays**
   - `courses/` holds per-course exam/syllabus tracking and links into vault pages.
   - `projects/` holds project-specific notes and work areas.

## Key conventions

1. **Follow operation model from `AGENTS.md` and `SOUL.md`**
   - Work through INGEST/QUERY/DRILL/PREP/LINT behavior patterns.
   - Important updates should be reflected in both `index.md` and `log.md`.

2. **Vault page schema is fixed**
   - Use frontmatter fields:
     - `title`, `tags`, `course`, `source_count`, `status`, `last_updated`, `prerequisites`
   - Use this section structure:
     - `## One-line Summary`
     - `## Core Intuition`
     - `## Formal Definition / Statement`
     - `## Key Properties / Complexity` (or `## Key Properties`)
     - `## Worked Example`
     - `## Common Pitfalls`
     - `## Connections`
     - `## Open Questions`

3. **Naming and link conventions**
   - File names are slugified/kebab-case.
   - Cross-link using Obsidian wikilinks (`[[page-slug]]`, `[[page-slug|Alias]]`).
   - New or updated content should be cross-linked, not isolated.

4. **Log format is strict**
   - Append entries as:
     - `## [YYYY-MM-DD] OPERATION | title | details`
   - Keep `log.md` append-only; rotate to `log-YYYY.md` when large.

5. **Source discipline**
   - Do not write generated content into `raw/`.
   - Put synthesized knowledge in `vault/` and exam materials in `study/`.
