import tkinter as tk
from models.ModuleData import ModuleData


class CanvasHandler:
    IDS = []
    @classmethod
    def set_canvas(cls, canvas: tk.Canvas):
        cls.canvas = canvas
        
    @classmethod
    def place_elem_on_canvas(cls, module_data: ModuleData):
        print("Created")
        cls.canvas.create_rectangle(60, 60, 120, 120, fill=module_data.fill_color, outline=module_data.outline_color, tags=module_data.tag, width=3)
        cls.canvas.create_text(60, 60, text=module_data.module_name, fill='#000000', tags=module_data.tag, angle=90, font=('Arial', 12, 'bold'))
        ## CALCULATE TEXT POSITION RELATIVE TO THE SHAPE