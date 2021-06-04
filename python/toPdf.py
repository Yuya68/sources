import os
import win32com.client
import openpyxl

# Using COM object for save as PDF
# !! ATTENTION !! docx file and xlsx file only

dirPath = os.getcwd()

# split docx or excel
for j in os.listdir():
    # word
    if '.docx' in j:
        word = win32com.client.Dispatch('Word.Application')
        #sclipt behind the window
        word.Visible = False

        #docx file path
        dcPath = dirPath + '\\' + j
        #PDF file path
        dPdfPath = dcPath[0:-5] + '.pdf'

        doc = word.Documents.Open(dcPath)
        #PDF format is '17' . so if you make other file, change this number
        doc.SaveAs2(FileName=dPdfPath, FileFormat=17)

        #delete cash
        doc.Close()
    # excel
    elif '.xlsx' in j:
        excel = win32com.client.Dispatch('Excel.Application')
        excel.Visible = False

        #excel file path
        wbPath = dirPath + '\\' + j
        #PDF file path
        ePdfPath = wbPath[0:-5] + '.pdf'

        wb = excel.Workbooks.Open(wbPath)
        #get sheet names as list
        wsList = openpyxl.load_workbook(j).get_sheet_names()
        #must for convert all sheets
        wb.Worksheets(wsList).Select()

        wb.ActiveSheet.ExportAsFixedFormat(0, ePdfPath)

        wb.Close()
