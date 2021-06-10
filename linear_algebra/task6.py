"""
You are provided with eigenvalues [0,7] 

and eigenvectors 
[[-0.9486833, -0.4472136],
 [0.31622777, -0.89442719]]

Rebuild the original matrix decomposed from these 
eigenvectors and eigenvalues. 
 
Complete the code below, then execute the script by 
typing this command in the terminal:
python3 task6.py 
"""

from numpy import array, diag
from post_answer import submit

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
