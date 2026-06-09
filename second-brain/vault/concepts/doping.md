---
title: "Doping"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[intrinsic-semiconductor]]", "[[silicon]]"]
---

## One-line Summary
Doping is the process of intentionally introducing impurity atoms into a semiconductor to modify its electrical properties, creating either n-type or p-type material.

## Core Intuition
Pure silicon is a poor conductor. Doping is like adding "flavor" to water — a tiny amount of impurity (1 part in 10⁶–10⁹) dramatically changes conductivity. Donor atoms (P, As) add free electrons → [[n-type-semiconductor]]. Acceptor atoms (B) create holes → [[p-type-semiconductor]].

## Formal Definition / Statement
Doping is the intentional introduction of impurity atoms into an [[intrinsic-semiconductor]] to control its electrical properties. Two types:

- **N-type doping:** Adding group-V elements (P, As, Sb) that have 5 valence electrons → 4 bond with Si, 1 becomes a free electron. Majority carrier: electron.
- **P-type doping:** Adding group-III elements (B, Al, Ga) that have 3 valence electrons → creates an [[electron hole]]. Majority carrier: hole.

## Key Properties / Complexity
- Typical doping concentrations: 10¹⁴ to 10²⁰ atoms/cm³
- Even small doping levels (10¹⁵ cm⁻³) vastly exceed intrinsic carrier concentration (nᵢ ≈ 1.5 × 10¹⁰ cm⁻³)
- Two main methods: [[ion-implantation]] (dominant since 1970s-80s) and [[thermal-diffusion]]
- [[photolithography]] controls which regions receive dopants
- Doping does not change crystal structure significantly (at moderate levels)
- n × p = nᵢ² (mass action law) holds for doped semiconductors

## Worked Example
Phosphorus doping of silicon at 10¹⁶ cm⁻³:
- Nd = 10¹⁶ cm⁻³ (donor concentration)
- n ≈ Nd = 10¹⁶ cm⁻³ (electron concentration)
- p = nᵢ²/n = (1.5 × 10¹⁰)² / 10¹⁶ ≈ 2.25 × 10⁴ cm⁻³ (hole concentration)
- Majority carrier (electrons) outnumber minority carriers (holes) by ~10¹²

## Common Pitfalls
- Assuming doping changes the material's identity — it's still silicon, just with controlled impurities
- Forgetting that doping creates both majority AND minority carriers (n × p = nᵢ²)
- Confusing n-type and p-type dopant elements

## Connections
- [[intrinsic-semiconductor]] — starting material before doping
- [[n-type-semiconductor]] — result of donor doping
- [[p-type-semiconductor]] — result of acceptor doping
- [[ion-implantation]] — modern doping method
- [[thermal-diffusion]] — traditional doping method
- [[photolithography]] — patterning for selective doping
- [[p-n-junction]] — formed by joining n-type and p-type regions

## Open Questions
- How does co-doping (both n-type and p-type) affect material properties?
- What are the limits of doping concentration before crystal damage?
