from typing import Callable, Set, Any, Dict, List, TypeVar

T = TypeVar('T')
class CatsFunction:
    """
    a class representing a function f: A -> B
    A, B: domain and codomain, where f maps every element of A to B, where each element of A only maps to one element
    graph of the function is represnted implicity by mapping: {((a), f(a)) for all a in A, and f(a) is an element of B}    
    """

    def __init__(self, domain: Set[Any], codomain: Set[Any], func: Callable[[Any], Any]) -> None:

        """
        Set type is enforced to ensure that the domain and codomain are well defined
        parameters:
            - domain: set of all possible inputs to the function
            - codomain: set of all possible valid outputs (may contain additional elements)
            - func: a callable function that takes an input from the domain and maps it an output in codomain
        """
        self.domain = domain
        self.codomain = codomain
        self.func = func

        """
        each element in domain must have an output in the codomain and raises error if the element or output value is not in the codomain
        """
        for a in domain:
            value = self.func(a)
            if value not in codomain:
                raise ValueError(f"Value {value} for input {a} is not in the specified codomain")

    
    def __call__(self, a: Any) -> None:
        """
        apply the function to an element in the domain
        a: an element from the domain
        returns the image f(a) in the codomain
        """
        if a not in self.domain:
            raise ValueError(f"Input {a} is not in the domain")
        return self.func(a)

    def graph(self) -> Set[tuple]:
        """
        computes the graph of the function, set of ordered pairs with (input, output) for every element in the domain
        f: A -> B defined as {(a, f(a) such that a belongs to domain (A))}
        the graph method returns a set of tuples where each tuple represents a function that is applied to every element (a, f(a))

        return value is a set comprehension, which iterates over every element in the domain and computes it's value and returns an ordered pair of the element and its value with respect to the function
        """
        return {(a, self.func(a) )for a in self.domain}
    

    def image(self, subset: Set[Any]) -> Set[Any]:
        """
        computes the image or range of a given subset of the domain under the given function,
        where if S is a subset of domain A, f(S) = {f(a) where a is an element in S}, thus is the set of all outputs with respect to inputs form S
        whilst codomain is full possible space of outputs, image is the actual values with respect to given function
        parameters: set of elements taken from the domain
        return: set of function values or outputs based on the input domain subset

        return value is a set comprehension that iterates over each element in the subset computs and collects it into a set
        """
        return {(a, self.func(a)) for a in subset if a in self.domain}

    def restrict(self, subset: Set[Any]) -> "CatsFunction":
        """
        creates a new function that is restricted to a subset of the domain
        parameters:
            - subset: a subset of the original domain
            - a new function with the same mapping rule but to a subset (smaller or restricted set of the domain)
        """
        if not subset.issubset(self.domain):
            """
            ensures that the given input set is a subset of the domain and raises error if any element of the subset is not a part of the domain
            """
            raise ValueError("The restricted subset must be within the domain")
        
        """returns a new CatsFunction class with a new domain which is the subset and the same function"""
        return CatsFunction(subset, self.codomain, self.func)
    
    """static is used so that it can be used without instantiating the class"""
    @staticmethod
    def identity(domain: Set[Any]) -> "CatsFunction":
        """
        identity method acts as a mapping that maps every element to itself id_A: A -> A; id_A(a) = a
        identity_fun that takes x as an input and returns it unchanged
        """
        identity_func = lambda x: x
        return CatsFunction(domain, domain, identity_func)
        
    
    @staticmethod
    def inclusion(subset: Set[Any], superset: Set[Any]) -> "CatsFunction":
        """
        inclusion function i : S -> A, where S is a subset of A and retusn a function that takes each element in S and mapst it to itself in A
        i(s) = s for all s in S, where S is a subset and A is a superset
        """
        if not subset.issubset(superset):
            """raises error if the given subset is not a subset of the given superset"""
            raise ValueError("Given subset is not an actual subset of the given superset")
        """ returns a new CatsFunction with subset as a domain, superset as a codomain and a function that maps each element to itself"""
        return CatsFunction(subset, superset, lambda s: s)
    
    def compose(self, other: "CatsFunction") -> "CatsFunction":
        """
        a method that combines two functions into a single function, where the result from the first function is passed on as input to the second function
        g o f : (A -> B) -> C = g(f(a)), where f: A -> B and g: B -> C;

        parameters:
        self: function f : A -> B
        other: another function of CatsFunction type, g: B -> C
        returns a new CatsFunction representing g o f
        """
        
        """
        validation: checks if the codomain of the first function is the same as domain of the second function
        """
        if self.codomain != other.domain:
            raise ValueError("THe codomain of the first function must be the same as the domain of the second function")
        
        """
        call method is used here to pass the value of the first function as an input of the other function
        """
        composed_func = lambda a: other(self.func(a))

        """
        returns a new function with the same domain and codomain that is a result of applying the other's func on the current codomain
        """
        return CatsFunction(self.domain, other.codomain, composed_func)
    

    def is_injective(self) -> bool:

        """
        checks if the given function is injective (one-to-one)
        if a, b are elements in the domain, the function is injective if no two a, b in the domain map to the same element in the codomain
        """

        """
        seen: a dictionary that inputs and corresponding function outputs
        iterates over all the elements in the domain, computs function and returns False if the image is already mapped to from an existing input else returns True
        """
        seen = {}

        for a in self.domain:
            """
            creates an image for a given input that are stored as key value pairs
            checks if the image is in the seen, and if yes, checks if there already exists a value for that given image and if yes returns false
            """
            image = self.func(a)
            if image in seen and seen[image] != a:
                return False
            seen[image] = a 
        return True


    def is_surjective(self) -> bool:
        """
        checks if the given function is surjective (onto)
        for every element b in the codomain there must be a respective preimage or element in the domain (all the elements of codomain must have a mapping)
        """
        """
        images: image or values of all the values of function applied onto domain
        is surjective if the images set is equal to the codomain
        """
        images = self.image(self.domain)
        return images == self.codomain
    

    def is_bijective(self):
        """ a function that is both injective and surjective and thus has a one-to-one correspondence between domain and codomain"""
        return self.is_injective and self.is_bijective