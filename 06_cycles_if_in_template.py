import pandas as pd
import pdfkit
from jinja2 import Template

data = pd.read_csv("https://video.ittensive.com/python-advanced/data-102743-2019-11-13.utf.csv", delimiter=";")

html_template = '''<html>
        <head>
            <meta charset="UTF-8">
            <title>Геральдические символы Москвы</title>
        </head>
        <body>
        {% for i, item in data}
            {% if i != 0%}
                <h1 style="page-break-before: always">{{item.Name}}</h1>
            {% else %}
                 <h1>{{item.Name}}</h1>
            {% endif %}
            <p>
                <img style="width:80%;margin-left:10%"
                src="https://op.mos.ru/MEDIA/showFile?id={{item.Picture}}" alt="{{item.Name}}"/>
            </p>
            <p style="font-size:150%">{{item.Description}}</p>
        {% endfor %}
        </body>
        </html>'''

# html = Template(html_template).render(data=data.iterrows())
html = Template(open('heraldic.html').read()).render(data=data.iterrows())

config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
options = {
    'page-size': 'A4',
    'header-right': '[page]'
}
pdfkit.from_string(html, 'heraldic_3.pdf', options=options, configuration=config)

