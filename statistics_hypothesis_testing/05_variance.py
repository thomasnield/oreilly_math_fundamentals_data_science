# Number of pets each person owns
sample = [1, 3, 2, 5, 7, 0, 2, 3]

def variance(values):
    mean = sum(values) / len(values)
    var = sum((v - mean) ** 2 for v in values) / len(values)
    return var

print(variance(sample))  # prints 4.359375

