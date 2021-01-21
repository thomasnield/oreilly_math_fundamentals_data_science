import math

# normal distribution, returns likelihood
def normal_pdf(x: float, mean: float, std_dev: float) -> float:
    return (1.0 / (2.0 * math.pi * std_dev ** 2) ** 0.5) * \
        math.exp(-1.0 * ((x - mean) ** 2 / (2.0 * std_dev ** 2)))

mean = 50.0
std_dev = 15.0

for x in range(0,100):
    likelihood_of_x = normal_pdf(x, mean, std_dev)
    print("{},{}".format(x, likelihood_of_x))

