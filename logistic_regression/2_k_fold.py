import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score

# Load the data
df = pd.read_csv('https://bit.ly/3cManTi', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)\

Y = df.values[:, -1]

# Use k-fold to evaluate and perform different train/test splits on 3 folds
# Set a random seed just to make the randomly selected split consistent
# Note that datasets in the thousands, tens of thousands that 3-10 folds are often used
# This will help prevent overfitting
kfold = KFold(n_splits=3, random_state=7, shuffle=True)
model = LogisticRegression(solver='liblinear')
results = cross_val_score(model, X, Y, cv=kfold)

# For the output, we assume the different outputs follow a Gaussian distribution
# so we report a mean and standard deviation
print("Accuracy Mean: %.3f (stdev=%.3f)" % (results.mean(), results.std()))
