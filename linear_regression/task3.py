"""
A dataset of red wine quality data is stored here, 
where the last column is a quality score: 
https://bit.ly/2Xov2ph

Perform a linear regression by completing the code below 
using a train-test split of 2/3 and 1/3 respectively, 
using a random_state of 42 for the split. 

Print the R2 score (rounded to 2 decimal places).

Then execute the script by typing this command in the terminal:
python3 task3.py  
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('https://bit.ly/2QhRLDk')

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

X_train, X_test, Y_train, Y_test = ?

# Perform a simple linear regression
model = LinearRegression()
model.fit(?, ?)
result = model.score(?, ?)

print(result)
