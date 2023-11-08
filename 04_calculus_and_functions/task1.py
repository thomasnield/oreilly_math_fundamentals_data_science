"""
You can calculate the slope at any point in a function
by calculating the Calculus derivative. 

But one way to intuitively discover the slope at a given point 
in a function is choose a close neighboring point. The intersecting 
line between these two points will have an approximate slope, 
and the closer together those two points are the closer you get 
to the slope. 

Play with this Desmos graph for intuition: 
https://www.desmos.com/calculator/9wftjfmpn0

For the function f(x) = x^2 + 1, approximate a slope that's 
accurate to 6 decimal places by completing the code below. 

Then execute the script.

"""

def my_function(x):
    return x ** 2 + 1


def approximate_slope_x(f, x, step_size):
    m = (f(x + step_size) - f(x)) / ((x + step_size) - x)
    return m


slope_at_2 = approximate_slope_x(my_function, 2, ?)

print(slope_at_2)
