"""
The mean for a pug weight is 20 lbs.
The standard deviation is 1.2 lbs.

For a pug weighing 18.5 lbs, what is its weight in 
terms of standard deviations (the Z-score)? 

Complete the code below to calculate the answer.

Then execute the script by typing this command in the terminal:
python3 task3.py 
"""
from post_answer import submit

def z_to_x(z, mean, std):
    return (z * std) + mean

def x_to_z(x, mean, std):
    return ?

mean = 20.0
stdev = 1.2

my_pug_weight = 18.5
my_pug_zscore = ?

# Submits the answer, please don't modify! 
submit(3, my_pug_zscore, 2)
