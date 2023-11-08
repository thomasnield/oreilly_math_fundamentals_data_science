from sympy import *
from sympy.plotting import plot3d

x,y = symbols('x y')
f = 2*x**2 * 3*y**3
plot3d(f)
