from scipy.special import erfinv
from math import sqrt


def inv_normal_cdf(p: float, mean: float, std_dev: float):
    return mean + (std_dev * (2.0 ** 0.5) * erfinv((2.0 * p) - 1.0))


def z_to_x(z, mean, std):
    return (z * std) + mean


def critical_z_value(p, mean=0.0, std=1.0):
    left_area = (1.0 - p) / 2.0
    right_area = 1.0 - ((1.0 - p) / 2.0)

    lower_cutoff = inv_normal_cdf(left_area, mean, std)
    upper_cutoff = inv_normal_cdf(right_area, mean, std)

    return lower_cutoff, upper_cutoff


def ci_large_sample(p, sample_mean, sample_std, n):
    # Sample size must be greater than 30

    lower, upper = critical_z_value(p)
    lower_ci = lower * (sample_std / sqrt(n))
    upper_ci = upper * (sample_std / sqrt(n))

    return sample_mean + lower_ci, sample_mean + upper_ci

print(ci_large_sample(p=.99, sample_mean= 1.715588, sample_std=0.029252, n=34))
# (1.7026658973748656, 1.7285101026251342)
