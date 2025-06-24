import tkinter as tk
from resources.colors import *
from widgets.MainCanvas import MainCanvas
from widgets.ModulesBar import ModulesBar
from widgets.MenuBar import MenuBar

class WorkWindow:
    def __init__(self, master, project):
        
        self.project = project
        self.window = tk.Toplevel(master)
        self.window.title(f"{self.project.project_name}")
        self.window.geometry("1920x1080")
        
        #have to create it first since its dims are not some "customizable" thingy
        # self.create_menu_bar()
        self.menu_bar = MenuBar(self.window, bg=DARKGRAY)
        # self.window.update_idletasks()
        self.window.update_idletasks()
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
        self.modules_bar = ModulesBar(self.window, bg=WHITE, width=self.MODULE_BAR_WIDTH, height=self.MODULE_BAR_HEIGHT)

        self.window.protocol("WM_DELETE_WINDOW", lambda: master.destroy()) ##TODO: it should first check if something needs to get saved before closing

    # def create_menu_bar(self):
