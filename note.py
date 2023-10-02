from sympy import *

A = [1,3,4,2]
B = [3,4,5,6]

M = Matrix([A, B])
#Matrix([[1, -1], [3, 4], [0, 2]])
print(M[7])