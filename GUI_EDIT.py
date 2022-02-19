import tkinter as tk
import tkinter.ttk as ttk

import config
from GUI_TEMPLATE import *

class frame_settings:
#-----------------------------------Header_frame---------------------------
    def header_frame(widget):
        frame = ttk.Frame(widget,height=10)
        frame.pack(expand=0,fill=tk.X)
        
        header_label = ttk.Label(frame,text='Title:',width=10)
        header_label.pack(side='left')
        header_title = ttk.Label(frame,text='Sample1',width=25)
        header_title.pack(side='left',expand=1,fill='both')
        header_editbutton = ttk.Button(frame,text='編集',width=5)
        header_editbutton.pack(side='left')
        
#-----------------------------------Main_frame-----------------------------
    def main_edit_frame(widget):
        
        def Change_Button(num):
            button_auto.config(state=tk.ACTIVE)
            button_manual.config(state=tk.ACTIVE)
            if num==1:
                button_auto.config(state=tk.DISABLED)
                second_frame_auto.tkraise()
            elif num==2:
                button_manual.config(state=tk.DISABLED)
                second_frame_manual.tkraise()
        
        frame = ttk.Frame(widget,height=60)
        frame.pack(expand=1,fill=tk.BOTH)
        
        #first_frame(Fixed)
        first_frame = ttk.Frame(frame,height=10)
        first_frame.pack(fill=tk.X)
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
        
        
        
        #third_frame
        third_frame = ttk.Frame(frame,heigh=10)
        third_frame.pack(expand=1,fill=tk.BOTH)
        third_frame.grid_rowconfigure(0,weight=1)
        third_frame.grid_columnconfigure(0,weight=1)
        
        third_frame_auto = ttk.Frame(third_frame,height=40)
        third_frame_auto.pack(expand=1,fill=tk.BOTH)
        txtbox =tk.Text(third_frame_auto,width=50,height=30)
        txtbox.pack(expand=1,fill=tk.BOTH,side='left')
        scroll = ttk.Scrollbar(third_frame_auto, orient='vertical', command=txtbox.yview)
        scroll.pack(side='right', fill=tk.Y)
        txtbox["yscrollcommand"] = scroll.set
        
        third_frame_manual = ttk.Frame(third_frame,height=10)
        third_frame_manual.pack(expand=1,fill=tk.BOTH)
        

            
        Change_Button(config.Default_edit)


#-----------------------------------Footer_frame---------------------------
    def footer_frame(widget):
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
        r1 = ttk.Button(right,text='入力欄クリア',width=15)
        r1.pack(side='left')
        r2 = ttk.Button(right,text='入力確定',width=15,command=lambda: button_event.Edit_Enter())
        r2.pack(side='left')
