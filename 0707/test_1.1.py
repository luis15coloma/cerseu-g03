"""Importando los modulos"""

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

"""Inicializando las variables con valores"""
fileName ="reporte.pdf"
documentTitle = "Reporte"
title = "Python"
subtitle = "Lo primordial ahora es!!"
textLine = [
    'La tecnología nos hace concientes de, '
    'el mundo alrededor de nosotros'
]

image = 'image.png'

"""Creando un objeto pdf"""
pdf = canvas.Canvas(fileName)

"""Estableciendo el título del documento pdf"""
pdf.setTitle(documentTitle)

"""Agregando una fuente externa de Python"""
pdfmetrics.registerFont(
    TTFont('abc', "SakBunderan.ttf")
)

"""Estableciendo el título y la fuente sobre el lienzo de mi pdf"""
pdf.setFont("abc", 36)
pdf.drawCentredString(300, 700, title)

"""Establecer el titulo dentro del lienzo de mi pdf"""
pdf.setFillColorRGB(255, 125, 24)
pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290, 720, subtitle)

"""Dibujando una línea"""
pdf.line(30, 680, 550, 680)

"""Creando un texto de muchas líneas usando líneas de texto y el ciclo for"""
text = pdf.beginText(50, 640)
text.setFont("Courier", 18)
text.setFillColor(colors.red)

for line in textLine:
    text.textLine(line)
pdf.drawText(text)

"""Dibujando una imagen en una posición específica"""
pdf.drawInlineImage(image, 290, 450, 200, 100)
"""Generandp el pdf"""
pdf.save()