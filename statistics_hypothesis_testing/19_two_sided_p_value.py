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
# I could have also just multiplied by 2 
p_value = p1 + p2

print("2-tailed P-value", p_value)
if p_value <= .05:
    print("Passes 2-tailed test")
else:
    print("Fails 2-tailed test")


# There is an 18.24% probability my results
# were due to random luck, rather than because
# my drug made an impact 
