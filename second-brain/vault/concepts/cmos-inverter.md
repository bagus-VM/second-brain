---
title: "CMOS Inverter"
tags: [concept, microelectronics, digital-logic, semester-1]
course: "Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
*The fundamental building block of CMOS digital circuits: an NMOS and PMOS transistor that switch complementary to produce an inverted output.*

## Core Intuition
The CMOS inverter is the atom of digital electronics. Every digital logic gate (AND, OR, XOR), every processor, every memory chip is built from combinations of this one circuit. Its beauty is that in steady state, there's almost no current flowing from power to ground — one transistor is always off. This is why CMOS dominates: it only consumes significant power during switching.

## Formal Definition / Statement
A CMOS inverter consists of:
- **PMOS** (pull-up): source to V_DD, drain to output
- **NMOS** (pull-down): source to GND, drain to output
- Input connected to both gates

**Operation:**
- Input HIGH (V_DD): NMOS ON, PMOS OFF → output pulled to GND (LOW)
- Input LOW (GND): NMOS OFF, PMOS ON → output pulled to V_DD (HIGH)

**Voltage Transfer Characteristic (VTC):**
- Sharp transition at V_DD/2 (ideally)
- Switching threshold: V_M where V_in = V_out
- V_M = (V_DD - |V_TP| + V_TN × √(β_n/β_p)) / (1 + √(β_n/β_p))
- Noise margins: NMH = V_OH - V_IH, NML = V_IL - V_OL

**Power consumption:**
- Static power: ≈ 0 (only leakage current, ~nW per gate)
- Dynamic power: P = α × C_L × V_DD² × f (switching activity × load cap × V² × frequency)
- Short-circuit power: brief current spike during switching

**CMOS scaling:**
- Technology node (e.g., 7nm, 5nm) refers to transistor feature size
- Smaller transistors → lower C_L → lower power, higher speed
- But leakage increases with scaling (subthreshold, gate oxide tunnelling)

## Key Properties / Complexity
- Rail-to-rail output swing (0 to V_DD) — full logic levels
- Symmetric propagation delays (if β_n/β_p = 1)
- Static power consumption near zero (CMOS advantage over NMOS/PMOS logic)
- Fan-out: can drive multiple CMOS inputs (capacitive loading)
- Propagation delay: t_p = 0.69 × R_eq × C_L (typically 10ps–10ns depending on technology)
- Power-delay product (PDP) is the figure of merit for digital circuits

## Worked Example
CMOS inverter in 65nm technology:
- V_DD = 1.2V, V_TN = 0.3V, |V_TP| = 0.3V
- NMOS: W/L = 200nm/65nm, PMOS: W/L = 400nm/65nm (2:1 ratio for symmetric switching)
- Load capacitance C_L = 10fF
- Propagation delay: t_p ≈ 15ps
- Dynamic power at 1GHz: P = 0.5 × 10fF × (1.2V)² × 1GHz = 7.2μW
- A modern processor has ~10 billion such inverters (plus other gates)

## Common Pitfalls
- **Sizing matters**: Wrong PMOS/NMOS ratio → asymmetric delays, reduced noise margins
- **Leakage at nanoscale**: Below 90nm, leakage power becomes significant
- **Short-channel effects**: Velocity saturation, DIBL, punchthrough at small geometries
- **Process variation**: Random dopant fluctuation causes V_T variation between transistors
- **Temperature**: Higher temperature increases leakage (positive feedback loop)

## Connections
- [[mosfet]] — Both PMOS and NMOS transistors in the inverter
- [[mosfet-operating-regions]] — Transistors switch between cutoff and triode/saturation
- [[digital-logic]] — CMOS inverter is the basis for all digital logic gates
- [[nmos-transistor]] — NMOS pull-down transistor
- [[threshold-voltage]] — V_T determines the switching threshold
- [[capacitor]] — Load capacitance determines speed and power

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
