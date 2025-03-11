"""
function f from a set A to set B is a rule that assigns each element in set A a unique element f(a) in B 
in set theory, a function can be described by a graph (a set of ordered pairs)
        graph(f) = {(a, b) in AxB , f(a) = b}

key properties:
    - for every a in A there exists a b in B such that f(a) = b
    - image of a subset S of A is given by f(S) = {b in B such that there exists an a in S with f(a)=b}
    - if S is a subset of A, the restriction of f to S is the function f|s: S -> B defined by f|s(a) = f(a) for each a in S
    - identity function id_A: A -> A defined by id_A(a) = a for all a in A

"""
from typing import TypeVar, Generic, Dict, Set, Iterable

"""
T, U placeholders for actual types that will be specified when the class is used,
if the function takes an input type of T and returns an output type of U, then Function[int, str] represents a function from a string to an int
"""
T = TypeVar('T')
U = TypeVar('U')

"""
Genric[T, U] a generic class parametrized by two variable types T and U
TFunctions class is a subclass of Generic, by passing [T, U] to Generic it is ensured that the static type checkers that Function expects two type arguments
for instance TFunction[int, str] gives a notion that T is int and s is str
"""
class TFunctions(Generic[T, U]):
    """
    Models function f: A -> B

    functions between sets can be redone as follows:
        - domain A and codomain B (provided as collection of elements or objects)
        - mapping rule f as a callable or dictionary that assigns each element A an element in B
        - graph of the function as a set or dictionary of ordered pairs
        - additional operations such as computing the image of a subset or restricting the function of a subset


        Attributes:
            - domain(Set[T]): set A of inputs
            - comdain(Set[U]): set B of all possible outputs
            - mapping(Dict[T, U]): a dictionary representing the rule f such that each input is of type T and output is of type U
    """
    def __init__(self, domain: Set[T], codomain: Set[U], mapping: Dict[T, U]):
        if domain != set(mapping.keys()):
            raise ValueError("Mapping must be defined for every element in the domain")
        if not all (value in codomain for value in mapping.values()):
            raise ValueError("All mapping values must be in the codomain")
        
        self.domain: Set[T] = domain
        self.codomain: Set[U] = codomain
        self.mapping: Dict[T, U] = mapping


    
    def __call__(self, a:T) -> U:
        if a not in self.domain:
            raise ValueError("Element not in the domain")
        return self.mapping[a]

    def graph(self):
        return {(a, self.mapping[a]) for a in self.domain}
    
    def image(self, subset: Iterable[T]): 
        subset = set(subset)
        if not subset.issubset(self.domain):
            raise ValueError("Subset must be contained in the domain")
        return {self.mapping[a] for a in subset}
    
    def restrict(self, subset):
        subset = set(subset)
        if not subset.issubset(self.domain):
            raise ValueError("subset must be contained in the domain")
        restricted_mapping = {a: self.mapping[a] for a in subset}
        return TFunctions(domain=subset, codomain=self.codomain, mapping=restricted_mapping)
    