import numpy as np
class Relation:

    def __init__(self, A, relation):
        """
        initalizes relation on set A
        parameters:
            - A: set (iterable elements)
            - relation: a callanle that takes two arguments a, b from set A
                        - (a, b) returns true if a is related to b by the given relation,
                            if yes then (a, b) belongs or satisfies the relation
        """

        self.A = set(A) # ensures that A is set with unique elements and avoids duplicate entries

        if not callable(relation):
            raise ValueError("Condition must be a callable that accepts two parameeters and returns a bool")
        
        self.relation = relation

        self.R = self.generate_relation() # a set of tuples (a, b) where (a, b) is true based on the given relation



    def generate_relation(self):

        # returns a set of tuple (a, b) for both a,b in A if it satisfies the given relation
        return {(a, b) for a in self.A for b in self.A if self.relation(a, b)}


    def get_relation(self):
        return self.R


    def is_reflexive(self):
        return all(self.relation(a, a) for a in self.A)

    def is_symmetric(self):
        return all(self.relation(b, a) for a in self.A for b in self.A if self.relation(a, b))

    def is_antisymmetric(self):
        return all((not (self.relation(a, b) and self.relation(b, a))) or (a == b) for a in self.A for b in self.A)

    def is_asymmetric(self):
        no_self_relations = all(not self.relation(a, a) for a in self.A)
        one_way_relation = all(not self.relation(b, a) for a in self.A for b in self.A if self.relation(a, b))
        return no_self_relations & one_way_relation

    def is_transitive(self):
        return all(self.relation(a, c) for a in self.A for b in self.A for c in self.A if self.relation(a, b) and self.relation(b, c))


    def is_equivalent(self):
        return self.is_reflexive() and self.is_symmetric() and self.is_transitive()




def parition_from_equivalence(A, eq):
    """
    given a set A and an equivalence relation eq, this function returns the partition of S as a set of frozensets, where each frozen set is an equivalence class
    parameters: 
        - A: set (collection of elements)
        - eq: callable function that returns true if a and b are equivalent
    """
    # check if the given relation is equivalent
    eq_relation = Relation(A, eq).is_equivalent()
    if eq_relation:
        # apply the given equivalence relation or function to every element in S
        return set(map(lambda x: frozenset(filter(lambda b: eq(x, b), A)), A))