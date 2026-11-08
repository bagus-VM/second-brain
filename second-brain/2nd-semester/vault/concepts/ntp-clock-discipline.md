---
title: "NTP Clock Discipline (the Hybrid PLL/FLL Loop)"
tags: [concept, dependable-distributed-systems, semester-2, clock-synchronization, ntp]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[network-time-protocol]]", "[[time-offset-measurement]]"]
---

## One-line Summary
Once the peers have agreed on an offset, something still has to apply it to a running clock: NTP runs a
phase-locked loop to absorb short-term noise and a frequency-locked loop to remove the oscillator's
long-term rate error, at the same time, on the same clock.

## Core Intuition

By the time the combination step has produced an offset, the hard part looks finished. It is not. An
offset is a measurement of where the clock *is*; correcting it means changing how the clock *runs*, and
those are different operations with opposite failure modes.

Setting the clock to the measured value (a step) fixes the offset in one move and breaks every property
that depends on time moving forward: timers that were near expiry, intervals measured across the jump,
and the monotony item on the lecture's own characterisation list. Correcting the *rate* instead keeps
time continuous but leaves the standing offset in place until the correction has been applied long
enough to work it off — during which the clock is still wrong, just less wrong each second.

The hybrid loop is the answer to both at once. **Phase control** acts on the measured offset and is
good at the short-term component: it responds to whatever the last few measurements say. **Frequency
control** acts on the observed rate error and is good at the long term: it estimates how fast the
oscillator actually runs and corrects it, which is what stops the offset from being re-created every
measurement round. Each alone fails: a pure phase corrector chases measurement noise and has to keep
stepping the clock, while a pure frequency corrector never removes the offset it started with.

## Formal Definition / Statement

**The three process types (slides 29-31).** The architecture slide labels the pipeline as peer
processes, a system process, and a clock process:

| Process | Periodicity | What sets its frequency (rate of operation) |
|---------|-------------|---------------------------------------------|
| **Peer processes** | independent and periodic | determined by the system process and the remote servers |
| **System process** | periodic | determined by the phase jitter and the stability of the local clock |
| **Clock process** | periodically, in 1-second intervals | fixed — it controls the VFO's phase and frequency |

The clock process is the one that touches the hardware: "control VFO phase and frequency". Slide 29's
architecture summary describes the same loop as "Loop filter and VFO: controlled local clock; minimize
jitter and drift in the control loop".

**The discipline algorithm (slide 40).**

- **Control principle:** a **hybrid PLL / FLL control loop**.
- **Aim of the hybrid scheme:**
  - **Frequency control** for compensating frequency errors and long-term fluctuations.
  - **Phase control** for correcting short-term fluctuations.

**Where the offset arrives.** The combination step's output "is passed to the clock control (clock
discipline algorithm)" — the discipline loop consumes a corrected offset, not raw measurements.

## Key Properties

- **Two error components, two control paths.** Offset (phase) and rate (frequency) are corrected by
  different halves of the loop; fixing one leaves the other.
- **Phase control is fast and noisy.** It answers to the latest measurements, so measurement noise
  enters the clock directly unless it is filtered — which is what the peer filter's 8-sample window is
  for.
- **Frequency control is slow and permanent.** It estimates the oscillator's rate error and removes it,
  so the offset stops being regenerated. This is the part that makes the correction last.
- **The clock process runs at 1-second intervals regardless of the peer polling rate.** Peers can poll
  on the order of minutes; the loop that steers the oscillator runs every second.
- **Loop stability is an explicit goal.** Slide 29's phrase is "minimize jitter and drift in the control
  loop" — a badly tuned loop introduces jitter of its own.
- **The output is a disciplined clock, not a corrected variable.** Applications read the system clock;
  no application is told the offset.
- **A control loop with feedback can oscillate.** The system process's own period is set by the phase
  jitter and the local clock's stability, which is a stability trade-off rather than an arbitrary
  choice.
- **Everything above this page is measurement; everything below is hardware.** The discipline loop is
  the boundary where a computed number becomes a physical rate change.

## Worked Example

Computed with `python`; the arithmetic is in this vault's own exercise-3 material
(`study/homework/dependable-distributed-systems/clock-sync.py` uses the same unit conventions).

**What a 100 ppm frequency error means.** 100 ppm is a fractional rate error of 1 × 10⁻⁴, i.e. the
clock gains 100 microseconds for every second of real time:

| Interval | Time gained by an uncorrected 100 ppm clock |
|----------|--------------------------------------------|
| 1 second | 0.0001 s = 100 µs |
| 1 hour | 0.36 s |
| 1 day | **8.64 s** |
| 1 week | 60.48 s |
| 1 year | ≈ 3153.6 s ≈ 52.6 minutes |

