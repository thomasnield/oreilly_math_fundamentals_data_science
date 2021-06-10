"""
You are provided with eigenvalues [0,7] 

and eigenvectors 
[[-0.9486833, -0.4472136],
 [0.31622777, -0.89442719]]

Rebuild the original matrix decomposed from these 
eigenvectors and eigenvalues. 
 
Complete the code below, then execute the script 
"""

from numpy import array, diag

eigenvals = array([0, 7])

eigenvecs = array(
    [[-0.9486833, -0.4472136],
     [0.31622777, -0.89442719]]
)

# Rebuild matrix from eigenvectors and eigenvalues
Q = eigenvecs
R = ?

L = diag(eigenvals)
B = ?

print(B)
