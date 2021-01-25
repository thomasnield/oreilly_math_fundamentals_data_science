from scipy.stats import norm

# $11,641 in sales on average, $552 standard deviation
mean = 11641
std_dev = 552

# Probability of $10,345 or less
p1 = norm.cdf(10345, mean, std_dev)

# Take advantage of symmetry for other side
p2 = p1

# P-value of both tails
p_value = p1 + p2

print(p_value)  # 0.01888333596496139
