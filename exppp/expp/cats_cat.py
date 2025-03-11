from typing import TypeVar, Generic, Callable, Dict, List, Set

"""TypeVar: to represent objects in a category"""
T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


class Morphism:
    """morphism is a directed relationship between two objects"""
    def __init__(self, source: Set[T], target: Set[U], func: Callable[[T], U]):
        """
        source: starting object or domain
        target: ending object or codomain
        func: a function mapping elements from source (domain object) to target (codomain object)
        """
        self.source = source
        self.target = target
        self.func = func


    
    def __call__(self, X: T) -> U:
        
        """
        parameters:
            x is an object of type T
            the call function applies and gives or maps from source of type T to target object of type U
        """
        return self.func(T)
    

    def __repr__(self):
        return f"Morphism( {self.source} -> {self.target})"


class Category:
    """
    represents a category consisting of objects and morphisms
    """
    def __init__(self):
        """
        initializes an empty category with objects and morphisms
        """
        self.objects: Set[Set[T]] = set()
        self.morphisms: Dict[str, Morphism] = {}


    def add_object(self, obj: Set[T]):
        """adds an object to the category"""
        self.objects.add(frozenset(obj))

    
    def add_morphism(self, name: str, morphism: Morphism[T, U]):
        self.morphisms[name] = morphism
        self.add_object(morphism.source)
        self.add_object(morphism.target)