---
title: "pMOS Transistor"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[mosfet]]", "[[threshold-voltage]]", "[[p-type-semiconductor]]"]
---
## One-line Summary
A pMOS transistor has P-type source and drain regions in an N-type substrate, using holes as charge carriers, and turns on when |VGS| exceeds |VTH| (gate pulled below source).

## Core Intuition
Apply a negative voltage to the gate relative to the source (gate more negative than source). The electric field repels electrons from the N-type surface and attracts holes, forming a P-type inversion layer (channel) connecting the P+ source to the P+ drain. Holes flow from source to drain. No channel exists until |VGS| > |VTH|.

## Formal Definition / Statement
A pMOS (P-channel Metal-Oxide-Semiconductor) transistor consists of:
- **N-type substrate** (body/bulk)
- **P+ source** and **P+ drain** regions (heavily doped P-type)
- **Gate oxide** (SiO₂) over the channel region
- **Gate electrode** (polysilicon or metal)

Turning ON: VGS must be negative enough that |VGS| > |VTH| to create a hole inversion layer.
Current direction: Holes flow source → drain; conventional current ID flows source → drain.

Drain current (using absolute values for pMOS):
- **Cutoff:** ID = 0 (|VGS| < |VTH|)
- **Linear/Triode:** ID = kp'[(|VGS| - |VTH|)|VDS| - |VDS|²/2](W/L)
- **Saturation:** ID = (kp'/2)(|VGS| - |VTH|)²(W/L)(1 + λ|VDS|)

Where kp' = μpCox (typically 2-4× smaller than kn').

## Key Properties / Complexity
- Holes are the channel carriers (lower mobility than electrons, μp ≈ μn/2 to μn/3)
- Must have |VGS| > |VTH| to turn on (gate voltage below source voltage)
- Slower than nMOS for the same W/L dimensions (due to lower hole mobility)
- To match nMOS speed, pMOS devices need 2-3× larger W/L ratio
- Passes a strong "1" well but passes "0" weakly (complementary to nMOS)
- Body effect: |VTH| increases when source is above substrate potential

## Worked Example
pMOS with kp' = 40 μA/V², W/L = 25, |VTH| = 0.7V, λ = 0:
- VGS = 0V: |VGS| = 0 < 0.7V → cutoff, ID = 0
- VGS = -2V, VDS = -0.5V (linear): ID = 40×10⁻⁶ × 25 × [(1.3)(0.5) - 0.125] = 10⁻³ × 0.525 = 0.525 mA
- VGS = -2V, VDS = -2V (saturation): ID = (40×10⁻⁶/2) × 25 × (1.3)² = 0.5×10⁻³ × 1.69 = 0.845 mA

## Common Pitfalls
- Forgetting that all voltages are negative for pMOS — use absolute values in formulas.
- Assuming pMOS and nMOS have the same current drive — pMOS is weaker unless sized larger.
- Confusing current direction — in pMOS, conventional current flows from source to drain.
- Mixing up body connection — pMOS body connects to the most positive supply (VDD), not ground.

## Connections
- Complementary counterpart to [[nmos-transistor]].
- Specific implementation of [[mosfet]] using holes as carriers.
- [[threshold-voltage]] is negative for pMOS.
- Uses [[p-type-semiconductor]] for source/drain regions.
- Combined with nMOS to form CMOS (Complementary MOS) logic.
- Operating behavior described by [[mosfet-operating-regions]].

## Open Questions
- What process innovations improve pMOS hole mobility (strained silicon, SiGe)?
- Why does CMOS require both nMOS and pMOS instead of just one type?
