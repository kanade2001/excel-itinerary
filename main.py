import openpyxl
import os
import csv

import editxlfile

#path = r"C:\Users\Yuki\GoogleDrive_kanade2001.cpp\travel\\"

name = "Sample1"

#
xlsx_filename = name + ".xlsx"
#filename = path + filename
#filename = os.path.expanduser(filename)
csv_filename = name + ".csv"


workbook = ""
worksheet = ""



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
        print(row)
        if row[0] == "0":
            print("Check DATE")
            if row[1] not in workbook.sheetnames:
                workbook.copy_worksheet(workbook.worksheets[0])
                workbook.worksheets[-1].title = row[1]
            worksheet = workbook[row[1]]
        
        if row[0] == "1":
            row_write = worksheet.max_row + 1
            worksheet.cell(row=row_write,column=4).value = row[1]
            worksheet.cell(row=row_write,column=1).value = row[2]
            worksheet.cell(row=row_write,column=3).value = row[3]
            worksheet.cell(row=row_write+3,column=4).value = row[4]
            worksheet.cell(row=row_write+3,column=1).value = row[5]
            worksheet.cell(row=row_write+3,column=3).value = row[6]
            worksheet.cell(row=row_write+1,column=5).value = row[7]
            worksheet.cell(row=row_write+1,column=6).value = row[8]
            worksheet.cell(row=row_write+2,column=5).value = row[9]
            worksheet.cell(row=row_write+2,column=6).value = row[10]


workbook.save(xlsx_filename)