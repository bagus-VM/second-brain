---
title: "Intrinsic Semiconductor"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[semiconductor]]", "[[bandgap]]"]
---

## One-line Summary
An intrinsic semiconductor is a pure semiconductor material with no added impurities, where charge carriers are generated only by thermal excitation across the bandgap.

## Core Intuition
An intrinsic semiconductor is like a perfectly clean crystal — the only way to get current flowing is by thermal energy exciting electrons across the [[bandgap]]. This makes its conductivity highly temperature-dependent and relatively low at room temperature.

## Formal Definition / Statement
An intrinsic semiconductor is a pure [[semiconductor]] material (e.g., pure [[silicon]]) with no intentionally introduced impurities. The concentration of free electrons in the [[conduction-band]] equals the concentration of [[electron-hole]] in the [[valence-band]]:

n = p = nᵢ

where nᵢ is the intrinsic carrier concentration. For silicon at room temperature, nᵢ ≈ 1.5 × 10¹⁰ cm⁻³.

## Key Properties / Complexity
- No impurities — pure crystal lattice
- Equal electron and hole concentrations (n = p)
- Conductivity determined entirely by temperature and [[bandgap]]
- Intrinsic carrier concentration: nᵢ = √(Nc × Nv) × exp(-Eg / 2kT)
- For Si: nᵢ ≈ 1.5 × 10¹⁰ cm⁻³ at 300K
- Very low conductivity compared to [[doping|doped]] semiconductors

## Worked Example
Pure silicon at 300K: nᵢ ≈ 1.5 × 10¹⁰ cm⁻³. Silicon has ~5 × 10²² atoms/cm³. So only about 1 in 10¹² atoms contribute a free carrier — intrinsic silicon is a very poor conductor.

## Common Pitfalls
- Assuming intrinsic semiconductors are insulators — they do conduct, just poorly
- Forgetting that n = p always in intrinsic semiconductors

## Connections
- [[semiconductor]] — intrinsic is the purest form
- [[silicon]] — most common intrinsic semiconductor
- [[bandgap]] — determines nᵢ
- [[doping]] — converts intrinsic to extrinsic semiconductor
- [[n-type-semiconductor]] — doped with electron donors
- [[p-type-semiconductor]] — doped with electron acceptors

## Open Questions
- How does temperature cycling affect intrinsic carrier concentration in practice?
