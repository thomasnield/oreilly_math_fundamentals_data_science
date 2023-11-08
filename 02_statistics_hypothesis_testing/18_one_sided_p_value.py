from scipy.stats import norm

# Cold has 18 day mean recovery, 1.5 std dev
mean = 18
std_dev = 1.5

# Probability of 16 or less days
p_value = norm.cdf(16, mean, std_dev)

print("1-tailed P-value: ", p_value) 
if p_value <= norm.ppf(.05):
    print("Passes 1-tailed test")
else:
    print("Fails 1-tailed test")
