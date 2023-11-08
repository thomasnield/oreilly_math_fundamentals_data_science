import pandas as pd

# Input data
data = pd.read_csv('https://bit.ly/3n1FKgE', header=0)
X = data.iloc[:, 0]
Y = data.iloc[:, 1]

# Building the model
m = 0.0
b =  0.0

L = .00001  # The learning Rate
epochs = 1000000  # The number of iterations to perform gradient descent

n = float(len(X))  # Number of elements in X

# Performing Gradient Descent
for i in range(epochs):
    Y_pred = m * X + b  # The current predicted value of Y
    D_m = (-2 / n) * sum(X * (Y - Y_pred))  # d/dm derivative of loss function
    D_b = (-2 / n) * sum(Y - Y_pred)  # d/dc derivative of loss function
    m = m - L * D_m  # Update m
    b = b - L * D_b  # Update b

    # print progress
    if i % 10000 == 0:
        print(i, m, b)

print(m, b)
