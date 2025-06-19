import tkinter as tk


class WorkWindow:
    def __init__(self, master, project):
        self.project = project
        self.window = tk.Toplevel(master)
        self.window.title(f"{self.project.project_name}")
        self.window.geometry("1920x1080")
        self.canvas = tk.Canvas(self.window)

    