from tkinter import filedialog as fd
import tkinter as tk
from models.Project import Project
from windows.work_window import WorkWindow


def create_project(master_of_master, master, model_name_tvar, path_tvar):
    master_of_master.withdraw()
    master.withdraw()
    model_name = model_name_tvar.get()
    path = path_tvar.get()
    project = Project(model_name, path)
    WorkWindow(master, project)



def browse(parent, path_tbox: tk.Entry):
    save_path = fd.askopenfilename(parent=parent)
    path_tbox.delete(0, tk.END)
    path_tbox.insert(0, save_path)
    pass