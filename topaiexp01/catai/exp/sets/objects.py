class Object:

    def __init__(self, name):
        self.name = name
        self._object_type = None


    @property
    def object_type(self, object_type):
        self._object_type = object_type

        