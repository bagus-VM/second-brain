---
title: "Lecture 7: CMOS Applications (Flip-Flops and Amplifiers)"
tags: [concept, semester-1, microelectronics]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-08
prerequisites: [[cmos-inverter]], [[cmos-logic-gates]], [[mosfet]], [[common-source-amplifier]]
---

## One-line Summary
CMOS circuits can store bits in flip-flops and amplify signals in three configurations, leading up to operational amplifiers.

## Core Intuition
The same CMOS transistor building blocks that implement logic gates can also hold state (memory) and process analog signals (amplification). A flip-flop uses feedback to latch a bit. An amplifier uses a MOSFET's transconductance to convert a small voltage change into a large one. The operational amplifier pushes this idea to its limit: with enough internal gain, negative feedback lets you set the overall gain with two external resistors.

## Formal Definition / Statement

**Flip-flops as memories.** An SRAM cell uses 6 transistors (two cross-coupled inverters plus two access transistors) to store one bit statically. A DRAM cell uses 1 access transistor and 1 capacitor: the bit is stored as charge on the capacitor. DRAM requires periodic refresh because charge leaks, but achieves higher density than SRAM. Flip-flop operation is controlled by a clock signal (phi), a Set signal (S), and a Reset signal (R).

**CMOS amplifier configurations.** A MOSFET can be used as an amplifier in three configurations depending on which terminal is grounded:

| Configuration | Grounded terminal | Phase shift | Function | Input impedance | Voltage gain |
|---|---|---|---|---|---|
| Common Source | Source | 180 degrees | Voltage amplifier | High | High |
| Common Gate | Gate | None | Current buffer | Low | Moderate |
| Common Drain (Source Follower) | Drain at VDD | None | Voltage buffer | High | Unity (approx. 1) |

**Two-stage voltage amplifier.** A practical voltage amplifier uses a differential pair (first stage) followed by a common-source gain stage (second stage). The gain-bandwidth product is a key figure of merit: gain times bandwidth stays constant, so you trade gain for bandwidth.

**Operational amplifiers (OpAmps).** An ideal OpAmp has infinite gain, infinite input impedance, and zero output impedance. Real CMOS OpAmps approximate this:

- Basic: 8 transistors + 1 capacitor
- Compensated: 8 transistors + 1 capacitor + 2 resistors
- Advanced: 22 transistors + 4 capacitors

**Non-inverting amplifier.** Input goes to the + terminal. Feedback from output to the - terminal through R2, with R1 from the - terminal to ground. The closed-loop gain is:

- Vout/Vin = 1 + R2/R1 (for finite but high internal gain)
- Vout/Vin = 1 + R2/R1 (for infinite internal gain, same formula)
- When R2 = 0: Vout/Vin = 1, a voltage follower (unity-gain buffer)

The key insight: with sufficient internal gain and negative feedback, the closed-loop gain depends only on the external resistor ratio, not on the OpAmp's internal gain.

## Key Properties / Complexity

- SRAM: 6 transistors per cell, fast access, volatile, no refresh needed, lower density
- DRAM: 1 transistor + 1 capacitor per cell, needs periodic refresh, higher density, slower than SRAM
- Common Source: highest voltage gain of the three configurations, inverts the signal
- Common Gate: no voltage gain, useful as a current buffer when low input impedance is desired
- Common Drain: no voltage gain, used to drive low-impedance loads without loading the source
- Gain-bandwidth product is constant for a given amplifier: doubling gain halves bandwidth
- OpAmp closed-loop gain is set by external resistors, making it temperature- and process-independent
- Voltage follower (R2 = 0) provides impedance matching without voltage amplification

## Worked Example

**Non-inverting amplifier with R1 = 10 kOhm and R2 = 90 kOhm.**

Gain = 1 + R2/R1 = 1 + 90/10 = 1 + 9 = 10.

If Vin = 100 mV, then Vout = 10 * 100 mV = 1 V, in phase with the input.

If R2 = 0 (short circuit), gain = 1 + 0/10 = 1. Vout = Vin. This is a voltage follower, used to buffer a high-impedance source driving a low-impedance load.

**SRAM vs DRAM density.** A 1 GB SRAM array needs 6 billion transistors for storage alone. A 1 GB DRAM array needs about 1 billion transistors plus 1 billion capacitors. DRAM packs more bits per area because each cell is much smaller, at the cost of refresh circuitry and slower access.

## Common Pitfalls

- Confusing the three amplifier configurations. Memorize which terminal is grounded and what each is good for. Exam questions ask you to identify the configuration from a circuit diagram.
- Forgetting that common source inverts (180 degree phase shift). Common gate and common drain do not invert.
- Assuming the voltage follower "does nothing" because its gain is 1. Its purpose is impedance transformation, not voltage gain.
- Thinking OpAmp closed-loop gain depends on the internal gain. It does not, as long as the internal gain is large enough. That is the whole point of negative feedback.
- Mixing up SRAM and DRAM transistor counts. SRAM = 6T, DRAM = 1T + 1C.
- Forgetting that DRAM needs refresh because charge leaks off the capacitor over time.

## Connections

[[cmos-inverter]] - SRAM cells are built from two cross-coupled CMOS inverters, the same circuit analyzed earlier.
[[cmos-logic-gates]] - Flip-flops are constructed from CMOS logic gates, extending digital CMOS to memory.
[[common-source-amplifier]] - The common-source configuration is the fundamental voltage amplifier stage covered in detail here.
[[mosfet]] - All three amplifier configurations rely on MOSFET transconductance as the amplification mechanism.
[[capacitor]] - DRAM stores bits as charge on a capacitor, and OpAmp compensation uses capacitors for frequency stability.
[[analog-amplifier]] - This lecture generalizes single-transistor amplifiers into the two-stage and OpAmp architectures.

## Open Questions

- How does the differential pair in the two-stage amplifier actually work? The lecture introduced it but did not derive the gain.
- What is the compensation capacitor for in the compensated OpAmp (8T + 1C + 2R)? Presumably frequency stability, but the mechanism is unclear.
- How does the gain-bandwidth product limit manifest in real circuit design? When does it matter?
- What are the trade-offs between the advanced OpAmp (22T + 4C) and the basic version beyond just more components?
