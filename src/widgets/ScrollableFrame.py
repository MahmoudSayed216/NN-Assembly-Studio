import tkinter as tk
import customtkinter
from models.ModuleData import ModuleData
from widgets.ModuleContainer import ModuleContainer
from resources.colors import *


class ScrollableFrame:

	def __init__(self, master, items, width, height):
		self.items = items

		self.scrollable_frame = customtkinter.CTkScrollableFrame(master, corner_radius=0, width=width, height=height)
		self.scrollable_frame.place(relx=0.5, rely=0, anchor='n')
		self.scrollable_frame.bind("<Button-4>", self._on_mouse_wheel)
		self.scrollable_frame.bind("<Button-5>", self._on_mouse_wheel)
		
		mod1 = ModuleData("Conv2D", "/home/mahmoud-sayed/Desktop/Code/Python/NN Assembly Studio/src/resources/modules_images/cnn.png")
		mod2 = ModuleData("MLP", "/home/mahmoud-sayed/Desktop/Code/Python/NN Assembly Studio/src/resources/modules_images/mlp.jpg")


		for i in range(10):
			ModuleContainer(self.scrollable_frame, bg=WHITE, width=130, height=130, module_data=mod1)
			ModuleContainer(self.scrollable_frame, bg=WHITE, width=130, height=130, module_data=mod2)
	def _on_mouse_wheel(self, event):
			direction = -1 if event.num == 4 else 1
			self.scrollable_frame._parent_canvas.yview_scroll(direction, "units")
