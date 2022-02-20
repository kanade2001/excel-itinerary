import csv
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from unicodedata import numeric

import config
import Create_csv
from GUI_TEMPLATE import *




def main_edit(widget):
    edit_mode = 1
    Transport_list = ['鉄道','バス','空路','フェリー','徒歩','観光']

#-----------------------------------Header_frame---------------------------
    
    frame = ttk.Frame(widget,height=10)
    frame.pack(expand=0,fill=tk.X)
    
    header_label = ttk.Label(frame,text='Title:',width=10)
    header_label.pack(side='left')
    header_title = ttk.Label(frame,text='Sample1',width=25)
    header_title.pack(side='left',expand=1,fill='both')
    header_editbutton = ttk.Button(frame,text='編集',width=5)
    header_editbutton.pack(side='left')
        
#-----------------------------------Main_frame-----------------------------
    frame = ttk.Frame(widget,height=60)
    frame.pack(expand=1,fill=tk.BOTH)
    
    #first_frame(Fixed)
    first_frame = ttk.Frame(frame,height=10)
    first_frame.pack(fill=tk.X)
    def Change_Button(num):
        global edit_mode
        button_auto.config(state=tk.ACTIVE)
        button_manual.config(state=tk.ACTIVE)
        if num==1:
            button_auto.config(state=tk.DISABLED)
            second_frame_auto.tkraise()
            third_frame_auto.tkraise()
            edit_mode = 1
        elif num==2:
            button_manual.config(state=tk.DISABLED)
            second_frame_manual.tkraise()
            third_frame_manual.tkraise()
            edit_mode = 2
    button_auto = ttk.Button(first_frame,text='Auto',width=10)
    button_manual = ttk.Button(first_frame,text='Manual',width=10)
    button_auto.config(command=lambda: Change_Button(1))
    button_manual.config(command=lambda: Change_Button(2))
    button_auto.pack(side='left',expand=1,fill='x')
    button_manual.pack(side='left',expand=1,fill='x')
    
    
    #second_frame
    second_frame = ttk.Frame(frame,height=10)
    second_frame.pack(fill=tk.X)
    second_frame.grid_rowconfigure(0, weight=1)
    second_frame.grid_columnconfigure(0, weight=1)
    
    second_frame_auto = ttk.Frame(second_frame)
    second_frame_auto.grid(row=0, column=0, sticky='nsew')
    widget_template.reference_file(second_frame_auto,'Sample1')     #ファイル参照ウィンドウ
    
    second_frame_manual = ttk.Frame(second_frame)
    second_frame_manual.grid(row=0, column=0, sticky='nsew')
    Transport_Buttons = []
    def Transport_change(num):
        def Transport_change_main():
            print('Change to ' + str(num))
            for i,name in enumerate(Transport_list):
                Transport_Buttons[i] = tk.ACTIVE
            Transport_Buttons[num]=tk.DISABLED
            third_frame_manual_frames[num].tkraise()
        return Transport_change_main
    for i,name in enumerate(Transport_list):
        Transport_Buttons.append(ttk.Button(second_frame_manual,text=name,command=Transport_change(i)))
        Transport_Buttons[i].pack(side='left',expand=1,fill='both')


    
    
    #third_frame
    third_frame = ttk.Frame(frame,heigh=10)
    third_frame.pack(expand=1,fill=tk.BOTH)
    third_frame.grid_rowconfigure(0,weight=1)
    third_frame.grid_columnconfigure(0,weight=1)
    
    third_frame_auto = ttk.Frame(third_frame,height=40)
    third_frame_auto.grid(row=0,column=0,sticky='nsew')
    txtbox =tk.Text(third_frame_auto,width=50,height=30)
    txtbox.pack(expand=1,fill=tk.BOTH,side='left')
    scroll = ttk.Scrollbar(third_frame_auto, orient='vertical', command=txtbox.yview)
    scroll.pack(side='right', fill=tk.Y)
    txtbox["yscrollcommand"] = scroll.set
    
    third_frame_manual = ttk.Frame(third_frame,height=10)
    third_frame_manual.grid(row=0,column=0,sticky='nsew')
    third_frame_manual_frames =[]
    for i,name in enumerate(Transport_list):
        third_frame_manual_frames.append(ttk.Frame(third_frame_manual))
        third_frame_manual_frames[i].grid(row=0,column=0,sticky='nsew')
        label = ttk.Label(third_frame_manual_frames[i],text=name)
        label.pack()
    

        
    Change_Button(config.Default_edit)
    Transport_change(0)()


#-----------------------------------Footer_frame---------------------------
    frame = ttk.Frame(widget)
    frame.pack(fill=tk.X)
    left = ttk.Frame(frame)
    left.pack(side='left')
    right = ttk.Frame(frame)
    right.pack(side='right')
    
    
    l1 = ttk.Button(left,text='戻る',width=10)
    l1.pack(side='left')
    l2 = ttk.Button(left,text='やり直し',width=10)
    l2.pack(side='left')
    
    def Clear():
        txtbox.delete('1.0',tk.END)
    r1 = ttk.Button(right,text='入力欄クリア',width=15,command=lambda: Clear())
    r1.pack(side='left')
    
    
    def Enter():
        global edit_mode
        if edit_mode == 1: #AUTO
            print('edit=1')
            Inputtext = txtbox.get('1.0',tk.END + '-1c')    #テキストボックスに入力されているデータを取得
            TransitData = str.split(Inputtext,'\n')
            if Inputtext == '':       #入力なし
                print('Error')
                messagebox.showwarning('入力エラー','何も入力されていません')
            elif Inputtext != '':     #文章入力あり
                termination = Create_csv.main_Create_csv(TransitData,Csv_export=True)
                if termination == 1:    #入力形式エラー
                    messagebox.showwarning('入力形式エラー','入力されたデータフォーマットに対応していません')
            txtbox.delete('1.0',tk.END)
        elif edit_mode ==2:
            print('edit=2')
    r2 = ttk.Button(right,text='入力確定',width=15,command=lambda: Enter())
    r2.pack(side='left')
