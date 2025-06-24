class ModuleData:
    ##TODO: refactor to get the path of the module, dpgk the module, and populate the object attributes
    def __init__(self, module_name, img_path, blue_print=None, builtin=True):
        self.module_name = module_name
        self.img_path = img_path
        self.mod_blueprint = blue_print
        self.builtin = builtin


    def convert_bb_to_pt_code(self):
        pass

    def __str__(self):
        string = f"module name: {self.module_name}\nimage path{self.img_path}\nbuilt in: {self.builtin}"
        return string
    
    def __repr__(self):
        start = "\n\n______ start of ModuleData Object __repr__ ______"
        string = f"\nmodule name: {self.module_name}\nimage path: {self.img_path}\nbuilt in: {self.builtin}"
        end= "\n______ end of ModuleData Object __repr__ ______\n\n"

        return start + string + end  