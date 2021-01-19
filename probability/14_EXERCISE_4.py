from scipy.stats import beta

a = 15
b = 4

x = 1.0 - beta.cdf(.50, a, b)

print(x)
