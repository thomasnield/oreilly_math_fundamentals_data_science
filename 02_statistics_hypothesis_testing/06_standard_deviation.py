from math import sqrt

# Number of pets each person owns
sample = [1, 3, 2, 5, 7, 0, 2, 3]

def variance(values):
    mean = sum(values) / len(values)
    var = sum((v - mean) ** 2 for v in values) / (len(values) - 1)
    return var

def std_dev(values):
    return sqrt(variance(values))

print(std_dev(sample))  # prints 2.0879116360612584
