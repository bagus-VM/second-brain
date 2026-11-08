---
title: "Mexis et al. 2021 (SIGCOMM Poster) — Secure Network of Networks Demonstrator"
tags: [paper, iot-security, semester-1, course-iot-security, systems-of-systems, puf]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[physical-unclonable-functions]]", "[[paper-iot-lightweight-hardware-architecture]]", "[[iot-lecture-5]]"]
---

## One-line Summary
Mexis, Anagnostopoulos, Chen, Bambach, Arul, Katzenbeisser (2021), "A Design for a Secure Network of Networks Using a Hardware and Software Co-Engineering Architecture" (SIGCOMM '21 Demos and Posters) — a 2-page demo companion to the JETC 2021 full paper, summarising the same architecture (DRAM PUF + HMAC-SHA-256 + AES-128-CBC + MQTT) with a focus on the demonstrator hardware and performance numbers.

## Core Intuition
This is the *demo paper* for the JETC 2021 work. It is two pages, conference-poster format, and exists to present the demonstrator at SIGCOMM 2021. The content overlaps almost entirely with [[paper-iot-lightweight-hardware-architecture]] but with:
- A clearer description of the hardware (the actual list of COTS boards in the demonstrator)
- The performance numbers in a table (Ethernet 11 ms, Wi-Fi 15 ms, LoRaWAN 60 ms, Bluetooth 100 ms)
- The Dolev-Yao security analysis in a paragraph rather than a full section
- A more explicit note that the architecture is "scalable, as well as effective against a Dolev-Yao attacker model"

For a student, the value of this paper is that it shows the architecture works on *real hardware* (not just simulation) and gives concrete timing numbers.

## Formal Definition / Statement

**The demonstrator** (Section 2.1): A collection of COTS evaluation boards connected as a network of networks:
- Multiple Raspberry Pi 3B+ boards
- 2× NodeMCU LUA Amica V2 (ESP8266)
- 2× Olimex ESP32-EVB
- 2× Arduino Uno with Dragino LoRa shields
- 1× Dragino RPi LoRa/GPS Hat
- LEDs, temperature/humidity sensors, light sensors, cooler fan

**Connectivity**: Ethernet, Wi-Fi, LoRaWAN, Bluetooth, Serial, GPIO, CAN — heterogeneous on purpose to demonstrate the architecture works across protocol boundaries.

**Architecture**: master-slave. The master acts as the time broker. Slaves are sensor / actuator endpoints. Gateways bridge MQTT to non-MQTT protocols (CAN, Serial).

**Security solution**: same as the JETC paper — DRAM PUF as security anchor, HMAC-SHA-256 for time message authentication, AES-128-CBC for data message encryption, MQTT for transport, nonces for replay protection.

**Performance** (from the demo): same as the JETC paper. The poster adds the observation that Wi-Fi and Ethernet are real-time suitable, LoRaWAN is the most stable, and Bluetooth/LoRaWAN libraries can be optimised further (e.g., BlueZ 5 driver).

**Security evaluation**: Dolev-Yao attacker model. The architecture protects confidentiality, integrity, and availability of the SoS. Same caveats as the JETC paper.

## Key Properties / Complexity
- **Real hardware demonstrator**: not simulation
- **Performance numbers**: ~30 ms typical T_msg, real-time suitable for Wi-Fi/Ethernet
- **COTS**: easy to reproduce
- **Dolev-Yao robust**: same as the JETC paper
- **Future work (per the poster)**: power consumption, broader library optimisation, more protocols

## Worked Example

**Demonstrator picture (Figure 1 of the poster)**: shows the board layout — a Raspberry Pi 3B+ in the centre as master, with multiple slaves radiating out: more Raspberry Pis, Arduinos, ESP32 boards, each connected via different protocols. The visual emphasises the *heterogeneity* of the network.

**Message flow (Figure 2 of the poster)**:
```
Sensor → Client → Broker
              ↑       ↓
              |    Time
              |   Request
              ↓       ↓
          Time     Time Sync
        Response
              ↓
       Plain text Data → Data → Message (encrypted) → broker/inbox
                                                                    Arbitrarily many messages
```

This figure appears in both the poster and the JETC paper. It shows the time-sync phase (with HMAC) and the data phase (with AES encryption and HMAC).

## Common Pitfalls
- **Treating the poster as a separate work from the JETC paper**: they are the same architecture. Use the JETC paper for depth, the poster for the visual and the performance table.
- **Ignoring the hardware constraints**: the Raspberry Pi 3B+ has a 1 GB DRAM, but the paper's PUF only uses a small portion of it. Scaling up would need to test more DRAM regions.

## Connections
- [[paper-iot-lightweight-hardware-architecture]] — the JETC 2021 full paper (primary reference)
- [[physical-unclonable-functions]] — DRAM PUF
- [[iot-security-hardware]] — topic overview
- [[iot-lecture-5]] — attack surface classes
- [[iot-lecture-6]] — cryptographic primitives
- [[iot-2-0]] — IoT 2.0 as SoS
- [[hmac]] — HMAC-SHA-256
- [[aes]] — AES-128-CBC
- [[mqtt-security]] — MQTT transport
- [[dolev-yao-attacker-model]] — security analysis framework
- [[paper-zhou-iot-2-0]] — the IoT 2.0 survey

## Open Questions
- Did the demonstrator get shown at SIGCOMM 2021 with live hardware, or was it a video demo?
- Have the authors published a follow-up with power consumption numbers?
- Has the architecture been ported to other platforms (e.g., ESP32-only, no Raspberry Pi)?
