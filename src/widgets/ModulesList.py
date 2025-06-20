import tkinter as tk
import customtkinter
from widgets.ModuleContainer import ModuleContainer
from models.ModuleData import ModuleData
from resources.colors import *


class ModulesList(tk.Frame):
    def __init__(self, master = None, cnf = None, *, background = None, bd = 0, bg = None, border = 0, borderwidth = 0, class_ = "Frame", colormap = "", container = False, cursor = "", height = 0, highlightbackground = None, highlightcolor = None, highlightthickness = 0, name = None, padx = 0, pady = 0, relief = "flat", takefocus = 0, visual = "", width = 0, x=0, y=0, relx= 0, rely=0):
        super().__init__(master, cnf, background=background, bd=bd, bg=bg, border=border, borderwidth=borderwidth, class_=class_, colormap=colormap, container=container, cursor=cursor, height=height, highlightbackground=highlightbackground, highlightcolor=highlightcolor, highlightthickness=highlightthickness, name=name, padx=padx, pady=pady, relief=relief, takefocus=takefocus, visual=visual, width=width)
        if relx!=0 and rely != 0:
            self.place(relx=relx, rely=rely, anchor='n')
        else:
            self.place(x=x, y=y)
        scrollable_frame = customtkinter.CTkScrollableFrame(self, corner_radius=0, width=width, height=height)
        scrollable_frame.place(relx=0.5, rely=0, anchor='n')


        mod1 = ModuleData("Conv2D", "/home/mahmoud-sayed/Desktop/Code/Python/NN Assembly Studio/src/resources/modules_images/cnn.png")
        mod2 = ModuleData("MLP", "/home/mahmoud-sayed/Desktop/Code/Python/NN Assembly Studio/src/resources/modules_images/mlp.jpg")

        # for mod in [mod1, mod2]:
            # customtkinter.CTkButton(scrollable_frame, text="this is a button!!", corner_radius=0).pack(pady=15)
            # print("loaded")
            # ModuleContainer(scrollable_frame, bg=WHITE, width=130, height=130, module_data=mod)

        for i in range(30):
            ModuleContainer(scrollable_frame, bg=WHITE, width=130, height=130, module_data=mod1)
