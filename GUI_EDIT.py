import csv
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from unicodedata import numeric
from xmlrpc.client import Transport

import config
import Create_csv
from GUI_TEMPLATE import *




def main_edit(widget):
    edit_mode = 1
    MODE_list = ['Auto','Manual']
    Transport_list = ['鉄道','バス','空路','フェリー','徒歩','観光']

#-----------------------------------Header_frame---------------------------
    frame = frame_widget.make_frame(widget)
    
    header_label = ttk.Label(frame,text='Title:',width=10)
    header_label.pack(side='left')
    header_title = ttk.Label(frame,text='Sample1',width=25)
    header_title.pack(side='left',expand=1,fill='both')
    header_editbutton = ttk.Button(frame,text='編集',width=5)
    header_editbutton.pack(side='left')
        
#-----------------------------------Main_frame-----------------------------

    frame = frame_widget.make_frame(widget)
    
    #select_frame(Fixed)
    select_frame = frame_widget.make_frame(frame)

    
    #second_frame
    second_frame = frame_widget.make_frame(frame,grid=True)
    second_frame_auto = frame_widget.make_frame_grid(second_frame)
    second_frame_manual = frame_widget.make_frame_grid(second_frame)
    
    
    widget_template.reference_file(second_frame_auto,'Sample1')     #ファイル参照ウィンドウ
    
    #third_frame
    third_frame = frame_widget.make_frame(frame,grid=True,fill='both')
    third_frame_auto = frame_widget.make_frame_grid(third_frame)
    txtbox = widget_template.ScrollTxt(third_frame_auto)
    
    third_frame_manual = frame_widget.make_frame_grid(third_frame)
    third_frame_manual_frames =[]
    for i,name in enumerate(Transport_list):
        third_frame_manual_frames.append(ttk.Frame(third_frame_manual))
        third_frame_manual_frames[i].grid(row=0,column=0,sticky='nsew')
        label = ttk.Label(third_frame_manual_frames[i],text=name)
        label.pack()

    
    
    Mode_buttons = button_template.make_buttons(select_frame, MODE_list)
    Mode_buttons[0].config(
        command=callback_button_command.mode_change(
            num = 0,
            buttons = Mode_buttons,
            raise_frame = [second_frame_auto,third_frame_auto]
            )
        )
    Mode_buttons[1].config(
        command=callback_button_command.mode_change(
            num = 1,
            buttons = Mode_buttons,
            raise_frame = [second_frame_manual,third_frame_manual]
            )
        )

    Transport_buttons = button_template.make_buttons(second_frame_manual, Transport_list)
    for button in Transport_buttons:
        button.config(command=callback_button_command.transportation_change(Transport_buttons, button))


#-----------------------------------Footer_frame---------------------------
    frame = frame_widget.make_frame(widget)

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
