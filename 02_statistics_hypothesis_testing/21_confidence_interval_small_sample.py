from math import sqrt
from scipy.stats import t

def critical_t_value(p, n):
    t_dist = t(df=n - 1)
    left_area = (1.0 - p) / 2.0
    right_area = 1.0 - ((1.0 - p) / 2.0)
    return t_dist.ppf(left_area), t_dist.ppf(right_area)


def ci_small_sample(p, sample_mean, sample_std, n):
    # Sample size must be greater than 30

    lower, upper = critical_t_value(p, n)
    lower_ci = lower * (sample_std / sqrt(n))
    upper_ci = upper * (sample_std / sqrt(n))

    return sample_mean + lower_ci, sample_mean + upper_ci


# What is the confidence interval my sample of 15 golden retrievers
# with sample mean of 65.13, sample std of 2.05?
print(ci_small_sample(p=.95, sample_mean=64.27, sample_std=2.75, n=15))
# (62.74710076069723, 65.79289923930276)
