from scipy.stats import beta

a = 15
b = 4

x = beta.cdf(1.0, a, b) - beta.cdf(.50, a, b)

print(x)
