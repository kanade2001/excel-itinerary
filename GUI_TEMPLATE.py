from atexit import register
import tkinter as tk
import tkinter.ttk as ttk
import re

edit_mode = 0



class widget_template:
    def reference_file(self,text=''):
        label = ttk.Label(self,text='ファイル',width=10)
        label.pack(side='left')
        entry = ttk.Entry(self,text=text)
        entry.pack(side='left',expand=1,fill=tk.X)
        button = ttk.Button(self,text='参照',width=5)
        button.pack(side='left')
        return entry
        
    def ScrollTxt(self):
        textbox =tk.Text(self,width=50,height=30)
        textbox.pack(expand=1,fill='both',side='left')
        scroll = ttk.Scrollbar(self, orient='vertical', command=textbox.yview)
        scroll.pack(side='right', fill='y')
        textbox["yscrollcommand"] = scroll.set
        return textbox
    
    def ENTRY(self, label_text,format = ''):
        def validate(str):
            return re.match(format,str)
        vc = register(validate)
        label = ttk.Label(self,width=15,text=label_text)
        label.pack(expand=0,side='left')
        entry = ttk.Entry(self)
        if format != '':
            print('validate')
            entry.configure(validate='key',validatecommand=(vc, '%P'))
        entry.pack(expand=1,side='left',fill='x')
        return entry



class button_event:
    
    def ChangeModeButtons(self,list,active_frame=None,active_frame_list=None,optcmd=0):
        def Change_frame(num):
            def Change_frame_main():
                for i in Buttons:
                    i.config(state=tk.ACTIVE)
                Buttons[num].config(state=tk.DISABLED)
                if active_frame != None:
                    active_frame[num].tkraise()
                if active_frame_list != None:
                    for i in active_frame_list[num]:
                        i.tkraise()
            return Change_frame_main
        Buttons = []
        for i,name in enumerate(list):
            Buttons.append(ttk.Button(self,text=name,command=Change_frame(i)))
            Buttons[i].pack(side='left',expand=1,fill='both')

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
    def make_frame(self,grid=False,height=10,expand=0,fill='x'):
        frame = ttk.Frame(self,height=height)
        frame.pack(expand=expand,fill=fill)
        if grid:
                frame.grid_rowconfigure(0, weight=1)
                frame.grid_columnconfigure(0, weight=1)
        return frame
    
    def make_frame_grid(self,height=10,width=40):
        frame = ttk.Frame(self,height=10,width=40)
        frame.grid(row=0, column=0,sticky='nsew')
        return frame
    
