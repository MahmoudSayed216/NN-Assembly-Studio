class ModuleData:
    ##TODO: refactor to get the path of the module, dpgk the module, and populate the object attributes
    ##TODO: SOME TAG SHOULD BE AUTO_GENERATED TO KEEP THE RECT AND TEXT TOGETHER DESPITE THE NUMBER OF ELEMENTS
    def __init__(self, module_name, img_path, tag, blue_print=None, builtin=True, fill_color = (255, 255, 255), outline_color = (0, 0, 0)):
        self.module_name = module_name
        self.img_path = img_path
        self.mod_blueprint = blue_print
        self.builtin = builtin
        self.fill_color = fill_color
        self.outline_color = outline_color
        self.tag = tag
        self.shape = 'r'


    def convert_bb_to_pt_code(self):
        pass

    def __str__(self):
        string = f"module name: {self.module_name}\nimage path{self.img_path}\nbuilt in: {self.builtin}"
        return string
    
    def __repr__(self):
        start = "\n\n______start of ModuleData Object______"
        string = f"\nmodule name: {self.module_name}\nimage path: {self.img_path}\nbuilt in: {self.builtin}"
        end= "\n______end of ModuleData Object______\n\n"

        return start + string + end  