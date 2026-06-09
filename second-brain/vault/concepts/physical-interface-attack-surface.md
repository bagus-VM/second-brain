---
title: "Physical Interface Attack Surface"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[attack-surface-analysis]]"]
---

## One-line Summary
The physical interface attack surface covers all hardware interfaces (JTAG, UART, USB, serial) on IoT devices that can be exploited for firmware extraction, privilege escalation, or resetting to insecure states.

## Core Intuition
If an attacker can touch your IoT device, they can probably own it. Physical interfaces designed for debugging, programming, and maintenance are often left exposed in production devices, giving attackers direct access to firmware, memory, and system configuration.

## Formal Definition / Statement
**Physical Interface Assessment (Miessler Class 3):**
1. **Firmware extraction** — Dumping firmware via physical access (JTAG, SPI flash, UART)
2. **User CLI** — User-level command-line interfaces exposed via serial/UART
3. **Admin CLI** — Administrative command-line interfaces exposed via physical ports
4. **Privilege escalation** — Gaining higher access through physical interfaces
5. **Reset to insecure state** — Factory reset leaving device in vulnerable state (default credentials, open services)

## Key Properties / Complexity

### Common Physical Interfaces
| Interface | Purpose | Risk |
|-----------|---------|------|
| JTAG/SWD | Hardware debugging | Full memory access, register control |
| UART/Serial | Console access | CLI shell, log output |
| SPI/I2C | Flash memory access | Firmware extraction |
| USB | Peripheral connectivity | Code execution, data exfiltration |
| SD card | Storage expansion | Firmware modification |

### Why It's Dangerous
- Direct access to hardware bypasses all software security
- Firmware extraction enables reverse engineering and vulnerability discovery
- Admin CLI gives full device control
- Factory reset can restore default credentials (enabling [[mirai-botnet|Mirai-class]] attacks)

## Worked Example
**JTAG Attack on IoT Camera:**
1. Attacker opens camera housing
2. Identifies JTAG header on PCB
3. Connects JTAG debugger
4. Dumps entire flash memory
5. Reverse engineers firmware in Ghidra
6. Finds hardcoded root password
7. Gains root shell via UART console
8. Camera fully compromised — video stream accessible, can be used in botnet

## Common Pitfalls
- Shipping production devices with exposed/unpopulated JTAG headers
- Not disabling debug interfaces in firmware
- Factory reset restoring default credentials
- Assuming physical security (devices in the field are often physically accessible)

## Connections
- [[attack-surface-analysis]] — Part of Miessler's 15 classes
- [[device-memory-attack-surface]] — Physical access enables memory extraction
- [[firmware-security]] — Physical interfaces enable firmware extraction
- [[mirai-botnet]] — Factory reset → default credentials → botnet recruitment
- [[security-by-design]] — Physical security must be designed in
- [[iot-security-hardware]] — Hardware security measures to mitigate

## Open Questions
- Should all physical interfaces be permanently disabled in production?
- How do we balance field serviceability with physical security?
- Can tamper-evident enclosures provide sufficient protection?
