---
title: "IoT Device Fundamentals"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
IoT device fundamentals covers the hardware and software building blocks — microcontrollers, SBCs, RTOS, and Linux — that define what an IoT device is and what security constraints it operates under.

## Core Intuition
You cannot secure what you do not understand. IoT devices range from a $1 sensor with 2KB of RAM to a Raspberry Pi running full Linux. The security implications are radically different: a microcontroller cannot run TLS in software, while an SBC can run a full firewall. Knowing the device type tells you what attacks are feasible and what defenses are possible.

## Formal Definition / Statement
IoT devices are categorized along two axes: **hardware capability** (constrained vs. unconstrained) and **software platform** (bare-metal/RTOS vs. general-purpose OS). These axes determine the device's attack surface, available security mechanisms, and operational constraints.

**Constrained devices** follow the IETF classification (RFC 7228):
- Class 0: ~10KB RAM, ~100KB ROM — extremely limited, cannot run standard security protocols
- Class 1: ~10KB RAM, ~100KB ROM — can run lightweight protocols (CoAP, OSCORE)
- Class 2: ~50KB RAM, ~250KB ROM — can run standard protocols with optimization

**Hardware platforms:**
- **Microcontrollers (MCUs)**: Single-chip computers (ARM Cortex-M, ESP32, AVR, PIC) with integrated CPU, RAM, flash, and peripherals. Typically run bare-metal or RTOS. Power-efficient, cost-effective, limited resources.
- **Single-Board Computers (SBCs)**: More capable processors (ARM Cortex-A, RISC-V) with separate RAM, storage, and networking. Run Linux or similar OS. Higher power consumption, more attack surface.
- **Systems on Chip (SoC)**: Integrated solutions combining MCU and SBC features, often with hardware accelerators and security co-processors.

**Software platforms:**
- **Bare-metal**: No OS — firmware directly controls hardware. Minimal attack surface but no memory protection, no process isolation.
- **RTOS (FreeRTOS, Zephyr, Contiki)**: Real-time operating systems providing task scheduling, memory management, and networking. Deterministic timing for safety-critical applications. Limited security features by default.
- **Embedded Linux (Yocto, Buildroot, OpenWrt)**: Full OS with process isolation, file system permissions, networking stack, and package management. Larger attack surface but richer security tooling.

## Key Properties / Complexity

- **Resource constraints** dictate security options: Class 0 devices cannot run TLS; they need lightweight alternatives like OSCORE or raw pre-shared keys
- **Memory architecture** affects key storage: MCUs often lack MMU, so no virtual memory isolation; keys in flash are extractable via debug interfaces
- **Power budgets** limit cryptographic operations: asymmetric crypto (RSA, ECDHE) is expensive on MCUs; hardware accelerators (ESP32's AES/SHA engine) mitigate this
- **Lifecycle mismatch**: MCUs may be deployed for 15+ years but security libraries have 3-5 year support cycles
- **Debug interfaces** (JTAG, SWD, UART) are essential for development but must be disabled in production — many manufacturers forget
- **Firmware update capability** varies: SBCs with Linux can use package managers; MCUs need custom OTA solutions with limited storage for A/B partitions
- **Peripheral attack surface**: Sensors, actuators, ADCs, GPIOs can be physically manipulated (sensor spoofing, voltage glitching)

## Worked Example

**Comparing two IoT devices:**

| Property | ESP32 Sensor Node | Raspberry Pi Gateway |
|---|---|---|
| CPU | Xtensa LX6 dual-core, 240MHz | ARM Cortex-A72, 1.5GHz |
| RAM | 520KB SRAM | 4-8GB DDR4 |
| Storage | 4MB flash | microSD, 32GB+ |
| OS | FreeRTOS or bare-metal | Raspberry Pi OS (Linux) |
| TLS | ESP-TLS (hw-accelerated) | OpenSSL (full) |
| Key storage | NVS flash or efuse | Filesystem + TPM optional |
| Debug interfaces | JTAG, UART (disableable) | JTAG (less commonly exposed) |
| Power | ~100mW active | ~3W idle |
| Cost | ~$3 | ~$35-75 |
| Security approach | Lightweight crypto, hardware AES | Full security stack, IDS possible |

The ESP32 can do TLS with hardware acceleration but has no memory protection — a buffer overflow in one task can corrupt any memory. The Raspberry Pi can run SELinux, iptables, and Snort, but has a massive attack surface with thousands of packages.

## Common Pitfalls

- Assuming all IoT devices are the same — a smart bulb and a medical infusion pump have vastly different security requirements
- Overlooking bare-metal firmware's lack of memory protection — no ASLR, no stack canaries, no process isolation by default
- Forgetting that RTOS tasks share an address space — a vulnerability in one task compromises all
- Treating SBCs like desktop servers — embedded Linux often runs with root privileges and no SELinux/AppArmor
- Ignoring physical attack vectors on constrained devices — JTAG, SPI flash dump, voltage glitching

## Connections

- [[iot-communication-protocols]] — Device capability determines which protocols are feasible
- [[iot-network-architecture]] — Device type determines placement in the three-tier model
- [[secure-boot-chain]] — Different hardware platforms implement secure boot differently
- [[side-channel-attacks]] — Constrained devices are especially vulnerable to power/EM analysis
- [[device-provisioning]] — Provisioning process varies by device capability class
- [[firmware-security]] — Firmware extraction methods depend on device hardware architecture
- [[physical-unclonable-functions]] — Hardware identity for MCUs vs. SBCs
- [[iot-lecture-1]] — IoT Security Landscape overview

## Open Questions
- How do RISC-V MCUs change the IoT security landscape compared to ARM Cortex-M?
- Can formal verification of bare-metal firmware scale to real commercial products?
- What is the minimum viable security for Class 0 devices that cannot run any standard protocol?
