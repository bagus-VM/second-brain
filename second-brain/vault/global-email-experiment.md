---
title: "Global Email Experiment (Dodds et al.)"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
==Dodds, Muhamad & Watts (2003)== replicated Milgram's experiment using email across 166 countries, confirming short paths exist but ==revealing that motivation — not topology — is the primary bottleneck (1.6% completion rate).==

## Core Intuition
Milgram's 1967 experiment was limited: US-only, postal mail, small sample. Dodds et al. (2003) ran a global version using email — no geographic constraints, 60,000 participants, 18 targets in 13 countries.

The results confirmed Milgram: completed chains had median length 4–7 steps, consistent with [[small-world-property|logarithmic scaling]]. But the completion rate plummeted to ~1.6% (vs. Milgram's ~25%). The bottleneck wasn't that short paths don't exist — it's that people choose not to forward. Motivation, not topology, is the limiting factor.

## Formal Definition / Statement
**Study parameters (Dodds, Muhamad & Watts, 2003):**

| Parameter | Value |
|---|---|
| Participants recruited | ~60,000 from 166 countries |
| Target persons | 18 in 13 countries |
| Chains started | 24,163 |
| Chains completed | 384 (~1.6%) |
| Median chain length (completed) | 4–7 steps |

**Key findings:**
1. Completed chains are short (median 4–7), consistent with $\log n / \log k$
2. Most chains die early — the bottleneck is motivation, not topology
3. Successful chains use geography and profession as search dimensions — consistent with [[kleinberg-decentralized-search|Kleinberg's model]] where search exploits multiple distance dimensions

## Key Properties
- Confirmed the [[small-world-property]] at global scale
- Revealed the **navigational gap**: short paths exist but are rarely found in practice
- Forwarders who brought the letter closer in geographic or professional distance were more effective
- Email ≠ acquaintance: the email network may be larger and weaker-tied than face-to-face networks
- No ground-truth network: cannot measure whether successful chains followed near-optimal paths

## Worked Example
Of 24,163 chains started:
- 384 completed (~1.6%)
- Median completed chain: 4–7 steps
- The other ~98.4% died because intermediaries chose not to forward, NOT because no short path existed

This means the true average distance between random pairs is likely close to 4–7, but most people can't find those paths because:
1. They lack motivation to forward
2. They lack the right social connections to make progress
3. The information cues (geography, profession) may be insufficient

## Common Pitfalls
- **"Only 1.6% completion means paths are rare"** — No, it means willingness to forward is rare. The paths exist; people just don't use them.
- **"Email experiment = Milgram's experiment"** — Email allows forwarding to anyone whose address you know, not just personal acquaintances. The social network traversed may be different.
- **"Median 4–7 is the true average distance"** — This is biased by selection: completed chains may over-represent easy targets (well-known, geographically close). The true distance may be higher.

## Connections
- [[milgrams-experiment-six-degrees]] — The original experiment this replicates
- [[small-world-property]] — Confirms logarithmic distances at global scale
- [[kleinberg-decentralized-search]] — Successful chains used multi-dimensional search (geography + profession), consistent with Kleinberg's $r = d$ condition
- [[web-bow-tie-structure]] — The directed Web has different navigability properties

## Open Questions
- What is the true completion rate if all intermediaries cooperated fully?
- How do social categories (profession, geography, ethnicity) guide routing?
- Would the results differ with a different target selection strategy?
