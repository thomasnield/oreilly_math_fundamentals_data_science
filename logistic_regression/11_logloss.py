import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score

# Load the data
df = pd.read_csv('https://bit.ly/34bqmpT', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)\

Y = df.values[:, -1]

kfold = KFold(n_splits=3, random_state=7, shuffle=True)
model = LogisticRegression(solver='liblinear')

# Logloss is another way to measure classification performance
# It aggregates measurements of probabilities between 0 and 1 and punsishes/rewards accordingly
# Smaller logloss is better, with "0" being perfect
results = cross_val_score(model, X, Y, cv=kfold, scoring='neg_log_loss')
print("Logloss: %.3f (%.3f)" % (results.mean(), results.std()))


