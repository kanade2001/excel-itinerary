from email import message
import os
import tkinter as tk
from tkinter import messagebox
import openpyxl

import System_csv

def Auto_(path,txt):
    print('edit=0')
    pathdata = path.get()
    txtdata = txt.get('1.0',tk.END + '-1c')
    
    
    if pathdata=='' and txtdata=='':
        messagebox.showwarning('入力エラー','何も入力されていません')
    elif pathdata != '':
        print('pathimput')
    else:
        termination = System_csv.main_Create_csv(str.split(txtdata,'\n'),Csv_export=True)
        if termination == 1:
            messagebox.showwarning('入力形式エラー','入力されたデータフォーマットに対応していません')
    
    path.delete(0,tk.END)
    txt.delete('1.0',tk.END)
    