import pandas as pd
import numpy as np

# Input data
data = pd.read_csv('https://bit.ly/3n1FKgE', header=0)

X = data.iloc[:, 0].values
Y = data.iloc[:, 1].values

n = data.shape[0]  # rows

# Building the model
m = 0.0
b = 0.0

sample_size = 10  # sample size
L = .00001  # The learning Rate
epochs = 1000000  # The number of iterations to perform gradient descent

# Performing Stochastic Gradient Descent
for i in range(epochs):
    idx = np.random.choice(n, sample_size, replace=False)
    x_sample = X[idx]
    y_sample = Y[idx]

    Y_pred = m * x_sample + b  # The current predicted value of Y
    D_m = (-2 / sample_size) * sum(x_sample * (y_sample - Y_pred))  # d/dm derivative of loss function
    D_b = (-2 / sample_size) * sum(y_sample - Y_pred)  # d/dc derivative of loss function
    m = m - L * D_m  # Update m
    b = b - L * D_b  # Update b

    # print progress
    if i % 10000 == 0:
        print(i, m, b)

print(m, b)
