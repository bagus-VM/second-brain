# Draws fig1_react_loop.png and fig2_memory.png for the IEEE report (300 dpi).
# Rule: text lives INSIDE boxes only (plus 1-word edge tags in dead space).
# All explanation goes into the figure captions in the document.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({"font.family": "serif",
                     "font.serif": ["Times New Roman", "DejaVu Serif"]})

BOX_Z, LINE_Z, TXT_Z = 5, 2, 8

def box(ax, x, y, label, w, h, fs=7.5, fill="white"):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                 boxstyle="round,pad=0.012", linewidth=0.8,
                 edgecolor="black", facecolor=fill, zorder=BOX_Z))
    ax.text(x, y, label, ha="center", va="center", fontsize=fs, zorder=TXT_Z)
    return dict(x=x, y=y, w=w, h=h)

def T(b): return (b["x"], b["y"] + b["h"] / 2)
def B(b): return (b["x"], b["y"] - b["h"] / 2)
def L(b): return (b["x"] - b["w"] / 2, b["y"])
def R(b): return (b["x"] + b["w"] / 2, b["y"])

def poly(ax, pts, arrow=True, dashed=False):
    n = len(pts) - 1
    for i in range(n):
        head = (i == n - 1) if arrow else False
        ax.add_patch(FancyArrowPatch(pts[i], pts[i + 1],
                     arrowstyle="-|>" if head else "-", mutation_scale=8,
                     linewidth=0.8, color="black",
                     linestyle="--" if dashed else "-", zorder=LINE_Z))

def tag(ax, x, y, t, ha="center"):
    ax.text(x, y, t, fontsize=6.5, ha=ha, va="center", zorder=TXT_Z)

# ================= FIG 1 =================
fig, ax = plt.subplots(figsize=(3.4, 5.1))
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

CX, LRAIL, RR, SIDE = 0.44, 0.10, 0.735, 0.865

start  = box(ax, CX, 0.945, "user message arrives\n(run_id minted)", 0.52, 0.072)
guard  = box(ax, CX, 0.840, "GUARD\nestimate vs. 80% window", 0.52, 0.072)
reason = box(ax, CX, 0.725, "REASON\nLLM call with current messages\nand tool schemas", 0.52, 0.072, fs=6.8)
decide = box(ax, CX, 0.610, "tool calls in\nresponse?", 0.34, 0.072)
gate   = box(ax, CX, 0.475, "GATE\npermission policy check", 0.44, 0.072)
act    = box(ax, CX, 0.350, "ACT\ntool runs; errors \u2192 strings", 0.44, 0.072)
obs    = box(ax, CX, 0.225, "OBSERVE\nappend TOOL message\nto context", 0.52, 0.072, fs=6.8)

cap   = box(ax, 0.245, 0.055, "STOP\ncap reached:\nmax_iterations", 0.25, 0.09, fs=6.8)
final = box(ax, SIDE, 0.610, "FINAL ANSWER\nrun ends: success", 0.24, 0.085, fs=6.4)
den   = box(ax, SIDE, 0.475, "refused or\ndenied", 0.20, 0.065, fs=6.8)

poly(ax, [B(start), T(guard)])
poly(ax, [B(guard), T(reason)])
poly(ax, [B(reason), T(decide)])
poly(ax, [B(decide), T(gate)]);  tag(ax, CX + 0.018, 0.545, "yes", ha="left")
poly(ax, [B(gate), T(act)]);     tag(ax, CX + 0.018, 0.418, "allow", ha="left")
poly(ax, [B(act), T(obs)])
poly(ax, [R(decide), L(final)]); tag(ax, 0.665, 0.638, "no")
poly(ax, [R(gate), L(den)])      # deny straight into its box
# denied -> down -> OBSERVE right edge
poly(ax, [B(den), (SIDE, 0.225), R(obs)])
# overflow (dashed): REASON right -> lane up -> over -> into GUARD top edge
poly(ax, [R(reason), (RR, 0.725), (RR, 0.892), (0.575, 0.892), (0.575, T(guard)[1])], dashed=True)
# loopback: OBSERVE left -> left lane up -> GUARD left
poly(ax, [L(obs), (LRAIL, 0.225), (LRAIL, 0.840), L(guard)])
# cap exit: branch off bottom of loopback lane into STOP box
poly(ax, [(LRAIL, 0.225), (LRAIL, 0.055), (0.12, 0.055), L(cap)])
fig.savefig("fig1_react_loop.png", dpi=300, bbox_inches="tight", pad_inches=0.04)
plt.close(fig)

# ================= FIG 2 =================
fig, ax = plt.subplots(figsize=(3.4, 4.9))
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

ax.add_patch(FancyBboxPatch((0.03, 0.70), 0.94, 0.27, boxstyle="round,pad=0.008",
             linewidth=0.9, edgecolor="black", facecolor="#f7f7f7", zorder=1))
ax.add_patch(FancyBboxPatch((0.03, 0.03), 0.94, 0.53, boxstyle="round,pad=0.008",
             linewidth=0.9, edgecolor="black", facecolor="#f7f7f7", zorder=1))
ax.text(0.5, 0.942, "SHORT-TERM  (context window)", fontsize=7.5, weight="bold",
        ha="center", zorder=TXT_Z)
ax.text(0.5, 0.532, "LONG-TERM  (SQLite + files, append-only)", fontsize=7.5,
        weight="bold", ha="center", zorder=TXT_Z)

sysb = box(ax, 0.27, 0.865, "SYSTEM message:\nsoul.md + date\n+ injected note", 0.40, 0.095, fs=6.6)
hist = box(ax, 0.73, 0.865, "history:\nuser / assistant / TOOL", 0.40, 0.095, fs=6.6)
comp = box(ax, 0.5, 0.755, "COMPACTION\ntier 1 blank TOOL outputs \u2192\ntier 2 summary + last 10", 0.62, 0.085, fs=6.6)

thr = box(ax, 0.17, 0.425, "THREADS\nepisodic:\nall messages", 0.26, 0.095, fs=6.6)
fac = box(ax, 0.5, 0.425, "FACTS\nsemantic:\ntopic + vector", 0.26, 0.095, fs=6.6)
prc = box(ax, 0.83, 0.425, "PROCEDURES\ndraft /\napproved", 0.26, 0.095, fs=6.6)
wr  = box(ax, 0.30, 0.145, "WRITE\nmemory_store", 0.40, 0.095, fs=6.6)
rd  = box(ax, 0.72, 0.145, "READ\nLIKE + cosine\n+ reranker", 0.42, 0.095, fs=6.6)

poly(ax, [(0.44, B(fac)[1]), (0.44, 0.1925)])            # store: facts -> WRITE top edge
poly(ax, [(0.72, T(rd)[1]), (0.72, 0.70)])                # read -> short-term container
poly(ax, [T(thr), (0.17, 0.70)])                           # resume -> container border
poly(ax, [T(prc), (0.83, 0.70)])                           # routines -> container border
fig.savefig("fig2_memory.png", dpi=300, bbox_inches="tight", pad_inches=0.04)
plt.close(fig)
print("figures written")
