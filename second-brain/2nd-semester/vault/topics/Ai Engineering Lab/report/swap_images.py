from docx import Document
from pathlib import Path
import zipfile

BLIP = '{http://schemas.openxmlformats.org/drawingml/2006/main}blip'
RID = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed'
p = Path(r"C:/Users/quiescent/Documents/Vault/second-brain/2nd-semester/projects/group-11/report/StudyMate_report_IEEE.docx")
doc = Document(p)
img_paras = [par for par in doc.paragraphs if par._p.findall('.//' + BLIP)]
assert len(img_paras) == 2, len(img_paras)
new = [Path("fig1_react_loop.png").read_bytes(), Path("fig2_memory.png").read_bytes()]
for par, data in zip(img_paras, new):
    rid = par._p.find('.//' + BLIP).get(RID)
    doc.part.related_parts[rid]._blob = data
doc.save(p)
z = zipfile.ZipFile(p)
names = [n for n in z.namelist() if 'media' in n]
print("media:", [(n, z.getinfo(n).file_size) for n in names])
