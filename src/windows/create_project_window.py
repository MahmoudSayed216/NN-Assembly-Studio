import tkinter as tk
from resources.colors import *
from resources.fonts import *
class CreateProjectWindow:


    def __init__(self, root):
        
        self.HORIZONTAL_WALL = 70
        self.VERTICAL_WALL = 100
        self.VERTICAL_SEP = 50

        self.root = root
        self.window = tk.Toplevel(root)
        self.window.title("New Project")
        self.window.geometry("800x500")
        self.create_buttons()
        self.create_labels()
        self.create_text_boxes()

        
    def trash(self):
            print(self.model_text_box.get())


    def create_buttons(self):
        button = tk.Button(self.window, text="Create",command=lambda: self.trash())
        button.place(x=670, y=420)


    def create_labels(self):
        self.model_name_lbl = tk.Label(self.window, text="Model name", fg= SKYBLUE, font=D12)
        self.model_name_lbl.place(x=self.VERTICAL_WALL, y=self.HORIZONTAL_WALL)
        
        self.path_lbl = tk.Label(self.window, text="path", fg= SKYBLUE, font=D12)
        self.path_lbl.place(x=self.VERTICAL_WALL, y=self.HORIZONTAL_WALL+self.VERTICAL_SEP)


    def create_text_boxes(self):
         self.model_text_box = tk.Entry(self.window,width=50)
         self.model_text_box.place(x=self.VERTICAL_WALL+100, y=self.HORIZONTAL_WALL)

         self.path_text_box = tk.Entry(self.window, width=50, textvariable=tk.StringVar(value="JONG DONG"))
         self.path_text_box.place(x=self.VERTICAL_WALL+100, y=self.HORIZONTAL_WALL+self.VERTICAL_SEP)