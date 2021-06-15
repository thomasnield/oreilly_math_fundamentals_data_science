# Solutions - Linear Algebra

## Task 1

On line 14, provide the vector as a collection. 

```
data = [2,4,1]
```

## Task 2

On line 23, scale and add the two vectors. 

```
scaled_a_plus_scaled_b = 3*a + 2*b
```

## Task 3

On line 25, transpose the vector. 

```
basis = array([i_hat, j_hat]).transpose()
```

On line 28, use the dot operation to transform vector v with the basis vector. 

```
w = basis.dot(v) 
```

## Task 4

On line 19, declare the basis vectors into a packaged matrix. 

```
basis = array([i_hat, j_hat]).transpose()
```

On line 21, calculate the determinant. 

```
from numpy.linalg import det
determinant = det(basis)
```


## Task 5

Starting at line 19, express the system of equations in matrix form. 

```
A = array([
    [3, 1, 0],
    [2, 4, 1],
    [3, 1, 8]
])
```

At line 23, express the right-hand values. 

```
B = array([
    54,
    12,
    6
])
```

On line 27, calculate the missing values using the inverse matrix and dot product functions. 

```
X = inv(A).dot(B)
```

Finally, do necessary imports. 

```
from numpy.linalg import inv 
```

### Task 6

On line 28, `R` is the inverse of `Q`. 

```
R = inv(Q) 
```

On line 38, reconstruct the original matrix from the eigendecomposition artifacts. 

```
B = Q.dot(L).dot(R)
```

Finally, do necessary imports. 

```
from numpy.linalg import inv 
```

