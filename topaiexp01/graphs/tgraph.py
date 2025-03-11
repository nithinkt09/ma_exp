"""
Graph: method or way to represent structure using nodes and edges that models pairwise relationships

"""

import graphs.tnode0 as tnode0, tedge

class TGraph:

    def __init__(self):
        """
        nodes: list to store all the nodes in the graph
        edges: list to store all the edges in the graph
        """
        #concepts: use sets to represent nodes, where the keys are the nodes and values are edges
        self.nodes = []
        self.edges = []

    def add_node(self, nodeval):
        """
        nodeval: an input value for the new node
        new_node: a new node that is created using the nodeval from the input parameter
        new_node is then appended to the existing nodes list of the graph
        new_node is also returned for immediate use
        """
        new_node = tnode0.TNode(nodeval)
        self.nodes.append(new_node)
        return new_node
    
    def add_edge(self, node1, node2, direction=False, weight=None):

        """
        node1, node2: two nodes that are connected by the edge
        if node1 and node2 are not in the graph they are created
        new_edge: a new edge that connects the two given nodes, added to the list and returned for immediate use and returns it for immediate use
        """
        new_node1 = node1 if node1 in self.nodes else node1
        new_node2 = node2 if node2 in self.nodes else node2

        new_edge = tedge.TEdge(new_node1, new_node2, direction, weight)
        self.edges.append(new_edge)

        return new_edge
    

    def classify_node(self, node):
        """
        classifies the nodes based on the number of edges (degree)
        isolated : if degree = 0
        leaf: if degree = 1
        internal: if degree >= 2
        """
        degree = node.degree()
        if degree == 0:
            return "Isolated"
        elif degree == 1:
            return "Leaf"
        else: 
            return "Internal"
        
        
