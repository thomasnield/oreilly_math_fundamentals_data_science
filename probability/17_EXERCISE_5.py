"""
You suspect your friend is not using a fair coin to kick off a football game. 

You borrow it and flip it 10 times, getting 8 heads and 2 tails. 

Using the beta distribution, what is the probability the underlying 
probability for heads is greater than 50%? 

Complete the code below.

"""
from scipy.stats import beta

heads = 8
tails = 2

p = ? - beta.cdf(?, ?, ?)

print(p)
