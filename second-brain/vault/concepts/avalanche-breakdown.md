---
title: "Avalanche Breakdown"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[zener-diode]]", "[[depletion-region]]"]
---

## One-line Summary
Avalanche breakdown is a carrier multiplication mechanism that occurs at high reverse voltages, where carriers gain enough kinetic energy to ionise atoms on collision, creating a cascade of new carriers.

## Core Intuition
Imagine a snowball rolling down a hill — as it rolls, it picks up more snow and grows. In avalanche breakdown, free carriers in the [[depletion-region]] are accelerated by the electric field. When they gain enough energy, they knock electrons free from atoms on collision. These new carriers are also accelerated and cause further collisions, creating an exponential cascade.

## Formal Definition / Statement
Avalanche breakdown occurs at higher reverse voltages (compared to [[zener-breakdown]]) when carriers in the [[depletion-region]] gain sufficient kinetic energy from the electric field to ionise atoms upon collision. The process:

1. Free carriers (electrons/holes) are accelerated by the electric field
2. Carriers gain kinetic energy: KE = q × E × λ (where λ is the mean free path)
3. When KE > bandgap energy, impact ionisation occurs
4. Each ionisation creates an electron-hole pair
5. New carriers are also accelerated → cascade/avalanche multiplication
6. Current increases dramatically

## Key Properties / Complexity
- Dominant at higher breakdown voltages (> 5V)
- Based on impact ionisation (not quantum tunnelling)
- Requires sufficient electric field AND mean free path
- Positive temperature coefficient (breakdown voltage increases with temperature — a longer mean free path is needed)
- Multiplication factor: M = 1/(1 - (V/VB)^n), where n ≈ 3–6

## Common Pitfalls
- Confusing avalanche breakdown with [[zener-breakdown]] — different mechanisms at different voltages
- Assuming avalanche breakdown is always destructive — [[zener-diode]]s are designed to operate safely in this region

## Connections
- [[zener-diode]] — designed to operate in breakdown
- [[zener-breakdown]] — the other breakdown mechanism (at lower voltages)
- [[depletion-region]] — where avalanche multiplication occurs
- [[bandgap]] — energy threshold for impact ionisation
- [[p-n-junction]] — all p-n junctions can experience avalanche breakdown

## Open Questions
- How does the transition voltage between Zener and avalanche mechanisms vary with doping?
