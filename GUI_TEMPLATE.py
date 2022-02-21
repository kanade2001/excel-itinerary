import tkinter as tk
import tkinter.ttk as ttk

class input:
    def Clear():
        print('Clear')

class button_event:
    def ChangeModeButtons(self,list,active_frame=None,active_frame_list=None):
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
                print(num)
            return Change_frame_main
        Buttons = []
        for i,name in enumerate(list):
            Buttons.append(ttk.Button(self,text=name,command=Change_frame(i)))
            Buttons[i].pack(side='left',expand=1,fill='both')




class widget_template:
    def reference_file(self,text=''):
        label = ttk.Label(self,text='ファイル',width=10)
        label.pack(side=tk.LEFT)
        entry = ttk.Entry(self,text=text)
        entry.pack(side=tk.LEFT,expand=1,fill=tk.X)
        button = ttk.Button(self,text='参照',width=5)
        button.pack(side=tk.LEFT)
        
