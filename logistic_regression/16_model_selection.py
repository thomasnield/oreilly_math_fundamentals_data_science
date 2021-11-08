import pandas as pd
import plotly.graph_objects as go
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('https://bit.ly/3cManTi', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)\
Y = df.values[:, -1]

# prepare models
models = []
models.append(('Logistic Regression', LogisticRegression(solver='liblinear')))
models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))
models.append(('K-neighbors', KNeighborsClassifier()))
models.append(('Decision Tree', DecisionTreeClassifier()))
models.append(('Naive Bayes', GaussianNB()))

# evaluate each model in turn
results = []
names = []


for name, model in models:
    kfold = KFold(n_splits=10, random_state=7, shuffle=True)
    cv_results = cross_val_score(model, X, Y, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    msg = "%s: mean=%f std=%f" % (name, cv_results.mean(), cv_results.std())
    print(msg)

# Plot results in box plots
fig = go.Figure()

for index,result in enumerate(results):
    fig.add_trace(go.Box(x=result, name = names[index]))

fig.show()