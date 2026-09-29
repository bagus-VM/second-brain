---
title: "Network Science E03 — Strong and Weak Ties Flashcards"
tags:
  - flashcards
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-06-02
---

# Flashcards — Exercise Sheet 3

## Flashcards

> [!question]- What is the Strong Triadic Closure (STC) property and the Weak-Ties Theorem?
> [!answer]- STC states that if a person A has strong ties to both B and C, then B and C are likely to become connected (closing the triad). The Weak-Ties Theorem says: Under STC, every local bridge must be a weak tie. This is because if the tie were strong, STC would predict closure, and it would no longer be a local bridge.

> [!question]- Why are rarely-seen acquaintances more useful for job finding than close friends?
> [!answer]- Close friends share your social world and information — their knowledge overlaps with yours (redundant information). Acquaintances bridge to different social circles, providing non-redundant job leads you would never hear about otherwise. Strong ties cluster in dense groups; weak ties are bridges to distant clusters.

> [!question]- What is neighbourhood overlap and what does O(u,v) = 0 indicate?
> [!answer]- Neighbourhood overlap is O(u,v) = |N(u) ∩ N(v)| / |N(u) ∪ N(v)|, measuring how many neighbours two connected nodes share. O(u,v) = 0 means u and v have zero common neighbours, making their edge a perfect local bridge — information passing through this edge is likely completely novel.

> [!question]- Is "unfriending all close friends" good advice based on the weak-ties theorem?
> [!answer]- No. Strong ties provide trust, emotional support, and reliable collaboration. Weak ties provide reach and novel information. You need both. The theorem does not say weak ties are "better" — it says they serve a different, complementary structural role (bridging non-redundant information).

> [!question]- What is the relationship between tie strength and neighbourhood overlap?
> [!answer]- There is a strong positive correlation: edges with high tie strength tend to have high neighbourhood overlap (close-knit groups share friends), while weak ties have low overlap (bridging ties remain socially isolated). This empirical pattern confirms Granovetter's theory that strong ties are embedded in dense clusters while weak ties span structural holes.


---

## Related Resources

### 📖 L03 — Strong and Weak Ties
- Lecture topic: [[network-science-l03]]

**Key concepts covered:**
- [[graph-fundamentals]]
- [[triadic-closure]]
- [[strong-triadic-closure]]
- [[maxstc-complexity]]
- [[clustering-coefficient]]
- [[neighborhood-overlap]]
- [[bridges-and-local-bridges]]
- [[weak-ties-hypothesis]]
- [[social-capital]]
- [[structural-holes]]
