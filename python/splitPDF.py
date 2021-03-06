import PyPDF2

def split_pdf_pages(src_path, dst_basepath):
    src_pdf = PyPDF2.PdfFileReader(src_path)
    for i in range(src_pdf.numPages):
        dst_pdf = PyPDF2.PdfFileWriter()
        dst_pdf.addPage(src_pdf.getPage(i))
        with open('{}_{}.pdf'.format(dst_basepath, i), 'wb') as f:
            dst_pdf.write(f)

# arg1 is file name and arg2 is exported file name.
# you must change these args every time
split_pdf_pages('filename.pdf', 'newfilename')
