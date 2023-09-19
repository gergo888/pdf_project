from pathlib import Path

from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import PDF

# create an empty Document
pdf = Document()

# add an empty Page
page = Page()
pdf.add_page(page)

# use a PageLayout (SingleColumnLayout in this case)
layout = SingleColumnLayout(page)

# add a Paragraph object
layout.add(Paragraph("abc abc abc abc abc"))
layout.add(Paragraph("Hello World!"))
layout.add(Paragraph("lorem ipsum lorem ipsum lorem ipsum"))
layout.add(Paragraph("xyz xyz xyz xyz"))

# store the PDF
with open(Path("output.pdf"), "wb") as pdf_file_handle:
    PDF.dumps(pdf_file_handle, pdf)