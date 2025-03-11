from typing import Any, Callable, Set, Iterable, Tuple, Union

def relation_pairs(S: Iterable[Any], R: Callable[[Any, Any], bool]) -> Set[Tuple]:
    """
    a relation R on a given set S is a subset of SxS such that for a,b in S (a, b) belongs to R if a is related to b
    the new set R is a subset of S x S

    parameters:
    - S: collection of elements that can be iterable that allows R to move through that iterable
    - R: a relation which takes two elements from the iterable and returns true and if yes the element is added 
    - returns a set with elements as tuples that satisfies the given relation or condition
    """
    return {(a, b) for a in S for b in S if R(a, b)}

def has_relation(S: Iterable[Any], R: Callable[[Any, Any], bool]) -> bool:
    """
    checks if all the elements in the  given iterable satisfies the given relation
    """
    return all(R(a, b) for a in S for b in S)

def is_reflexive(S: Iterable[Any], R: Callable[[Any, Any], bool]) -> bool:
    """
    is reflexive if every element is related to istelf by the given relation or condition
    """
    return all(R(a, a) for a in S)

def is_symmetric(S: Iterable[Any], R: Callable[[Any, Any], bool]) -> bool:
    """
    is symmetric where if (a, b) is a relation then (b, a) is also a realtion and a != b
    """
    return all(R(b, a) for a in S for b in S if R(a, b))

def is_transitive(S: Iterable[Any], R: Callable[[Any, Any], bool]) -> bool:
    """
    is transitive where if (a, b) and (b, c) are in relation then (a, c) is also in relation
    """
    return all(R(a, c) for a in S for b in S for c in S if (R(a,b) and R(b, c)))

def is_equivalent(S: Iterable, R: Callable[[Any, Any], bool]) -> bool:
    """
    a relation is equivalent if it is reflexive, symmetric, and transitive
    """
    return is_reflexive(S, R) and is_symmetric(S, R) and is_transitive(S, R)

def partition_by_equivalence(S: Iterable[Any], R: Callable[[Any, Any], bool]):
    """
    a partition of set is family or collection of disjoint nonempty subsets of S, union of which is S itself
    every element in a given partition set has eq_relation (equivalence relation) 
    """
    if not is_equivalent(S, R):
        return f"{R.__name__} is not an equivalent relation"
    
    partition: Set = set() # set that will hold all the classes that are partitioned based on the equivalence relation
    seen = set() # set that checks if the elements are already partitioned and only uses if the element isn't in already partitioned classes

    for a in S: #loops through the elements in the given iterable set that needs to be partitioned
        if a in seen: # if the element has already participated in partition it is skipped
            continue
        eq_class = {b for b in S if R(a, b)} # an equivalent class (set of elements) where all the elements are in equivalence relation to each other
        partition.add(frozenset(eq_class)) # the derived partition or eqiuvalent class is added to the partition set
        seen |= eq_class # all the elements that have participated in the parition are added to the seen 

    return partition