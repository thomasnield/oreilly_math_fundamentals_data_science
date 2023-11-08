import random


def f(x):
    return (x - 3) ** 2 + 4

def dx_f(x):
    return 2*(x - 3)

L = 0.001  # The learning rate
epochs = 100000  # The number of iterations to perform gradient descent

x = random.randint(-15,15)   # start at a random x

for i in range(epochs):
    d_x = dx_f(x) # get slope
    x = x - L * d_x  # update x by subtracting the (learning rate) * (slope)

print(x, f(x)) # prints 2.999999999999889 4.0
