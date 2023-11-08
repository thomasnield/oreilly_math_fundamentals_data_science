import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data
df = pd.read_csv('https://bit.ly/2X1HWH7', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)\
Y = df.values[:, -1]

# Plain ordinary least squares
fit = LinearRegression().fit(X, Y)

# Print "m" and "b" coefficients
print("Coefficients = {0}".format(fit.coef_))
print("Intercept = {0}".format(fit.intercept_))
print("y = {0} + {1}x1 + {2}x2".format(fit.intercept_, fit.coef_[0], fit.coef_[1]))

# Predict a new “y" value for x1 = 3.5 and x2 = 4.5
print("x1 = 3.5, x2 = 4.5, y = {0}".format(fit.predict([[3.5, 4.5]])))
