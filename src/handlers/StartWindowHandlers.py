from windows.CreateProjectWindow import CreateProjectWindow
from ServiceLocator import ServiceLocator
def create_project(root):
    ServiceLocator.get('wman').get_window_instance('CreateProjectWindow', root)

def load_project():
    print("hello from load project")
    pass

def create_module():
    print("hello from create module")
    pass

def goto_settings():
    print("hello from goto settings")
    pass

def exit_app():
    ##TODO ANY CHECKS BEFORE CLOSING ???????????????????????
    exit()

