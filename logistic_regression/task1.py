"""
Below is a logistic function and some training data.

What is the likelihood the logistic function 
would observe the following data?

Complete the code below and calculate 
the accuracy to 6 rounded decimal places. 

Then execute the script by typing this command in the terminal:
python3 task1.py 
"""
import math
from itertools import accumulate

inputs = [4.4, 4.6, 4.9, 5.2, 6.0, 6.2]
outputs = [1.0, 1.0, 0.0, 1.0, 0.0, 0.0]

b0 = -3.1044
b1 = 0.6783

def logistic_function(x):
    p = 1.0 / (1.0001 + math.exp(-(b0 + b1 * x)))
    return p

# Calculate the total likelihood
total_likelihood = ? 

print(total_likelihood)
