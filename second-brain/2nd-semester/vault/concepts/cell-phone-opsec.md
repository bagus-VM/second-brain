---
title: "Cell Phone OPSEC"
tags: [concept, advanced-it-security, semester-2, operational-security, mobile-security]
course: "Advanced IT Security"
source_count: 2
status: current
last_updated: 2026-10-29
prerequisites: ["[[gsm-security-political-constraints]]", "[[advanced-it-security-lecture-0]]"]
---

## One-line Summary
The closing slides argue that a device which is uniquely identified, geo-trackable, a listening device, a secret store, a behaviour monitor and an archive cannot be made private by software alone, and answer the phone-privacy question with an operational-security procedure for both peers.

## Core Intuition

The "Private phone calls?" slide lists six properties of a smartphone, each a statement about the device rather than about an app: a uniquely identified device (IMEI, IMSI, WLAN-MAC, ...); a real-time geo-location tracking device (GPS and WLAN beacons); a remote listening device (voice and sound fingerprinting); storage for intimate secrets (email, pictures); a monitor for the owner's behaviour (gait analysis); and everything you do with it — calls, messages, pictures, motion — can be monitored, collected, and archived. The slide then asks the question the section answers.

None of the six is a software setting, so the lecture answers with operating security: protecting the operation rather than the message. The two "Cell Phone OPSEC" slides address both peers and explicitly allow "a larger time delay before operation". The delay is part of the design — the procedure trades speed for deniability, moving the exchange beyond the reach of the identification and location properties above.

## Formal Definition / Statement

The procedure, as the slide states it, for both peers: exchange an OTP string (directly, or at least with a tamper-evident package); analyse daily movements, paying attention to anchor points (home or work) and dormant periods in schedules (8–12 p.m., or when cell phones aren't changing locations); leave the daily cell phone behind during dormant periods and purchase a prepaid no-contract "burner phone" months ahead; the phone should be as dumb as possible and bought from a small shop without surveillance cameras; pay with cash and pay attention to where the cash comes from; never turn the phone on in or around home, and remove the battery when it is not being used; encrypt the cell phone number with a one-time-pad (OTP) system and rename an image file with the encrypted code; use Tor to hide web traffic and post that image to an agreed account (Twitter, Facebook, ...), which signals a communications request to the partner; leave the cell phone behind, avoid anchor points, and receive a phone call (no SMS) from the partner on the burner phone at a pre-arranged "dormant" time on the following day; use a speech generator to say the words to be exchanged; prefer signalling over operational data, in the slide's own ordering, "signaling > open codes > plain talk"; wipe down and destroy the handset and dispose of it with extreme prejudice.

## Key Properties

- Every step is shared: the rules apply to both peers, and the procedure fails if either side deviates.
- Explicit slack. The framing clause "allow for a larger time delay before operation" makes latency a design parameter rather than a cost to be minimised.
- Timing and location are the load-bearing variables: anchor points, dormant periods, and a call the following day at a pre-arranged dormant time.
- The procurement chain is part of the attack surface: prepaid, no contract, months ahead, dumb phone, camera-free small shop, and cash whose origin also matters.
- The channel carries a request, not a payload, and the medium is restricted to a call with explicitly no SMS.

## Worked Example

Trace the OTP-plus-image-file channel. Before any operation the two peers exchange the OTP string, directly or in a tamper-evident package; this is the only step in which the secret exists outside the communications channel. On the day, peer A writes down the burner number to be called, encrypts it with the one-time pad, renames an image file with the resulting code, and posts the image to the account the two agreed on, using Tor to hide the web traffic. Peer B watches that account, reads the code from the filename, and decrypts it with the same pad to recover the number.

What an observer holding only the public post learns is limited to the post: that an image was posted to that account, at a time, with a filename that is a string of characters, plus the image content and whatever account metadata the platform publishes. Because the pad is one-time, the filename reveals the number only to someone holding the same pad, and Tor is what keeps the poster's network identity out of the picture. What the observer cannot learn is the number, hence who is to be called. What the post still is, in the slide's vocabulary, is a signal: its occurrence and timing say that a communications request was made, which is why the scheme depends on the agreed account not being attributable to either peer.

## Common Pitfalls

- Reading the six properties as six separate problems and treating one of them, location say, as the only threat, when the slide's list is cumulative.
- Assuming an encrypted-call app fixes the requirement: the first property (IMEI, IMSI, WLAN-MAC) and the last (monitoring, collection, archiving) survive an encrypted call.
- Treating the OTP channel as secure communication rather than as a communications request, when the payload avoids the channel and only the request is public.
- Reading the procedure as a guaranteed method: the slide names no threat model and states no success or failure criterion.

## Connections

- [[gsm-security-political-constraints]] — the IMSI catcher and location-history material explaining why identification and location are the properties to defeat.
- [[advanced-it-security-lecture-0]] — the lecture whose closing section this procedure belongs to.
- [[attacker-classification]] — the deck's attacker classes; the OPSEC slides name none, so no mapping to them is given.
- [[risk-perception-and-dread-risk]] — why fear and dismissiveness are equally poor guides to the effort such procedures cost.
- [[security-terminology-and-risk-model]] — the vocabulary in which the six device properties are risk statements.

## Open Questions

- The slides name no threat model: not who the procedure is meant to defeat, how capable that adversary is, or which of the six properties each step addresses.
- No success or failure criterion is given, and the deck does not say how the peers would detect that an operation has been broken.
- The pad's one-time property is stated for the encrypted number, but not how the pad exchange, or one peer being compromised, is handled.
- Whether "dormant periods" are read from the peers' own schedules or from an adversary's observed coverage is ambiguous in the slide's wording, "8-12 p.m. or when cell phones aren't changing locations".
