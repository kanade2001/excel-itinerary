import openpyxl
import os

#path = r"C:\Users\Yuki\GoogleDrive_kanade2001.cpp\travel\\"

name = "sample1.xlsx"



#Make file

filename = name
#filename = path + filename
#filename = os.path.expanduser(filename)
if os.path.exists(filename):
    print("File exists.")
    workbook = openpyxl.load_workbook(filename)
else:
    print("File doesn't exist.")
    workbook = openpyxl.Workbook()
    workbook.save(filename)

worksheet = workbook.create_sheet(title="toppage", index = 0)
worksheet.cell(row = 1, column = 1, value="this should be the first sheet")

#Data input


workbook.save(filename)