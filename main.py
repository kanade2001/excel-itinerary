import os
import csv

import System_xlsx
import System_csv
import System_filemanager
from config import *


workbook = System_filemanager.openXLSX(xlsx_filename)

with open(csv_filename, encoding='utf8',newline="") as csv_file:
    csvreader = csv.reader(csv_file)
    for row in csvreader:
        System_xlsx.edit(row,workbook)


workbook.save(xlsx_filename)