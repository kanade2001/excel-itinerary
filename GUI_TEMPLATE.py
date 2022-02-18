import tkinter as tk
import tkinter.ttk as ttk

class button_event:
    def Edit_Enter():
        print('Hello')


class widget_template:
    def reference_file(widget,text=''):
        label = ttk.Label(widget,text='ファイル',width=10)
        label.pack(side=tk.LEFT)
        entry = ttk.Entry(widget,text=text)
        entry.pack(side=tk.LEFT,expand=1,fill=tk.X)
        button = ttk.Button(widget,text='参照',width=5)
        button.pack(side=tk.LEFT)