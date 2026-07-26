---
title: "Nanoelectronics"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[electronics]]", "[[microelectronics]]", "[[semiconductor]]"]
---

## One-line Summary
Nanoelectronics is the subfield of electronics that exploits nanotechnology and quantum mechanical properties at the atomic scale for electronic applications.

## Core Intuition
When electronic components shrink to the nanometre scale, classical physics breaks down and quantum mechanics dominates. Electrons behave as waves, tunnel through barriers, and exhibit discrete energy levels. Nanoelectronics harnesses these quantum effects rather than fighting them.

## Formal Definition / Statement
Nanoelectronics is the subfield of [[electronics]] that uses nanotechnology in electronic devices, exploiting inter-atomic interactions and quantum mechanical properties that emerge at the nanometre (10⁻⁹ m) scale.

## Key Properties / Complexity
- Operates at nanometre scale where quantum effects are significant
- Exploits quantum tunnelling, discrete energy levels, and wave-particle duality
- Complements and extends traditional [[microelectronics]]
- Key technologies: quantum dots, single-electron transistors, tunnel FETs, spintronics
- Represents the frontier beyond conventional CMOS scaling

## Worked Example
A single-electron transistor (SET) illustrates the shift from classical to quantum behaviour:

- **Classical MOSFET** (gate length ~5 nm): the channel conducts or blocks based on a continuous threshold voltage. Current is a smooth function of gate voltage.
- **SET** (island diameter ~1–3 nm): a single electron tunnels onto a conductive island, raising its energy by e²/(2C), where C is the island capacitance. At sufficiently low temperature (kT < e²/(2C)), adding one electron blocks further tunnelling — the **Coulomb blockade**. Current flows only at discrete gate-voltage peaks, one electron at a time.

This is qualitatively different from a MOSFET: the SET exhibits **discrete charge states** and requires energy quantisation, not continuous drift current.

## Common Pitfalls
- Confusing nanoelectronics with simply "smaller microelectronics" — the physics fundamentally changes at this scale
- Assuming nanoelectronics replaces microelectronics — it extends and complements it
- Forgetting that quantum effects (tunnelling, discrete energy levels) require cryogenic temperatures for many devices

## Connections
- [[electronics]] — parent field
- [[microelectronics]] — predecessor at larger scales
- [[semiconductor]] — material foundation
- [[silicon]] — current dominant material, but nanoelectronics may use other materials (graphene, carbon nanotubes)

## Open Questions
- Will nanoelectronics replace CMOS or coexist with it?
- What are the practical limits of quantum-effect-based computation?
