import uuid
class Element:

    def __init__(self, name):
        self.name = name # name of the entity
        self.uid = uuid.uuid4()
        self.properties = {}
        self.element_type = None
        self.sources_hom_set = {}
        self.target_hom_set = {}
        self.morphisms = {}

    