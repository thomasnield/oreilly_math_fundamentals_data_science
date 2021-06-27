import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# Load the data
df = pd.read_csv('https://bit.ly/32fPYS8', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

# Perform train/test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1.0/3.0, random_state=10)

model = LogisticRegression(solver='liblinear')
y_predict = model.fit(X_train, Y_train)

# Create confusion matrix
y_true = Y_test
y_predict = model.predict(X_test)
tn, fp, fn, tp = confusion_matrix(y_true, y_predict).ravel()

print(tn, fp, fn, tp)
sensitivity = tp / (tp + fn)
specificity = tn / (tn + fp)
print(sensitivity, specificity)
