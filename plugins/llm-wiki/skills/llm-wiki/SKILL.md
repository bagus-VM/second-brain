---
name: llm-wiki
description: Build, ingest into, query, and lint a Karpathy-style interlinked markdown wiki or second-brain vault, with raw source capture, hashed provenance, cross-referenced pages, index and log maintenance. Use for a user's wiki, knowledge base, notes vault, or Obsidian vault.
---

# LLM Wiki

A persistent, compounding knowledge base made of interlinked markdown files, based on
Andrej Karpathy's LLM Wiki pattern. Knowledge is compiled once and kept current, unlike
RAG, which rediscovers it per query: cross-references already exist, contradictions are
already flagged, and synthesis reflects everything ingested.

The human curates sources and directs analysis. The agent summarizes, cross-references,
files, and maintains consistency.

## When to use this skill

- Creating, building, or starting a wiki or knowledge base.
- Ingesting, adding, or processing a source into the wiki.
- Answering a question that the wiki's domain covers.
- Linting, auditing, or health-checking the wiki.
- Working in a notes vault, second brain, or Obsidian vault, when the user treats it as
  compiled knowledge rather than a scratchpad.

## Where the wiki lives

`wikiPath` configuration, then `WIKI_PATH`, then a `second-brain/` or `wiki/` directory
under the workspace, then `~/wiki`. Every wiki tool accepts an explicit `wikiPath`, so ask
the user once when the default is empty. The wiki is a plain directory of markdown files:
portable to Obsidian, VS Code, or any editor, with no database.

A vault may use its own layer-2 directory names (`vault/concepts`, `vault/topics`,
`1st-semester/...`). Follow what exists instead of imposing a tree.

## Wiki tools

Use these instead of re-implementing the scans. They are deterministic and cheap.

| Tool | Use it for |
| --- | --- |
| `wiki_orient` | Start of session, and before any ingest or query. Reads the schema, index, and recent log; reports page counts and missing backbone files. |
| `wiki_lint` | Audits broken links, orphans, index gaps, raw hash drift, contested pages, stale pages, oversized pages, taxonomy violations, frontmatter gaps, log size. |
| `wiki_ingest` | Stores one source under `raw/` with provenance frontmatter and a body hash; reports `created`, `unchanged`, or `drift`. |
| `wiki_log` | Appends one `## [YYYY-MM-DD] action \| subject` entry plus touched files. |

For reads and targeted edits, use the normal file tools: `read`, `grep`, `glob`, `write`,
`edit`. Fetch URLs with `web_fetch` before handing the text to `wiki_ingest`.

## First pass

Orient before touching anything. Skipping this causes duplicate pages, missed
cross-references, schema violations, and repeated work that is already logged.

1. Run `wiki_orient`. If it reports no wiki, confirm the root with the user before creating
   one.
2. Find the domain layout: `raw/` for immutable sources, and the agent-owned page
   directories (`entities/`, `concepts/`, `comparisons/`, `queries/`, or the vault's own
   equivalents). Page names are lowercase with hyphens.
3. Read one or two existing pages in the target directory to match tone, length, and
   frontmatter shape.
4. For anything larger than a single-page edit, `grep` the vault for the entities and
   concepts involved before writing.

## Capture the source

1. Get the text: `web_fetch` for URLs, `read` for local files and PDFs already extracted,
   or the user's paste.
2. Call `wiki_ingest` with `title`, the text as `content` (or `sourceFile`), an optional
   `sourceUrl`, and a `kind` of `article`, `paper`, `transcript`, or `note`.
3. Act on its status:
   - `created`: new source, continue to the next section.
   - `unchanged`: the same content is already stored. Stop and report that nothing changed.
   - `drift`: the stored copy differs from this content. Report both hashes and ask whether
     the new version supersedes the old one. `raw/` is immutable, so re-run with
     `force: true` only after the user agrees.
4. Discuss the takeaways with the user: what is interesting, what matters for the domain.
   Skip this in automated contexts.

## Write the pages

1. Check what exists: read `index.md`, then `grep` for the entities and concepts.
2. Create pages only above the schema's thresholds; otherwise extend an existing page.
3. Give every page YAML frontmatter with `title`, `created`, `updated`, `type`, `tags`,
   and `sources`, plus optional `confidence`, `contested`, and `contradictions`. Read
   `references/templates.md` when you need the exact field set, the SCHEMA/index/log
   templates, or the tag taxonomy rules.
4. Cross-reference: link to at least 2 other pages with `[[wikilinks]]`, and make sure the
   pages you linked from link back.
