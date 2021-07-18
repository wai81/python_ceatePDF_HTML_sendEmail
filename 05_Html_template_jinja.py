import pandas as pd
import pdfkit
from jinja2 import Template

data = pd.read_csv("https://video.ittensive.com/python-advanced/data-102743-2019-11-13.utf.csv", delimiter=";")

html = '''<html>
        <head>
            <meta charset="UTF-8">
            <title>Геральдические символы Москвы</title>
        </head>
        <body>
'''
item_template = '''
<h1 style="page-break-before: always">{{data.Name}}</h1>
<p>
    <img style="width:80%;margin-left:10%"
    src="https://op.mos.ru/MEDIA/showFile?id={{data.Picture}}" alt="{{data.Name}}"/>
</p>
<p style="font-size:150%">{{data.Description}}</p>
'''
for i, item in data.iterrows():
    html += Template(open('heraldic.item.html').read()).render(data=item)

html += '</body></html>'

config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
options = {
    'page-size': 'A4',
    'header-right': '[page]'
}
pdfkit.from_string(html, 'heraldic_2.pdf', options=options, configuration=config)
