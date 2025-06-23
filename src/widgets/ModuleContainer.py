import tkinter as tk
from resources.colors import *
from PIL import Image ,ImageTk


class ModuleContainer:
    def __init__(self, master, bg, width, height, module_data):
        self.frame = tk.Frame(master, width=width, height=height, bg=bg, cursor="hand2")
        self.frame.pack(pady=10)
        self.module_data = module_data
        img = Image.open(module_data.img_path)
        img = img.resize(size=(160, 160))
        photo = ImageTk.PhotoImage(img)

        img_container = tk.Label(self.frame, image=photo)
        img_container.image = photo
        img_container.pack()

        self.frame.pack(pady=15)

        self.label = tk.Label(self.frame, text=module_data.module_name, bg=WHITE).pack()

    def show(self, pack_info):
        self.frame.pack(pack_info)

    def hide(self):
        self.frame.pack_forget()
