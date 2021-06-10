"""
Transform vector v with a basis vectors i-hat and j-hat. 

Vector v is [5, 2] but then is transformed in space. 

After this transformation i-hat moves from [1, 0] and lands at [3, 1]. 
j-hat moves from [0, 1] and lands at [4, 2]

Where does vector v land after this transformation?
 
Complete the code below, then execute the script
"""

from numpy import array

v = array([5,2])

i_hat = array([3, 1])
j_hat = array([4, 2])

# fix this line 
basis = array([i_hat, j_hat]) 

# transform vector v into w 
w = ?

print(w)
