import os
import csv
import openpyxl

def openXLSX(xlsx_filename):
    if os.path.exists(xlsx_filename):
        #open file
        print("File exists.")
        return openpyxl.load_workbook(xlsx_filename)
        
    else:
        #create new file
        print("File doesn't exist.")
        
#確認ダイアログ
        
        workbook = openpyxl.Workbook()
        workbook.save(xlsx_filename)
        
        #edit sheet name
        workbook.worksheets[0].title = "TITLE"
        
        #margines settings
        worksheet = workbook.active
        worksheet.page_margins.left = 1
        worksheet.page_margins.right = 1
        worksheet.page_margins.top = 1
        worksheet.page_margins.bottom = 1
        worksheet.page_margins.header = 0
        worksheet.page_margins.footer = 0
        
        #dimensions settings
        worksheet.column_dimensions['A'].width = 5
        worksheet.column_dimensions['B'].width = 1
        worksheet.column_dimensions['C'].width = 3
        worksheet.column_dimensions['D'].width = 7
        worksheet.column_dimensions['E'].width = 35
        worksheet.column_dimensions['F'].width = 15
        
        return workbook
        
