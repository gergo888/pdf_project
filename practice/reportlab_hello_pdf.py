from reportlab.pdfgen import canvas
from pprint import pprint

c = canvas.Canvas("hello-world.pdf")
c.drawString(50, 50, "-------------------")
pprint((c.getpdfdata()))

c.save()