import tkinter as tk
from resources.colors import *
from widgets.MainCanvas import MainCanvas
# from widgets.MenuBar import MenuBar
from widgets.ModulesBar import ModulesBar

class WorkWindow:
    def __init__(self, master, project):
        
        self.project = project
        self.window = tk.Toplevel(master)
        self.window.title(f"{self.project.project_name}")
        self.window.geometry("1920x1080")
        
        #have to create it first since its dims are not some "customizable" thingy
        self.create_menu_bar()

        self.MENUBAR_WIDTH = self.menu_bar.winfo_width()
        self.MENUBAR_HEIGHT = self.menu_bar.winfo_height()
        self.MENUBAR_x = 0
        self.MENUBAR_y = 0
        self.MODULE_BAR_WIDTH = 250
        self.MODULE_BAR_HEIGHT = 1080
        self.MODULE_BAR_X = 0
        self.MODULE_BAR_Y = self.MENUBAR_HEIGHT
        self.MAIN_CANVAS_X = self.MODULE_BAR_X+self.MODULE_BAR_WIDTH
        self.MAIN_CANVAS_Y = self.MENUBAR_HEIGHT
        self.MAIN_CANVAS_WIDTH = 1920 - self.MODULE_BAR_WIDTH
        self.MAIN_CANVAS_HEIGHT = 1080

        #main work window components
        self.main_canvas = MainCanvas(self.window, width=self.MAIN_CANVAS_WIDTH, height=self.MAIN_CANVAS_HEIGHT, x=self.MAIN_CANVAS_X, y=self.MAIN_CANVAS_Y, bg=WHITE)
        self.modules_bar = ModulesBar(self.window, bg=LIGHTGRAY, width=self.MODULE_BAR_WIDTH, height=self.MODULE_BAR_HEIGHT, x=self.MODULE_BAR_X,y=self.MODULE_BAR_Y)

        self.window.protocol("WM_DELETE_WINDOW", lambda: master.destroy())

    def create_menu_bar(self):
        self.menu_bar = tk.Menu(self.window, bg=DARKGRAY)

        LJUST = 50

        file_menu = tk.Menu(self.window, tearoff=0, )
        file_menu.add_command(label="  New".ljust(LJUST))
        file_menu.add_command(label="  Open".ljust(LJUST))
        file_menu.add_command(label="  Save".ljust(LJUST))
        file_menu.add_separator()
        file_menu.add_command(label="  Exit".ljust(LJUST), command=self.window.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        
        edit_menu = tk.Menu(self.window, tearoff=0)
        edit_menu.add_command(label="  Undo".ljust(LJUST))
        edit_menu.add_command(label="  Redo".ljust(LJUST))
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)

        self.window.config(menu=self.menu_bar)