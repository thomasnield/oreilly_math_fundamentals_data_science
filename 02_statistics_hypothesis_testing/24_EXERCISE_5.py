"""
Your marketing department has started a new advertising campaign
and wants to know if it affected sales,
which in the past averaged $10,345 a day with a standard deviation of $552.

The new advertising campaign ran for 45 days and averaged $11,641 in sales.

Did the campaign affect sales? Use a 2-tailed Z-test to calculate the p-value. 

Then execute the script by typing this command in the terminal:
python3 task5.py 
"""
from post_answer import submit
from scipy.stats import norm

# $11,641 in sales on average, $552 standard deviation
mean = 11641
std_dev = 552

# Probability of $10,345 or less
p_left_tail = norm.cdf(?, ?, ?)
p_right_tail = ?

# P-value of both tails
p_value = ?

# Submits the answer, please don't modify! 
submit(5, p_value, 4) 
