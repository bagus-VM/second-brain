# Export the docx to PDF using installed MS Word (COM), for a visual layout check.
import sys
import win32com.client  # noqa
from pathlib import Path

src = Path(sys.argv[1]).resolve()
dst = src.with_suffix(".pdf")
word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
try:
    doc = word.Documents.Open(str(src), ReadOnly=True)
    doc.ExportAsFixedFormat(str(dst), 17)  # wdExportDocumentPDF
    pages = doc.ComputeStatistics(2)  # wdStatisticPages
    doc.Close(False)
    print("PDF:", dst, "pages:", pages)
finally:
    word.Quit()
