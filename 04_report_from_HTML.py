from IPython.core.display import HTML
import pdfkit

config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
# settings page
options = {
    'page-size': 'A4',
    'margin-top': '0.5in',
    'margin-right': '0.5in',
    'margin-left': '0.5in',
    'margin-bottom': '0.5in',
    'encoding': 'UTF-8',
    'footer-html': 'footer.html',
    'header-right': '[page]',
    'page-offset': 1
}

# pdfkit.from_url("https://airee.cloud","airee.pdf", configuration=config) # example import by url to pdf

'''footer.html'''
'''<html>
    <head>
    <meta charset="UTF-8"/>
    </head>
    <body>
        <p>Культурная стататистика Москвы</p>
    </body>
</html>
'''

index = '''<html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Посещаемость библиотек в Москве</title>
            <style>
                h2 {page-break-before: always}
            </style>
        </head>
        <body>
            <h1 style="background: #666;">
            Посещаемость библиотек в Москве
            </h1>
            <p><img src="libraries.png" alt="Библиотеки Москвы"/></p>
            <h2>Самые читающие районы</h2>
            <p><img src="readers.png" alt="Самые читающие районы Москвы"/></p>
            <h2>Табличнык данные</h2>
            <table>
                <thead>
                    <tr>
                        <th>Заголовок таблицы</th><th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Ячейка таблицы</td><td>Данные</td>
                    </tr>
                </tbody>
            </table>
        </body>
</html>
'''


pdfkit.from_string(index, 'index.pdf', configuration=config, options=options)

# html = '''
#     <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <title>Заголовок документа</title>
#         </head>
#         <body>
#             <h1 style="background: #666;">
#             Заголовок текста
#             </h1>
#             <p>
#             Описание проекта
#                 <a href="https://www.ittensive.com/"> ссылка на сайт</a>
#             </p>
#             <p>
#                 <img src="libraries.png" alt="Бидлиотеки Москвы"/>
#             </p>
#             <h2>Табличнык данные</h2>
#             <table>
#                 <thead>
#                     <tr>
#                         <th>Заголовок таблицы</th><th></th>
#                     </tr>
#                 </thead>
#                 <tbody>
#                     <tr>
#                         <td>Ячейка таблицы</td><td>Данные</td>
#                     </tr>
#                 </tbody>
#             </table>
#         </body>
#     </html>
# '''
# pdfkit.from_string(html, "example.pdf", configuration=config)

# HTML(html)
