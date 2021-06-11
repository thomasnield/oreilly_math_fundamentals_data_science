def derivative_x(f, x, step_size):
    m = (f(x + step_size) - f(x)) / ((x + step_size) - x)
    return m

def my_function(x):
    return x ** 2

slope_at_2 = derivative_x(my_function, 2, .00001)

print(slope_at_2)  # prints 4.000010000000827
