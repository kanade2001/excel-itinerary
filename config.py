import os
path = os.getcwd()
print(path)

name = "Sample1"

xlsx_filename = name + ".xlsx"
csv_filename = name + ".csv"
txt_filename = name + ".txt"



jorudan_datapattern_date = "\d{4}/\d{2}/\d{2}"
jorudan_datapattern_train = "(■|◇)[^ ]+"

#Default Open Edit Mode
Default_edit = 1
#AUTO = 1
#MANUAL = 2

with open(txt_filename) as f:
    s = f.read()
    print(s)