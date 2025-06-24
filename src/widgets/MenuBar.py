import tkinter as tk
from handlers.MenuBarHandlers import *
from resources.colors import *




class MenuBar(tk.Menu):
    def __init__(self, master = None, cnf = None, *, activebackground = None, activeborderwidth = None, activeforeground = None, background = None, bd = None, bg = None, border = None, borderwidth = None, cursor = "arrow", disabledforeground = None, fg = None, font = None, foreground = None, name = None, postcommand = "", relief = None, selectcolor = None, takefocus = 0, tearoff = 1, tearoffcommand = "", title = "", type = "normal"):
        super().__init__(master, cnf, activebackground=activebackground, activeborderwidth=activeborderwidth, activeforeground=activeforeground, background=background, bd=bd, bg=bg, border=border, borderwidth=borderwidth, cursor=cursor, disabledforeground=disabledforeground, fg=fg, font=font, foreground=foreground, name=name, postcommand=postcommand, relief=relief, selectcolor=selectcolor, takefocus=takefocus, tearoff=tearoff, tearoffcommand=tearoffcommand, title=title, type=type)
        
        
        LJUST = 50
        file_menu = tk.Menu(master, tearoff=0)
        file_menu.add_command(label="  New".ljust(LJUST))
        file_menu.add_command(label="  Open".ljust(LJUST))
        file_menu.add_command(label="  Save".ljust(LJUST), command=save_modules) ## TODO: this should not be here, it saved modules, but this menu item is supposed to save a project
        file_menu.add_separator()
        file_menu.add_command(label="  Exit".ljust(LJUST), command=master.quit)
        self.add_cascade(label="File", menu=file_menu)
        
        edit_menu = tk.Menu(master, tearoff=0)
        edit_menu.add_command(label="  Undo".ljust(LJUST))
        edit_menu.add_command(label="  Redo".ljust(LJUST))
        self.add_cascade(label="Edit", menu=edit_menu)

        master.config(menu=self)
    # def __init__(self, master):
    #     self.menu_bar = tk.Menu(master, bg=DARKGRAY)

   