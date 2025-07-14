import tkinter as tk
from models.ModuleData import ModuleData

## CHANGE THIS TO "MODULE IMPORTER OR OBJECT CREATOR" AND THE ACTUAL MOVING AND ZOOMING TAKES PLACE IN THE ORIGINAL CANVAS CLASS
class CanvasHandler:
    # IDS = []
    selected = None
    x0, y0, x1, y1 = 0, 0, 100, 100
    @classmethod
    def set_canvas(cls, canvas: tk.Canvas):
        cls.canvas = canvas
        
    @classmethod
    def place_elem_on_canvas(cls, module_data: ModuleData):
        
        print("Created")

        cls.canvas.create_rectangle(cls.x0, cls.y0, cls.x1, cls.y1, fill=module_data.fill_color, outline=module_data.outline_color, tags=module_data.tag, width=3)
        cls.canvas.create_text(cls.x0, cls.y0, text=module_data.module_name, fill='#000000', tags=module_data.tag, angle=90, font=('Arial', 12, 'bold'))
        cls.x0+=10
        cls.y0+=10
        cls.x1+=10
        cls.y1+=10
        ## CALCULATE TEXT POSITION RELATIVE TO THE SHAPE
    
    

## TODO: ADD SOMETHING [LIKE A LOWER THIN BAR] THAT SHOWS THE CURRENT POSITION OF THE MOUSE, AND ANOTHER THING THAT SHOWS INFO LIKE POSITION AND SIZE OF THE CURRENTLY SELECTED ELEMENT