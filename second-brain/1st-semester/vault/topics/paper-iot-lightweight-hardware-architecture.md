---
title: "Mexis et al. 2021 — Lightweight Architecture for Hardware-Based Security in SoS"
tags: [paper, iot-security, semester-1, course-iot-security, systems-of-systems, puf]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[physical-unclonable-functions]]", "[[iot-security-hardware]]", "[[iot-lecture-6]]"]
---

## One-line Summary
Mexis, Anagnostopoulos, Chen, Bambach, Arul, Katzenbeisser (2021), "A Lightweight Architecture for Hardware-Based Security in the Emerging Era of Systems of Systems" (ACM JETC, Vol. 17, No. 3, Article 43) — proposes a hardware-software co-engineered security architecture for heterogeneous IoT networks of networks, using a DRAM-based PUF as the security anchor, HMAC-SHA-256 for message authentication, AES-128-CBC for encryption, and MQTT for transport, validated against the Dolev-Yao attacker model.

## Core Intuition
The paper is a foundational work from the Passau group (Anagnostopoulos is the IoT Security lecturer; Mexis is from the same faculty). It directly motivates the IoT Security L6 lecture content on memory-based PUFs, TRNGs, TPMs, and lightweight cryptography.

The argument: existing IoT security approaches focus on individual devices or subsystems. But IoT 2.0 is *systems of systems* (SoS) — heterogeneous devices and networks combined in an ad hoc manner. The security must be **holistic** (securing the whole SoS, not just components), **lightweight** (because of cost constraints in IoT economies of scale), and **scalable** (because SoS can have tens to thousands of devices).

The solution is a **hardware-software co-engineering** paradigm:
- **Hardware anchor**: DRAM decay-based PUF (intrinsic, no extra silicon, on a Raspberry Pi 3B+)
- **Software crypto**: HMAC-SHA-256 (integrity, authentication of time messages) + AES-128-CBC with PKCS#7 padding (confidentiality, integrity of data messages)
- **Transport**: MQTT with topic-based channels (allows messages to reach only subscribed devices)
- **Time synchronisation**: master-slave architecture, with the master acting as time broker; nonces prevent replay attacks
- **Implementation**: Commercial Off-The-Shelf (COTS) devices — Raspberry Pis, Arduinos, ESP32 boards, LoRa shields — connected over Wi-Fi, Ethernet, LoRaWAN, Bluetooth, CAN, Serial, GPIO

The contribution: a *real implementation* of a secure SoS, not a theoretical proposal. The performance evaluation shows the total message time T_msg (RTT + packet processing) is:
- Ethernet: 11 ms (good for real-time)
- Wi-Fi: 15 ms (good for real-time)
- LoRaWAN: 60 ms (most stable)
- Bluetooth: 100 ms (highest latency, but most library overhead remains)

This is fast enough for in-vehicle communication and other time-critical IoT use cases. The Dolev-Yao attacker analysis shows the protocol is robust against confidentiality, integrity, and availability attacks (with the explicit caveat that physical destruction of a subsystem is unmitigable).

## Formal Definition / Statement

**The Security Architecture (from Section 3 of the paper):**

1. **Security anchor**: DRAM decay-based PUF on a Raspberry Pi 3B+, extended from Chen et al. 2019. The DRAM is a hardware component that is intrinsic to the system — no additional silicon. Manufacturing variations in the DRAM cells' decay characteristics provide unique, persistent, unclonable responses.

2. **Key generation**: PUF responses are processed through a "simple scheme that selects stable response bits" to construct a cryptographic key. This is the "simple helper data scheme" — not a full fuzzy extractor, but a stable-bit-selection mechanism that has been shown efficient for DRAM decay PUFs.

3. **Message authentication (time messages)**: HMAC-SHA-256 over the nonce + time, through a local broker node. Provides integrity and data-origin authentication.

4. **Encryption (data messages)**: AES-128-CBC with PKCS#7 padding over the timestamp + data. Provides confidentiality.

5. **Transport**: MQTT (Message Queuing Telemetry Transport) protocol, with topic-based channels. The broker routes messages only to devices subscribed to the relevant topic. Gateway devices bridge MQTT to protocols that don't natively support it (CAN, Serial, etc.).

6. **Time synchronisation**: master device acts as the time broker. Slaves send TimeRequest, master responds with TimeResponse + HMAC. Nonces prevent replay attacks. Synchronised devices then exchange encrypted, authenticated data messages with valid timestamps.

7. **PUF choice rationale**: a *weak* memory-based PUF (limited number of CRPs). Weak PUFs require physical access to compromise — attackers can't model them. Memory-based PUFs are intrinsic, so no extra silicon.

8. **Attacker model**: Dolev-Yao — the attacker controls the network, can intercept, modify, replay, and inject messages, but cannot break the cryptographic primitives. The analysis shows the architecture is robust against attacks on CIA.

**Performance measurements (from Section 3 evaluation):**

| Protocol | T_msg average | Time variance |
|---|---|---|
| Ethernet | 11.04 ms | 20.73 ms |
| Wi-Fi | 15.40 ms | 83.53 ms |
| LoRaWAN | 60.33 ms | 1.16 ms |
| Bluetooth | 100.58 ms | 58.35 ms |

