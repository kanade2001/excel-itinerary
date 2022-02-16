import os
import csv
import kivy
import openpyxl

import Edit_xlsx
import Create_csv
from config import *


workbook = Edit_xlsx.openXLSX(xlsx_filename)
worksheet = workbook.worksheets[0]

with open(csv_filename, encoding='utf8',newline="") as csv_file:
    csvreader = csv.reader(csv_file)
    for row in csvreader:
        print (row)

        if row[0] == 'DATE':
            worksheet = Edit_xlsx.sheet_edit(workbook,row[1])
        else:
            Edit_xlsx.edit(row,worksheet)


workbook.save(xlsx_filename)