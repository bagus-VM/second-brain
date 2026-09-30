# Builds StudyMate_report_IEEE.docx in IEEEtran conference style (two-column,
# Times New Roman, centered small-caps heads) from report_spec.json content.
import json, re
from pathlib import Path
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, Inches, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = Path(__file__).parent
spec = json.loads((HERE / "report_spec.json").read_text(encoding="utf-8"))
blocks = spec["blocks"]

doc = Document()

# --- base style: Times New Roman 10pt (IEEE body) ---
normal = doc.styles["Normal"]
normal.font.name = "Times New Roman"
normal.font.size = Pt(10)
normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
pf = normal.paragraph_format
pf.space_after = Pt(0)
pf.space_before = Pt(0)
pf.line_spacing = 1.0

# --- section 1: title + authors, single column (US Letter, IEEE margins) ---
sec1 = doc.sections[0]
sec1.page_width, sec1.page_height = Inches(8.5), Inches(11)
sec1.top_margin = Inches(0.75)
sec1.bottom_margin = Inches(1.04)
sec1.left_margin = sec1.right_margin = Inches(0.644)

def set_cols(section, num, space_twips=340):
    sectPr = section._sectPr
    cols = sectPr.find(qn("w:cols"))
    if cols is None:
        cols = OxmlElement("w:cols")
        sectPr.append(cols)
    cols.set(qn("w:num"), str(num))
    cols.set(qn("w:space"), str(space_twips))
    cols.set(qn("w:equalWidth"), "1")

def body_par(text="", size=10, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY,
             first_indent=None, space_before=0, space_after=0, small_caps=False):
    p = doc.add_paragraph()
    p.alignment = align
    f = p.paragraph_format
    f.space_before = Pt(space_before)
    f.space_after = Pt(space_after)
    if first_indent is not None:
        f.first_line_indent = Inches(first_indent)
    if text:
        r = p.add_run(text)
        r.font.size = Pt(size)
        r.bold, r.italic = bold, italic
        r.font.small_caps = small_caps
    return p

def run_in(p, lead, rest, lead_italic=False, size=10):
    r = p.add_run(lead)
    r.bold = True
    r.italic = lead_italic
    r.font.size = Pt(size)
    r2 = p.add_run(rest)
    r2.font.size = Pt(size)
    return p

# Title (block 0) and author line (block 1)
title = blocks[0]["text"]
author_line = blocks[1]["text"]
body_par(title, size=24, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

# IEEE author block: centered italic, split name / dept / org / city / email
author_bits = [s.strip() for s in author_line.split("|")]
for i, bit in enumerate(author_bits):
    body_par(bit, size=11, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER,
             space_after=2 if i < len(author_bits) - 1 else 14)

# --- section 2: two-column body ---
sec2 = doc.add_section(WD_SECTION.CONTINUOUS)
sec2.page_width, sec2.page_height = Inches(8.5), Inches(11)
sec2.top_margin = Inches(0.75)
sec2.bottom_margin = Inches(1.04)
sec2.left_margin = sec2.right_margin = Inches(0.644)
set_cols(sec2, 2)

# Abstract + index terms (IEEE requires them; composed to match the report)
ab = body_par(align=WD_ALIGN_PARAGRAPH.JUSTIFY, first_indent=0.0)
run_in(ab, "Abstract\u2014", "StudyMate is an agent harness built from scratch in Python 3.12 for the "
       "AI Engineering Lab at the University of Passau: a ReAct loop over a sandboxed tool registry that "
       "turns lecture material into an interlinked Obsidian knowledge base. This report explains the "
       "control loop and the harness's short- and long-term memory handling (context compaction, episodic "
       "threads, hybrid fact recall with embedding and reranking, and file-based procedural routines), then "
       "describes where the team exceeded the lab's minimum requirements and which extensions were considered "
       "and not pursued, with reasons.")
it = body_par(align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6)
run_in(it, "Index Terms\u2014", "agent harness, ReAct, long-term memory, context compaction, retrieval-"
         "augmented generation, Model Context Protocol, observability.", lead_italic=True)

def heading1(text):
    # IEEE: centered, bold, small-caps, roman numeral typed literally
    body_par(text, size=10, bold=True, small_caps=True, align=WD_ALIGN_PARAGRAPH.CENTER,
             space_before=6, space_after=6)

def heading2(text):
    # IEEE: run-in bold italic subsection head; left aligned
    body_par(text, size=10, bold=True, italic=True, align=WD_ALIGN_PARAGRAPH.LEFT,
             space_before=3, space_after=3)

def add_table(header, rows):
    t = doc.add_table(rows=1 + len(rows), cols=len(header))
    t.style = "Table Grid"
    for j, htxt in enumerate(header):
        cell = t.rows[0].cells[j]
        cell.text = ""
        r = cell.paragraphs[0].add_run(htxt)
        r.bold = True
        r.font.size = Pt(8)
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = t.rows[i + 1].cells[j]
            cell.text = ""
            r = cell.paragraphs[0].add_run(val)
            r.font.size = Pt(8)
    body_par("", size=4)  # spacer
    return t

skip_first_two = True
for blk in blocks:
    kind = blk.get("type")
    if kind == "heading" and blk["level"] == 1:
        continue  # title already rendered
    if kind == "paragraph" and skip_first_two and blk["text"].startswith("Bagus Trilaksono"):
        skip_first_two = False
        continue
    if kind == "heading" and blk["level"] == 2:
        heading1(blk["text"])
    elif kind == "heading" and blk["level"] == 3:
        heading2(blk["text"])
    elif kind == "paragraph":
        if blk.get("runs"):  # editor note
            txt = blk["runs"][0]["text"]
            body_par(txt, size=9, italic=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=4, space_after=4)
        elif re.match(r"^\[\d+\]", blk["text"]) or blk["text"] == "References":
            body_par(blk["text"], size=9, align=WD_ALIGN_PARAGRAPH.JUSTIFY, first_indent=0.0)
        else:
            body_par(blk["text"], size=10, first_indent=0.2)
    elif kind == "bullet_list":
        for item in blk["items"]:
            p = body_par(item, size=10, first_indent=0.2)
            p.paragraph_format.left_indent = Inches(0.15)
    elif kind == "table":
        add_table(blk["header"], blk["rows"])

out = HERE / "StudyMate_report_IEEE.docx"
doc.save(out)

# word count excluding tables + editor notes
words = 0
for blk in blocks:
    if blk.get("type") == "table":
        continue
    if blk.get("type") == "paragraph" and blk.get("runs"):
        continue
    t = blk.get("text") or " ".join(blk.get("items", []))
    words += len(re.findall(r"\S+", t))
words += 120  # abstract+index terms rough count
print("saved", out, "| approx body words (excl. tables/notes):", words)
