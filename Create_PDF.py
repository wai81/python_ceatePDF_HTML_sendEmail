# pyPDF2 / pyMuPDF(fitz) / ReportLab / PyFPDF : data -> PDF
# pdfminer / pdfminer.six / pdfquery : PDF -> data
# pdfhtmldoc / xhtml2pdf / pdfkrit : (data ->) HTML -> PDF
from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont  # import fonts


PDF = canvas.Canvas("title.pdf", pagesize=pagesizes.A4)
# PDF = canvas.Canvas("title.pdf")
print(PDF.getAvailableFonts())
pdfmetrics.registerFont(TTFont("Trebuchet", "trebuc.ttf"))  # регистрация шрифта
PDF.setFont("Trebuchet", 13)
PDF.drawString(30, 820, "ITtensive/")  # типо верхний колонтитул
PDF.drawString(197, 820, "Python PDF")  # типо верхний колонтитул
PDF.drawString(430, 20, "от команды ITtensive")  # типо нижний колонтитул
PDF.drawString(550, 820, "1")  # номер страницы
PDF.setFont("Trebuchet", 48)
PDF.drawString(180, 550, "Культурная")  # загаловок
PDF.drawString(185, 490, "статаистика")
PDF.drawString(215, 430, "Москвы")
PDF.save()
