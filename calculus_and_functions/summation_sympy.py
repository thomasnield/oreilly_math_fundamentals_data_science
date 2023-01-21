from sympy import *

i, n = symbols('i n')

# iterate each element i from 1 to n
# then multiply and sum
summation = Sum(2*i, (i,1,n))

# Specify n as 5
# iterating the numbers 1 to 5
up_to_5 = summation.subs(n, 5)
print(up_to_5.doit())