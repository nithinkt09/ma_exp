"""
set: a well-defined collection of distinct elements where the order of elements and repetition does not matter
key properties:
    - memebership: an element belongs to a set if it is contained in it
    - equality: two sets are equal iff they have the same element
    - subset: a set A is a subset of set B if every element of A is in B
    - A union B: gives a new set containing all the elements of A and B
    - A intersection B: gives a new set containing all the common elements of A and B
    - A difference B: new set containing elements in A but not in B

"""
from itertools import chain, combinations
from typing import Any, Set, Callable, TypeVar
"""
typing module offers explicity type hints
    - Any allows elements of any type
    - Set[Any]: represents collection of unique elements
    - Callable[[Any], returnType] used for functions that takesan element and returns a returnType object
"""
class TopSet:

    def __init__(self, elements: Set[Any]):
        """
        intializes a set with a collection of unique elements
        (elements: Set[Any]): ensures that the input is a set containing elements of any type
        """
        # using inbuilt set function that ensures uniqueness of elements and also offers standard built-in methods
        self.elements: Set[Any] = set(elements) 

    def __eq__(self, other: Any) -> bool:
        """
        two sets are equal iff they contain the same elements
        other: another set to compare with
        returns a boolean indicating whether the sets are equal
        """
        return self.elements == other.elements
    
    def contains(self, element: Any) -> bool:
        """
        checks if an element belongs to the set
        element: element to check 
        returns a boolean indicating membership
        """
        return element in self.elements
    
    def add(self, element: Any):
        """
        adds an element to the set
        element: element to add to the set
        """
        self.elements.add(element)
    
    def remove(self, element: Any):
        """
        removes an element from the set
        element: element to be removed
        """
        self.elements.remove(element)
    
    def union(self, other):
        """
        creates a new set by adding the elements from other set
        __class__method calls this class itself and passes elements from both the classes
        returns a new class of set with union of elements from both sets
        """
        return self.__class__(self.elements | other.elements)

    def intersection(self, other):
        """
        returns a new set with the elements that are common in both the sets
        """
        return self.__class__(self.elements & other.elements)
    
    def difference(self, other):
        """
        returns a new set with elements that in this set and are not in the other set
        """
        return self.__clas__(self.elements - other.elements)
    
    def filter_by_property(self, property_function: Callable[[Any], bool]):
        """
        constructs a new set based on the property function
        property_function: defines the property that elements must satisfy
            - takes an element as input and returns True if it should be included
        """
        return self.__class__({element for element in self.elements if property_function(element)})
    
    def is_subset(self, other):
        """
        checks if the current set is a subset of other set
        """
        return self.elements.issubset(other.elements)
    
    def is_proper_subset(self, other):
        "checks if the current set is a proper subset of the other set"
        return self.elements < other.elements
    
    def power_set(self):
        """ generates power set of elements """
        elements_list = list(self.elements)
        return [set(subset) for subset in chain.from_iterable(combinations(elements_list, r) for r in range(len(elements_list)))]

    def disjoint_union(s, t): 
        tagged_s = {('S', element) for element in s}
        tagged_t = {('T', element) for element in t}
        return tagged_s | tagged_t

    def cartesian_product(s, t):
        return {(a, b) for a in s for b in t}

    def cardinality(self):
        return len(self.elements)

    def __repr__(self):
        """
        string representation of the set
        """
        return f"{self.__class__.__name__}: ({self.elements})"