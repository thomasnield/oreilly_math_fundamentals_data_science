# Solutions - Calculus Fundamentals

## Task 1

On line 31, make a step that is small enough of at most .0000001. 

```
slope_at_2 = approximate_slope_x(my_function, 2, .0000001)
```

## Task 2

On line 32, express the specified function in the problem: 

```
return .5 * x**2
```

On line 35, approximate the integral between 0 and 2. 1000 rectangles or more is sufficient. 

```
area = approximate_integral(lower=0, upper=2, n=1000, f=my_function)
```

## Task 3 

On line 29, make the learning rate sufficiently small. 

```
L = .001 # The learning rate
```

On line 30, use a sufficient number of iterations. 

```
epochs = 100_000  
```

On line 36, perform gradient descent for each iteration.  

```
x = x - d_x*L  # perform gradient descent here
```

## Task 4

On line 37, make a sufficiently small learning rate. 

```
L = .001
```

On line 38, use a sufficient number of iterations. 

```
epochs = 100_000 
```

On lines 49-52, perform gradient descent on the three variables. 

```
x = x - d_x*L  # update x
y = y - d_y*L  # update y
z = z - d_z*L  # update z
```