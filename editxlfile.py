import openpyxl

def edit(row, worksheet):

    if row[0] =="1":
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