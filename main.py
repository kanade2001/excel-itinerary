import openpyxl
import os
import csv

import editxlfile
from config import *


if os.path.exists(xlsx_filename):
    #open file
    print("File exists.")
    workbook = openpyxl.load_workbook(xlsx_filename)
    
else:
    #create new file
    print("File doesn't exist.")
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
    worksheet.column_dimensions['C'].width= 3
    worksheet.column_dimensions['D'].width = 7
    worksheet.column_dimensions['E'].width = 35
    worksheet.column_dimensions['F'].width = 15
    

with open(csv_filename, encoding='utf8',newline="") as csv_file:
    csvreader = csv.reader(csv_file)
    for row in csvreader:
        if row[0] == "DATE":
            worksheet = editxlfile.sheet_edit(workbook,row[1])
        else:
            editxlfile.edit(row,worksheet)


workbook.save(xlsx_filename)