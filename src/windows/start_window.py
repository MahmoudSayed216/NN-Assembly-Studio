import tkinter as tk
from resources.fonts import *
from resources.colors import *
from PIL import Image, ImageTk
from windows.create_project_window import CreateProjectWindow
from widgets.ClickableLabel import ClickableLabel

def print_hw(event):
    print("Hello world")

def create_project(root):
    CreateProjectWindow(root)

def load_project(event):
    pass

def create_module(event):
    pass

def goto_settings(event):
    print("iiii")
    pass

def exit_app(event):
    ##TODO ANY CHECKS BEFORE CLOSING ???????????????????????
    exit()


class StartWindow:


    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("NASM Main Menu")
        self.root.geometry("1920x1080")
        self.root.configure(bg=WHITE)
        self.HORIZONTAL_WALL = 140
        self.VERTICAL_WALL = 150
        self.VERTICAL_SEP = 70
        self.create_clickable_labels()

    def create_clickable_labels(self):
        create_proj = ClickableLabel(self.root, self.VERTICAL_WALL, self.HORIZONTAL_WALL, text="Create project", fg=SKYBLUE, font=A15BU, command=lambda event: create_project(self.root))
        create_proj.set_onhover_color(LIGHTYELLOW)

        load_proj = ClickableLabel(self.root, self.VERTICAL_WALL, self.HORIZONTAL_WALL + self.VERTICAL_SEP, text="Load project", fg=SKYBLUE, font=A15BU, command=load_project)
        load_proj.set_onhover_color(LIGHTYELLOW)

        create_mod = ClickableLabel(self.root, self.VERTICAL_WALL, self.HORIZONTAL_WALL + self.VERTICAL_SEP * 2, text="Create module", fg=SKYBLUE, font=A15BU, command=create_module)
        create_mod.set_onhover_color(LIGHTYELLOW)

        settings_ = ClickableLabel(self.root, self.VERTICAL_WALL, self.HORIZONTAL_WALL + self.VERTICAL_SEP * 3, text="Settings", fg=SKYBLUE, font=A15BU, command=goto_settings)
        settings_.set_onhover_color(LIGHTYELLOW)

        exit_ = ClickableLabel(self.root, self.VERTICAL_WALL, self.HORIZONTAL_WALL + self.VERTICAL_SEP * 4, text="Exit", fg=SKYBLUE, font=A15BU, command=exit_app)
        exit_.set_onhover_color(LIGHTYELLOW)

    def load_images(self):
        image = Image.open("/home/mahmoud-sayed/Desktop/Code/Python/NN Assembly Studio/src/resources/logo/Q.png")
        photo = ImageTk.PhotoImage(image)
        im_label = tk.Label(self.root, image=photo)
        im_label.image = photo
        im_label.place(x=1000, y=250)

    def mainloop(self):
        self.root.mainloop()