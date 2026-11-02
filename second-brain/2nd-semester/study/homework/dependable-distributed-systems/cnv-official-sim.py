#!/usr/bin/env python3
"""Run the professor's own CNV simulator (raw/.../Ubung/code/exercise3-cnv.py)
under every scenario the sheet asks for, and report the divergence.

Their file is used verbatim. The ONLY textual edits applied are the two needed
to make it runnable in a batch: `time.sleep(1)` is neutralised (otherwise a run
takes minutes) and the `while True` is bounded to ROUNDS iterations. Every
scenario is produced by uncommenting the line their own file already carries for
it, which is exactly how the sheet tells you to use it.

Output: tables of the max difference between the correct nodes per round.
"""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = (HERE / "../../../raw/lectures/Dependable Distributed Systems/Ubung/code/exercise3-cnv.py").resolve()
ROUNDS = 12

# (label, what to uncomment)
SCENARIOS = [
    ("1 perfect start", None),
    ("2 one node initial clock error (+40)", 'b = CNV("B", 40, 1)'),
    ("3 one node initial clock error (+400)", ("b = CNV(\"B\", 0, 1)", 'b = CNV("B", 400, 1)')),
    ("4 one node 5% frequency error", 'c = CNV("C", 0, 1.05)'),
    ("5 one node EVILCNV", 'd = EVILCNV("D", 0, 1)'),
]


def build(source: str, uncomment) -> str:
    s = source
    s = s.replace("time.sleep(1)", "pass  # sleep neutralised for batch running")
    s = s.replace("while True:", f"for _round in range({ROUNDS}):")
    s = s.replace(")\n\ttime.sleep", ")\n")
    if isinstance(uncomment, tuple):
        old, new = uncomment
        if old not in s:
            raise SystemExit(f"could not find {old!r}")
        return s.replace(old, new)
    if uncomment:
        # the file carries each scenario commented out, with trailing ### notes
        pat = re.compile(r"^([ \t]*)#[ \t]*(" + re.escape(uncomment) + r")[^\n]*$", re.M)
        s2, n = pat.subn(lambda m: m.group(1) + uncomment, s)
        if n != 1:
            raise SystemExit(f"could not uncomment {uncomment!r} (matched {n})")
        s = s2
    return s


def maxdiff(block: str) -> float | None:
    m = re.search(r"max diff ([\d.]+)", block)
    return float(m.group(1)) if m else None


def run(label: str, code: str):
    p = HERE / f"_cnv_scenario.py"
    p.write_text(code, encoding="utf-8")
    r = subprocess.run([sys.executable, str(p)], capture_output=True, text=True, timeout=120)
    out = r.stdout
    if r.returncode != 0:
        return None, out + r.stderr
    rounds = re.findall(r"nodes have clock values from ([\d.-]+) to ([\d.-]+) \(max diff ([\d.]+)\)", out)
    return rounds, out


def main():
    src = RAW.read_text(encoding="utf-8")
    print(f"source: {RAW}")
    print(f"rounds per run: {ROUNDS} x 100 ticks,  time.sleep neutralised")
    print()

    hdr = f"{'scenario':40}" + "".join(f"{'r'+str(i):>10}" for i in range(1, ROUNDS + 1))
    for label, unc in SCENARIOS:
        rounds, _ = run(label, build(src, unc))
        if rounds is None:
            print(f"{label:40}FAILED")
            continue
        row = "".join(f"{float(r[2]):10.2f}" for r in rounds)
        print(f"{label:40}{row}")
    print()
    print("values are the max clock difference among the CORRECT nodes after each round\n")

    # the fix: add the delta clamp of the lecture's CNV
    fixed = src.replace(
        """	def sync(self, nodelist):
		self.adjust = 0
		for n in nodelist:
			diff = n.read() - self.ticks
			self.adjust += diff
		self.adjust = self.adjust / len(nodelist)""",
        """	def sync(self, nodelist):
		self.adjust = 0
		for n in nodelist:
			diff = n.read() - self.ticks
			if abs(diff) > DELTA:      # <<< the clamp the partial version omits
				diff = 0               # reading replaced by own clock value
			self.adjust += diff
		self.adjust = self.adjust / len(nodelist)""",
    )
    assert fixed != src, "clamp patch did not apply"
    print("=== after adding the delta clamp of the lecture's CNV definition ===")
    for label, unc in SCENARIOS:
        rounds, _ = run(label, build(fixed, unc))
        if rounds is None:
            print(f"{label:40}FAILED")
            continue
        print(f"{label:40}" + "".join(f"{float(r[2]):10.2f}" for r in rounds))

    print()
    print("=== EVILCNV tuned for maximum damage ===")
    print("Note on what 'maximum damage' can mean here. read() is not passed the")
    print("caller's identity, so the attacker cannot tailor a value per victim.")
    print("A CONSTANT lie (own ticks + k*delta for any k) does not damage")
    print("convergence at all: every correct node sees the same offset and is")
    print("pushed the same way, so they stay in step with each other. What does")
    print("damage convergence is a lie that VARIES BETWEEN READERS, because then")
    print("the correct nodes are pulled in different directions. read() is called")
    print("once per node per round, so alternating the sign does exactly that.")
    evil = src.replace(
        """	def read(self):
		return self.ticks + random.randint(-100,1000)""",
        """	def read(self):
		# alternate between the two extremes: consecutive readers get
		# opposite signs, so the correct nodes are pulled apart
		EVILCNV.flip ^= 1
		return self.ticks + (1000 if EVILCNV.flip else -1000)""",
    )
    if "EVILCNV.flip" not in evil:
        raise SystemExit("evil patch did not apply")
    evil = evil.replace(
        'class EVILCNV(CNV):\n	def read(self):',
        'class EVILCNV(CNV):\n	flip = 0\n	def read(self):',
    )
    rounds, _ = run("alternating +/-1000, unclamped", build(evil, 'd = EVILCNV("D", 0, 1)'))
    if rounds:
        print(f"{'unclamped (their code)':40}" + "".join(f"{float(r[2]):10.2f}" for r in rounds))

    rounds, _ = run("alternating, clamped", build(fixed.replace(
        """	def read(self):
		return self.ticks + random.randint(-100,1000)""",
        """	def read(self):
		EVILCNV.flip ^= 1
		return self.ticks + (1000 if EVILCNV.flip else -1000)""").replace(
        'class EVILCNV(CNV):\n	def read(self):',
        'class EVILCNV(CNV):\n	flip = 0\n	def read(self):'), 'd = EVILCNV("D", 0, 1)'))
    if rounds:
        print(f"{'clamped (correct CNV)':40}" + "".join(f"{float(r[2]):10.2f}" for r in rounds))
        print()
        print("the clamp bounds each accepted reading to within delta of the reader's")
        print("own clock, so the best the liar can do is move a reader by delta/4 per")
        print("round instead of 250.")

    (HERE / "_cnv_scenario.py").unlink(missing_ok=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
