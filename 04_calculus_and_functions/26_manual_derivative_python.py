# Using Plain Python
def f(x):
    return x ** 2

def dx_f(x):
    return 2 * x

slope_at_2 = dx_f(2.0)

print(slope_at_2)  # prints 4.0
