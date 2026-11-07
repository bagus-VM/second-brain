---
title: "The Birthday Bound for Hash Collisions"
tags: [concept, advanced-it-security, semester-2, cryptography]
course: "Advanced IT Security"
source_count: 2
status: current
last_updated: 2026-11-07
prerequisites: ["[[cryptographic-hash-functions]]", "basic probability"]
---

## One-line Summary

For an n-bit hash, finding a pre-image costs about 2ⁿ work but finding *a* collision costs only
about 2^(n/2) — the birthday paradox — so the security of a digest is half its bit-length against
collisions.

## Core Intuition

The counter-intuitive part is that a collision does not need a target. Finding a message that hashes
to a *specified* value requires searching 2ⁿ candidates; finding *two* messages that hash to the same
value requires nothing specified at all, and among m hashed messages there are m(m−1)/2 pairs, each a
candidate collision. Pair counts grow quadratically, so m only has to grow like √(2ⁿ).

The pigeonhole in a birthday party is the standard analogy: with 23 people in a room, some pair
sharing a birthday is more likely than not, even though the chance that any *specific* person shares
*yours* is tiny. The lecture phrases the general case as an urn problem: "put m balls numbered 1 to m
into an urn; draw a ball, list its number, and put it back; repeat; for m → ∞, the expected number of
draws before a previously drawn number appears is …" — the answer being ≈ √(πm/2).

## Formal Definition / Statement

The slide's three statements, in its own wording:

- "It depends on the bit-length of the hash how probable it is to find collisions by accident."
- "Given an n-bit hash y, the expected number of tries before an x with h(x) = y is found is 2ⁿ."
- "Given n-bit hash values, a set of 2^(n/2) inputs is likely to contain a pair causing a collision."

**The complexity table**, which is the examinable form:

| Attack | Output size n bits | Average complexity |
|---|---|---|
| Pre-image | n | O(2ⁿ) |
| Second pre-image | n | O(2ⁿ) |
| Collision ("birthday attack") | n | O(2^(0.5n)) |

**The slide's illustration of what those exponents mean**, assuming "1 Gops/s, 100 parallel
ops/unit, 1000 units" — i.e. 10¹⁴ operations per second:

| Work | Time at 10¹⁴ ops/s |
|---|---|
| 2⁶⁴ ops | about 50 hours |
| 2⁸⁰ ops | about 380 years |
| 2¹²⁸ ops | about 10¹⁷ years |

All three figures check out arithmetically: 2⁶⁴/10¹⁴ s ≈ 1.8·10⁵ s ≈ 51 h; 2⁸⁰/10¹⁴ s ≈ 1.2·10¹⁰ s
≈ 3.8·10² years; 2¹²⁸/10¹⁴ s ≈ 3.4·10²⁴ s ≈ 1.1·10¹⁷ years.

## Key Properties

**The bound is the design rule for digest sizes, and the numbers show why.** A 128-bit hash gives
only 2⁶⁴ collision security — 50 hours on the slide's hypothetical machine — which is why MD5's
128-bit output was dead long before a pre-image was found, and why SHA-256 (128-bit collision
security) is the current floor.

**"Birthday attack" is in scare quotes for a reason: there is no attack.** Nothing is broken; the
quadratic pair counting is a property of any compressing function. Only the *engineering* of finding
the pair efficiently (memory, sorting, distinguished points) is an attack technique.

**The exact constant is √(2·2ⁿ·ln 2), not 2^(n/2).** For n = 32 the rule of thumb gives 2¹⁶ = 65 536
tries, the exact expectation is √(2·2³²·ln 2) ≈ 77 163 — a factor of 1.18. The lecture uses the
2^(n/2) form, and the exact value is worth knowing because it is the version that can be computed.

**Collision *resistance* is a claim about feasibility, not existence.** A hash function that compresses
necessarily has collisions (infinitely many inputs, finitely many outputs); the property is that
finding one is computationally infeasible. The sheet's true/false item makes exactly this point:
"a collision-resistant hash function guarantees that collisions do not exist" — false.

## Worked Example

**The 32-bit case, in full** (the exercise sheet's question, computed): n = 32 bits gives 2³² =
4 294 967 296 possible digests. Against a specified digest, expect 2³² ≈ 4.3·10⁹ evaluations; for any
collision, expect ≈ 2¹⁶ = 65 536 by the bound, or √(2·2³²·ln 2) = 77 162.7 ≈ 77 163 exactly.

At a modest 10⁷ hashes/s that is 7.7 milliseconds for a collision and 430 seconds for a pre-image.
The gap of ~2¹⁶ is the whole lesson: on a 32-bit digest, "find any two messages that collide" is
trivial while "find a message with this digest" is merely slow.

**The MD5 case, as the lecture tells it**, is the same arithmetic with real engineering behind it:
identical-prefix collisions (Wang, Feng, Lai, Yu 2004) gave "two 128-byte messages with same hash" and
"MD5(A|M|B) = MD5(A|M′|B) (i.e. two messages differ in 128 consecutive 'random' bytes)"; chosen-prefix
collisions (Stephens et al. 2006) allowed "two arbitrary (same-length) files; append 716 'random'
bytes to make them collide"; and the theoretical pre-image attack of 2009 was O(2^123.4) — far above
the birthday bound, which is why MD5 died from collisions, not from pre-images.

## Common Pitfalls

- **Quoting 2ⁿ for collision security.** The whole point of the bound is the halving; a 256-bit hash
  gives 128-bit collision resistance.
- **Confusing "collision exists" with "collision is findable".** Compression makes the first certain
  and the second the property that matters.
- **Assuming a birthday attack is a cryptanalytic break.** It applies to an ideal hash; a real break
  (MD5, SHA-1) is faster than the bound, which is what makes it a break.
- **Using the bound for pre-images.** Pre-image and second pre-image stay at 2ⁿ; only the
  free-both-inputs problem halves.
- **Ignoring memory.** The naive collision search needs to store ~2^(n/2) digests; memory, not time,
  is often the binding constraint in practice (the slide does not discuss it).
- **Applying 2^(n/2) to password hashing.** A salted password hash is a pre-image problem per
  password, which is why salt and slow KDFs are the relevant defences, not digest length alone.

## Connections

- [[cryptographic-hash-functions]] — the three resistance properties whose costs this page quantifies.
- [[merkle-damgard-construction]] — the structure that makes a digest's *effective* bit-length a
  question at all (length extension and padding matter here).
- [[mdc-vs-mac]] — why a digest that can be collided is not an authentication mechanism.
- [[advanced-it-security-lecture-2]] — the deck that introduces the bound.
- [[advanced-it-security-exercise-2]] — question 2(d), where the count and the bound were computed.
- [[unconditional-vs-conditional-security]] — the resource model that makes O(2^(n/2)) a security
  claim at all.

## Open Questions

- **The urn formula is printed as garbled text** in the deck ("the expected number of draws before a
  previously drawn number appears is …" with the expression lost in extraction); the standard result
  ≈ √(πm/2) is not verified against the slide.
- **The slide's 10¹⁴ ops/s assumption is never justified**, and it excludes memory costs entirely.
- **Whether the course expects the exact constant or the 2^(n/2) rule of thumb** in an answer is not
  stated; the slide gives the rule of thumb and the exercise sheet asks only for the count.
- **Quantum speed-ups (Grover, 2^(n/3) for collisions)** are not mentioned anywhere in the material,
  although they change the sizing argument.