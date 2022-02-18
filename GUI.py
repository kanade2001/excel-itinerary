import tkinter as tk
import tkinter.ttk as ttk

from GUI_TEMPLATE import *
import GUI_EDIT


#-----------------------------------Edit_frame-----------------------------
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title('Itinerary Tool')
        self.geometry('1024x768+0+0')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


#-----------------------------------main_frame-----------------------------
        paned_window = ttk.PanedWindow(self,orient='horizontal')
        paned_window.pack(expand=True,fill=tk.BOTH,side='left')
        
        left_frame = ttk.PanedWindow(paned_window,orient='vertical')
        paned_window.add(left_frame)
        right_frame = ttk.PanedWindow(paned_window,orient='vertical')
        paned_window.add(right_frame)
        
#-----------------------------------Left_frame-----------------------------
        GUI_EDIT.frame_settings.header_frame(left_frame)
        GUI_EDIT.frame_settings.main_edit_frame(left_frame)
        GUI_EDIT.frame_settings.footer_frame(left_frame)

#-----------------------------------Right_frame----------------------------


if __name__ == '__main__':
    app = App()
    app.mainloop()