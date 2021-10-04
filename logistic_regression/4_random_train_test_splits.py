import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, ShuffleSplit

# Load the data
df = pd.read_csv('https://bit.ly/3cManTi', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)\
Y = df.values[:, -1]

# Do random splits that randomly samples the data on each split
# Note that training and testing data can overlap
kfold = ShuffleSplit(n_splits=100, test_size=.33, random_state=7)

model = LogisticRegression(solver='liblinear')
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy mean: %.3f (stdev=%.3f)" % (results.mean(), results.std()))
