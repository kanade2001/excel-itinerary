import tkinter as tk
import tkinter.ttk as ttk
import Edit_main



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
    
    def buttons(widget,list,width,expandsettings):
        for i, text in enumerate(list):
            button = ttk.Button(widget,text=text,width=width[i])
            button.pack(expand=expandsettings[i],side=tk.LEFT,fill=tk.BOTH)


#-----------------------------------Edit_frame-----------------------------

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title('Itinerary Tool')
        self.geometry('1024x768+0+0')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

#-----------------------------------main_frame-----------------------------
        # メインページフレーム作成
        
        paned_window = ttk.PanedWindow(self,orient='horizontal')
        paned_window.pack(expand=True,fill=tk.BOTH,side='left')
        
        left_frame = ttk.PanedWindow(paned_window,orient='vertical')
        paned_window.add(left_frame)
        right_frame = ttk.PanedWindow(paned_window,orient='vertical')
        paned_window.add(right_frame)
        
#-----------------------------------Left_frame-----------------------------
        frame_settings.header_frame(left_frame)
        frame_settings.main_edit_frame(left_frame)
        frame_settings.footer_frame(left_frame)

#-----------------------------------Right_frame----------------------------

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
        frame = ttk.Frame(widget,height=60)
        frame.pack(expand=1,fill=tk.BOTH)
        
        first_frame = ttk.Frame(frame,height=10)
        first_frame.pack(fill=tk.X)
        button_auto = ttk.Button(first_frame,text='Auto',width=10)
        button_auto.pack(side='left',expand=1,fill='x')
        button_auto = ttk.Button(first_frame,text='Manual',width=10)
        button_auto.pack(side='left',expand=1,fill='x')
        
        
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
        r2 = ttk.Button(right,text=test,width=15,command=button_event.Edit_Enter())
        r2.pack(side='left')



if __name__ == '__main__':
    app = App()
    app.mainloop()