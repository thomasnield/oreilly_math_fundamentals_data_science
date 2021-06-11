from sympy import *

# x and step size
x, s = symbols('x s')

# declare function
f = x**2

# slope between two points with step s
slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)

# substitute 2 for x
slope_2 = slope_f.subs(x, 2)

# calculate slope at x = 2
# by forever approaching a step size of 0
result = limit(slope_2, s, 0)

print(result) # 4
