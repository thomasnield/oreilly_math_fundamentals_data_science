from scipy.stats import norm

# Cold has 18 day mean recovery, 1.5 std dev
mean = 18
std_dev = 1.5

# Probability of 16 or less days
x = norm.cdf(16, mean, std_dev)

print(x) # 0.09121121972586788
