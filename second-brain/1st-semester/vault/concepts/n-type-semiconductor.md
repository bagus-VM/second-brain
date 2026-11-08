---
title: "N-Type Semiconductor"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[doping]]", "[[intrinsic-semiconductor]]"]
---

## One-line Summary
An n-type semiconductor is a semiconductor doped with electron donor atoms (P, As), creating an abundance of free electrons as majority charge carriers.

## Core Intuition
An n-type semiconductor is like adding extra "free runners" to a crowd — donor atoms contribute extra electrons that don't need to break bonds. These electrons are the majority carriers and make the material more negatively charged (hence "n-type").

## Formal Definition / Statement
An n-type semiconductor is created by [[doping]] an [[intrinsic-semiconductor]] (e.g., [[silicon]]) with group-V elements such as phosphorus (P) or arsenic (As). These donor atoms have 5 valence electrons — 4 form covalent bonds with silicon, and the 5th becomes a free electron in the [[conduction-band]].

- **Majority carrier:** electron (negative)
- **Minority carrier:** hole (positive)
- **Donor atoms:** P, As, Sb (group V)
- **Charge neutrality:** n ≈ Nd (donor concentration), p = nᵢ²/Nd

## Key Properties / Complexity
- n >> p (electrons dominate)
- n ≈ Nd for moderate doping levels
- Electrons are thermally excited from donor levels (very small energy, ~0.045 eV for P in Si)
- Mass action law: n × p = nᵢ²
- Conductivity: σ = q(nμₙ + pμₚ) ≈ qNdμₙ

## Worked Example
Silicon doped with phosphorus at Nd = 10¹⁶ cm⁻³:
- n ≈ 10¹⁶ cm⁻³ (free electrons)
- p = nᵢ²/n = (1.5 × 10¹⁰)² / 10¹⁶ ≈ 2.25 × 10⁴ cm⁻³ (holes)
- Ratio: n/p ≈ 4.4 × 10¹¹ → overwhelmingly n-type

## Common Pitfalls
- Assuming n-type material is negatively charged — it's electrically neutral overall (donor ions balance free electrons)
- Confusing donor atoms with acceptor atoms

## Connections
- [[doping]] — process that creates n-type material
- [[p-type-semiconductor]] — complementary type
- [[p-n-junction]] — formed by joining n-type and p-type
- [[conduction-band]] — where free electrons reside
- [[silicon]] — base material

## Open Questions
- How does heavy doping (degenerate doping) affect material properties?
