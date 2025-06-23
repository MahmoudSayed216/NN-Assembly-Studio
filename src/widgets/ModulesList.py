import tkinter as tk
from resources.colors import *
from widgets.ScrollableFrame import ScrollableFrame
from models.ModuleData import ModuleData



class ModulesList(tk.Frame):
    def __init__(self, master = None, cnf = None, *, background = None, bd = 0, bg = None, border = 0, borderwidth = 0, class_ = "Frame", colormap = "", container = False, cursor = "", height = 0, highlightbackground = None, highlightcolor = None, highlightthickness = 0, name = None, padx = 0, pady = 0, relief = "flat", takefocus = 0, visual = "", width = 0, x=0, y=0, relx= 0, rely=0):
        super().__init__(master, cnf, background=background, bd=bd, bg=bg, border=border, borderwidth=borderwidth, class_=class_, colormap=colormap, container=container, cursor=cursor, height=height, highlightbackground=highlightbackground, highlightcolor=highlightcolor, highlightthickness=highlightthickness, name=name, padx=padx, pady=pady, relief=relief, takefocus=takefocus, visual=visual, width=width)
        if relx!=0 and rely != 0:
            self.place(relx=relx, rely=rely, anchor='n')
        else:
            self.place(x=x, y=y)
        

        self.module_containers_refs = []


        mod1 = ModuleData("Conv2D", "/home/mahmoud-sayed/Desktop/Code/Python/NN Assembly Studio/src/resources/modules_images/Conv2D.png")
        mod2 = ModuleData("MaxPooling2D", "/home/mahmoud-sayed/Desktop/Code/Python/NN Assembly Studio/src/resources/modules_images/MaxPooling2D.png")
        mod3 = ModuleData("Linear", "/home/mahmoud-sayed/Desktop/Code/Python/NN Assembly Studio/src/resources/modules_images/noname.png")

        models = [mod1, mod2, mod3]


        self.scrollable_frame = ScrollableFrame(self, models, width, height)

    def reflect_on_list(self, search_txt):
        self.scrollable_frame.hide_unhide_containers(search_txt)