---
title: "OTA Updates"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[security-by-design]]", "[[firmware-security]]"]
---

## One-line Summary
Over-The-Air (OTA) updates are the mechanism for remotely updating IoT device firmware and software — a critical security capability but also a significant attack surface if not properly secured.

## Core Intuition
OTA updates are IoT's "immune system" — the only way to fix vulnerabilities on devices that are deployed in the field, often physically inaccessible. But if the update mechanism itself is compromised, attackers can push malicious firmware to millions of devices at once.

## Formal Definition / Statement
**OTA Updates:** Over-The-Air updates allow firmware and software patches to be installed on IoT devices remotely, without physical access. As a secure design goal, updates should:
- Be installed without consuming additional bandwidth
- Be **authenticated** (only signed updates accepted)
- Be **encrypted** (update content not interceptable)
- Come from **write-protected source locations**

## Key Properties / Complexity

### Miessler's Update Mechanism Attack Surface (Class 11)
- **Updates sent unencrypted** — Firmware intercepted or modified in transit
- **Updates not hash signed** — No integrity verification; attacker can inject malicious firmware
- **Source location writable** — Attacker can redirect update server to malicious source

### Security Requirements
1. **Authentication:** Verify the update came from the legitimate vendor
2. **Integrity:** Verify the update hasn't been modified (hash/signature)
3. **Encryption:** Protect update content from eavesdropping
4. **Rollback protection:** Prevent downgrade to vulnerable versions
5. **Atomic updates:** Either fully applied or not at all (no partial states)

### Challenges in IoT
- Limited bandwidth (LoRaWAN, ZigBee)
- Limited storage (can't download large updates)
- Limited power (updates must not drain battery)
- Devices may be offline for extended periods
- Heterogeneous device fleet (different hardware, different firmware)

## Worked Example
**Secure OTA Update Flow:**
1. Vendor builds firmware update, signs with private key
2. Update package pushed to update server
3. IoT device checks for updates periodically
4. Device downloads update over TLS
5. Device verifies signature using embedded public key
6. Device applies update to secondary partition (A/B update)
7. Device reboots into new firmware
8. If boot fails → automatic rollback to previous partition

**Insecure OTA (what NOT to do):**
1. Vendor posts firmware on HTTP server
2. Device downloads and applies without verification
3. Attacker MITM the connection → pushes malicious firmware
4. All devices compromised simultaneously

## Common Pitfalls
- Not signing firmware updates (Mirai-class vulnerability)
- Using HTTP instead of HTTPS for update delivery
- Not implementing rollback protection (downgrade attacks)
- Not handling interrupted updates (bricked devices)
- Assuming devices will always have connectivity for updates

## Connections
[[digital-signatures]] — firmware images are signed and verified before installation
- [[firmware-security]] — OTA updates protect firmware integrity
- [[security-by-design]] — OTA is a secure design goal
- [[devops-security]] — OTA enables continuous delivery for IoT
- [[operational-security-lifecycle]] — Firmware management in Operate phase
- [[attack-surface-analysis]] — Update mechanism is attack surface class 11
- [[krack-attack]] — Example of a vulnerability requiring OTA patching
- [[iot-compliance-frameworks]] — Patch management is a compliance requirement

## Open Questions
- How do we handle updates for devices with intermittent connectivity?
- What's the right update frequency (security patches vs. stability)?
- Who is responsible for updates after a manufacturer exits the market?
