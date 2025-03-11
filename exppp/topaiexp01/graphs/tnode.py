"""
Node: a node or a vertex is a discrete entity that represents an object, idea, or an entity 
and node can be regarded as a fundamental building block or a unit in the given context.
Identifier: a unique or distinct identity that distinguishes it from other nodes in the given context
Attributes or properties: data or information about the node (object, idea, or entity)

Each node is connected by edges or links that represents relationships between the nodes,
however, node in itself can be regarded as a standalone object that could later be linked to form networks or structures
"""
import tedge

class TNode:

    def __init__(self, identifier):
        """
        Initializes a new node
        identifier: a distinct or unique string, int, or any relevant object that identifies this node

        Attributes: 
            id: stores the unique identifier
            attributes: a dictonary that holds additional data about the node
            degree: number of edges connected to this node
        """
        self.identifier = identifier
        self.attributes = {}
        self.edges = []
        
    
    def degree(self):
        return len(self.edges)
    
 
    def add_edge(self, edge):
        self.edges.add(edge)

    def set_attributes(self, key, value):
        """
        set an attribute for the node
        parameters:
            key: string value that denotes the name of the attribute
            value: value associated with the attribute
        """
        self.attributes[key] = value

    
    def get_attributes(self, key):
        """
        retrieve the value of an attribute
        parameters:
            key (string): name of the attribute        
            return: value of the attribute if exists, else None
        """
        return self.attributes.get(key)
    
    def __repr__(self):
        """
        a string representation of the Node
        return: a string that return's the node's identifier and attributes
        """
        return f"Node: id={self.identifier}, attributes={self.attributes}"
    