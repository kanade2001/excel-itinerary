import openpyxl
import os
import csv

#path = r"C:\Users\Yuki\GoogleDrive_kanade2001.cpp\travel\\"

name = "Sample1"



#Make file

xlsx_filename = name + ".xlsx"
#filename = path + filename
#filename = os.path.expanduser(filename)
if os.path.exists(xlsx_filename):
    #open file
    print("File exists.")
    workbook = openpyxl.load_workbook(xlsx_filename)
    
    worksheet = workbook.active
    
else:
    #create new file
    print("File doesn't exist.")
    workbook = openpyxl.Workbook()
    workbook.save(xlsx_filename)
    
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
    worksheet.column_dimensions['C'].width= 5
    worksheet.column_dimensions['D'].width = 35
    worksheet.column_dimensions['E'].width = 15
    worksheet.column_dimensions['F'].width = 10
    

csv_filename = name + ".csv"
with open(csv_filename, encoding='utf8',newline="") as csv_file:
    csvreader = csv.reader(csv_file)
    for row in csvreader:
        print(row)




workbook.save(xlsx_filename)