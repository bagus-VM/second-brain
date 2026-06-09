---
title: "P-Type Semiconductor"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[doping]]", "[[intrinsic-semiconductor]]"]
---

## One-line Summary
A p-type semiconductor is a semiconductor doped with electron acceptor atoms (B, Al), creating an abundance of electron holes as majority charge carriers.

## Core Intuition
A p-type semiconductor is like creating "empty seats" in a crowd — acceptor atoms can't complete their bonds, leaving holes that act as positive carriers. Neighboring electrons fill these holes, effectively moving the hole through the material.

## Formal Definition / Statement
A p-type semiconductor is created by [[doping]] an [[intrinsic-semiconductor]] (e.g., [[silicon]]) with group-III elements such as boron (B) or aluminum (Al). These acceptor atoms have 3 valence electrons — they form 3 bonds with silicon but cannot complete the 4th, creating an [[electron hole]] in the [[valence-band]].

- **Majority carrier:** hole (positive)
- **Minority carrier:** electron (negative)
- **Acceptor atoms:** B, Al, Ga (group III)
- **Charge neutrality:** p ≈ Na (acceptor concentration), n = nᵢ²/Na

## Key Properties / Complexity
- p >> n (holes dominate)
- p ≈ Na for moderate doping levels
- Holes are created by acceptor levels (very small energy, ~0.045 eV for B in Si)
- Mass action law: n × p = nᵢ²
- Conductivity: σ = q(nμₙ + pμₚ) ≈ qNaμₚ

## Worked Example
Silicon doped with boron at Na = 10¹⁶ cm⁻³:
- p ≈ 10¹⁶ cm⁻³ (holes)
- n = nᵢ²/p = (1.5 × 10¹⁰)² / 10¹⁶ ≈ 2.25 × 10⁴ cm⁻³ (electrons)
- Ratio: p/n ≈ 4.4 × 10¹¹ → overwhelmingly p-type

## Common Pitfalls
- Confusing holes with positrons — holes are absences of electrons in the crystal lattice, not antiparticles
- Assuming p-type material is positively charged — it's electrically neutral overall

## Connections
- [[doping]] — process that creates p-type material
- [[n-type-semiconductor]] — complementary type
- [[p-n-junction]] — formed by joining p-type and n-type
- [[valence-band]] — where holes reside
- [[silicon]] — base material

## Open Questions
- How does the hole mobility compare to electron mobility in practice?
