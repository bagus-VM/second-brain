---
title: "The Merkle–Damgård Construction"
tags: [concept, advanced-it-security, semester-2, cryptography]
course: "Advanced IT Security"
source_count: 2
status: current
last_updated: 2026-11-07
prerequisites: ["[[cryptographic-hash-functions]]"]
---

## One-line Summary

Hash functions of arbitrary input length are built by iterating a fixed-size compression function
over padded input blocks, so hᵢ = f(xᵢ ‖ hᵢ₋₁) from a fixed initial value h₀ — which is why every
MD5/SHA-1/SHA-2 design is structurally the same, and why their collisions were found in the
compression function.

## Core Intuition

You cannot design a function for arbitrary-length input directly; you can design one for a fixed
block. The construction is the bridge, and it is a chain: each block is mixed into the running
state, and the final state is the digest. The whole security of the resulting function reduces to
the security of the compression function plus the assumption that chaining does not create new
weaknesses.

The other half of the intuition is that the construction *fixes* the input length rather than
absorbing it. Padding is what forces the input onto block boundaries, and the padding rule is a
design decision with security consequences (length-extension attacks, for instance), which the
lecture does not mention.

## Formal Definition / Statement

The slide's construction, verbatim:

- "The core of the hash function is a compression function f that works on fixed size input blocks."
- "An input x of arbitrary length is broken up into blocks x₁, …, xₘ of the given block size; the
  last block has to be padded."
- "Compute the hash of x by repeatedly applying the compression function: with a (fixed) initial
  value h₀, compute hᵢ = f(xᵢ ‖ hᵢ₋₁) for i = 1, …, m and take hₘ as the hash value of x."
- "The symbol '‖' denotes concatenation."

**The architecture slide** adds the shape of a single step: a message block and an "intermediate
value" enter the compression function g, and an intermediate value leaves; the last one is the hash
value.

**The internals slide** says what is inside the compression function and, more usefully, what is
*not*: "lots of (fast) operations (rotations, ⊕, ∧, ∨, +, …)" and "no good theory for general
design (so far)". The concrete example is SHA-512's round function:

Ch(e, f, g) = (e AND f) XOR (NOT e AND g)
Maj(a, b, c) = (a AND b) XOR (a AND c) XOR (b AND c)
Σ(a) = ROTR(a, 28) XOR ROTR(a, 34) XOR ROTR(a, 39)
Σ(e) = ROTR(e, 14) XOR ROTR(e, 18) XOR ROTR(e, 41)
σ₀(x) = ROTR(x, 1) XOR ROTR(x, 8) XOR SHR(x, 7)
σ₁(x) = ROTR(x, 19) XOR ROTR(x, 61) XOR SHR(x, 6)

— chosen for diffusion and cheapness, not derived from any hardness assumption.

## Key Properties

**The design has no security proof, and the slide says so.** "No good theory for general design (so
far)" is the honest statement of the situation: the construction reduces the problem to the
compression function, and the compression function is then argued for by cryptanalysis rather than by
theorem. This is why the field is littered with broken schemes.

**The list of casualties is long and instructive.** "Loads of (50+) broken schemes: Rabin, Jueneman,
X.509 Annex D, FFT-hash I and II, N-hash, Snefru, MD2, …". Then the generations: "fast schemes for
32-bit machines: popular early designs (broken): MD4 and MD5; US government (NIST): SHA-*; Europe:
RIPEMD-160"; and "current generation: SHA-512, Whirlpool, …, SHA-3 (Keccak)".

**The iteration is what makes the digest cheap and streaming.** Each block is processed once with a
fixed-size state, so memory is constant regardless of input length — the property that makes hashing
a multi-gigabyte file practical, and the reason the "ease of computation" property is achievable at
all.

**Padding is part of the specification, not an implementation detail.** The slide says only "the last
block has to be padded"; the standard construction appends a 1 bit, zeros, and the message length,
which is exactly what prevents two different messages from producing the same block sequence. Without
the length field, the construction would be ambiguous — and the way the padding ends is also the
mechanism behind length-extension weaknesses.

**The output size is the state size, not the block size.** MD5's state is 128 bits with 512-bit
blocks; SHA-1's is 160 with 512; SHA-512's is 512 with 1024. The birthday bound applies to the
*output* size, so the block size buys nothing against collisions.

## Worked Example

**The chain, written out for a three-block message.** With block size 512 and state size 128 (MD5's
parameters), padding a message to three blocks gives:

```
h₀ = IV (fixed, specified in the standard)
h₁ = f(x₁ ‖ h₀)
h₂ = f(x₂ ‖ h₁)
h₃ = f(x₃ ‖ h₂)      ← the digest is h₃
```

Three applications, constant memory, one pass. Now suppose an attacker finds a collision in the
compression function: two distinct blocks a ≠ a′ with f(a ‖ h) = f(a′ ‖ h) for the *same* incoming
state h. Substituting a′ for a leaves every later hᵢ unchanged, so the two full messages collide. That
is the mechanism by which "collisions for the compression function" (Dobbertin 1996, MD5) escalates
into message collisions — the construction propagates a local break to a global one, which is exactly
why MD5's history reads the way it does:

| Year | Event |
|---|---|
| 1991 | MD5 published by Rivest |
| 1993 | pseudo-collision (den Boer et al.), "limited practical value" |
| 1996 | collision on the compression function (Dobbertin) — "in the future MD5 should no longer be implemented … where a collision-resistant hash function is required" |
| 2004 | identical-prefix collisions: two 128-byte messages with the same hash |
| 2006 | chosen-prefix collisions: two arbitrary files, 716 "random" bytes appended |
| 2008 | practical collision attack generating SSL certificates with the same MD5 hash |
| 2009 | theoretical pre-image attack, O(2^123.4) |

## Common Pitfalls

- **Confusing the block size with the digest size.** Security scales with the digest; the block size
  only affects speed and padding.
- **Treating the construction as a security proof.** It only reduces the question to the compression
  function, and the slide states that no general theory exists.
- **Ignoring the IV.** Different IVs make different functions from the same compression function;
  that is how SHA-256's variants are parameterised, and why "the same algorithm" can have several
  digests.
- **Forgetting padding when reasoning about collisions.** Two messages collide if their *padded*
  block sequences do; a message that is a prefix of another is not automatically related.
- **Assuming a compression-function collision implies a message collision without the same incoming
  state** — the propagation needs equal h in both branches.
- **Assuming newer constructions are Merkle–Damgård.** SHA-3 (Keccak) is a sponge construction, and
  the slide lists it separately for that reason.

## Connections

- [[cryptographic-hash-functions]] — the properties this construction is supposed to deliver.
- [[birthday-bound]] — the output-size arithmetic that determines how much collision security the
  digest has.
- [[hmac]] — the keyed construction built *on top of* an iterated hash, and the reason its nesting is
  shaped the way it is.
- [[advanced-it-security-lecture-2]] — the deck that presents it.
- [[mdc-vs-mac]] — the unkeyed/keyed distinction the construction sits underneath.

## Open Questions

- **The padding rule is not specified in the deck** ("the last block has to be padded" is all it
  says), so the length-extension weakness of Merkle–Damgård hashes is not explained here.
- **No comparison with sponge constructions is offered**, although SHA-3 is listed.
- **"No good theory for general design" is asserted without discussing the indifferentiability
  results** that partially justify the iteration.
- **The performance slide is an image with no extracted numbers**, so no throughput figures are
  available from this deck.
- **Whether the exam requires the SHA-512 round-function expressions** (Ch, Maj, Σ, σ) or only the
  chain structure is not indicated.