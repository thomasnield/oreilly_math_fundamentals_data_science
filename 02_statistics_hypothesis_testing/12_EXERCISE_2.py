
"""
A market researcher estimates that the Z-Phone 
smart phone has a mean consumer life of 42 months 
with a standard deviation of 8 months. 

Assuming a normal distribution, what is the probability 
a given random Z-Phone will last between 20 and 30 months? 

Correct the code below to print the answer. 

Then execute the script by typing this command in the terminal:
python3 task2.py 
"""

from scipy.stats import norm

mean = 42
std_dev = 8

x = norm.cdf(30, mean, std_dev) 

print(x)
