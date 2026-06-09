---
title: "Network Science E01 — What Is a Network? Flashcards"
tags:
  - flashcards
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-06-02
---

# Flashcards — Exercise Sheet 1

## Flashcards

> [!question]- What does the network model reveal that a plain list of elements cannot?
> [!answer]- A list of elements tells you only what the elements are. A network model reveals structural properties: which elements are central (high degree), which serve as hubs between groups, and which are isolated. These structural questions are computable once you have a graph but unanswerable from a list alone.

> [!question]- Why is a list of student attributes (age, gender, grades) insufficient to explain how a rumour spreads?
> [!answer]- Rumours travel along social ties, not via demographic categories. A list of attributes tells you who the students are, but not who talks to whom. Without the connections (the network), you cannot trace the path of information through the student body.

> [!question]- Why is App A (200 students, existing friendships) more likely to survive than App B (public launch, no user base)?
> [!answer]- App A already has a critical mass of interconnected users. New users find their friends already there — the value of joining is immediately high (network effect). App B starts from zero. Network effects mean the structural fact of who is already connected overrides feature quality once a tipping point is crossed.

> [!question]- In which scenario does a rumour reach more students after 2 steps: starting from the dense centre or from the periphery?
> [!answer]- The dense centre. A central student has many direct friends (high degree), each of whom also has many friends. A peripheral student has few direct friends, so after 2 steps only a small chain is informed. Structure shapes the velocity of diffusion independent of content.

> [!question]- What is the condition that determines whether a rumour eventually reaches the same students regardless of starting point?
> [!answer]- Connectivity. If every student is part of the same connected component, any starting point will eventually reach everyone. The difference is only in speed, not final reach — hubs spread information exponentially while periphery nodes spread linearly along chains.
