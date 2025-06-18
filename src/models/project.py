from datetime import datetime

class Project:
    def __init__(self, project_name, path):
        self.project_name = project_name
        self.create_date = datetime.now()
        self.path = path