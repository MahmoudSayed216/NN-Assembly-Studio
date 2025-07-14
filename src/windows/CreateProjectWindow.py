import tkinter as tk
from resources.colors import *
from resources.fonts import *
from handlers.CreateProjectWindowHandlers import *



class CreateProjectWindow:


    def __init__(self, root):
        
        self.HORIZONTAL_WALL = 70
        self.VERTICAL_WALL = 100
        self.VERTICAL_SEP = 50

        self.root = root
        self.window = tk.Toplevel(root)
        self.window.title("New Project")
        self.window.geometry("800x500")
        self.create_labels()
        self.create_vars()
        self.create_text_boxes()
        self.create_buttons()


    def create_buttons(self) -> None:
        create_button = tk.Button(self.window, text="Create",command=lambda: create_project(self.root, self.window, self.model_name_tvar, self.path_tvar))
        create_button.place(x=670, y=420)

        browse_button = tk.Button(self.window, text="Browse", command=lambda: browse(self.window, self.path_text_box))
        browse_button.place(x=580, y=self.HORIZONTAL_WALL+self.VERTICAL_SEP-5)

    def create_labels(self):
        self.model_name_lbl = tk.Label(self.window, text="Model name", fg= SKYBLUE, font=D12)
        self.model_name_lbl.place(x=self.VERTICAL_WALL, y=self.HORIZONTAL_WALL)
        
        self.path_lbl = tk.Label(self.window, text="path", fg= SKYBLUE, font=D12)
        self.path_lbl.place(x=self.VERTICAL_WALL, y=self.HORIZONTAL_WALL+self.VERTICAL_SEP)

        self.load_all_mods_lbl = tk.Label(self.window, text="Load all Modules")


    def create_text_boxes(self):
         self.model_text_box = tk.Entry(self.window,width=50, textvariable=self.model_name_tvar)
         self.model_text_box.place(x=self.VERTICAL_WALL+100, y=self.HORIZONTAL_WALL)

         self.path_text_box = tk.Entry(self.window, width=50, textvariable=self.path_tvar)
         self.path_text_box.place(x=self.VERTICAL_WALL+100, y=self.HORIZONTAL_WALL+self.VERTICAL_SEP)

    def create_vars(self):
         self.path_tvar = tk.StringVar(value="path/to/project")
         self.model_name_tvar = tk.StringVar(value="ResNet50")