---
title: "Digital Circuit Design"
tags: [concept, microelectronics, digital-design, vlsi, semester-1]
course: "Introduction to Microelectronics"
source_count: 0
status: current
last_updated: 2026-06-09
prerequisites:
  - mos-transistors
  - digital-logic
  - cmos-inverter
---

## One-line Summary
*Digital circuit design is the art of combining MOS transistors into logic gates, and logic gates into functional systems — turning physics into computation.*

## Core Intuition
You know how a single MOSFET works. Digital circuit design is what happens when you connect billions of them together. The key insight is abstraction: at the transistor level, you worry about voltages and currents. At the gate level, you think in 1s and 0s. At the system level, you think in adders, multiplexers, and memory arrays. Each level hides the complexity below. The CMOS inverter is the foundation — NAND, NOR, and all other gates are extensions of the same complementary pull-up/pull-down topology. The challenge isn't making one gate work; it's making a billion gates work fast, reliably, and without burning too much power.

## Formal Definition / Statement
Digital circuit design is the process of implementing Boolean functions using networks of transistors, optimized for speed, power, area, and reliability.

**Combinational circuits** (output = f(inputs) only):
- Basic gates: NAND, NOR, NOT, AND, OR, XOR
- NAND and NOR are universal — any function can be built from one type
- Complex gates: AOI (AND-OR-INVERT), OAI (OR-AND-INVERT) — implement multi-level logic in one stage
- Multiplexer: selects one of N inputs based on control signals
- Adder: half-adder (2 inputs), full-adder (3 inputs), ripple-carry, carry-lookahead
- Decoder: N inputs → 2^N outputs (one-hot)
- Encoder: inverse of decoder

**Sequential circuits** (output = f(inputs, state)):
- SR latch: two cross-coupled NOR or NAND gates
- D latch: level-sensitive storage (transparent when enabled)
- D flip-flop: edge-triggered storage (captures input on clock edge)
  - Master-slave configuration: two D latches in series
  - Setup time (t_setup): input must be stable before clock edge
  - Hold time (t_hold): input must remain stable after clock edge
  - Clock-to-Q delay (t_CK→Q): time from clock edge to output change
- Register: N flip-flops sharing a common clock
- Counter: sequential circuit that cycles through states
- Finite state machine (FSM): combinational logic + state register

**CMOS gate design:**
- Pull-up network (PUN): pMOS transistors — conducts when output should be HIGH
- Pull-down network (PDN): nMOS transistors — conducts when output should be LOW
- PUN and PDN are dual networks (series ↔ parallel, AND ↔ OR)
- NAND: PUN = 2 pMOS in parallel, PDN = 2 nMOS in series
- NOR: PUN = 2 pMOS in series, PDN = 2 nMOS in parallel
- Transistor sizing: series transistors need 2× width to match single transistor drive strength

**Power in digital circuits:**
- Dynamic power: P_dynamic = α × C_L × V_DD² × f
  - α = switching activity factor (0 to 1)
  - C_L = load capacitance
  - V_DD = supply voltage (most effective knob: power ∝ V²)
  - f = clock frequency
- Static power: P_static = I_leak × V_DD
  - Subthreshold leakage, gate leakage, junction leakage
  - Becomes dominant below 90nm technology
- Short-circuit power: ~10-15% of dynamic power during transitions

**Timing:**
- Critical path: longest combinational delay between any two flip-flops
- Maximum frequency: f_max = 1 / (t_CK→Q + t_comb + t_setup + t_skew)
- Clock skew: variation in clock arrival time between different flip-flops
- Metastability: when setup/hold times are violated, flip-flop output is unpredictable

## Key Properties / Complexity
- CMOS static power is near zero — only dynamic switching consumes significant power
- NAND is preferred over NOR in CMOS: nMOS in series (NAND) is faster than pMOS in series (NOR) due to higher electron mobility
- Fan-out limit: each gate output can drive ~10-20 CMOS inputs (capacitive loading)
- Noise margins must be maintained across all process, voltage, and temperature (PVT) corners
- Logic effort: framework for sizing gates to minimize delay along a path
- Technology scaling: each generation (~0.7×) reduces area by 2×, increases speed by ~30%, but increases leakage
- Standard cell libraries: pre-designed, characterized gates (INV, NAND2, NOR2, AOI21, etc.) used in automated place-and-route

## Worked Example
**Design a 2-input XOR gate in CMOS:**

XOR: Y = A⊕B = A·B' + A'·B

Method 1: From NAND gates (4 NAND gates):
  - W1 = NAND(A, B)
  - W2 = NAND(A, W1)
  - W3 = NAND(B, W1)
  - Y = NAND(W2, W3)
  - Total: 16 transistors (4 NANDs × 4 transistors)

Method 2: Transmission gate XOR (8 transistors):
  - TG1: passes A when B=0, passes A' when B=1
  - Uses 2 transmission gates + 2 inverters
  - More efficient but less standard in cell libraries

Timing analysis (65nm technology, NAND2 delay = 40ps):
  - Method 1 critical path: 3 NAND delays = 120ps
  - Method 2 critical path: ~80ps (inverter + TG delay)
  - Method 2 is faster and uses fewer transistors

**Power calculation for a 32-bit adder at 1GHz:**
  - ~500 transistors, average α = 0.15 (not all switch every cycle)
  - C_L ≈ 2 fF per gate output, V_DD = 1.2V
  - P = 0.15 × 500 × 2×10⁻¹⁵ × 1.44 × 10⁹ = 0.216 mW
  - Plus leakage: ~0.05 mW in 65nm

## Common Pitfalls
- **Forgetting the dual network rule**: PUN must be the dual of PDN. Getting this wrong produces a gate that can't pull to both rails.
- **Ignoring PVT variation**: A gate that works at typical conditions may fail at worst-case corners (slow process, low voltage, high temperature).
- **Race conditions**: Combinational logic between flip-flops can produce glitches that violate setup/hold times.
- **Clock distribution**: In large chips, clock skew can consume a significant fraction of the timing budget.
- **Area ≠ transistor count**: Layout efficiency depends on routing, not just gate count. A 4-transistor gate might need more area than a 6-transistor gate if interconnect is complex.

## Connections
- [[mos-transistors]] — Every gate is built from nMOS and pMOS transistors
- [[digital-logic]] — Boolean algebra and gate-level abstraction
- [[cmos-inverter]] — The fundamental CMOS gate; all others are extensions
- [[mosfet-operating-regions]] — Transistors switch between cutoff and triode in digital circuits
- [[threshold-voltage]] — V_T determines switching point and noise margins
- [[vlsi-design]] — Scaling up from gates to complete chip systems
- [[finite-automata]] — Sequential circuits are physical realizations of finite state machines

## Open Questions
- How does asynchronous logic (no global clock) compare to synchronous design in power and performance?
- What are the fundamental limits of energy per operation (Landauer's principle)?
- How do emerging devices (tunnel FETs, negative-capacitance FETs) change the digital design paradigm?
