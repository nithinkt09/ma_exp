from types import SimpleNamespace

class DynamicObject(SimpleNamespace):
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)

    
