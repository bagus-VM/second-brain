---
title: "nMOS Transistor"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[mosfet]]", "[[threshold-voltage]]", "[[n-type-semiconductor]]"]
---
## One-line Summary
An nMOS transistor has N-type source and drain regions in a P-type substrate, using electrons as charge carriers, and turns on when VGS exceeds the threshold voltage VTH.

## Core Intuition
Apply a positive voltage to the gate relative to the source. The electric field through the oxide repels holes from the P-type surface and attracts electrons, forming an N-type inversion layer (channel) that connects the N+ source to the N+ drain. Electrons flow from source to drain (conventional current flows drain to source). No channel exists until VGS > VTH.

## Formal Definition / Statement
An nMOS (N-channel Metal-Oxide-Semiconductor) transistor consists of:
- **P-type substrate** (body/bulk)
- **N+ source** and **N+ drain** regions (heavily doped N-type)
- **Gate oxide** (SiO₂) over the channel region
- **Gate electrode** (polysilicon or metal)

Turning ON: VGS > VTH creates an inversion layer of electrons connecting source to drain.
Current direction: Electrons flow source → drain; conventional current ID flows drain → source.

Drain current in different regions:
- **Cutoff:** ID = 0 (VGS < VTH)
- **Linear/Triode:** ID = kn'[(VGS - VTH)VDS - VDS²/2](W/L)
- **Saturation:** ID = (kn'/2)(VGS - VTH)²(W/L)(1 + λVDS)

Where kn' = μnCox (process transconductance parameter).

## Key Properties / Complexity
- Electrons are the channel carriers (higher mobility than holes, μn > μp)
- Must have VGS > VTH to turn on
- Body effect: VTH increases when VSB > 0 (source raised above substrate)
- Typically faster than pMOS for the same dimensions (due to higher electron mobility)
- nMOS alone has ratio logic issues — CMOS (nMOS + pMOS) solves this
- Speed depends on W/L ratio and oxide thickness

## Worked Example
nMOS with kn' = 100 μA/V², W/L = 10, VTH = 0.7V, λ = 0:
- VGS = 0V: ID = 0 (cutoff)
- VGS = 2V, VDS = 0.5V (linear): ID = 100×10⁻⁶ × 10 × [(2-0.7)(0.5) - 0.25/2] = 10⁻³ × [0.65 - 0.125] = 0.525 mA
- VGS = 2V, VDS = 2V (saturation): ID = (100×10⁻⁶/2) × 10 × (2-0.7)² = 5×10⁻⁴ × 1.69 = 0.845 mA

## Common Pitfalls
- Confusing electron flow direction (source→drain) with conventional current direction (drain→source).
- Forgetting the body effect when source ≠ substrate potential.
- Assuming nMOS passes a strong "1" — nMOS passes "0" well but "1" weakly (threshold drop).

## Connections
- Specific implementation of [[mosfet]] using electrons as carriers.
- [[threshold-voltage]] determines the ON/OFF switching point.
- Uses [[n-type-semiconductor]] for source/drain regions.
- Combined with [[pmtransistor]] to form CMOS logic.
- Operating behaviour described by [[mosfet-operating-regions]].

## Open Questions
- How does channel length modulation (λ) affect saturation region behaviour?
- What limits the minimum channel length in modern nMOS devices?
