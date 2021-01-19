from scipy.stats import beta

a = 8
b = 2

p = 1.0 - beta.cdf(.90, a, b)

print(p)
