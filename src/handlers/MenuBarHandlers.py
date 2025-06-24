from ServiceLocator import ServiceLocator


def save_modules():
    ServiceLocator.get('rman').save_all_modules()