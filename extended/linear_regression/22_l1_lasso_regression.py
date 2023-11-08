import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import KFold, cross_val_score

# Wine quality data
df = pd.read_csv('https://bit.ly/39uuK7J', delimiter=",")
print(df)

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

kfold = KFold(n_splits=3, random_state=7, shuffle=True)

# Lasso regression with 0.1 penalty
model = Lasso(alpha=0.1)

results = cross_val_score(model, X, Y, cv=kfold, scoring='neg_mean_squared_error')

print("Accuracy Mean: %.3f (stdev=%.3f)" % (results.mean(), results.std()))
