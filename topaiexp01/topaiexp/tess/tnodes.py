"""
node (vertices): discrete fundamental unit or building block representing an entity or idea
nodes connected by edges describe relationships or interactions between them 
each node can be conceptualized as a self-contained object that holds intrinsic properties/attributes

identity: each node is represented by a nique identity or label in the given context
attributes/properties: defines a node's characteristics
relationships: by connecting with other nodes via edges they represent various forms of relationships
"""

class TNodeMeta(type):
    """
    name: identifier of the node (object or a concept)
    bases: list of base concepts or ideas from which node inherits their fundamental characteristics
    namespaces: 
        properties: intrinsic attributes of the node
        transformations: functions or operations that change or refine the node's state
        relations: how one node connects to or interacts with other nodes
    """
    def __new__(cls, name, bases, namespace):
        namespace.setdefault('properties', {})
        namespace.setdefault('transformations', {})
        namespace.setdefault('relations', {})
        return super().__new__(cls, name, bases, namespace)
    


# base node class using TNodeMeta as it's metaclass
class TNode(metaclass=TNodeMeta):
    """
    node class represents an individual object or concept
    attributes: dictionary that represents the following: 
        - properties: intrinsic attributes of the node
        - transformations: functions that modify node's properties
        - relations: descriptions or functions representing relationships with other nodes
    """

    def __init__(self, **kwargs):
        