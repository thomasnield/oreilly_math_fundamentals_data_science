"""
We want to use a logistic regression to recommend 
a light font (0) or dark font (1) given a color background 
expressed as 3 RGB values (red, green, and blue). 

A dataset of background colors and the recommended light/dark 
font indicator is provided here: 
https://bit.ly/30ngND7

Complete the code below to perform a logistic regression. 

Use 2/3 of the data for training and 1/3 for testing, and 
use a random_state of 10 for the split.

Output the accuracy for the testing data. 

Then execute the script by typing this command in the terminal:
python3 task2.py 
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load the data
df = pd.read_csv('https://bit.ly/30ngND7', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

X_train, X_test, Y_train, Y_test = ?

# Perform logistic regression
model = LogisticRegression(solver='liblinear')
model.fit(?, ?)

result = model.score(?, ?)

print(result)
