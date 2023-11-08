from scipy.special import erfinv


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


# What range around the mean gives an area of .95?
print(critical_z_value(p=.95, mean=18, std=1.5))
# (15.060054023189918, 20.93994597681008)
