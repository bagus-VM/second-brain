---
title: "Lecture 7 - CMOS Applications: Flip-Flops and Amplifiers"
tags: [lecture, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-08
prerequisites: [[mosfet]], [[cmos-logic-gates]], [[cmos-inverter]], [[common-source-amplifier]]
---

## One-line Summary
*CMOS circuits can store bits (memory) and amplify signals (analog), not just compute logic.*

## Core Intuition
Digital logic gates are one use of CMOS. The same transistors, wired differently, solve two other problems: remembering state (memory cells) and making weak signals stronger (amplifiers). The shift from logic to memory is about feedback loops. The shift from logic to amplifiers is about biasing transistors in their analog region instead of switching them fully on or off. The operational amplifier pushes this idea to its limit: with enough internal gain, negative feedback lets you set the overall gain with two external resistors.

## Formal Definition / Statement

### Memory Cells

**SRAM cell:** 6 transistors forming two cross-coupled CMOS inverters. Static memory: the state persists as long as power is applied. Fast access, but volatile and lower density (6 transistors per bit).

**DRAM cell:** 1 access transistor (gatekeeper) plus 1 capacitor. The bit is stored as charge on the capacitor. The transistor gates access during read and write. Higher density than SRAM (1 transistor + 1 cap per cell), but the charge leaks, so the cell needs periodic refresh.

**Flip-flop signals:** phi (clock), S (set), R (reset). The clock synchronizes state transitions. S forces the output to 1. R forces the output to 0.

### CMOS Amplifier Configurations

Three configurations, named by which terminal is grounded (or at AC ground):

| Configuration | Grounded terminal | Phase shift | Function | Input impedance | Voltage gain |
|---|---|---|---|---|---|
| Common Source | Source | 180 degrees | Voltage amplifier | High | High |
| Common Gate | Gate | None | Current buffer | Low | Moderate |
| Common Drain (Source Follower) | Drain at VDD | None | Voltage buffer | High | Unity (approx. 1) |

**Common Source:** Source grounded, input at gate, output at drain. Voltage amplifier with high gain. 180 degree phase shift (inverting). The most common voltage amplifier topology.

**Common Gate:** Gate grounded, input at source, output at drain. Non-inverting. Acts as a current buffer or voltage amplifier with low input impedance. Useful when the signal source has low impedance.

**Common Drain (Source Follower):** Drain at VDD, input at gate, output at source. Voltage buffer with unity voltage gain (gain approximately 1). High input impedance, low output impedance. Used for impedance matching, not voltage amplification.

### Voltage Amplifiers

Two-stage architecture: a differential pair (for high input impedance and common-mode rejection) followed by a common-source gain stage. The gain-bandwidth product is a key figure of merit: gain times bandwidth stays constant, so you trade gain for bandwidth.

### Operational Amplifiers (OpAmps)

Ideal OpAmp properties:
- Infinite open-loop gain
- Infinite input impedance (draws no current from the input)
- Zero output impedance (can drive any load)
- Infinite bandwidth

Real OpAmps approximate these ideals closely enough for most applications.

**CMOS OpAmp complexity progression:**
- Basic: 8 transistors + 1 capacitor
- Compensated: 8 transistors + 1 capacitor + 2 resistors (compensation network for stability)
- Advanced: 22 transistors + 4 capacitors

### Non-Inverting Amplifier

Input applied to the + (non-inverting) terminal. Feedback from output to the - (inverting) terminal through a voltage divider (R2 and R1).

For finite gain: Vout/Vin = 1 + R2/R1

For infinite open-loop gain: same formula applies. The negative feedback forces the output to whatever value makes the - terminal match the + terminal. The gain depends only on the external resistor ratio, not on the OpAmp's internal gain.

Special case: when R2 = 0, gain = 1. This is a voltage follower (unity-gain buffer), useful for impedance matching.

The key insight: with sufficient internal gain and negative feedback, the closed-loop gain depends only on the external resistor ratio, not on the OpAmp's internal gain.

## Key Properties

- SRAM: 6 transistors/bit, static, fast, volatile, no refresh needed, lower density
- DRAM: 1 transistor + 1 capacitor/bit, dynamic (needs refresh), slower, higher density
- Common Source: highest voltage gain of the three configurations, inverts the signal
- Common Gate: no voltage gain, useful as a current buffer when low input impedance is desired
- Common Drain: no voltage gain, used to drive low-impedance loads without loading the source
- Gain-bandwidth product is constant for a given amplifier: doubling gain halves bandwidth
- OpAmp closed-loop gain is set by external resistors, making it temperature- and process-independent
- Voltage follower (R2 = 0) provides impedance matching without voltage amplification

## Worked Example

Non-inverting amplifier with R1 = 1 kOhm and R2 = 9 kOhm:

Gain = 1 + R2/R1 = 1 + 9000/1000 = 1 + 9 = 10

If Vin = 0.1 V, then Vout = 1.0 V.

The OpAmp's internal gain might be 100,000, but the closed-loop gain is 10 because the feedback network sets the gain. The OpAmp only needs enough open-loop gain to make the error between + and - terminals negligibly small.

If R2 = 0 (short circuit), gain = 1 + 0/10 = 1. Vout = Vin. This is a voltage follower, used to buffer a high-impedance source driving a low-impedance load.

**SRAM vs DRAM density.** A 1 GB SRAM array needs 6 billion transistors for storage alone. A 1 GB DRAM array needs about 1 billion transistors plus 1 billion capacitors. DRAM packs more bits per area because each cell is much smaller, at the cost of refresh circuitry and slower access.

## Common Pitfalls

- Confusing SRAM (static, 6 transistors) with DRAM (dynamic, 1 transistor + 1 capacitor). The exam will test this distinction.
- DRAM refresh requirement: the capacitor leaks charge, so the cell must be read and rewritten periodically. Forgetting this is a classic mistake.
- Confusing the three amplifier configurations. Memorize which terminal is grounded and what each is good for. Exam questions ask you to identify the configuration from a circuit diagram.
- Forgetting that common source inverts (180 degree phase shift). Common gate and common drain do not invert.
- Assuming the voltage follower "does nothing" because its gain is 1. Its purpose is impedance transformation, not voltage gain.
- Thinking OpAmp closed-loop gain depends on the internal gain. It does not, as long as the internal gain is large enough. That is the whole point of negative feedback.
- The non-inverting amplifier formula 1 + R2/R1 assumes the OpAmp has enough open-loop gain. With finite open-loop gain A, the actual gain is slightly less than 1 + R2/R1.
- Mixing up SRAM and DRAM transistor counts. SRAM = 6T, DRAM = 1T + 1C.

## Connections

- [[mosfet]] - The amplifier configurations are all built on MOSFETs biased in their saturation region.
- [[cmos-inverter]] - SRAM cells use cross-coupled CMOS inverters as their storage element.
- [[cmos-logic-gates]] - The same CMOS technology that builds logic gates also builds memory and analog circuits.
- [[common-source-amplifier]] - The common-source configuration is the fundamental voltage amplifier stage covered in detail here.
- [[analog-amplifier]] - General amplifier concepts: gain, input/output impedance, bandwidth.
- [[capacitor]] - The DRAM cell stores its bit as charge on a capacitor, and OpAmp compensation uses capacitors for frequency stability.
- [[microelectronics-lecture-6]] - Previous lecture covered CMOS logic gates, the foundation for this lecture's memory and amplifier applications.
- [[microelectronics-lecture-8]] - Next lecture extends OpAmp discussion to inverting amplifiers.

## Open Questions

- What is the exact trade-off between SRAM speed and DRAM density in modern processor caches? How does this affect cache hierarchy design?
- How does the compensation network in the compensated CMOS OpAmp (8 transistors + cap + 2 resistors) ensure stability, and what happens without it?
- How does the differential pair in the two-stage amplifier actually work? The lecture introduced it but did not derive the gain.
- How does the gain-bandwidth product limit manifest in real circuit design? When does it matter?
- What are the trade-offs between the advanced OpAmp (22T + 4C) and the basic version beyond just more components?
