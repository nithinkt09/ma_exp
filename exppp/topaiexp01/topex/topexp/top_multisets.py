"""
multiset is a generalization of set that allows elements to appear multiple times where it stores the frequency or multiplicity of each element
indexed set is a collection of objects where each object is associated with unique index from a set I called the index set
    - formally indexed set can be viewed as a function f: I -> A, A: set of possible elements, I: set of indicies
"""

class TMultiset:
    """
    multiset can be represented using a dictionary where keys are elements from the set and values are multiplicites of the elements
    """
    def __init__(self):
        self.elements = {}

    def add(self, element, count=1):
        if element in self.elements:
            self.elements[element] += count
        else:
            self.elements[element] = count
    
    def remove(self, element, count=1):
        if element in self.elements:
            self.elements[element] -= count
            if self.elements[element] <= 0:
                del self.elements[element]


class TIndexedSet:
    """
    indexed set can be represented as a dictionary where the keys are indicies from I and the values are elements associaed with the indicies    
    """
    def __init__(self):
        self.indicies = {}

    def add(self, index, element):
        self.indicies[index] = element

    def remove(self, index):
        if index in self.indicies:
            del self.indicies[index]
    
    