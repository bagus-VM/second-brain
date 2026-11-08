---
title: "Authentication"
tags: [concept, iot-security, semester-1, iot-security]
course: "IoT Security"
source_count: 0
status: current
last_updated: 2026-06-09
prerequisites: ["[[cia-triad]]"]
---

## One-line Summary
Authentication is the process of verifying the identity of a user, device, or system — proving you are who you claim to be before being granted access or trust.

## Core Intuition
When someone knocks on your door, you look through the peephole to verify their identity before opening. Authentication is the digital peephole. In IoT, it's even more critical: you need to verify that a temperature reading actually came from your legitimate sensor (not an attacker's spoofed device), that a firmware update actually came from the manufacturer (not malware), and that the person sending a "unlock door" command is actually the homeowner (not a burglar).

## Formal Definition / Statement

### Authentication Factors
Authentication relies on one or more of three factor types:

| Factor | Category | Examples |
|--------|----------|----------|
| Something you **know** | Knowledge | Password, PIN, security questions |
| Something you **have** | Possession | Smart card, hardware token, phone (TOTP) |
| Something you **are** | Inherence | Fingerprint, iris scan, voice recognition |

**Multi-factor authentication (MFA)** requires two or more different factor types. Using a password + security question is single-factor (both are knowledge). Using a password + hardware token is two-factor.

### Authentication in IoT
IoT authentication operates at multiple levels:
1. **Device-to-network:** The device proves its identity to join the network (e.g., ZigBee network key, Wi-Fi WPA3)
2. **Device-to-device:** Devices authenticate each other before exchanging data (e.g., TLS mutual authentication)
3. **Software authentication:** The device verifies that running software is legitimate (e.g., secure boot, signed firmware)
4. **User-to-device:** Users authenticate before accessing device management interfaces

### Certificate-Based Authentication
- Device receives a digital certificate from a trusted Certificate Authority (CA)
- Certificate binds the device's identity to its public key
- During TLS handshake, the device presents its certificate and proves possession of the private key
- The verifier checks the certificate chain up to a trusted root CA

## Key Properties / Complexity

### Challenges in IoT
- **Resource constraints:** Heavy cryptographic protocols may not run on microcontrollers
- **Scale:** Millions of devices need individual identities and credentials
- **Lifecycle management:** Credentials must be provisioned, rotated, and revoked over 10+ year device lifespans
- **Physical exposure:** Devices in uncontrolled environments can be physically tampered with
- **Default credentials:** Many IoT devices ship with admin/admin or root/password — the Mirai botnet exploited exactly this

### Authentication vs. Authorisation
- **Authentication:** "Who are you?" (identity verification)
- **Authorisation:** "What are you allowed to do?" (permission checking)
- Authentication always comes first — you must know who someone is before deciding what they can do

## Worked Example
**IoT Device Joining a Secure Network (ZigBee 3.0):**
1. New device sends a join request to the ZigBee coordinator
2. Coordinator sends a challenge (random nonce)
3. Device computes a response using its pre-shared install code (unique per device)
4. Coordinator verifies the response against the known install code
5. If valid: device receives the network key (encrypted with the install code)
6. Device can now communicate on the network

**What goes wrong without authentication (Mirai):**
1. IoT cameras and routers use default credentials (admin/admin)
2. Botnet scanner tries common username/password combinations
3. Device accepts the login — no identity verification beyond password
4. Device joins the botnet and participates in DDoS attacks

## Common Pitfalls
- Using default credentials — the single most exploited IoT vulnerability
- Confusing authentication with authorisation — they are separate concerns
- Hardcoding credentials in firmware — extractable through reverse engineering
- Not implementing certificate revocation — compromised devices remain trusted
- Assuming physical presence equals trust — physical access enables credential extraction
- Skipping mutual authentication — only the server authenticates to the device, not vice versa

## Connections
- [[digital-signatures]] — Used in certificate-based authentication to prove identity
- [[information-assurance]] — Authentication is one of the seven IA properties
- [[non-repudiation]] — Authentication verifies identity; non-repudiation prevents denial
- [[cia-triad]] — Authentication supports all three CIA properties
- [[mirai-botnet]] — Failure of authentication (default credentials) at massive scale
- [[trusted-platform-module]] — TPMs store authentication credentials securely
- [[firmware-security]] — Software authentication via secure boot and signed updates
- [[iot-device-fundamentals]] — Device identity and credential provisioning
- [[zigbee-pairing-vulnerability]] — Authentication weakness in ZigBee pairing protocol
- [[attack-surface-analysis]] — Admin interfaces are an authentication attack surface

## Open Questions
- How do we handle authentication for devices with 10+ year lifespans when cryptographic standards change?
- Is passwordless authentication (certificates, PUFs) feasible for all IoT devices?
- How do we revoke trust in a compromised device that has already joined a network?
