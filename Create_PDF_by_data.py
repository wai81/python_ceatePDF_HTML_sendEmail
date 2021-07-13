from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont  # import fonts
from reportlab.lib.utils import ImageReader
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

r = requests.get("https://video.ittensive.com/python-advanced/data-7361-2019-11-28.utf.json")
data = pd.DataFrame(json.loads(r.content),
                    columns=["NumOfVisitors", "CommonName"]).fillna(value=0)  # отбор данных по колонкам
sns.displot(data["NumOfVisitors"]).set(xlabel="Посещаемость")  # вывод гистограммы
# plt.show()
plt.savefig('libraries.png')
# print(data.head())
pdfmetrics.registerFont(TTFont("Trebuchet", "trebuc.ttf"))  # регистрация шрифта
PDF = canvas.Canvas("libraries.pdf", pagesize=pagesizes.A4)  # указываем имя файла и размер холста
PDF.setFont("Trebuchet", 13)
PDF.drawString(550, 820, "2")  # номер страницы
PDF.setFont("Trebuchet", 48)
PDF.drawString(100, 750, "Библиолеки Москвы")  # загаловок диаграммы
PDF.drawImage(ImageReader("libraries.png"), 50, 200)  # вставка изображения диаграммы
PDF.save()
