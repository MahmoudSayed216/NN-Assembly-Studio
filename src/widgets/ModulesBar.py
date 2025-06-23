import tkinter as tk
from widgets.ModulesList import ModulesList
import customtkinter
from resources.fonts import *
from resources.colors import *


class ModulesBar(tk.Frame):

    def __init__(self, master = None, cnf = None, *, background = None, bd = 0, bg = None, border = 0, borderwidth = 0, class_ = "Frame", colormap = "", container = False, cursor = "", height = 0, highlightbackground = None, highlightcolor = None, highlightthickness = 0, name = None, padx = 0, pady = 0, relief = "flat", takefocus = 0, visual = "", width = 0, x=0, y=0):
        super().__init__(master, cnf, background=background, bd=bd, bg=bg, border=border, borderwidth=borderwidth, class_=class_, colormap=colormap, container=container, cursor=cursor, height=height, highlightbackground=highlightbackground, highlightcolor=highlightcolor, highlightthickness=highlightthickness, name=name, padx=padx, pady=pady, relief=relief, takefocus=takefocus, visual=visual, width=width)
        # self.place(x=x, y=y)
        self.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.configure(width=width, height=height)
        

        self.top_label = tk.Label(self, text="Modules", bg=bg, font=A12B, fg=BLACK)
        self.top_label.pack(pady=5)
        
        self.search_bar_text = tk.StringVar()
        self.search_bar = customtkinter.CTkEntry(self, placeholder_text="Search...", textvariable=self.search_bar_text)
        self.search_bar.bind('<KeyRelease>', lambda event: self.filter_on_key_release())
        self.search_bar.pack(pady=5)

        self.modules_list = ModulesList(self, bg=LIGHTYELLOW, width=width, height=0.95*height)
        self.modules_list.pack(pady=5, fill=tk.Y)

    def filter_on_key_release(self):
        self.modules_list.reflect_on_list(self.search_bar_text.get())