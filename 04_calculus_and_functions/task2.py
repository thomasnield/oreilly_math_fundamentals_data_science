"""
We want to find the area for the function y = .5x^2 
within the range 0 and 2. 

Here is a graph showing the function and area we want to calculate: 
https://www.desmos.com/calculator/ihfabetgqm

Complete the code below to approximate this area by using a Reimann Sums, 
which packs rectangles under the function (at their midpoints) and summing their areas. 

Be sure to specify enough rectangles so we get accuracy of at least 6 decimal places. 

Then execute the script
"""

# This function will pack `n` rectangles under the function `f` for the
# specified `lower` and `upper` bounds, and above the x-axis. 
def approximate_integral(lower, upper, n, f):
    delta_x = (upper - lower) / n
    total_sum = 0

    for i in range(1, n + 1):
        midpoint = 0.5 * (2 * lower + delta_x * (2 * i - 1))
        total_sum += f(midpoint)

    return total_sum * delta_x


def my_function(x):
    return ?


area = approximate_integral(lower=?, upper=?, n=?, f=?)

print(area)
