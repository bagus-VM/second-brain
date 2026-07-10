---
title: "DRAM-PUF Based IoT Security Protocol"
tags: [topic, iot-security, semester-1, course-iot-security, authentication, physical-unclonable-functions]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-07-09
prerequisites: ["[[iot-lecture-6]]", "[[physical-unclonable-functions]]"]
sources: ["raw/lectures/iot_security/IoTsec9_2026.pdf"]
---

## One-line Summary
A concrete IoT authentication protocol that uses DRAM retention decay as a Physical Unclonable Function (PUF) to derive shared encryption keys between a constrained IoT device and a server — no stored secrets required on the device.

## Core Intuition
Instead of storing a cryptographic key on the IoT device (which can be extracted by physical attacks), this protocol uses the *physics of DRAM decay* as the key source. When DRAM cells lose power, their contents decay at rates that depend on temperature and the cell's physical characteristics — and these rates are unique per chip. The server knows the decay profile (enrolled once in a secure environment); the device just needs to be the *same physical hardware*. The key is never stored — it is *re-derived* each time from the PUF response and helper data.

## Formal Definition / Statement

### Protocol Phases

**Enrollment Phase** (one-time, in a secure environment):
1. The server records PUF characteristics: challenges (c), responses (R), decay times (t), temperatures (T)
2. Associated helper data (HD) and keys (k) are computed and stored server-side
3. The PUF-equipped hardware is physically delivered to the IoT device
4. This phase happens exactly once per device

**Authentication Phase** (repeatable):
1. **Server → IoT:** Sends decay time (t) and challenge (c)
2. **IoT → Server:** PUF produces response R' = PUF_t(c) at temperature T; reports T to server
3. **Server → IoT:** Looks up helper data HD for (c, t, T) and sends HD to device
4. **IoT:** Computes key k = HD ⊕ R'; encrypts measurement data m as Enc_k(IoTD)
5. **IoT → Server:** Sends encrypted data
6. **Server:** Derives same k from (HD, c, t, T), decrypts: Dec_k(m) = IoTD

### Protocol Diagram
```
        IoT Device                          Server
           |                                  |
           |──── Auth ──────────────────────>|
           |<─── (t, c) ─────────────────────|
           |──── PUF_t(c) = R' ─────────────>|
           |<─── HD ─────────────────────────|  (T → HD lookup)
           |──── HD ⊕ R' = k ──────────────>|
           |<─── Enc_k(IoTD) = m ───────────|  (IoT measurement data)
           |──── Dec_k(m) = IoTD ──────────>|
```

## Key Properties / Complexity
- **No stored keys on device** — key is derived from PUF physics + helper data each session
- **Server knows everything** — it stores (c, R, t, T, HD, k) from enrollment; can re-derive k from any valid (c, t, T) triple
- **Temperature-dependent** — the PUF response varies with temperature, so T must be reported and the server must have HD for that temperature
- **Replay-resistant** — server selects a different (t, c) each time; the resulting R' and k change per session
- **Enrollment is the trust anchor** — happens once in a controlled environment; if enrollment is compromised, the whole protocol fails
- **Scalability** — server must store CRPs + HD for every enrolled device; practical for moderate IoT deployments but may strain at billions of devices

## Common Pitfalls
- Confusing this with generic PUF-based authentication — this protocol is specific to *DRAM retention* PUFs (not SRAM start-up, not arbiter PUFs)
- Forgetting that temperature is a required input — DRAM decay rate varies with T, so the server needs T to select the right HD
- Thinking the key is transmitted — it is *derived* on both sides from PUF physics + helper data; the key never crosses the wire
- Assuming the helper data is secret — HD can be sent in the clear; without the physical PUF response R', an attacker cannot reconstruct k

## Connections
- [[physical-unclonable-functions]] — This protocol is a concrete application of PUFs; the general PUF concept page covers SRAM PUFs, arbiter PUFs, etc.
- [[iot-lecture-6]] — Lecture 6 introduced PUFs, TPMs, and TRNGs as hardware security primitives
- [[trusted-platform-module]] — Alternative hardware root of trust (stores keys in tamper-resistant hardware vs. deriving them from physics)
- [[iot-lecture-5]] — IoT Security Hardware — context for where PUFs fit in the hardware security stack
- [[device-provisioning]] — The enrollment phase is a form of device provisioning

## Open Questions
- What happens if the DRAM degrades over time — does the PUF response drift enough to break key derivation?
- How does this compare to SRAM-PUF-based protocols in terms of reliability and entropy?
- Is there a standardised version of this protocol, or is it research-stage?
