import tkinter as tk
from resources.colors import *
from PIL import Image ,ImageTk


class ModuleContainer:
    def __init__(self, master, bg, width, height, module_data):
        self.frame = tk.Frame(master, width=width, height=height, bg=bg)
        self.frame.pack(pady=10)
        self.module_data = module_data
        img = Image.open(module_data.img_path)
        img = img.resize(size=(128, 128))
        photo = ImageTk.PhotoImage(img)

        img_container = tk.Label(self.frame, image=photo)
        img_container.image = photo
        img_container.pack()

        self.frame.pack(pady=15)

        self.label = tk.Label(self.frame, text=module_data.module_name, bg=WHITE).pack()