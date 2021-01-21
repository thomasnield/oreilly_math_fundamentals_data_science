from scipy.stats import norm

# $10,345 in sales on average, $552 standard deviation
mean = 10345
std_dev = 552

# Probability of $11,641 or more
p1 = 1.0 - norm.cdf(11641, mean, std_dev)

# Take advantage of symmetry for other side
p2 = p1

# P-value of both tails
p_value = p1 + p2

print(p_value) # 0.01888333596496139
