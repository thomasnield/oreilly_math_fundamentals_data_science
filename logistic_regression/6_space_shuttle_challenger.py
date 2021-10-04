import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression

# Load the data
df = pd.read_csv("https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/classification/space_shuttle_challenger_complete.csv", delimiter=",")

# Duplicate and convert records to have binary outcomes
df = df.loc[df.index.repeat(df["o_ring_failures"])].append(df[df["o_ring_failures"] == 0])
df.loc[(df["o_ring_failures"] > 0), 'o_ring_failures'] = 1


# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)\
Y = df.values[:, -1]


model = LogisticRegression()
model.fit(X, Y)

# Print "m" and "b" coefficients
print("m = {0}".format(model.coef_.flatten()))
print("b = {0}".format(model.intercept_.flatten()))

# Plot results
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["temperature"], y = df["o_ring_failures"], mode='markers', name="Observations"))
fig.add_trace(go.Scatter(x=np.arange(0.0,90.0,.1),
                         y= model.predict_proba(np.arange(0.0,90.0,.1).reshape(-1, 1))[:,-1],
                         mode='lines',
                         name='Logistic Regression'))
fig.show()