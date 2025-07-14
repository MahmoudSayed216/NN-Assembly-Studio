from windows.StartWindow import StartWindow
from Services.ResourcesManager import ResourcesManager
from Services.SettingsManager import SettingsManager
from Services.WindowsManager import WindowsManager
from ServiceLocator import ServiceLocator


class NNAssemblyStudio:
    def __init__(self):
        
        windows_man = WindowsManager()
        resources_man = ResourcesManager()
        settings_man = SettingsManager()
        ServiceLocator.register('wman', windows_man)
        ServiceLocator.register('rman', resources_man)
        ServiceLocator.register('sman', settings_man)    

        self.start_window = ServiceLocator.get('wman').get_window_instance('StartWindow')


    def run(self):
        self.start_window.mainloop()