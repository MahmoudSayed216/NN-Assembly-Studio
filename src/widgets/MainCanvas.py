import tkinter as tk
from resources.fonts import *


# class MainCanvas(tk.Canvas):
#     def __init__(self, master, x, y, width, height, bg):
#         super().__init__(master=master, width=width, height=height, bg=bg)
#         self.place(x=x, y=y)


class MainCanvas(tk.Canvas):
    def __init__(self, master = None, cnf = None, *, background = None, bd = 0, bg = None, border = 0, borderwidth = 0, closeenough = 1, confine = True, cursor = "", height = None, highlightbackground = None, highlightcolor = None, highlightthickness = None, insertbackground = None, insertborderwidth = 0, insertofftime = 300, insertontime = 600, insertwidth = 2, name = None, offset=None, relief = "flat", scrollregion = None, selectbackground = None, selectborderwidth = 1, selectforeground = None, state = "normal", takefocus = "", width = None, xscrollcommand = "", xscrollincrement = 0, yscrollcommand = "", yscrollincrement = 0, x=0, y=0):
        super().__init__(master, cnf, background=background, bd=bd, bg=bg, border=border, borderwidth=borderwidth, closeenough=closeenough, confine=confine, cursor=cursor, height=height, highlightbackground=highlightbackground, highlightcolor=highlightcolor, highlightthickness=highlightthickness, insertbackground=insertbackground, insertborderwidth=insertborderwidth, insertofftime=insertofftime, insertontime=insertontime, insertwidth=insertwidth, name=name, offset=offset, relief=relief, scrollregion=scrollregion, selectbackground=selectbackground, selectborderwidth=selectborderwidth, selectforeground=selectforeground, state=state, takefocus=takefocus, width=width, xscrollcommand=xscrollcommand, xscrollincrement=xscrollincrement, yscrollcommand=yscrollcommand, yscrollincrement=yscrollincrement)
        self.place(x=x, y=y)
        

        self.create_buttons()

    def create_buttons(self):
        BUTTONS_SEP_Y = 0.04
        BUTTONS_VERTICAL_WALL = 0.95
        BUTTONS_HORIZONTAL_BASE = 0.82
        self.home_btn = tk.Button(self, text="H", font=A15B)
        self.home_btn.place(relx=BUTTONS_VERTICAL_WALL, rely=BUTTONS_HORIZONTAL_BASE)
        
        self.zoom_in_btn = tk.Button(self, text="+", font=A15B)
        self.zoom_in_btn.place(relx=BUTTONS_VERTICAL_WALL, rely=BUTTONS_HORIZONTAL_BASE+BUTTONS_SEP_Y*1)
        
        self.zoom_out_btn = tk.Button(self, text="-", font=A15B)
        self.zoom_out_btn.place(relx=BUTTONS_VERTICAL_WALL, rely=BUTTONS_HORIZONTAL_BASE+BUTTONS_SEP_Y*2)
        