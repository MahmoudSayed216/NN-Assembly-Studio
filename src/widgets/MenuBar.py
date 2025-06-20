import tkinter as tk



# class MenuBar(tk.Frame):
#     def __init__(self, master = None, cnf = None, *, background = None, bd = 0, bg = None, border = 0, borderwidth = 0, class_ = "Frame", colormap = "", container = False, cursor = "", height = 0, highlightbackground = None, highlightcolor = None, highlightthickness = 0, name = None, padx = 0, pady = 0, relief = "flat", takefocus = 0, visual = "", width = 0, x=0, y=0):
#         super().__init__(master, cnf, background=background, bd=bd, bg=bg, border=border, borderwidth=borderwidth, class_=class_, colormap=colormap, container=container, cursor=cursor, height=height, highlightbackground=highlightbackground, highlightcolor=highlightcolor, highlightthickness=highlightthickness, name=name, padx=padx, pady=pady, relief=relief, takefocus=takefocus, visual=visual, width=width)
#         self.place(x=x, y=y)
        


class MenuBar(tk.Menu):
    def __init__(self, master = None, cnf = None, *, activebackground = None, activeborderwidth = None, activeforeground = None, background = None, bd = None, bg = None, border = None, borderwidth = None, cursor = "arrow", disabledforeground = None, fg = None, font = None, foreground = None, name = None, postcommand = "", relief = None, selectcolor = None, takefocus = 0, tearoff = 1, tearoffcommand = "", title = "", type = "normal", x=0, y=0):
        super().__init__(master, cnf, activebackground=activebackground, activeborderwidth=activeborderwidth, activeforeground=activeforeground, background=background, bd=bd, bg=bg, border=border, borderwidth=borderwidth, cursor=cursor, disabledforeground=disabledforeground, fg=fg, font=font, foreground=foreground, name=name, postcommand=postcommand, relief=relief, selectcolor=selectcolor, takefocus=takefocus, tearoff=tearoff, tearoffcommand=tearoffcommand, title=title, type=type)
        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=master.quit)
        self.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(self, tearoff=0)
        edit_menu.add_command(label="Undo")
        edit_menu.add_command(label="Redo")
        self.add_cascade(label="Edit", menu=edit_menu)


        master.config(menu=self)



        # self.place(x=x, y=y)