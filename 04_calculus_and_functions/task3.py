"""
Let's apply gradient descent to a simple problem. It may
be overkill because we could solve it algebraically,
but complex techniques are best introduced on simple problems.

Use gradient descent to approximate the minimum of the function
f(x) = (x-5)^2 + 10 by completing the code below.

The answer must round to 6 decimal places to the correct answer,
so find a learning rate and number of iterations to achieve that accuracy.

Then execute the script.
"""

import random


def f(x):
    return (x - 5) ** 2 + 10


# The derivative of f(x)
def dx_f(x):
    return 2 * (x - 5)


L = ? # The learning rate
epochs = ?  # The number of iterations to perform gradient descent

x = random.randint(-15, 15)  # start at a random x

for i in range(epochs):
    d_x = dx_f(x)  # get slope
    x = ?  # perform gradient descent here

print(x)
