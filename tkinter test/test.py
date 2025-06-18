import tkinter as tk
from tkinter import ttk
import math

class AdvancedCanvas:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Draggable & Zoomable Canvas")
        self.root.geometry("1200x800")
        
        # Canvas state
        self.zoom_factor = 1.0
        self.pan_start_x = 0
        self.pan_start_y = 0
        self.canvas_offset_x = 0
        self.canvas_offset_y = 0
        self.is_panning = False
        
        # Object manipulation
        self.selected_object = None
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.is_dragging_object = False
        
        # Object storage
        self.canvas_objects = []
        self.object_counter = 0
        
        self.setup_ui()
        self.bind_events()
        self.create_sample_objects()
    
    def setup_ui(self):
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Sidebar
        self.sidebar = ttk.Frame(main_frame, width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        self.sidebar.pack_propagate(False)
        
        # Sidebar content
        ttk.Label(self.sidebar, text="Canvas Controls", font=("Arial", 12, "bold")).pack(pady=10)
        
        # Zoom controls
        zoom_frame = ttk.LabelFrame(self.sidebar, text="Zoom", padding=10)
        zoom_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(zoom_frame, text="Zoom In", command=self.zoom_in).pack(fill=tk.X, pady=2)
        ttk.Button(zoom_frame, text="Zoom Out", command=self.zoom_out).pack(fill=tk.X, pady=2)
        ttk.Button(zoom_frame, text="Reset Zoom", command=self.reset_zoom).pack(fill=tk.X, pady=2)
        
        self.zoom_label = ttk.Label(zoom_frame, text=f"Zoom: {self.zoom_factor:.1f}x")
        self.zoom_label.pack(pady=5)
        
        # Object controls
        object_frame = ttk.LabelFrame(self.sidebar, text="Add Objects", padding=10)
        object_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(object_frame, text="Add Circle", command=self.add_circle).pack(fill=tk.X, pady=2)
        ttk.Button(object_frame, text="Add Rectangle", command=self.add_rectangle).pack(fill=tk.X, pady=2)
        ttk.Button(object_frame, text="Add Triangle", command=self.add_triangle).pack(fill=tk.X, pady=2)
        ttk.Button(object_frame, text="Add Star", command=self.add_star).pack(fill=tk.X, pady=2)
        ttk.Button(object_frame, text="Add Diamond", command=self.add_diamond).pack(fill=tk.X, pady=2)
        
        # Object info
        info_frame = ttk.LabelFrame(self.sidebar, text="Selected Object", padding=10)
        info_frame.pack(fill=tk.X, pady=5)
        
        self.info_label = ttk.Label(info_frame, text="No selection", wraplength=180)
        self.info_label.pack()
        
        ttk.Button(info_frame, text="Delete Selected", command=self.delete_selected).pack(fill=tk.X, pady=5)
        
        # Instructions
        inst_frame = ttk.LabelFrame(self.sidebar, text="Instructions", padding=10)
        inst_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        instructions = """
• Right-click + drag to pan
• Mouse wheel to zoom
• Left-click objects to select
• Drag selected objects to move
• Use buttons to add shapes
        """
        ttk.Label(inst_frame, text=instructions, justify=tk.LEFT, wraplength=180).pack()
        
        # Canvas container
        canvas_frame = ttk.Frame(main_frame)
        canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Canvas with scrollbars
        self.canvas = tk.Canvas(canvas_frame, bg='white', highlightthickness=1, highlightbackground='gray')
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        h_scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        
        self.canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack scrollbars and canvas
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Set scroll region
        self.canvas.configure(scrollregion=(-2000, -2000, 2000, 2000))
    
    def bind_events(self):
        # Mouse events
        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.canvas.bind("<B3-Motion>", self.on_pan_drag)
        self.canvas.bind("<ButtonRelease-3>", self.on_pan_release)
        self.canvas.bind("<B1-Motion>", self.on_left_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_left_release)
        
        # Mouse wheel for zooming
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        self.canvas.bind("<Button-4>", self.on_mousewheel)
        self.canvas.bind("<Button-5>", self.on_mousewheel)
        
        # Keyboard events
        self.canvas.bind("<Key>", self.on_key_press)
        self.canvas.focus_set()
    
    def on_left_click(self, event):
        # Convert screen coordinates to canvas coordinates
        canvas_x = self.canvas.canvasx(event.x)
        canvas_y = self.canvas.canvasy(event.y)
        
        # Find clicked object
        clicked_item = self.canvas.find_closest(canvas_x, canvas_y)[0]
        
        # Check if clicked item is one of our objects
        clicked_object = None
        for obj in self.canvas_objects:
            if clicked_item in obj['items']:
                clicked_object = obj
                break
        
        if clicked_object:
            self.select_object(clicked_object)
            self.drag_start_x = canvas_x
            self.drag_start_y = canvas_y
            self.is_dragging_object = True
        else:
            self.deselect_object()
    
    def on_left_drag(self, event):
        if self.is_dragging_object and self.selected_object:
            canvas_x = self.canvas.canvasx(event.x)
            canvas_y = self.canvas.canvasy(event.y)
            
            dx = canvas_x - self.drag_start_x
            dy = canvas_y - self.drag_start_y
            
            # Move all items of the selected object
            for item in self.selected_object['items']:
                self.canvas.move(item, dx, dy)
            
            # Update object position
            self.selected_object['x'] += dx
            self.selected_object['y'] += dy
            
            self.drag_start_x = canvas_x
            self.drag_start_y = canvas_y
            
            self.update_object_info()
    
    def on_left_release(self, event):
        self.is_dragging_object = False
    
    def on_right_click(self, event):
        self.pan_start_x = event.x
        self.pan_start_y = event.y
        self.is_panning = True
    
    def on_pan_drag(self, event):
        if self.is_panning:
            dx = event.x - self.pan_start_x
            dy = event.y - self.pan_start_y
            
            self.canvas.scan_dragto(dx, dy, gain=1)
            
            self.pan_start_x = event.x
            self.pan_start_y = event.y
    
    def on_pan_release(self, event):
        self.is_panning = False
    
    def on_mousewheel(self, event):
        # Get mouse position
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        
        # Determine zoom direction
        if event.delta > 0 or event.num == 4:
            factor = 1.1
        else:
            factor = 0.9
        
        self.zoom_at_point(x, y, factor)
    
    def zoom_at_point(self, x, y, factor):
        self.zoom_factor *= factor
        self.canvas.scale("all", x, y, factor, factor)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.zoom_label.config(text=f"Zoom: {self.zoom_factor:.1f}x")
    
    def zoom_in(self):
        center_x = self.canvas.winfo_width() / 2
        center_y = self.canvas.winfo_height() / 2
        canvas_x = self.canvas.canvasx(center_x)
        canvas_y = self.canvas.canvasy(center_y)
        self.zoom_at_point(canvas_x, canvas_y, 1.2)
    
    def zoom_out(self):
        center_x = self.canvas.winfo_width() / 2
        center_y = self.canvas.winfo_height() / 2
        canvas_x = self.canvas.canvasx(center_x)
        canvas_y = self.canvas.canvasy(center_y)
        self.zoom_at_point(canvas_x, canvas_y, 0.8)
    
    def reset_zoom(self):
        # Reset zoom and pan
        self.canvas.delete("all")
        self.zoom_factor = 1.0
        self.canvas_offset_x = 0
        self.canvas_offset_y = 0
        
        # Recreate all objects
        for obj in self.canvas_objects:
            self.create_object_items(obj)
        
        self.canvas.configure(scrollregion=(-2000, -2000, 2000, 2000))
        self.zoom_label.config(text=f"Zoom: {self.zoom_factor:.1f}x")
        self.deselect_object()
    
    def select_object(self, obj):
        # Deselect previous
        self.deselect_object()
        
        # Select new object
        self.selected_object = obj
        
        # Highlight selected object
        for item in obj['items']:
            self.canvas.itemconfig(item, width=3)
        
        self.update_object_info()
    
    def deselect_object(self):
        if self.selected_object:
            # Remove highlight
            for item in self.selected_object['items']:
                self.canvas.itemconfig(item, width=1)
        
        self.selected_object = None
        self.info_label.config(text="No selection")
    
    def update_object_info(self):
        if self.selected_object:
            obj = self.selected_object
            info_text = f"Type: {obj['type']}\nID: {obj['id']}\nPosition: ({obj['x']:.0f}, {obj['y']:.0f})\nColor: {obj['color']}"
            self.info_label.config(text=info_text)
    
    def delete_selected(self):
        if self.selected_object:
            # Delete canvas items
            for item in self.selected_object['items']:
                self.canvas.delete(item)
            
            # Remove from objects list
            self.canvas_objects.remove(self.selected_object)
            self.selected_object = None
            self.info_label.config(text="No selection")
    
    def create_object_items(self, obj):
        """Create the actual canvas items for an object"""
        obj['items'] = []
        
        if obj['type'] == 'circle':
            item = self.canvas.create_oval(
                obj['x'] - obj['size'], obj['y'] - obj['size'],
                obj['x'] + obj['size'], obj['y'] + obj['size'],
                fill=obj['color'], outline='black', width=1
            )
            obj['items'].append(item)
        
        elif obj['type'] == 'rectangle':
            item = self.canvas.create_rectangle(
                obj['x'] - obj['size'], obj['y'] - obj['size'],
                obj['x'] + obj['size'], obj['y'] + obj['size'],
                fill=obj['color'], outline='black', width=1
            )
            obj['items'].append(item)
        
        elif obj['type'] == 'triangle':
            points = [
                obj['x'], obj['y'] - obj['size'],  # top
                obj['x'] - obj['size'], obj['y'] + obj['size'],  # bottom left
                obj['x'] + obj['size'], obj['y'] + obj['size']   # bottom right
            ]
            item = self.canvas.create_polygon(points, fill=obj['color'], outline='black', width=1)
            obj['items'].append(item)
        
        elif obj['type'] == 'star':
            points = self.create_star_points(obj['x'], obj['y'], obj['size'])
            item = self.canvas.create_polygon(points, fill=obj['color'], outline='black', width=1)
            obj['items'].append(item)
        
        elif obj['type'] == 'diamond':
            points = [
                obj['x'], obj['y'] - obj['size'],  # top
                obj['x'] + obj['size'], obj['y'],  # right
                obj['x'], obj['y'] + obj['size'],  # bottom
                obj['x'] - obj['size'], obj['y']   # left
            ]
            item = self.canvas.create_polygon(points, fill=obj['color'], outline='black', width=1)
            obj['items'].append(item)
    
    def create_star_points(self, cx, cy, size):
        """Create points for a 5-pointed star"""
        points = []
        for i in range(10):
            angle = i * math.pi / 5
            if i % 2 == 0:
                # Outer point
                radius = size
            else:
                # Inner point
                radius = size * 0.4
            
            x = cx + radius * math.cos(angle - math.pi / 2)
            y = cy + radius * math.sin(angle - math.pi / 2)
            points.extend([x, y])
        
        return points
    
    def add_object(self, obj_type):
        colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan']
        
        self.object_counter += 1
        obj = {
            'id': self.object_counter,
            'type': obj_type,
            'x': 100 + (self.object_counter * 50) % 400,
            'y': 100 + (self.object_counter * 50) % 300,
            'size': 30,
            'color': colors[self.object_counter % len(colors)],
            'items': []
        }
        
        self.create_object_items(obj)
        self.canvas_objects.append(obj)
        return obj
    
    def add_circle(self):
        self.add_object('circle')
    
    def add_rectangle(self):
        self.add_object('rectangle')
    
    def add_triangle(self):
        self.add_object('triangle')
    
    def add_star(self):
        self.add_object('star')
    
    def add_diamond(self):
        self.add_object('diamond')
    
    def create_sample_objects(self):
        """Create some sample objects to demonstrate functionality"""
        # Add a few sample objects
        self.add_circle()
        self.add_rectangle()
        self.add_triangle()
        self.add_star()
        self.add_diamond()
    
    def on_key_press(self, event):
        if event.keysym == 'Delete' and self.selected_object:
            self.delete_selected()

def main():
    root = tk.Tk()
    app = AdvancedCanvas(root)
    root.mainloop()

if __name__ == "__main__":
    main()