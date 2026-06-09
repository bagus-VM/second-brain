---
title: "Wikilinks"
tags: [concept, obsidian, meta, semester-1]
course: "General"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*Obsidian's internal linking syntax using double brackets to create bidirectional connections between notes.*

## Core Intuition
Wikilinks are the connective tissue of a knowledge base. Instead of referencing files by path, you reference them by name, and Obsidian automatically tracks which notes link to which. This creates a web of knowledge — the graph view, backlinks, and link suggestions all emerge from simple [[bracket]] syntax.

## Formal Definition / Statement
Wikilinks are Obsidian's markdown extension for internal links:

**Basic syntax:**
- `[[note-name]]` — Link to a note by its filename (without .md)
- `[[note-name|display text]]` — Link with custom display text
- `[[note-name#heading]]` — Link to a specific heading within a note
- `[[note-name#heading|display]]` — Combined

**Features:**
- Bidirectional: linking A → B automatically creates a backlink from B → A
- Graph view: visualizes all notes and their connections
- Backlinks pane: shows all notes that link to the current note
- Link suggestions: autocomplete when typing [[
- Unresolved links: links to non-existent notes appear as 'dangling' — useful for identifying knowledge gaps

**Best practices:**
- Use descriptive slugs: [[gradient-descent]] not [[gd]]
- Link concepts naturally within prose, not just in a 'Related' section
- Check for orphan pages (no inbound links)
- Use aliases for common variations: `aliases: [GD, gradient descent algorithm]`

## Key Properties / Complexity
- Wikilinks are resolved by filename, not path (unique filenames required)
- Broken links (to non-existent pages) are tracked by Obsidian
- Aliases allow multiple names for the same note
- The graph view reveals structural patterns in the knowledge base
- Excalidraw and other plugins extend wikilinks to diagrams and canvases

## Worked Example
Creating a well-linked concept page:

```markdown
---
title: "Gradient Descent"
---

Gradient descent is an [[optimization-algorithm]] that minimizes a [[loss-function]] 
by iteratively moving in the direction of steepest descent.

It's closely related to [[backpropagation]] in [[neural-networks]] and uses 
[[partial-derivatives]] from [[multivariable-calculus]].

See also: [[stochastic-gradient-descent]], [[adam-optimizer]]
```

This creates 7 outbound links, each of which creates a backlink. The graph view shows gradient-descent as a hub connecting optimization, calculus, and neural networks.

## Common Pitfalls
- **Broken links**: Linking to pages that don't exist creates dangling references
- **Over-linking**: Linking every other word dilutes the signal
- **Name collisions**: Two notes with the same filename (in different folders) create ambiguity
- **Rename cascades**: Renaming a note requires updating all links to it (Obsidian handles this, but not all tools do)
- **Case sensitivity**: `[[My-Note]]` and `[[my-note]]` may resolve differently depending on settings

## Connections
- [[network-science-graph-fundamentals]] — Wikilinks create a graph structure over your knowledge base
- [[information-assurance]] — Well-linked notes improve knowledge retrieval and reduce duplication
- [[network-community-structure-l06]] — Clusters of linked notes form topic communities

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
