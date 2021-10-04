"""
Below we perform a logistic regression on employee retention data.

The training data can be found here, and the last column is an indicator
where the employee will leave (1) or not leave (0). 
https://bit.ly/32fPYS8

Complete the code below to perform a logistic regression using 2/3 of the data for training, 
and 1/3 of the data for testing.

Then evaluate against the testing data using a confusion matrix
showing true postives, false positives, true negatives, and false negatives. 

Finally, use the confusion matrix to calculate sensitivity and specificity. 

Then execute the script by typing this command in the terminal:
python3 task3.py 
"""

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
X_train, X_test, Y_train, Y_test = train_test_split(?, ?, test_size=?, random_state=10)

model = LogisticRegression(solver='liblinear')
y_predict = model.fit(?, ?)

# Create confusion matrix
y_true = Y_test
y_predict = ?
tn, fp, fn, tp = confusion_matrix(?, ?).ravel()

# Calculate and print sensitivity and specificity
sensitivity = ?
specificity = ?

print("{0} {1}".format(round(sensitivity, 3), round(specificity, 3)))
