import pandas as pd
from sklearn.linear_model import LinearRegression

# Import points

df = pd.read_csv('https://bit.ly/3cIH97A', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

# Plain ordinary least squares
fit = LinearRegression().fit(X, Y)

# Print "m" and "b" coefficients
print("m = {0}".format(fit.coef_.flatten()))
print("b = {0}".format(fit.intercept_.flatten()))

# Predict a new "y" value for x = 3.5
print("x = 3.5, y = {0}".format(fit.predict([[3.5]]).flatten()))

