from PyPDF2 import PdfFileMerger, PdfFileReader
from PIL import Image

with open("libraries.pdf", "rb") as pdf_file:
    pdf_reader = PdfFileReader(pdf_file)
    print("Count page", pdf_reader.getNumPages())
    print("Metadata", pdf_reader.documentInfo)
    print("File Author", pdf_reader.documentInfo["/Author"])
    print("File Creator", pdf_reader.documentInfo["/Creator"])

with open("title.pdf", "rb") as pdf_file:
    pdf_reader = PdfFileReader(pdf_file)
    for page_num in range(pdf_reader.getNumPages()):
        pdf_page = pdf_reader.getPage(page_num)
        if '/XObject' in pdf_page['/Resources']:
            xObject = pdf_page['/Resources']['/XObject'].getObject()
            for obj in xObject:
                if xObject[obj]['/Subtype'] == '/Image':
                    size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                    data = xObject[obj].getData()
                    img = Image.frombytes("RGB", size, data)
                    img.save("image.png")

files = ["title.pdf", "libraries.pdf"]
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

with open("report.pdf", "rb") as pdf_file:
    pdf_reader = PdfFileReader(pdf_file)
    print("Count page", pdf_reader.getNumPages())
    print("Metadata", pdf_reader.documentInfo)
    print("File Author", pdf_reader.documentInfo["/Author"])
    print("File Creator", pdf_reader.documentInfo["/Creator"])