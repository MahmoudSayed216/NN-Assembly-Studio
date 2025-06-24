from windows.StartWindow import StartWindow
from Services.ResourcesManager import ResourcesManager
from Services.SettingsManager import SettingsManager
from ServiceLocator import ServiceLocator


class NNAssemblyStudio:
    def __init__(self):
        self.start_window = StartWindow()
        resources_man = ResourcesManager()
        settings_man = SettingsManager()
        ServiceLocator.register('rman', resources_man)
        ServiceLocator.register('sman', settings_man)    

    def run(self):
        self.start_window.mainloop()