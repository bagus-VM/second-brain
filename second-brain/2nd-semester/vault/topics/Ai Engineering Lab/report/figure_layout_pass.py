# In-place edit of StudyMate_report_IEEE_plain.docx (user hand-edited; do NOT rebuild):
#  - Fig. 2 (wide memory diagram) currently sits INLINE in a justified text paragraph and
#    renders at ~2in inside one column. Split it out, give it its own continuous
#    SINGLE-column section so it spans the full page width, and scale it up.
#  - IEEE captions ("Fig. N. ...", 8pt Times, bold run-in, centered) below both figures.
#  - Remove the body-style first-line indent from image paragraphs.
import copy
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = Path(__file__).parent
SRC = HERE / "StudyMate_report_IEEE_plain.docx"

doc = Document(SRC)
paras = doc.paragraphs

def is_img(p):
    return p._p.find('.//' + qn('a:blip')) is not None

img_paras = [p for p in paras if is_img(p)]
assert len(img_paras) == 2, f"expected 2 image paragraphs, got {len(img_paras)}"
fig1p, fig2p = img_paras
print("fig1 para text:", repr(fig1p.text[:60]))
print("fig2 para text:", repr(fig2p.text[:60]))

# --- 1. split fig2 out of its text paragraph into a fresh image-only paragraph ---
drawing_run = None
for r in fig2p._p.findall(qn('w:r')):
    if r.find('.//' + qn('a:blip')) is not None:
        drawing_run = r
        break
assert drawing_run is not None
if fig2p.text.strip():  # shares the paragraph with prose
    new_p = OxmlElement('w:p')
    fig2p._p.addnext(new_p)
    new_p.append(drawing_run)  # moves the run
    fig2p = type(fig2p)(new_p, fig2p._parent)
    print("fig2 split into its own paragraph")

e2 = fig2p._p.find('.//' + qn('wp:extent'))
e1 = fig1p._p.find('.//' + qn('wp:extent'))
assert int(e2.get('cx')) / int(e2.get('cy')) > 1 > int(e1.get('cx')) / int(e1.get('cy')), \
    "expected fig1 portrait (tall) and fig2 landscape (wide)"

# --- 2. no first-line indent on image paragraphs ---
for p in (fig1p, fig2p):
    ppr = p._p.get_or_add_pPr()
    for ind in ppr.findall(qn('w:ind')):
        ppr.remove(ind)

# --- 3. scale fig2 to full text width (body-level: 8.5 - 2*0.644 = 7.212in) ---
w_in = 6.9
cur_cx, cur_cy = int(e2.get('cx')), int(e2.get('cy'))
h_in_emu = int(cur_cy * (Inches(w_in) / cur_cx))
e2.set('cx', str(int(Inches(w_in))))
e2.set('cy', str(h_in_emu))
print(f"fig2 extent -> {w_in:.2f} x {h_in_emu/914400:.2f} in")

# --- 4. helpers: continuous single-column section wrapper ---
sectPr_final = doc.sections[-1]._sectPr

def make_sect_pr(num_cols):
    sp = copy.deepcopy(sectPr_final)
    # force continuous
    t = sp.find(qn('w:type'))
    if t is None:
        t = OxmlElement('w:type'); sp.insert(0, t)
    t.set(qn('w:val'), 'continuous')
    cols = sp.find(qn('w:cols'))
    if cols is None:
        cols = OxmlElement('w:cols'); sp.append(cols)
    cols.set(qn('w:num'), str(num_cols))
    cols.set(qn('w:space'), '340')
    return sp

def section_break_para(sect_pr):
    p = OxmlElement('w:p')
    ppr = OxmlElement('w:pPr')
    ppr.append(sect_pr)
    p.append(ppr)
    return p

# --- 5. captions below each figure (8pt Times, centered, bold "Fig. N." run-in) ---
def add_caption_after(anchor_el, number, text):
    cap = OxmlElement('w:p')
    ppr = OxmlElement('w:pPr')
    spc = OxmlElement('w:spacing'); spc.set(qn('w:before'), '2'); spc.set(qn('w:after'), '6')
    jc = OxmlElement('w:jc'); jc.set(qn('w:val'), 'center')
    ppr.append(spc); ppr.append(jc)
    cap.append(ppr)
    for t, bold in ((f"Fig. {number}. ", True), (text, False)):
        r = OxmlElement('w:r')
        rpr = OxmlElement('w:rPr')
        f = OxmlElement('w:rFonts'); f.set(qn('w:ascii'), 'Times New Roman'); f.set(qn('w:hAnsi'), 'Times New Roman')
        sz = OxmlElement('w:sz'); sz.set(qn('w:val'), '16')
        szc = OxmlElement('w:szCs'); szc.set(qn('w:val'), '16')
        rpr.append(f); rpr.append(sz); rpr.append(szc)
        if bold:
            rpr.append(OxmlElement('w:b'))
        r.append(rpr)
        wt = OxmlElement('w:t'); wt.set(qn('xml:space'), 'preserve'); wt.text = t
        r.append(wt)
        cap.append(r)
    anchor_el.addnext(cap)
    return cap

add_caption_after(fig1p._p, 1,
    "ReAct loop of the agent. The context (soul.md, conversation history, tool schemas) goes to the "
    "InnKube model; if the response contains tool calls, each one passes the registry checkpoint and "
    "the permission layer before it runs, and its result is appended as an observation for the next "
    "iteration. A response without tool calls exits as the final answer.")

cap2 = add_caption_after(fig2p._p, 2,
    "The two memory tiers and their traffic. Short-term memory is the live context window (the system "
    "message with its injected note plus the conversation history), kept in budget by two-tier "
    "compaction. Long-term memory is an append-only SQLite store plus procedure files: episodic "
    "threads restore into the context when entered, semantic facts are written by the memory_store "
    "tool and read back through hybrid LIKE + cosine recall with an optional reranker.")

# --- 6. wrap [fig2, caption] in its own continuous 1-column section ---
before = section_break_para(make_sect_pr(1))   # ends the 2-col section before fig2
fig2p._p.addprevious(before)
after = section_break_para(make_sect_pr(2))    # ends the 1-col fig2 section, back to 2 cols
cap2.addnext(after)

doc.save(SRC)
print("saved", SRC)
