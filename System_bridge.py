from email import message
import os
import tkinter as tk
from tkinter import messagebox

import main
from config import *
import System_csv
import System_xlsx
import System_filemanager


def Auto_(path,txt):
    print('edit=0')
    pathdata = path.get()
    txtdata = txt.get('1.0',tk.END + '-1c')
    
    
    if pathdata=='' and txtdata=='':
        messagebox.showwarning('入力エラー','何も入力されていません')
    elif pathdata != '':
        print('pathimput')
    else:
        termination = System_csv.main_Create_csv(str.split(txtdata,'\n'),Csv_export=False)
        if termination[0] == 0:
            print('正常終了')
            for row in termination[1]:
                System_xlsx.edit(row,main.workbook)
            main.workbook.save(xlsx_filename)
        if termination[0] == 1:
            messagebox.showwarning('入力形式エラー','入力されたデータフォーマットに対応していません')
    
    path.delete(0,tk.END)
    txt.delete('1.0',tk.END)