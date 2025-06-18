import tkinter as tk

class ClickableLabel(tk.Label):
    def __init__(self, parent, x, y, text, bg=None, fg=None, font=None, command=None):
        super().__init__(parent, text=text, bg=bg, fg=fg, font=font, cursor="hand2")
        self.place(x=x, y=y)
        self.default_color = bg if bg is not None else self.cget("bg")
        self.bind("<Button-1>", command)

    def set_onhover_color(self, hover_color):
        self.bind('<Enter>', lambda event: self.configure(bg=hover_color))
        self.bind('<Leave>', lambda event: self.configure(bg=self.default_color))
