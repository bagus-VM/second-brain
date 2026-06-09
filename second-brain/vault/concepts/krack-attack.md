---
title: "KRACK Attack"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[iot-attack-taxonomy]]", "[[cia-triad]]"]
---

## One-line Summary
The Key Reinstallation Attack (KRACK, 2017) exploits the WPA2 protocol itself, forcing devices to reuse cryptographic keys and potentially allowing decryption and injection of Wi-Fi traffic.

## Core Intuition
KRACK is devastating because it attacks the protocol standard, not an implementation bug. Every device using WPA2 was vulnerable — the math was correct, but the handshake process could be manipulated to reinstall an already-used key, effectively resetting encryption to a known state.

## Formal Definition / Statement
**KRACK Attack (2017):** Key Reinstallation Attack against the WPA2 protocol, discovered by Mathy Vanhoef. The attacker forces a device to reuse a cryptographic key by manipulating the four-way handshake. When a client installs a key that has already been used, associated nonces (random numbers) can be replayed, potentially allowing:
- Decryption of Wi-Fi traffic (confidentiality violation)
- Packet injection (integrity violation)
- TCP connection hijacking

See: https://www.krackattacks.com/

**Attack classification:** Cryptographic Algorithm and Key Management Attack

## Key Properties / Complexity

### Attack Mechanism
1. WPA2 four-way handshake negotiates a new session key
2. Client sends Message 3 acknowledgment
3. If the access point doesn't receive the ack, it retransmits Message 3
4. Client receives retransmitted Message 3 and reinstalls the same key
5. Key reinstallation resets the nonce (packet number) to zero
6. Attacker can now replay/decrypt packets using the known nonce sequence

### Why It's Fundamental
- **Protocol-level flaw** — not a bug in any specific implementation
- Affects ALL WPA2 implementations (Windows, Linux, Android, iOS, IoT devices)
- The WPA2 standard itself mandated the vulnerable behavior
- Android 6.0 was especially vulnerable (using wpa_supplicant that installed an all-zero key)

### Impact on IoT
- IoT devices typically use Wi-Fi for connectivity
- Many IoT devices cannot be easily patched
- Wi-Fi-based IoT devices in smart homes, healthcare, industry are all affected
- Unlike software bugs, protocol fixes require ecosystem-wide updates

## Worked Example
1. Victim's IoT camera connects to Wi-Fi access point via WPA2 handshake
2. Attacker is within Wi-Fi range, intercepts Message 3 of handshake
3. Attacker blocks Message 3 from reaching the camera, then replays it
4. Camera reinstalls the same key, resetting its nonce counter to 0
5. Attacker now knows the nonce sequence → can decrypt camera's video stream
6. Confidentiality of the IoT camera feed is completely compromised

## Common Pitfalls
- Thinking KRACK is "just a Wi-Fi problem" — it's a protocol design problem
- Assuming WPA2 is secure because the math is correct — the protocol state machine was flawed
- Believing a firmware update "fixes" KRACK — the protocol standard itself needed revision
- Ignoring that many IoT devices will never receive patches

## Connections
- [[iot-attack-taxonomy]] — Cryptographic/key management attack category
- [[iot-common-attacks]] — Major attack case study
- [[iot-connectivity-protocols]] — Wi-Fi protocol vulnerability
- [[information-assurance]] — Violates confidentiality and integrity
- [[mirai-botnet]] — Another landmark IoT attack
- [[zigbee-pairing-vulnerability]] — Another protocol-level vulnerability
- [[ota-updates]] — Patching KRACK requires update mechanisms

- [[iot-lecture-1]] — IoT Security Landscape — course overview
- [[iot-lecture-2]] — IoT Common Attacks — taxonomy
- [[iot-lecture-4]] — IoT Secure Design — best practices

## Open Questions
- How do we design protocols that are provably resistant to state manipulation?
- What is the responsibility of standards bodies when their specifications contain vulnerabilities?
- How do we patch billions of IoT devices that may never receive updates?