The protocol is "real-time suitable" for Wi-Fi and Ethernet. LoRaWAN is the most stable (lowest variance). Bluetooth and LoRaWAN libraries could be optimised further (e.g., BlueZ 5 driver for Bluetooth).

**Out of scope:**
- Safety analysis (the paper explicitly notes this is future work)
- Power consumption analysis (future work)
- All forms of physical destruction (unmitigable by definition)

## Key Properties / Complexity
- **Lightweight**: T_msg mostly < 30 ms, often < 15 ms. Suitable for real-time use cases.
- **Cost-efficient**: COTS devices, no dedicated hardware beyond a Raspberry Pi's DRAM.
- **Scalable**: architecture supports few to hundreds of devices.
- **Flexible**: network topology can be adapted (master-slave demonstrated, but other topologies are possible).
- **Holistic**: security covers the whole SoS, not individual subsystems.
- **COTS-based**: easy to reproduce, no proprietary hardware required.
- **Dolev-Yao robust**: secure against CIA attacks under standard cryptographic assumptions.

## Worked Example

**Demonstrator setup (from Section 2 of the paper):**
- 3× Raspberry Pi 3B+ (one master, two slaves; one of the slaves has the DRAM PUF as security anchor)
- 2× NodeMCU LUA Amica V2 (ESP8266 boards)
- 2× Olimex ESP32-EVB (with LED, temperature/humidity sensor, light sensor)
- 2× Arduino Uno with Dragino LoRa shields
- 1× Dragino RPi LoRa/GPS Hat (master side)
- 1× Cooler Fan (actuator)
- 1× LED (indicator)

Protocols: Wi-Fi, LoRaWAN, Bluetooth, Ethernet, Serial, GPIO, CAN.

**Message flow (time sync, then data exchange):**
```
1. Slave → Master: TimeRequest
2. Master → Slave: TimeResponse + nonce
3. Slave authenticates TimeResponse with HMAC(K, "TimeResponse"||nonce)
4. Slave ↔ Master: Data message, AES-128-CBC(K, timestamp||data) + HMAC(K, ...)
5. Master verifies HMAC, decrypts, validates timestamp
6. Master routes data to subscribers via MQTT topic
```

This is the L6-lecture content on cryptographic primitives applied to a concrete SoS.

## Common Pitfalls
- **Confusing "lightweight" with "weak"**: lightweight means low-resource, not insecure. The architecture uses AES-128 and HMAC-SHA-256 — strong primitives.
- **Thinking the architecture solves physical attacks**: the paper explicitly says physical destruction of a subsystem is unmitigable. The architecture provides CIA under Dolev-Yao, not tamper-proofing.
- **Ignoring the safety/security distinction**: the paper is about *security*, not *safety*. Safety analysis (fault tree, hazard analysis from L4) is future work.
- **Forgetting the energy budget**: the paper notes "a study of the power consumption remains as future work" — don't assume the architecture is energy-optimal.

## Connections
- [[iot-lecture-6]] — source lecture (cryptography + PUF details directly apply)
- [[iot-lecture-5]] — attack surface classes; this paper's architecture is the *defence*
- [[iot-lecture-4]] — DevOps, secure design goals; the paper's architecture is the realisation
- [[iot-lecture-1]] — IoT 2.0, systems of systems; the paper's motivating context
- [[physical-unclonable-functions]] — DRAM PUF is the security anchor
- [[iot-security-hardware]] — topic page covering PUFs, TPMs, secure co-processors
- [[iot-2-0]] — the paper's vision of IoT 2.0 = SoS of heterogeneous devices
- [[iot-security-landscape]] — broader course context
- [[iot-architecture]] — the layered SoS architecture
- [[iot-attack-surfaces]] — Dolev-Yao attacks on the architecture
- [[dolev-yao-attacker-model]] — the security analysis framework
- [[hmac]] — HMAC-SHA-256, the authentication primitive
- [[aes]] — AES-128-CBC, the encryption primitive
- [[mqtt-security]] — MQTT is the transport protocol
- [[lightweight-cryptography]] — the broader family
- [[ascon]] — successor; the paper uses AES/HMAC, but ASCON is the next step
- [[paper-iot-mexis-2021-poster]] — the SIGCOMM'21 poster summary of this work
- [[paper-zhou-iot-2-0]] — the IoT 2.0 survey that contextualises the paper
- [[nist-iot-cybersecurity]] — NIST's role in standardising the underlying primitives

## Open Questions
- How would ASCON-128 (the NIST lightweight crypto winner) compare to AES-128-CBC + HMAC-SHA-256 on the same hardware? (Likely smaller code, similar speed, post-quantum-safer.)
- How does the architecture scale beyond a few hundred devices? (Paper says "highly scalable" but only demonstrates ~10 devices.)
- Can the PUF key generation be made robust to temperature variation without helper data expansion? (Anagnostopoulos et al. 2018 showed DRAM decay PUFs can be robust; the paper relies on this.)
- Is the architecture's power consumption acceptable for battery-powered IoT? (Future work per the paper.)
