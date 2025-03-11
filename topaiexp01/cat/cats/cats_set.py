from collections import Counter
from itertools import product

class CatsSet:


    def __init__(self, elements):
        self.elements = set(elements)


    
    def __str__(self):
        return "{" + ", " .join(map(str, self.elements)) + "}"
    

    def __repr__(self):
        return f"Set : ({self.elements})"



    def union(self, other):
        return CatsSet(self.elements.union(other.elements))
    
    def intersection(self, other):
        return CatsSet(self.elements.intersection(other.elements))

    def difference(self, other):
        return CatsSet(self.elements.difference(other.elements))
    
    def cartesian_product(self, other):
        return {(a, b) for a,b in product(self.elements, other.elements)}
    

    @staticmethod
    def set_builder(universe, predicate):
        return CatsSet([x for x in universe if predicate(x)])
    

def powerset(s):
    s = list(s)
    n = len(s)
    result = []
    for i in range (2 ** n):
        subset = {s[j] for j in range(n) if (i >> j) & 1}
        result.append(subset)
    return result