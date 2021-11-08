import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression

# Load the data
df = pd.read_csv('https://bit.ly/33ebs2R', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)\
Y = df.values[:, -1]

model = LogisticRegression(solver='liblinear')
model.fit(X, Y)

# Predict a new "y" value for x = 3.5
print("x = 3.5, y = {0}".format(model.predict([[3.5]]).flatten()))

# Plot results
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["x"], y = df["y"], mode='markers', name="Observations"))
fig.add_trace(go.Scatter(x=np.arange(0.0,10.0,.1),
                         y= model.predict_proba(np.arange(0.0,10.0,.1).reshape(-1, 1))[:,-1],
                         mode='lines',
                         name='Logistic Regression'))
fig.show()
