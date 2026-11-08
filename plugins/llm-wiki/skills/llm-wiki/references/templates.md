# Wiki templates

Load this file when initializing a wiki, defining its conventions, or checking the exact
frontmatter fields. Day-to-day ingest work does not need it.

## Page frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from the taxonomy]
sources: [raw/articles/source-name.md]
# Optional quality signals:
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

`confidence` and `contested` are optional but recommended on opinion-heavy or fast-moving
topics. Lint surfaces `contested: true`, `contradictions:`, and `confidence: low` pages so
weak claims do not silently harden into accepted fact.

## Raw source frontmatter

`wiki_ingest` writes this block; compute the hash over the body only, never the
frontmatter, so re-ingesting the same source can be skipped when unchanged.

```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest of the body below the frontmatter>
---
```

## SCHEMA.md

```markdown
# Wiki Schema

## Domain
[What this wiki covers, e.g. "AI/ML research", "personal health"]

## Conventions
- File names: lowercase, hyphens, no spaces (e.g. `transformer-architecture.md`)
- Every wiki page starts with YAML frontmatter
- Use [[wikilinks]] between pages, at least 2 outbound links per page
- When updating a page, bump its `updated` date
- Every new page is added to index.md under the correct section
- Every action is appended to log.md
- Provenance: on pages that synthesize 3+ sources, append ^[raw/articles/source-file.md]
  at the end of paragraphs whose claims come from a specific source

## Frontmatter
[Paste the page frontmatter block from this file.]

## raw/ frontmatter
[Paste the raw source frontmatter block from this file.]

## Tag taxonomy
[10-20 top-level tags for the domain. Add a new tag here BEFORE using it.]

Example for AI/ML:
- Models: model, architecture, benchmark, training
- People/Orgs: person, company, lab, open-source
- Techniques: optimization, fine-tuning, inference, alignment, data
- Meta: comparison, timeline, controversy, prediction

Every tag on a page must appear in this taxonomy; that is what prevents tag sprawl.

## Page thresholds
- Create a page when an entity or concept appears in 2+ sources, or is central to one source
- Add to an existing page when a source mentions something already covered
- Do not create pages for passing mentions, minor details, or things outside the domain
- Split a page over ~200 lines into sub-topics with cross-links
- Archive a page whose content is fully superseded: move it to `_archive/`, drop it from the index

## Page shapes
- Entity: overview, key facts and dates, relationships ([[wikilinks]]), sources
- Concept: definition, current state of knowledge, open questions, related concepts
- Comparison: what is compared and why, dimensions in a table, verdict, sources

## Update policy
1. Check the dates; newer sources generally supersede older ones
2. If genuinely contradictory, record both positions with dates and sources
3. Mark the conflict in frontmatter: `contradictions: [page-name]`
4. Flag it for user review in the lint report
```

## index.md

```markdown
# Wiki Index

> Content catalog. Every wiki page is listed under its type with a one-line summary.
> Read this first to find relevant pages for any query.
> Last updated: YYYY-MM-DD | Total pages: N

## Entities

## Concepts

## Comparisons

## Queries
```

Scaling: split a section over 50 entries into sub-sections; over 200 entries total, add
`_meta/topic-map.md` grouping pages by theme.

## log.md

```markdown
# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [YYYY-MM-DD] create | Wiki initialized
- Domain: [domain]
- Structure created with SCHEMA.md, index.md, log.md
```
