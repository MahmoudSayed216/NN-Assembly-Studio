from ServiceLocator import ServiceLocator

def get_all_built_in_modules():
    return ServiceLocator.get("rman").get_builtin_modules()