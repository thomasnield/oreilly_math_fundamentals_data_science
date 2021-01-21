from scipy.stats import norm

# Cold has 18 day mean recovery, 1.5 std dev
mean = 18
std_dev = 1.5

# Probability of 16 or less days
p1 = norm.cdf(16, mean, std_dev)

# Probability of 20 or more days
# Take advantage of symmetry
p2 = p1

# P-value of both tails
p_value = p1 + p2

print(p_value) # 0.18242243945173575
