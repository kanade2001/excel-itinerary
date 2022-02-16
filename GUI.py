import tkinter as tk


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
        
        paned_window = tk.PanedWindow(self,orient='horizontal')
        paned_window.pack(expand=True,fill=tk.BOTH,side='left')
        
        left_frame = tk.PanedWindow(paned_window,orient='vertical')
        paned_window.add(left_frame)
        right_frame = tk.PanedWindow(paned_window,orient='vertical')
        paned_window.add(right_frame)
        

#-----------------------------------Left_frame-----------------------------
#-----------------------------------Header_frame---------------------------

        header_frame = tk.Frame(left_frame,height=50,bg='gray')
        header_frame.pack(expand=0,fill=tk.X)
        
        header_label = tk.Label(header_frame,text='Title:',width=10)
        header_label.pack(side='left')
        header_title = tk.Label(header_frame,text='Sample1',width=25)
        header_title.pack(side='left',expand=1,fill='both')
        header_editbutton = tk.Button(header_frame,text='編集',width=5)
        header_editbutton.pack(side='left')
        
#-----------------------------------Main_frame-----------------------------
        main_edit_frame = tk.Frame(left_frame,height=100,bg='black')
        main_edit_frame.pack(expand=1,fill=tk.BOTH)
        
        
        
        first_frame = tk.Frame(main_edit_frame,height=25)
        first_frame.pack(fill=tk.X)
        button_auto = tk.Button(first_frame,text='Auto')
        button_auto.pack(expand=1,fill=tk.BOTH,side=tk.LEFT)
        button_manual = tk.Button(first_frame,text='Manual')
        button_manual.pack(expand=1,fill=tk.BOTH,side=tk.LEFT)
        
        second_frame_auto = tk.Frame(main_edit_frame,height=25)
        second_frame_auto.pack(fill=tk.X)
        sfa_label = tk.Label(second_frame_auto,text='ファイル',width=10)
        sfa_label.pack(side=tk.LEFT)
        sfa_entry = tk.Entry(second_frame_auto)
        sfa_entry.pack(side=tk.LEFT,expand=1,fill=tk.X)
        sfa_button = tk.Button(second_frame_auto,text='参照',width=5)
        sfa_button.pack(side=tk.LEFT)
        
        
        
        
#-----------------------------------Footer_frame---------------------------
        footer_frame = tk.Frame(left_frame,bg='gray')
        footer_frame.pack(fill=tk.X)
        

#-----------------------------------Right_frame----------------------------



if __name__ == '__main__':
    app = App()
    app.mainloop()