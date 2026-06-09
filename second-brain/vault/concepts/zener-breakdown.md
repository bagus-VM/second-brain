---
title: "Zener Breakdown"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[zener-diode]]", "[[depletion-region]]"]
---

## One-line Summary
Zener breakdown is a quantum mechanical tunnelling mechanism that occurs in heavily doped p-n junctions at low reverse voltages, where the intense electric field pulls electrons from valence bands.

## Core Intuition
In a heavily doped [[zener-diode]], the [[depletion-region]] is so thin that the electric field across it becomes enormous. This intense field literally pulls electrons through the [[bandgap]] via quantum tunnelling — they don't need to climb over the barrier, they tunnel through it.

## Formal Definition / Statement
Zener breakdown occurs in heavily doped p-n junctions when the reverse voltage reaches the Zener voltage (VZ). The mechanism:

1. Heavy doping creates a very thin [[depletion-region]]
2. The electric field within the depletion region becomes very intense
3. Near VZ, the field pulls electrons from valence groups, creating current
4. Based on quantum tunnelling: electric field enables tunnelling of electrons from [[valence-band]] to [[conduction-band]]
5. Creates numerous free minority carriers that suddenly increase reverse current

**Key distinction:** Occurs at low reverse voltages (typically < 5V) and is the dominant mechanism in heavily doped junctions.

## Key Properties / Complexity
- Dominant at low breakdown voltages (< 5V)
- Based on quantum tunnelling (not impact ionization)
- Requires heavy doping → thin depletion region → high electric field
- Negative temperature coefficient (VZ decreases with temperature)
- Very fast response (tunnelling is nearly instantaneous)

## Common Pitfalls
- Confusing Zener breakdown with [[avalanche-breakdown]] — they are different mechanisms
- Assuming breakdown is always destructive — in Zener diodes, it's the intended operating mode

## Connections
- [[zener-diode]] — designed to exploit Zener breakdown
- [[depletion-region]] — must be thin for Zener breakdown
- [[avalanche-breakdown]] — the other breakdown mechanism
- [[bandgap]] — electrons tunnel across the bandgap
- [[valence-band]] — source of tunneling electrons
- [[conduction-band]] — destination of tunneling electrons

## Open Questions
- How does the transition between Zener and avalanche breakdown occur around 5V?
