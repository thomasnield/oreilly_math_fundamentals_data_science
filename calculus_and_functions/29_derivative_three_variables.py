from sympy import *

# Declare x and y to SymPy
x,y,z = symbols('x y z')

# Now just use Python syntax to declare function
f = (x+10)**2 + (y-3)**2 + (1-z)**2

# Calculate the partial derivatives for x and y
dx_f = diff(f, x)
dy_f = diff(f, y)
dz_f = diff(f, z)

print(dx_f) # 2*x + 20
print(dy_f) # 2*y - 6
print(dz_f) # 2*z - 2
