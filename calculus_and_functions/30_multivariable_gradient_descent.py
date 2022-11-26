def f(x,y,z):
    return (x+10)**2 + (y-3)**2 + (1-z)**2

def dx_f(x):
    return 2*x + 20

def dy_f(y):
    return 2*y - 6

def dz_f(z):
    return 2*z - 2

L = 0.0001  # The learning rate
epochs = 1000000  # The number of iterations to perform gradient descent

x = 0   # we will find the x for the minimum
y = 0   # we will find the y for the minimum
z = 0   # we will find the z for the minimum

for i in range(epochs):
    d_x = dx_f(x) # get x slope
    d_y = dy_f(y) # get y slope
    d_z = dz_f(z) # get z slope

    x = x - L * d_x  # update x
    y = y - L * d_y  # update y
    z = z - L * d_z  # update z

# -9.999999999995559 2.9999999999988898 0.9999999999997224 2.1031154992708616e-23
print(x, y, z, f(x,y,z))
