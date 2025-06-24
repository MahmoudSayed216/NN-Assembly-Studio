class ServiceLocator:
    _services = {}

    @classmethod
    def register(cls, name, service):
        cls._services[name] = service

    @classmethod
    def get(cls, name):
        if name not in cls._services:
            raise ValueError(f"\"{name}\" is not a service")
        return cls._services[name]