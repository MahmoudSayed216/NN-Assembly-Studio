import tkinter as tk


class ModuleContainer:
    def __init__(self, master, bg, width, height):
        self.frame = tk.Frame(master, width=width, height=height)
        