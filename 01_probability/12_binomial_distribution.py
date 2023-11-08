from scipy.stats import binom

n = 10
p = 0.9

for x in range(n + 1):
    probability = binom.pmf(x, n, p)
    print("{0} - {1}".format(x, probability))
