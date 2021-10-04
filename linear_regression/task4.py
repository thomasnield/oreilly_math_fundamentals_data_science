"""
A small training dataset of X and Y values is provided here: 
https://bit.ly/3sdlri9

Perform a linear regression by means of gradient descent
by filling out the code below. 

You will need to experiment to find a learning rate L 
and number of iterations to reach the minimum loss. 

Get an accuracy within 1 rounded decimal places. 

It may take a minute or two to run!

Then execute the script by typing this command in the terminal:
python3 task4.py 
"""
import pandas as pd

# Input data
data = pd.read_csv('https://bit.ly/3sdlri9', header=0)
X = data.iloc[:, 0]
Y = data.iloc[:, 1]

# Building the model
m = 0.0
b = 0.0

L = ?  # The learning Rate
epochs = ?  # The number of iterations to perform gradient descent

n = float(len(X))  # Number of elements in X

# Performing Gradient Descent
for i in range(epochs):
    Y_pred = m * X + b  # The predicted value of Y
    D_m = (-2 / n) * sum(X * (Y - Y_pred))  # d/dm derivative of loss function
    D_b = (-2 / n) * sum(Y - Y_pred)  # d/dc derivative of loss function
    m = ?  # Update m
    b = ?  # Update b

print("{0} {1}".format(round(m, 1), round(b, 1)))
