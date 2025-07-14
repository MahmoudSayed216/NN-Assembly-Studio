from configs import *  ##TODO: BASE_MODULES_PATH  SHOULD BE STORED IN SETTINGS.txt NOT IN CONFIGS
import os
from models.ModuleData import ModuleData

class ResourcesManager:
    # project = None
    def set_curr_project(self, project):
        self.project = project
    def __init__(self):
        # self.modules = {'Conv2D': ModuleData("Conv2D", "/home/mahmoud-sayed/Desktop/Code/Python/NN Assembly Studio/src/resources/modules_images/Conv2D.png"),
        #                 'MaxPool2D':ModuleData("MaxPooling2D", "/home/mahmoud-sayed/Desktop/Code/Python/NN Assembly Studio/src/resources/modules_images/MaxPooling2D.png"),
        #                 'MLP': ModuleData("Linear", "/home/mahmoud-sayed/Desktop/Code/Python/NN Assembly Studio/src/resources/modules_images/noname.png")}
        self.modules = {}
        self.load_modules_on_start()
    
    def _load_module(self, module_full_path):
        with open(module_full_path) as file:
            module_name = file.readline().split(':')[1].strip('\n')
            image_path = file.readline().split(':')[1].strip('\n')
            built_in = bool(file.readline().split(':')[1].strip('\n'))

            module = ModuleData(module_name, image_path, None, built_in)

        return module
    
    def load_modules_on_start(self):
        all_mods = os.listdir(BASE_MODULES_PATH)
        print(all_mods)
        for mod in all_mods:
            full_path = os.path.join(BASE_MODULES_PATH, mod)
            mod = self._load_module(full_path)
            self.modules[mod.module_name] = mod
        print(self.modules)

    def load_project(self, project_full_path):
        ## TODO: THIS INCLUDES LOADING THE PROJECT ITSELF, AND LOADING ALL RELEVANT MODULES IF NOT ALREADY LOADED
        pass

    def _save_module(self, module, save_path):    
        with open(save_path, "w") as file:
            file.write(f"MN:{module.module_name}\n")
            file.write(f"IP:{module.img_path}\n")
            file.write(f"BI:{module.builtin}\n")
            #TODO: WRITE THE BLUEPRINT WHEN YOU IMPLEMENT IT
            #TODO: file names can start with either B or N [e.g.] to tell wether it's built in or not, and if not, then we don't need to load it on start?? 

    def save_all_modules(self):
        for key in self.modules.keys():
            full_path = os.path.join(BASE_MODULES_PATH, key+'.nasm')
            print(full_path)
            self._save_module(self.modules[key], full_path)

    def get_builtin_modules(self):
        return [self.modules[key] for key in self.modules.keys()]