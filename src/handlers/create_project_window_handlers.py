from tkinter import filedialog as fd
import tkinter as tk
from models.Project import Project

def create_project(model_name_tvar, path_tvar):
    print(model_name_tvar.get())
    print(path_tvar.get())
    model_name = model_name_tvar.get()
    path = path_tvar.get()
    project = Project(model_name, path)
    print(project)


def browse(parent, path_tbox: tk.Entry):
    save_path = fd.askopenfilename(parent=parent)
    path_tbox.delete(0, tk.END)
    path_tbox.insert(0, save_path)
    pass