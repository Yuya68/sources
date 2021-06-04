#! Python3.7
# combinePdfs.py

import PyPDF2, os

# get all pdf_Fil_Name
pdf_files = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)

pdf_files.sort(key=str.lower)
pdf_writer = PyPDF2.PdfFileWriter()

# roop all pdfFiles
for filename in pdf_files:
    pdf_files_obj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_files_obj)
    # add all pages and roop
    for page_num in range(0, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

# save pdf file
pdf_putput = open('all.pdf', 'wb')
pdf_writer.write(pdf_putput)
pdf_putput.close()
