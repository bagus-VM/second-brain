---
title: "pMOS Transistor"
tags: [concept, microelectronics, semester-1, introduction-to-microelectronics]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-09
prerequisites: ["[[mosfet]]", "[[threshold-voltage]]", "[[p-type-semiconductor]]"]
---

## One-line Summary
A pMOS transistor has P-type source and drain regions in an N-type substrate, using holes as charge carriers, and turns on when VGS drops below the (negative) threshold voltage VTH.

## Core Intuition
Apply a negative voltage to the gate relative to the source. The electric field through the oxide repels electrons from the N-type surface and attracts holes, forming a P-type inversion layer (channel) that connects the P+ source to the P+ drain. Holes flow from source to drain (conventional current flows source to drain). No channel exists until VGS < VTH (where VTH is negative for pMOS).

## Formal Definition / Statement
A pMOS (P-channel Metal-Oxide-Semiconductor) transistor consists of:
- **N-type substrate** (body/bulk)
- **P+ source** and **P+ drain** regions (heavily doped P-type)
- **Gate oxide** (SiO₂) over the channel region
- **Gate electrode** (polysilicon or metal)

Turning ON: VGS < VTH (VTH is negative) creates an inversion layer of holes connecting source to drain.
Current direction: Holes flow source → drain; conventional current ID flows source → drain.

Drain current in different regions (note: signs are flipped relative to nMOS):
- **Cutoff:** ID = 0 (|VGS| < |VTH|)
- **Linear/Triode:** |ID| = kp'[(|VGS| - |VTH|)|VDS| - VDS²/2](W/L)
- **Saturation:** |ID| = (kp'/2)(|VGS| - |VTH|)²(W/L)(1 + λ|VDS|)

Where kp' = μpCox (process transconductance parameter for holes).

## Key Properties / Complexity
- Holes are the channel carriers (lower mobility than electrons, μp < μn)
- Must have VGS < VTH (negative) to turn on
- Typically ~2–3× slower than nMOS for the same dimensions (due to lower hole mobility)
- Body effect: |VTH| increases when |VSB| > 0
- Passes a strong "1" but weak "0" (complementary to nMOS behaviour)
- Speed depends on W/L ratio and oxide thickness — pMOS devices are often sized wider (2–3×) to match nMOS speed in CMOS designs

## Worked Example
pMOS with kp' = 40 μA/V², W/L = 10, VTH = -0.7V, λ = 0 (all quantities in absolute value):
- VGS = 0V: ID = 0 (cutoff, |VGS| < |VTH|)
- VGS = -2V, VDS = -0.5V (linear): |ID| = 40×10⁻⁶ × 10 × [(1.3)(0.5) - 0.25/2] = 4×10⁻⁴ × [0.65 - 0.125] = 0.21 mA
- VGS = -2V, VDS = -2V (saturation): |ID| = (40×10⁻⁶/2) × 10 × (1.3)² = 2×10⁻⁴ × 1.69 = 0.338 mA

## Common Pitfalls
- Forgetting that VTH is negative for pMOS — the gate must go below VTH (not above).
- Confusing current direction: in pMOS, conventional current flows source → drain (opposite of nMOS).
- Assuming pMOS and nMOS have equal drive strength — hole mobility is lower, so pMOS needs a wider device to match nMOS performance.
- Mixing up absolute and signed values when computing drain current.
- Thinking pMOS is "just nMOS with flipped doping" — the sign conventions for voltages and currents require careful attention.

## Connections
- Specific implementation of [[mosfet]] using holes as carriers.
- [[threshold-voltage]] determines the ON/OFF switching point (negative for pMOS).
- Uses [[p-type-semiconductor]] for source/drain regions.
- Combined with [[nmos-transistor]] to form CMOS logic.
- Operating behaviour described by [[mosfet-operating-regions]].

## Open Questions
- How does the body effect differ between pMOS and nMOS in practice?
- What determines the optimal Wp/Wn ratio in a CMOS inverter?
- How do modern FinFET technologies change the pMOS vs nMOS performance gap?
