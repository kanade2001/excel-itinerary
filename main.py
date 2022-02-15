import os
import csv
import openpyxl

import Edit_xlsx
import Edit_csv
from config import *


workbook = Edit_csv.openXLSX(xlsx_filename)

with open(csv_filename, encoding='utf8',newline="") as csv_file:
    csvreader = csv.reader(csv_file)
    for row in csvreader:
        if row[0] == "DATE":
            worksheet = Edit_xlsx.sheet_edit(workbook,row[1])
        else:
            Edit_xlsx.edit(row,worksheet)


workbook.save(xlsx_filename)