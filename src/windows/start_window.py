import tkinter as tk
from resources.fonts import *
from resources.colors import *
from PIL import Image, ImageTk
from widgets.ClickableLabel import ClickableLabel
from handlers import start_window_handlers





class StartWindow:


    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("NASM Main Menu")
        self.root.geometry("1920x1080")
        self.root.configure(bg=WHITE)
        self.HORIZONTAL_WALL = 140
        self.VERTICAL_WALL = 100
        self.VERTICAL_SEP = 70
        self.create_clickable_labels()
        self.load_images()

    def create_clickable_labels(self):
        create_proj = ClickableLabel(self.root, self.VERTICAL_WALL, self.HORIZONTAL_WALL, text="Create project", fg=SKYBLUE, font=A15BU, command=lambda event: start_window_handlers.create_project(self.root))
        create_proj.set_onhover_color(LIGHTYELLOW)

        load_proj = ClickableLabel(self.root, self.VERTICAL_WALL, self.HORIZONTAL_WALL + self.VERTICAL_SEP, text="Load project", fg=SKYBLUE, font=A15BU, command=lambda event: start_window_handlers.load_project())
        load_proj.set_onhover_color(LIGHTYELLOW)

        create_mod = ClickableLabel(self.root, self.VERTICAL_WALL, self.HORIZONTAL_WALL + self.VERTICAL_SEP * 2, text="Create module", fg=SKYBLUE, font=A15BU, command=lambda event: start_window_handlers.create_module())
        create_mod.set_onhover_color(LIGHTYELLOW)

        settings_ = ClickableLabel(self.root, self.VERTICAL_WALL, self.HORIZONTAL_WALL + self.VERTICAL_SEP * 3, text="Settings", fg=SKYBLUE, font=A15BU, command=lambda event: start_window_handlers.goto_settings())
        settings_.set_onhover_color(LIGHTYELLOW)

        exit_ = ClickableLabel(self.root, self.VERTICAL_WALL, self.HORIZONTAL_WALL + self.VERTICAL_SEP * 4, text="Exit", fg=SKYBLUE, font=A15BU, command=lambda event: start_window_handlers.exit_app())
        exit_.set_onhover_color(LIGHTYELLOW)

    def load_images(self):
        image = Image.open("/home/mahmoud-sayed/Desktop/Code/Python/NN Assembly Studio/src/resources/logo/Q.png")
        photo = ImageTk.PhotoImage(image)
        im_label = tk.Label(self.root, image=photo)
        im_label.image = photo
        im_label.place(x=1000, y=250)

    def mainloop(self):
        self.root.mainloop()