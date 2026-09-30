# Add IEEE captions below each figure in StudyMate_report_IEEE_plain2.docx.
# Layout is the user's own — ONLY change: insert two caption paragraphs
# (8pt Times, centered, bold run-in "Fig. N.") right after the paragraph
# containing each image. Anchored by blip presence, never by index.
from pathlib import Path
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = Path(__file__).parent
SRC = HERE / "StudyMate_report_IEEE_plain2.docx"

doc = Document(SRC)

img_paras = [p for p in doc.paragraphs if p._p.find('.//' + qn('a:blip')) is not None]
assert len(img_paras) == 2, f"expected 2 image paragraphs, got {len(img_paras)}"
fig1p, fig2p = img_paras

def make_caption(number, text):
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
        sz = OxmlElement('w:sz'); sz.set(qn('w:val'), '16')      # 8 pt
        szc = OxmlElement('w:szCs'); szc.set(qn('w:val'), '16')
        rpr.append(f); rpr.append(sz); rpr.append(szc)
        if bold:
            rpr.append(OxmlElement('w:b'))
        r.append(rpr)
        wt = OxmlElement('w:t'); wt.set(qn('xml:space'), 'preserve'); wt.text = t
        r.append(wt)
        cap.append(r)
    return cap

c1 = make_caption(1,
    "ReAct loop of the agent. The context (soul.md, conversation history, tool schemas) goes to the "
    "InnKube model; if the response contains tool calls, each one passes the registry checkpoint and "
    "the permission layer before it runs, and its result is appended as an observation for the next "
    "iteration. A response without tool calls exits as the final answer.")
c2 = make_caption(2,
    "The two memory tiers and their traffic. Short-term memory is the live context window (the system "
    "message with its injected note plus the conversation history), kept in budget by two-tier "
    "compaction. Long-term memory is an append-only SQLite store plus procedure files: episodic "
    "threads restore into the context when entered, semantic facts are written by the memory_store "
    "tool and read back through hybrid LIKE + cosine recall with an optional reranker.")

fig1p._p.addnext(c1)
# fig2 caption goes after the prose paragraph that contains the image
fig2p._p.addnext(c2)

doc.save(SRC)
print("saved", SRC)
