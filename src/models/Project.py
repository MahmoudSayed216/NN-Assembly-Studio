from datetime import datetime
from models.CanvasData import CanvasData


class Project:
    def __init__(self, project_name, path):
        self.project_name = project_name
        self.path = path
        self.creation_date = datetime.now()
        self.saved_after_changes = False
        self.project_canvas = CanvasData()
    def save(self):
        if not self.saved_after_changes:
            # some saving logic stuff
            self.saved_after_changes = True
            pass

    def __str__(self):
        obj_desc = f"Project Object:\n  Model Name:   {self.project_name}\n  Path:         {self.path}\n  Datetime:     {self.creation_date}"
        return obj_desc 