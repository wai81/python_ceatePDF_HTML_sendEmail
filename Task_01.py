from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont  # import fonts
from reportlab.lib.utils import ImageReader
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from PyPDF2 import PdfFileMerger, PdfFileReader
import seaborn as sns


def get_district(x):
    return list(map(lambda a: a["District"], x))[0]


r = requests.get("https://video.ittensive.com/python-advanced/data-7361-2019-11-28.utf.json")
data = pd.DataFrame(json.loads(r.content)).fillna(value=0)
data["District"] = data["ObjectAddress"].apply(get_district)
data_summa = data.groupby("District").sum().sort_values("NumOfVisitors",
                                                        ascending=False)
fig = plt.figure(figsize=(11, 6))
area = fig.add_subplot(1, 1, 1)
data_summa[0:20]["NumOfVisitors"].plot.pie(ax =area,
                                         labels=[""]*20,
                                         label="Посещаемость",
                                         cmap="tab20")
plt.legend(data_summa[0:20].index,
           bbox_to_anchor=(1.5, 1, 0.1, 0))
plt.savefig("readers.png")
# print(data.head())

pdfmetrics.registerFont(TTFont("Trebuchet", "trebuc.ttf"))  # регистрация шрифта
PDF = canvas.Canvas("readers.pdf", pagesize=pagesizes.A4)  # указываем имя файла и размер холста
PDF.setFont("Trebuchet", 13)
PDF.drawString(550, 820, "2")  # номер страницы
PDF.setFont("Trebuchet", 38)
PDF.drawString(100, 750, "Посетитеели библиотек")  # загаловок диаграммы
PDF.drawImage(ImageReader("readers.png"), -50, 400, width=650, height=350)  # вставка изображения диаграммы
PDF.setFont("Trebuchet", 20)
PDF.drawString(100, 250, "Самый посещаемый рйон")  # загаловок диаграммы
PDF.setFont("Trebuchet", 24)
PDF.drawString(100, 200, data_summa.index[0])
PDF.setFont("Trebuchet", 20)
PDF.drawString(100, 150, "Посетителей: " + str(int(data_summa["NumOfVisitors"].values[0])))
PDF.save()

# объединение файлов
files = ["title.pdf", "readers.pdf"]
merger = PdfFileMerger()

for file_name in files:
    merger.append(PdfFileReader(open(file_name, "rb")))

merger.addMetadata({
    '/Producer': "w@i",
    '/Author': "Vashkelevich Andrei",
    '/Creator': "Vashkelevich Andrei",
    '/Copyright': "ITtensive 2021",
    '/Title': "Культурная статисика Москвы",
})
merger.write("report.pdf")
