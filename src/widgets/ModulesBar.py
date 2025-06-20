import tkinter as tk
from widgets.ModulesList import ModulesList
from resources.fonts import *
from resources.colors import *


class ModulesBar(tk.Frame):

    def __init__(self, master = None, cnf = None, *, background = None, bd = 0, bg = None, border = 0, borderwidth = 0, class_ = "Frame", colormap = "", container = False, cursor = "", height = 0, highlightbackground = None, highlightcolor = None, highlightthickness = 0, name = None, padx = 0, pady = 0, relief = "flat", takefocus = 0, visual = "", width = 0, x=0, y=0):
        super().__init__(master, cnf, background=background, bd=bd, bg=bg, border=border, borderwidth=borderwidth, class_=class_, colormap=colormap, container=container, cursor=cursor, height=height, highlightbackground=highlightbackground, highlightcolor=highlightcolor, highlightthickness=highlightthickness, name=name, padx=padx, pady=pady, relief=relief, takefocus=takefocus, visual=visual, width=width)
        self.place(x=x, y=y)
        self.update_idletasks()
        self.WIDTH = self.winfo_width()
        self.HEIGHT = self.winfo_height()

        self.top_label = tk.Label(self, text="Modules", bg=bg, font=A12B, fg=BLACK)
        self.top_label.place(relx=0.5, rely=0.015, anchor='n')

        
        # self.modules_list = tk.Canvas(self, bg=WHITE, width=0.9*self.WIDTH, height=0.89*self.HEIGHT)
        # self.modules_list.place(relx=0.5, rely=0.05, anchor='n')
        self.modules_list = ModulesList(self, bg=WHITE, width=0.9*self.WIDTH, height=0.9*self.HEIGHT,relx=0.5, rely=0.045)