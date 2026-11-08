---
title: "Bandgap"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[valence-band]]", "[[conduction-band]]"]
---

## One-line Summary
The bandgap is the energy difference between the top of the [[valence-band]] and the bottom of the [[conduction-band]] in a solid material. It determines whether a material is a conductor, semiconductor, or insulator.

## Core Intuition
The bandgap is like a "jump" electrons must make to become free and carry current. In conductors, there is no jump needed (bands overlap). In semiconductors, it is a small jump (~1 eV). In insulators, it is a huge jump that electrons rarely make.

## Formal Definition / Statement
The bandgap (Eg) is the energy difference between the top of the [[valence-band]] and the bottom of the [[conduction-band]] in a solid material. It determines the material's electrical conductivity:

- **Conductor (metal):** Valence and conduction bands overlap (Eg = 0)
- **Semiconductor:** Small bandgap (typically 0.1–4 eV)
- **Insulator:** Large bandgap (> 4 eV)

For [[silicon]], Eg ≈ 1.12 eV at room temperature.

## Key Properties / Complexity
- Determines material classification (conductor/semiconductor/insulator)
- Smaller bandgap → easier electron excitation → higher conductivity
- Temperature-dependent: bandgap decreases as temperature increases
- Can be engineered through alloying (bandgap engineering)
- Direct vs. indirect bandgap affects optical properties

## Worked Example
Silicon (Eg ≈ 1.12 eV): At room temperature, thermal energy kT ≈ 0.026 eV. Since Eg ≫ kT, only a small fraction of electrons are thermally excited across the bandgap. This makes silicon a controlled semiconductor — not too conductive, not too insulating.

Germanium (Eg ≈ 0.66 eV): Smaller bandgap means more thermal carriers → higher leakage current. This is why silicon is preferred over germanium in most applications.

## Common Pitfalls
- Assuming bandgap is the only factor determining conductivity — doping concentration, temperature, and carrier mobility also matter
- Confusing direct and indirect bandgap semiconductors

## Connections
- [[valence-band]] — lower edge of the bandgap
- [[conduction-band]] — upper edge of the bandgap
- [[semiconductor]] — materials with small bandgap
- [[silicon]] — Eg ≈ 1.12 eV
- [[intrinsic-semiconductor]] — carrier concentration depends on bandgap

## Open Questions
- How does bandgap engineering enable new optoelectronic devices?
- What role does bandgap play in [[nanoelectronics]]?
