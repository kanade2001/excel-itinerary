from argparse import FileType
from atexit import register
from distutils import command
from textwrap import fill

import tkinter as tk
import tkinter.filedialog
import tkinter.ttk as ttk
import re
import os
import sys


edit_mode = 0



class widget_template:
    def reference_file(self,text=''):
        label = ttk.Label(self,text='ファイル',width=10)
        label.pack(side='left')
        entry = ttk.Entry(self,text=text)
        entry.pack(side='left',expand=1,fill=tk.X)
        def dialog():
            File = os.path.abspath(os.path.dirname(__file__))
            FilePath = tkinter.filedialog.askopenfilename()
            entry.delete(0,tk.END)
            entry.insert(tk.END,FilePath)
        button = ttk.Button(self,text='参照',width=5,command=lambda: dialog())
        button.pack(side='left')
        return entry
        
    def ScrollTxt(self):
        textbox =tk.Text(self,width=50,height=30)
        textbox.pack(expand=1,fill='both',side='left')
        scroll = ttk.Scrollbar(self, orient='vertical', command=textbox.yview)
        scroll.pack(side='right', fill='y')
        textbox["yscrollcommand"] = scroll.set
        return textbox
    
    def ENTRY(self, row, label_text, format = ''):
        def validate(str):
            if re.fullmatch(format,str):
                return True
            return False
        vc = self.register(validate)
        label = ttk.Label(self,width=15,text=label_text)
        label.grid(row=row,column=0,sticky=tk.W)
        entry = ttk.Entry(self)
        if format != '':
            print('validate')
            entry.configure(validate='key',validatecommand=(vc, '%P'))
        entry.grid(row=row,column=1,sticky=tk.W+tk.E)
        return entry


class button_command:
    def Select_button(buttons, disable_button):
        for i in buttons:
            i.config(state = tk.ACTIVE)
        disable_button.config(state = tk.DISABLED)
    
    def Change_frame(frame):
        frame.tkraise()


class callback_button_command:
    def mode_change(num, buttons, raise_frame):
        def main():
            button_command.Select_button(buttons, buttons[num])
            for frame in raise_frame:
                button_command.Change_frame(frame)
            global edit_mode
            edit_mode = num
        return main

    def transportation_change(buttons, button):
        def main():
            button_command.Select_button(buttons, button)
        return main

class button_template:
    def make_buttons(self, list):
        Buttons = []
        for i, text in enumerate(list):
            Buttons.append(ttk.Button(self,text=text))
            Buttons[i].pack(side='left',expand=1,fill='both')
        return Buttons




class frame_widget:
    def make_frame(self,grid=False,height=10,expand=0,fill='x',padding=0):
        frame = ttk.Frame(self,height=height,padding=padding)
        frame.pack(expand=expand,fill=fill)
        if grid:
                frame.grid_rowconfigure(0, weight=1)
                frame.grid_columnconfigure(0, weight=1)
        return frame
    
    def make_frame_grid(self,height=10,width=40):
        frame = ttk.Frame(self,height=10,width=40)
        frame.grid(row=0, column=0,sticky='nsew')
        return frame
    
    def make_labelframe(self,text,height=10,expand=0,fill='x'):
        frame = ttk.LabelFrame(self,height=10,width=40,text=text)
        frame.pack(expand=expand,fill=fill)
        return frame
