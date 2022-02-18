import tkinter as tk
import tkinter.ttk as ttk
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
        def change_button(button1,button2):
            button1.config(state=tk.DISABLED)
            button2.config(state=tk.ACTIVE)
            print('Changed')
            
        
        frame = ttk.Frame(widget,height=60)
        frame.pack(expand=1,fill=tk.BOTH)
        
        first_frame = ttk.Frame(frame,height=10)
        first_frame.pack(fill=tk.X)
        button_auto = ttk.Button(first_frame,text='Auto',width=10)
        button_manual = ttk.Button(first_frame,text='Manual',width=10)
        button_auto.config(command=lambda: change_button(button_auto,button_manual),state=tk.ACTIVE)
        button_manual.config(command=lambda: change_button(button_manual,button_auto),state=tk.DISABLED)
        button_auto.pack(side='left',expand=1,fill='x')
        button_manual.pack(side='left',expand=1,fill='x')
        
        
        second_frame_auto = ttk.Frame(frame,height=10)
        second_frame_auto.pack(fill=tk.X)
        widget_template.reference_file(second_frame_auto,'Sample1')     #ファイル参照ウィンドウ
        
        third_frame_auto = ttk.Frame(frame,height=40)
        third_frame_auto.pack(expand=1,fill=tk.BOTH)
        txtbox =tk.Text(third_frame_auto,width=50,height=30)
        txtbox.pack(expand=1,fill=tk.BOTH,side='left')
        scroll = ttk.Scrollbar(third_frame_auto, orient='vertical', command=txtbox.yview)
        scroll.pack(side='right', fill=tk.Y)
        txtbox["yscrollcommand"] = scroll.set


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