5. Use only tags from the taxonomy in `SCHEMA.md`. Add a new tag there first.
6. Mark provenance on pages that synthesize 3+ sources: append `^[raw/articles/source.md]`
   to paragraphs whose claims come from one source.
7. Set `confidence: medium` or `low` for opinion-heavy, fast-moving, or single-source
   claims. Do not claim `high` without corroboration.
8. When new information conflicts with existing content, check the dates, record both
   positions with dates and sources, and add `contradictions: [page-name]`. Never
   silently overwrite.

## Update the navigation

Add new pages to `index.md` under the correct section, alphabetically, and refresh its
"Total pages" count and "Last updated" date. Then call `wiki_log` once with the action,
subject, and every file created or updated.

One source routinely touches 5-15 pages. That is the compounding effect, not scope creep.

## Bulk ingest

1. Read all sources first.
2. Collect the entities and concepts across all of them.
3. Check existing pages in one search pass, not N passes.
4. Create and update pages in one pass.
5. Update `index.md` once at the end.
6. Write a single `wiki_log` entry covering the batch.

## Answer a query

1. Read `index.md` to find the relevant pages.
2. For wikis with 100+ pages, also `grep` for key terms; the index alone misses content.
3. Read the relevant pages and synthesize from compiled knowledge, citing what you used:
   "Based on [[page-a]] and [[page-b]]…".
4. File valuable answers back: a substantial comparison, deep dive, or novel synthesis
   belongs in `queries/` or `comparisons/`. Trivial lookups do not.
5. Record the query with `wiki_log`, noting whether it was filed.

## Lint

Run `wiki_lint`, then act in its severity order:

1. Broken wikilinks are dead references; fix them first.
2. Orphans get an inbound link from a related page, or are archived.
3. Index gaps get added to `index.md`.
4. Raw source drift is confirmed with the user before anything is re-ingested.
5. Contested and low-confidence pages get reviewed before being quoted as settled fact.
6. Stale pages get refreshed from newer sources.
7. Oversized pages get split into sub-topics with cross-links.
8. Tags outside the taxonomy get added to `SCHEMA.md` or replaced.
9. Frontmatter gaps get filled.
10. A log past 500 entries gets rotated to `log-YYYY.md`.

Do not mass-rewrite pages without asking. Append one `wiki_log` entry summarizing what
you fixed and what remains.

## Archiving

Create `_archive/` if absent, move the page while preserving its relative path, remove it
from `index.md`, replace inbound wikilinks with plain text plus "(archived)", and record
the action with `wiki_log` using action `archive`.

## Obsidian

The same directory is an Obsidian vault: `[[wikilinks]]` are clickable, Graph View shows
the network, YAML frontmatter powers Dataview, and `raw/assets/` can hold attachments. For
best results set the attachment folder to `raw/assets/`, keep wikilinks enabled, and
install Dataview for queries such as
`TABLE tags FROM "entities" WHERE contains(tags, "company")`.

Headless machines can sync a vault through Obsidian Sync with `obsidian-headless`:
`npm install -g obsidian-headless`, then `ob login`, `ob sync-setup`, and `ob sync
--continuous` under a user systemd unit with `Restart=on-failure` and lingering enabled.

## Pitfalls

- **Never modify `raw/`.** Corrections belong in wiki pages.
- **Orient first.** Schema, index, then recent log, before any operation.
- **Always update `index.md` and `log.md`.** They are the navigational backbone.
- **No pages for passing mentions.** A footnote mention does not warrant an entity page.
- **No page without cross-references.** Isolated pages are invisible.
- **Frontmatter is required.** It drives filtering, staleness checks, and confidence
  review.
- **Tags come from the taxonomy.** Freeform tags decay into noise.
- **Keep pages scannable.** 30 seconds to read; split past 200 lines.
- **Ask before mass updates.** An ingest touching 10+ existing pages needs confirmation.
- **Rotate the log** past 500 entries.
- **Handle contradictions explicitly.** Never silently overwrite.

## Validate

- `wiki_lint` returns no new broken links, orphans, or index gaps caused by your change.
- Every created or updated page has complete frontmatter, at least 2 outbound
  `[[wikilinks]]`, and taxonomy-only tags.
- `index.md` lists every new page, with a fresh "Total pages" count and "Last updated" date.
- `wiki_log` has exactly one entry for the work, listing every file touched.
- `wiki_ingest` reported `created` or `unchanged`, and any `drift` was confirmed before a
  forced rewrite.

Report which checks ran, what remains unresolved, and any page you deliberately left
unlinked.
