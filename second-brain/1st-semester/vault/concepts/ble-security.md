---
title: "BLE Security"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[iot-communication-protocols]]"]
---
## One-line Summary
Bluetooth Low Energy (BLE) security covers the pairing modes, encryption mechanisms, and known vulnerabilities of the protocol that connects billions of wearables, sensors, and smart-home devices.

## Core Intuition
BLE was designed for low power, not high security. Its "Just Works" pairing mode — the most commonly used — provides zero authentication, making it trivially vulnerable to man-in-the-middle attacks. Even with stronger pairing modes, BLE has a history of implementation-level vulnerabilities (KNOB, BIAS, SweynTooth) that undermine the protocol's cryptographic guarantees. Understanding BLE security means understanding both the protocol spec and the gap between spec and real-world implementations.

## Formal Definition / Statement
BLE (Bluetooth Low Energy, Bluetooth 4.0+) is a wireless protocol operating in the 2.4 GHz ISM band with a typical range of 10-50 meters and data rates of 125kbps-2Mbps.

**BLE Security Architecture:**

**Pairing Modes (LE Legacy Pairing):**
1. **Just Works**: No authentication. Vulnerable to MITM. Used for devices without display or keyboard (sensors, beacons).
2. **Passkey Entry**: 6-digit PIN entered on one or both devices. Provides MITM protection if PIN is not eavesdroppable. 20-bit entropy.
3. **Numeric Comparison**: Both devices display a 6-digit number; user confirms match. MITM protection. BLE 4.2+ only.
4. **Out-of-Band (OOB)**: Key exchange via NFC or other non-BLE channel. Strong MITM protection if OOB channel is secure.

**LE Secure Connections (BLE 4.2+):**
- Replaces legacy pairing with ECDH (P-256) key exchange
- Numeric Comparison, Passkey Entry, and OOB modes provide authenticated key exchange
- Just Works still unauthenticated (provides encryption but no MITM protection)
- Generates Long-Term Key (LTK) for link encryption

**Encryption:**
- AES-128-CCM for link-layer encryption
- Session key derived from LTK during encryption setup
- Encryption is hop-by-hop (each link in a mesh/piconet encrypted separately)

**BLE Mesh Security:**
- Application-level security with Application Keys (AppKeys)
- Network-level security with Network Key (NetKey)
- Device-specific security with Device Key (DevKey)
- AES-128-CCM at network and application layers

## Key Properties / Complexity

- **Just Works is the default** for most IoT devices because they lack displays/keyboards — this means most BLE IoT devices have no MITM protection
- **KNOB Attack (CVE-2019-9506)**: Forces encryption key entropy down to 1 byte, making brute-force trivial. Affects all BLE versions.
- **BIAS Attack (CVE-2020-10135)**: Allows impersonation of previously paired devices by exploiting role-switching during reconnection.
- **SweynTooth**: Family of vulnerabilities in BLE SDK implementations (Texas Instruments, NXP, Dialog Semiconductor) causing crashes, security bypasses, and arbitrary code execution.
- **MAC address tracking**: BLE devices often use static MAC addresses, enabling physical tracking even without breaking encryption.
- **BLE has no native authentication** — identity is based on stored bonding keys, which can be stolen from device storage.
- **Range extension attacks**: Directional antennas can extend BLE range to 1km+, defeating proximity assumptions.
- **GATT profile manipulation**: Unauthorized modification of GATT service characteristics can alter device behaviour.

## Worked Example

**BLE Smart Lock Attack:**
1. Attacker uses Ubertooth to sniff BLE pairing between phone and smart lock
2. Lock uses "Just Works" pairing (no authentication)
3. Attacker performs MITM during pairing, obtains LTK
4. Attacker clones the phone's BLE identity
5. Attacker sends unlock command to the lock
6. Lock has no way to distinguish attacker from legitimate phone

**Mitigation with LE Secure Connections:**
1. Lock supports Numeric Comparison pairing
2. User verifies 6-digit code matches on phone and lock display
3. ECDH key exchange prevents MITM from obtaining shared secret
4. Even if LTK is later compromised, past sessions remain encrypted (forward secrecy)

## Common Pitfalls

- Relying on "Just Works" pairing for security-critical applications (locks, medical devices)
- Using static BLE MAC addresses that enable tracking
- Not implementing BLE encryption at all (some devices transmit in cleartext)
- Assuming BLE range is limited to 10 meters (antenna attacks extend to 1km+)
- Not validating GATT service access controls
- Ignoring SDK-level vulnerabilities (SweynTooth class)
- Using BLE 4.0 legacy pairing instead of LE Secure Connections

## Connections

- [[iot-communication-protocols]] — BLE in the context of other IoT protocols
- [[zigbee-security-model]] — Compare mesh security approaches
- [[krack-attack]] — Similar protocol-level key reinstallation concept
- [[side-channel-attacks]] — BLE radio can be analyzed for side-channel leakage
- [[smart-home-security]] — BLE is dominant in consumer IoT
- [[iot-lecture-2]] — BLE exploitation in the protocol attacks taxonomy
- [[device-provisioning]] — BLE pairing as a provisioning mechanism

## Open Questions
- Will BLE 6.0's Channel Sounding (distance bounding) mitigate relay/range extension attacks?
- Can BLE Mesh security scale to city-wide deployments without key management overhead?
- How do we handle BLE security for devices that will be in the field for 10+ years?