**What phase-only correction would have to do.** To remove 8.64 s per day without stepping the clock
backwards, the loop must run the oscillator *fast* by an extra amount for a while: spreading the
correction over one full day requires an extra rate of 8.64 s / 86400 s = 1 × 10⁻⁴ = **100 ppm** — the
same magnitude as the error being corrected. Practically: to erase one day's worth of a 100 ppm error,
the loop has to spend a day running the clock at 200 ppm and then settle at the correct rate. If the
correction is spread over an hour instead, the required rate change is 24× larger (8.64/3600 = 2.4 ×
10⁻³ = 2400 ppm) for that hour. **The faster you fix the offset by phase alone, the more violently the
clock's rate has to be disturbed** — which is exactly why the frequency half of the loop exists, and
why the lecture names long-term fluctuations as the frequency half's responsibility.

**And why the offset alone is not enough.** With the frequency error uncorrected, the offset comes back
at 8.64 s per day. A loop that only ever applied phase corrections would be correcting the same error
forever, at a rate limited by how much rate disturbance it dares to introduce.

**The DST question (exercise 3.4d).** NTP distributes **UTC**, which has no daylight-saving component.
The ±1 hour shift twice a year is applied by the operating system from the timezone database at the
moment of display, so the discipline loop never sees it and never corrects it — there is nothing in the
protocol for DST to disturb. The distinction worth keeping: DST is a change in the local *label*;
a leap second is a change in UTC itself, and that one reaches the protocol.

## Common Pitfalls

- **Assuming NTP sets the clock.** It disciplines the local oscillator; the clock process steers phase
  and frequency rather than assigning a value.
- **Expecting one control loop to do both jobs.** Frequency control without phase control leaves the
  standing offset; phase control without frequency control re-corrects the same drift forever.
- **Forgetting that phase correction moves time.** A phase correction applied as a step breaks monotony;
  the lecture's own characterisation list asks about exactly this.
- **Confusing the polling interval with the discipline interval.** Peers poll on their own schedule; the
  clock process runs at 1-second intervals.
- **Assuming a faster correction is strictly better.** The worked example: halving the correction window
  doubles the rate disturbance, and the loop's stability is an explicit design goal.
- **Blaming the oscillator for a persistent offset.** An uncorrected *frequency* error looks like a
  permanent offset that keeps coming back.
- **Expecting DST to appear in the protocol.** It does not; NTP carries UTC and the OS renders local
  time.
- **Treating jitter and drift as the same thing.** Jitter is short-term variation (phase control's
  problem); drift is a persistent rate error (frequency control's).

## Connections

- [[network-time-protocol]] — the stages that produce the offset this loop consumes.
- [[time-offset-measurement]] — where delta and theta (and therefore the phase error the loop acts on)
  come from.
- [[physical-clock-drift]] — offset versus frequency error, and why the frequency error is the dangerous
  one; this page is the mechanism that answers it.
- [[tai-utc-time-scales]] — the scale the protocol carries, and why leap seconds (unlike DST) reach the
  protocol.
- [[convergence-algorithm-cnv]] — the contrasting approach: no reference clock and no oscillator to
  steer, just convergence of the group to a common value.
- [[dependable-distributed-systems-exercise-3]] — task 3.4(b) asks where a clock protocol belongs in
  the stack, which is this page seen from the implementation side, and 3.4(d) is the DST question.
- [[runtime-system]] — the kernel-level machinery a disciplined clock actually lives in.
- [[dependable-distributed-systems-lecture-3]] — the source lecture, slides 29-31 and 40.

## Open Questions

- **No PLL/FLL parameters are given.** Loop gain, time constants, the maximum slew rate, and the
  conditions under which NTP steps rather than slews the clock are all absent from the deck.
- **"Phase jitter and stability of the local clock" is stated qualitatively.** No formula for the system
  process's period is given, and no stability criterion for the loop.
- **The VFO is named and not described.** What a voltage- or frequency-controlled oscillator looks like
  on modern hardware — where the clock is usually a counter driven by a crystal — is not discussed.
- **No bound on achievable accuracy from the loop itself**, as distinct from the network measurement
  accuracy quoted on slide 26 (about 0.01 s WAN, below 1 ms LAN).
- **The interaction with leap seconds is not covered.** Whether the discipline loop steps through
  23:59:60 or smears the correction is not stated in the ingested material, and this is left open on
  [[tai-utc-time-scales]] too.
- **DST is not mentioned anywhere in the deck** — the answer above follows from the protocol carrying
  UTC; the lecture itself only asks the question in the exercise sheet.