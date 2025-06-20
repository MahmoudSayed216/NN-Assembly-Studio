from tkinter import filedialog as fd
from tkinter import messagebox
import tkinter as tk

from models.Project import Project
from windows.WorkWindow import WorkWindow


def create_project(master_of_master, master, model_name_tvar, path_tvar):

    model_name = model_name_tvar.get()
    path = path_tvar.get()
    
    if model_name == "" or path == "":
        messagebox.showerror("Incomplete info", message="Project can't be created without incomplete info", parent=master)
        return
    
    master_of_master.withdraw()
    master.withdraw()
    project = Project(model_name, path)
    WorkWindow(master_of_master, project)



def browse(parent, path_tbox: tk.Entry):
    save_path = fd.askopenfilename(parent=parent)
    path_tbox.delete(0, tk.END)
    path_tbox.insert(0, save_path)
    pass