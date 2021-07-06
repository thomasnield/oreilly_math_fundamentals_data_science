# Solutions - Logistic Regression

## Task 1

At line 28, you'll need to calculate the joint probability of true and false cases to find total likelihood. 

```
total_likelihood = 1.0

for input, output in zip(inputs, outputs): 
    total_likelihood *= logistic_function(input) if output == 1.0 else 1.0 - logistic_function(input) 
```
Alternatively you can use logarithmic addition to avoid floating point underflow, but in this case it should yield the same answer: 

```
total_likelihood = 0.0

for input, output in zip(inputs, outputs):
    total_likelihood += math.log(logistic_function(input)) if output == 1.0 else math.log(1.0 - logistic_function(input))

total_likelihood = math.exp(total_likelihood)
```

## Task 2

On line 34, do a train-test split using random state 10 by a proportion of 1/3. 

```
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.33, random_state=10)
```

On line 38, fit using the training data. 

```
model.fit(X_train, Y_train)
```

On line 40, score using the testing data. 

```
result = model.score(X_test, Y_test)
```

## Task 3

On line 30, do a train/test split using random state 10. 

```
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1.0/3.0, random_state=10)
```

On line 39, do a fit with the training data. 

```
y_predict = model.fit(X_train, Y_train)
```

On line 43, create predicted Y values. 

```
y_predict = model.predict(X_test) 
```

On line 44, extract the confusion matrix counts. 

```
tn, fp, fn, tp = confusion_matrix(y_true, y_predict).ravel()
```

Finally on line 47 and 48, calculate specificity and sensitivity. 

```
sensitivity = tp / (tp + fn)
specificity = tn / (fp + tn)
```
