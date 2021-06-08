"""
A veterinary study sampled the weights of 13 pugs.

The mean of the sample is 19.2 lbs and the sample
standard deviation is 1.3.

What range (confidence interval) can I be 99% confident that the population
mean falls in, based on my sample?

Complete the code below to calculate the answer.

Then execute the script by typing this command in the terminal:
python3 task4.py 
"""

from post_answer import submit
from math import sqrt
from scipy.stats import t

# Returns the lower and upper bounds of 
# my critical T area
def critical_t_value(p, n):
    t_dist = t(df=?)
    left_area = (1.0 - p) / 2.0
    right_area = 1.0 - ((1.0 - p) / 2.0)
    return t_dist.ppf(?), t_dist.ppf(?)


def ci_small_sample(p, sample_mean, sample_std, n):

    lower, upper = critical_t_value(p, n)
    lower_ci = lower * (sample_std / sqrt(n))
    upper_ci = upper * (sample_std / sqrt(n))

    return sample_mean + ?, sample_mean + ?


# What is the confidence interval my sample of 13 pugs
# with sample mean of 19.2, sample std of 1.3?
confidence_interval = ci_small_sample(p=.99, sample_mean=19.2, sample_std=1.3, n=13)

# Submits the answer, please don't modify! 
submit(4, str(confidence_interval))
