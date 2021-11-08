"""
The code below is supposed to calculate the variance and standard deviation 
for a data sample, but there is an error. 

Fix the code so it returns the correct standard deviation for a sample. 

Then execute the script by typing this command in the terminal:
python3 task1.py 
"""
from math import sqrt

# Sample for number of pets each person owns
sample = [1, 3, 2, 5, 7, 0, 2, 3]

def variance_sample(values):
    mean = sum(values) / len(values)
    var = sum((v - mean) ** 2 for v in values) / len(values)
    return var

def std_dev_sample(values):
    return sqrt(variance_sample(values))

result = std_dev_sample(sample)

print(result)
