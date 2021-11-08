import matplotlib.pyplot as plt
import pandas as pd
from numpy.linalg import inv
import numpy as np

# Import points
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1].flatten()

# Add placeholder "1" column to generate intercept
X_1 = np.vstack([X, np.ones(len(X))]).T

# Extract output column (all rows, last column)
Y = df.values[:, -1]

# Calculate coefficents for slope and intercept
b = inv(X_1.transpose().dot(X_1)).dot(X_1.transpose()).dot(Y)
print(b) # [1.93939394 4.73333333]

# Predict against the y-values 
y_predict = X_1.dot(b)
