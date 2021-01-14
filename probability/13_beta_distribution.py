from scipy.stats import beta

a = 8
b = 2

p = beta.cdf(1.0, a, b) - beta.cdf(.90, a, b)

print(p)
