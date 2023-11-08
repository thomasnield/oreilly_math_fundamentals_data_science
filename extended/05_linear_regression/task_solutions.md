# Solutions - Linear Regression

## Task 1

On line 18, calculate the difference between the actual and predicted value, square it, and add it to the loss sum. 

```
loss += (predicted - actual)**2
```

## Task 2

For line 19, you can use the `r2_score` function from sklearn. 

```
from sklearn.metrics import r2_score
r_square = r2_score(y_test, [slope*x + y_intercept for x in x_test])
```

If done from scratch, there will be many more lines. 

```
y_test_avg = sum(y_test) / len(y_test)
# 17.25

y_test_predict = [(slope * x) + y_intercept for x in x_test]

sum_sq_regression = sum((y_test[i] - y_test_predict[i])**2 for i in range(0,len(y_test)))
sum_sq_total = sum((y_test[i] - y_test_avg)**2 for i in range(0,len(y_test)))

r_square = 1.0 - sum_sq_regression / sum_sq_total
```

## Task 3 

On line 28, do a train-test split by 1/3 proportion. Don't forget the random state. 

```
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test =  train_test_split(X, Y, test_size=1.0/3.0, random_state=42)
```

On line 32, fit using the training data. 

```
model.fit(X_train, Y_train)
```

On line 33, test using the testing data. 

```
result = model.score(X_test, Y_test)
```

## Task 4

Note this problem will take a moment to run.

On line 30, use a small enough learning rate. 

```
L = .0001 
```

On line 31, make a sufficient number of iterations. 

```
epochs = 120_000
```

Finally, perform gradient descent on `m` and `b` starting on line 40. 

```
m = m - D_m*L  # Update m
b = b - D_b*L  # Update b
```
