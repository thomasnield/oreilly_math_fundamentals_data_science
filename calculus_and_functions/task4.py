"""
Jumping things up a notch, let's try some multivariable calculus. 

Again this is a problem that could be solved algebraically but 
try to use gradient descent to solve it. 

Find the minimum for the function: 
f(x,y,z) = (x + 3)^2 + (y - 2)^2 + (z + 3)^2

The partial derivatives have been declared below. 

Complete and experiment with the rest of the code 
to get a rounded accuracy to 6 decimal places. 

Then execute the script
"""
def f(x, y, z):
    return (x + 3) ** 2 + (y - 2) ** 2 + (z + 3) ** 2


def dx_f(x):
    return 2 * (x + 3)


def dy_f(y):
    return 2 * (y - 2)


def dz_f(z):
    return 2 * (z + 3)


L = ?  # The learning rate
epochs = ?  # The number of iterations to perform gradient descent

x = 0  # we will find the x for the minimum
y = 0  # we will find the y for the minimum
z = 0  # we will find the z for the minimum

for i in range(epochs):
    d_x = dx_f(x)  # get x slope
    d_y = dy_f(y)  # get y slope
    d_z = dz_f(z)  # get z slope

    x = ?  # update x
    y = ?  # update y
    z = ?  # update z

print("{0} {1} {2}".format(round(x, 6), round(y, 6), round(z, 6)))
