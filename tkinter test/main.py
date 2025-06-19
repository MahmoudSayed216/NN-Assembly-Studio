import tkinter as tk

class ZoomDragCanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Zoom and drag parameters
        self.scale_factor = 1.0
        self.min_scale = 0.2
        self.max_scale = 5.0
        self.offset_x = 0
        self.offset_y = 0
        self._drag_data = {"x": 0, "y": 0}
        self._selected_item = None

        # Bindings
        self.bind("<ButtonPress-1>", self.select_item_or_start_drag)
        self.bind("<B1-Motion>", self.drag_selected_or_canvas)
        self.bind("<MouseWheel>", self.zoom_windows)
        self.bind("<Button-4>", self.zoom_linux)
        self.bind("<Button-5>", self.zoom_linux)
        self.bind("<Button-2>", self.reset_view)

        self.populate_canvas()

    def populate_canvas(self):
        """Add some demo content to the canvas with draggable items."""
        for i in range(5):
            x0 = 100 + i * 120
            y0 = 100 + i * 60
            x1 = x0 + 100
            y1 = y0 + 50
            group_id = f"group_{i}"

            self.create_rectangle(x0, y0, x1, y1, fill="lightblue", outline="black", width=2,
                                  tags=("movable", group_id))
            self.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=f"Box {i+1}", font=("Arial", 12, "bold"),
                             tags=("movable", group_id))
            
    def add_box(self):
        x0, y0 = 300, 300
        x1, y1 = x0 + 100, y0 + 50
        group_id = f"group_{self.find_all().__len__()}"
        self.create_rectangle(x0, y0, x1, y1, fill="orange", tags=("movable", group_id))
        self.create_text((x0 + x1) / 2, (y0 + y1) / 2, text="New Box", tags=("movable", group_id))

    def select_item_or_start_drag(self, event):
        items = self.find_withtag("current")
        if items:
            self._selected_item = items[0]
            tags = self.gettags(self._selected_item)
            if "movable" in tags:
                self._drag_data["x"] = event.x
                self._drag_data["y"] = event.y
            else:
                self._selected_item = None
                self.start_drag(event)
        else:
            self._selected_item = None
            self.start_drag(event)

    def drag_selected_or_canvas(self, event):
        if self._selected_item:
            dx = event.x - self._drag_data["x"]
            dy = event.y - self._drag_data["y"]
            tags = self.gettags(self._selected_item)
            for tag in tags:
                if tag.startswith("group_"):
                    self.move(tag, dx, dy)
            self._drag_data["x"] = event.x
            self._drag_data["y"] = event.y
        else:
            self.do_drag(event)

    def start_drag(self, event):
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def do_drag(self, event):
        dx = event.x - self._drag_data["x"]
        dy = event.y - self._drag_data["y"]
        self.move("all", dx, dy)
        self.offset_x += dx
        self.offset_y += dy
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def zoom_windows(self, event):
        factor = 1.1 if event.delta > 0 else 0.9
        self.apply_zoom(factor, event.x, event.y)

    def zoom_linux(self, event):
        factor = 1.1 if event.num == 4 else 0.9
        self.apply_zoom(factor, event.x, event.y)

    def apply_zoom(self, factor, x, y):
        new_scale = self.scale_factor * factor
        if self.min_scale <= new_scale <= self.max_scale:
            self.scale("all", x, y, factor, factor)
            self.scale_factor = new_scale
            self.offset_x = (self.offset_x - x) * factor + x
            self.offset_y = (self.offset_y - y) * factor + y

    def reset_view(self, event=None):
        self.scale_factor = 1.0
        self.offset_x = 0
        self.offset_y = 0
        self.delete("all")
        self.populate_canvas()


# Main App Window
root = tk.Tk()
root.title("Draggable Zoom Canvas with Sidebar")
root.geometry("1200x700")

# Sidebar
sidebar = tk.Frame(root, width=200, bg="#f0f0f0")
sidebar.pack(side="left", fill="y")

tk.Label(sidebar, text="Sidebar", bg="#f0f0f0", font=("Arial", 14, "bold")).pack(pady=10)
tk.Button(sidebar, text="Reset Canvas", command=lambda: canvas.reset_view()).pack(pady=5)
tk.Button(sidebar, text="Add Box", command=lambda: canvas.add_box()).pack(pady=5)

# Canvas Area
canvas = ZoomDragCanvas(root, bg="white")
canvas.pack(side="right", fill="both", expand=True)

root.mainloop()
