from math import sqrt

# Filament samples
sample = [1.78, 1.75, 1.72, 1.74, 1.77]

def mean(values):
    return sum(sample) / len(sample)

def variance_sample(values):
    mean = sum(values) / len(values)
    var = sum((v - mean) ** 2 for v in values) / (len(values) - 1.0)
    return var

def std_dev_sample(values):
    return sqrt(variance_sample(values))


print("MEAN = {}".format(mean(sample))) # 1.752
print("STD DEV = {}".format(std_dev_sample(sample))) # 0.023874672772626667
