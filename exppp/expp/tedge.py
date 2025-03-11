"""
Edge: an edge is connection or a link between two nodes or vertices
edge can represent relationship, association, or interaction between the entities that nodes symbolizes
Undirected edges: edge has no direction; if there is an edge between Nodes A & B, the connection works both ways
Directed edges: edge has a direction, where it goes from the source Node to destination node
Edges capture the essence of how nodes are related or interacted
"""

class TEdge:

    def __init__(self, node1, node2, directed=False, weight=None):
        """
        Initializes a new edge connecting two nodes

        Parameters:
            node1: first endpoint of the edge or source
            node2: second endpoint of the edge or destination

            directed: a boolean value indicating directed(true) or undirected(false)
            weight: parameter or a value representing the weight of the edge
        """
        self.node1 = node1
        self.node2 = node2
        self.directed = directed
        self.weight = weight


    def get_endpoints(self):
        """
        returns a tuple (two nodes) connected by this edge; (node1, node2)
        """
        return (self.node1, self.node2)
    

    def __repr__(self):
        """
        provides a string representation of the edge including nodes, direction, and weight
        """
        # arrow if it is directed, else -- representing the connection
        node_connector = '->' if self.directed else '--'
        # includes weight if exists
        if self.weight is not None:
            return f"{self.node1} {node_connector} {self.node2} (weight = {self.weight})"
        else:
            return f"{self.node1} {node_connector} {self.node2}"