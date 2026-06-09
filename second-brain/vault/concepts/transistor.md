---
title: "Transistor"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[diode]]"]
---
## One-line Summary
A transistor is a three-terminal semiconductor device that can amplify signals or act as a switch, forming the foundation of all modern digital and analog circuits.

## Core Intuition
A transistor uses a small voltage or current at one terminal (gate or base) to control a much larger current flowing between the other two terminals (source-drain or collector-emitter). This control mechanism enables both amplification (analog) and switching (digital).

## Formal Definition / Statement
A transistor is a semiconductor device with three terminals that can amplify or switch electronic signals. The two major families are:

**BJT (Bipolar Junction Transistor):** Current-controlled. A small base current controls a larger collector-emitter current. Has three regions: emitter, base, collector.
**FET (Field-Effect Transistor):** Voltage-controlled. An electric field from the gate terminal controls current flow between source and drain through a channel. Includes MOSFETs and JFETs.

Both types have two states of primary interest:
- **OFF (cutoff):** No significant current flows between the main terminals.
- **ON (saturation/linear):** Current flows freely (or in a controlled manner) between the main terminals.

## Key Properties / Complexity
- Three terminals: Gate/Base (control), Source/Drain or Collector/Emitter (controlled current path)
- Voltage-controlled (FET) vs. current-controlled (BJT) — MOSFETs dominate modern IC design
- Can operate as amplifier (active region) or switch (cutoff + saturation)
- Foundation of logic gates, memory, processors, and all digital electronics
- Billions of transistors can be fabricated on a single chip

## Worked Example
A MOSFET as a digital switch:
- VGS = 0V: Transistor OFF, no current flows (logic 0 output via pull-up)
- VGS = 5V (VDD): Transistor ON, current flows from drain to source, output ≈ 0V (logic 0)
- With complementary PMOS: CMOS inverter forms the basis of digital logic

## Common Pitfalls
- Confusing BJT and MOSFET operation — one is current-controlled, the other voltage-controlled.
- Assuming a transistor is always either fully ON or fully OFF — the active/linear region is critical for analog circuits.
- Ignoring the body effect in MOSFETs when source is not at substrate potential.

## Connections
- Built upon [[diode]] junctions (PN junctions form the basis of all transistor types).
- Extended to [[mosfet]] for modern integrated circuits.
- The [[mos-capacitor]] is the fundamental physics behind MOSFET operation.
- Enables [[digital-logic]] and [[analog-amplifier]] design.

## Open Questions
- What are the fundamental physical limits on transistor switching speed?
- How does miniaturization (Moore's Law) affect transistor behavior at nanometer scales?
