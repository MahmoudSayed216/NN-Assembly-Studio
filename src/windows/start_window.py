import tkinter as tk
from resources.fonts import *
from resources.colors import *
from PIL import Image, ImageTk
from windows.create_project_window import CreateProjectWindow

def print_hw(event):
    print("Hello world")

def create_project(event):
    CreateProjectWindow(root)

def load_project(event):
    pass

def create_module(event):
    pass

def exit_app(event):
    ##TODO ANY CHECKS BEFORE CLOSING ???????????????????????
    exit()


root = tk.Tk()
root.title("NASM Main Menu")
root.geometry("1920x1080")
root.configure(bg=WHITE)


HORIZONTAL_WALL = 140
VERTICAL_WALL = 150
VERTICAL_SEP = 70

create_proj = tk.Label(root, text="Create project", fg=SKYBLUE, cursor="hand2", font=A15BU)
create_proj.place(x=VERTICAL_WALL, y=HORIZONTAL_WALL)
create_proj.bind("<Button-1>", create_project)


load_proj = tk.Label(root, text="Load project", fg=SKYBLUE, cursor="hand2", font=A15BU)
load_proj.place(x=VERTICAL_WALL, y=HORIZONTAL_WALL+VERTICAL_SEP)
load_proj.bind("<Button-1>", load_project)


create_mod = tk.Label(root, text="Create module", fg=SKYBLUE, cursor="hand2", font=A15BU)
create_mod.place(x=VERTICAL_WALL, y= HORIZONTAL_WALL+VERTICAL_SEP*2)
create_mod.bind("<Button-1>", create_module)


exit_ = tk.Label(root, text="Exit", fg=SKYBLUE, cursor="hand2", font=A15BU)
exit_.place(x=VERTICAL_WALL, y= HORIZONTAL_WALL+VERTICAL_SEP*3)
exit_.bind("<Button-1>", exit_app)

image = Image.open("/home/mahmoud-sayed/Desktop/Code/Python/NN Assembly Studio/src/resources/logo/Q.png")
photo = ImageTk.PhotoImage(image)
im_label = tk.Label(root, image=photo)
im_label.image = photo
im_label.place(x=1000, y=250)