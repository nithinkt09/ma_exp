"""
functions are type of assignments that map elements from one set to the other set
    - f: A -> B; f takes an element from set A and maps it to an element in set B
    - g: B -> C; g takes an element from set B and maps it to an element in set C

composition of functions: given two functions f and g, the composition g o f is a new function
    g o f takes an element a and applies f to reach set B and then applies g to the result to reach set C
    (g  o f)(a) = g(f(a))

key properties:
    - associativity: (f: A -> B), (g: B -> C), (h: C -> D), composition is associative. (h o (g o f)) = ((h o g) o f)
    - identity: for any set A, identity function id_A: A -> A; id_A(a) = a;
                f : A -> B; (f o id_A = f); (id_B o f = f)


in terms of interactions, functions can be composed sequentially
"""