---
title: "Mirai Botnet"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[iot-attack-taxonomy]]", "[[cia-triad]]"]
---

## One-line Summary
The Mirai Botnet (2016) exploited default passwords on IP cameras and routers to build a botnet of millions of IoT devices, launching massive DDoS attacks that took down DNS infrastructure.

## Core Intuition
Mirai proved that the weakest link in IoT security is often the simplest: factory-default credentials. By scanning the internet for IoT devices with default usernames/passwords, attackers built one of the largest botnets ever — not through sophisticated exploits, but through sheer laziness in device configuration.

## Formal Definition / Statement
**Mirai Botnet (2016):** A botnet formed by exploiting default passwords on IP cameras and internet routers. The attack vector was simple authentication exploitation — scanning for devices using factory-default credentials (e.g., admin/admin, root/password). The botnet scaled to millions of devices and was used for Distributed Denial of Service (DDoS) attacks against DNS infrastructure, causing widespread internet outages.

**Attack classification:** Spoofing and Masquerading (Authentication Attack)

## Key Properties / Complexity

### Attack Mechanism
1. Scan internet for IoT devices (cameras, routers, DVRs)
2. Attempt login with a dictionary of default credentials
3. Once compromised, device joins the botnet
4. Botnet receives commands from C2 (command and control) server
5. Massive DDoS launched against target

### Why It Worked
- IoT devices ship with default credentials that users never change
- Many devices have no mechanism to force password changes
- Devices are internet-facing with no firewall protection
- Scale: billions of IoT devices, many with default passwords

### Impact
- Dyn DNS provider attacked → major websites (Twitter, Netflix, Reddit) went offline
- Demonstrated that IoT insecurity affects the entire internet, not just device owners
- Source code was publicly released, spawning variants

### Connection to Information Assurance
- **Confidentiality:** Default passwords = credentials effectively public
- **Integrity:** Compromised devices run unauthorized software
- **Availability:** DDoS attacks make target services unavailable

## Worked Example
The attack flow:
1. Attacker deploys scanner across IP ranges
2. Scanner finds a Hikvision camera at 203.0.113.50
3. Attempts login: admin/12345 ✓ — success
4. Camera joins botnet, awaits DDoS command
5. Thousands of compromised devices flood target with traffic
6. DNS infrastructure overwhelmed → major websites unreachable

## Common Pitfalls
- Thinking Mirai is "just a DDoS botnet" — it exposed fundamental IoT security failures
- Assuming the fix is "just change passwords" — many devices have hardcoded credentials that can't be changed
- Believing Mirai is solved — variants are still active years later
- Ignoring that Mirai's impact extended far beyond IoT device owners

## Connections
- [[iot-attack-taxonomy]] — Authentication/spoofing attack category
- [[iot-common-attacks]] — Common attack case study
- [[information-assurance]] — Violates all three CIA properties
- [[security-by-design]] — Devices should not ship with default passwords
- [[device-memory-attack-surface]] — Hardcoded credentials stored in device memory
- [[firmware-security]] — Hardcoded passwords in firmware
- [[krack-attack]] — Another major IoT attack case study
- [[zigbee-pairing-vulnerability]] — Another protocol-level vulnerability

- [[iot-lecture-1]] — IoT Security Landscape — course overview
- [[iot-lecture-2]] — IoT Common Attacks — taxonomy
- [[iot-lecture-3]] — IoT Attack Surfaces — Miessler's 15 classes
- [[iot-lecture-4]] — IoT Secure Design — best practices

## Open Questions
- Should legislation mandate unique-per-device credentials?
- How do we force password changes on devices with no user interface?
- What is the liability of device manufacturers whose products are weaponized?
