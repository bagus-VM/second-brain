---
title: "MOSFET Operating Regions"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[nmos-transistor]]", "[[pmtransistor]]", "[[threshold-voltage]]"]
---
## One-line Summary
MOSFETs operate in three distinct regions — Cutoff, Linear (Triode), and Saturation — determined by the relationship between VGS, VDS, and VTH.

## Core Intuition
The region of operation depends on two questions: (1) Is there a channel? (VGS vs VTH), and (2) Is the channel pinched off at the drain end? (VDS vs VGS - VTH). If no channel → cutoff. If channel exists and not pinched → linear. If channel exists but pinched at drain → saturation.

## Formal Definition / Statement

### nMOS Transistor:
| Region | Conditions | Drain Current |
|--------|-----------|---------------|
| **Cutoff** | VGS < VTH | ID = 0 |
| **Linear (Triode)** | VGS ≥ VTH AND VDS < VGS - VTH | ID = kn'[(VGS - VTH)VDS - VDS²/2](W/L) |
| **Saturation** | VGS ≥ VTH AND VDS ≥ VGS - VTH | ID = (kn'/2)(VGS - VTH)²(W/L)(1 + λVDS) |

### pMOS Transistor:
| Region | Conditions | Drain Current |
|--------|-----------|---------------|
| **Cutoff** | |VGS| < |VTH| | ID = 0 |
| **Linear (Triode)** | |VGS| ≥ |VTH| AND |VDS| < |VGS| - |VTH| | ID = kp'[(|VGS|-|VTH|)|VDS| - |VDS|²/2](W/L) |
| **Saturation** | |VGS| ≥ |VTH| AND |VDS| ≥ |VGS| - |VTH| | ID = (kp'/2)(|VGS|-|VTH|)²(W/L)(1+λ|VDS|) |

Where:
- kn' = μnCox (nMOS process transconductance)
- kp' = μpCox (pMOS process transconductance)
- W/L = width-to-length ratio
- λ = channel-length modulation parameter (V⁻¹)
- Cox = εox/tox (oxide capacitance per unit area)

## Key Properties / Complexity
- **Cutoff:** Transistor acts as open switch, no current flows
- **Linear/Triode:** Transistor acts as voltage-controlled resistor, ID depends on both VGS and VDS
- **Saturation:** ID depends primarily on VGS (VGS - VTH)², acts as current source
- In saturation, ID is relatively independent of VDS (ideal current source behavior)
- λ (channel-length modulation) causes slight ID increase with VDS in saturation
- Pinch-off occurs at the drain end when VDS = VGS - VTH
- Digital circuits use cutoff and triode (switching); analog circuits use saturation (amplification)

## Worked Example
nMOS with kn' = 100 μA/V², W/L = 10, VTH = 0.5V, λ = 0.02 V⁻¹:

**Case 1:** VGS = 0.3V → Cutoff (VGS < VTH), ID = 0

**Case 2:** VGS = 2V, VDS = 0.5V → Linear (VDS = 0.5 < 2 - 0.5 = 1.5V)
- ID = 100×10⁻⁶ × 10 × [(1.5)(0.5) - 0.25/2] = 10⁻³ × [0.75 - 0.125] = 0.625 mA

**Case 3:** VGS = 2V, VDS = 2V → Saturation (VDS = 2 ≥ 1.5V)
- ID = (100×10⁻⁶/2) × 10 × (1.5)² × (1 + 0.02×2) = 5×10⁻⁴ × 2.25 × 1.04 = 1.17 mA

## Common Pitfalls
- Confusing VDS < VGS - VTH (linear) with VDS ≥ VGS - VTH (saturation) — it's the pinch-off condition.
- Forgetting that pMOS uses absolute values — all voltage relationships must use magnitudes.
- Assuming saturation means maximum current — it means the transistor is in the active/amplifier region.
- Ignoring λ (channel-length modulation) — ID is not truly constant in saturation.
- Mixing up "linear" region (analog: triode) with "linear" in digital context (ON state).

## Connections
- Region conditions defined by [[threshold-voltage]].
- Applies to both [[nmos-transistor]] and [[pmtransistor]].
- Derived from [[mosfet]] physics and [[mos-capacitor]] behavior.
- Critical for [[cmos-inverter]] voltage transfer characteristics.
- Saturation region used in [[common-source-amplifier]] design.

## Open Questions
- How does velocity saturation at short channel lengths modify the saturation region equations?
- What is the transition behavior at the boundary between linear and saturation regions?
