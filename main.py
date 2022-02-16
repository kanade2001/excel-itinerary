import os
import csv
import kivy
import openpyxl

import Edit_xlsx
import Create_csv
from config import *


workbook = Edit_xlsx.openXLSX(xlsx_filename)

with open(csv_filename, encoding='utf8',newline="") as csv_file:
    csvreader = csv.reader(csv_file)
    for row in csvreader:
        Edit_xlsx.edit(row,workbook)


workbook.save(xlsx_filename)