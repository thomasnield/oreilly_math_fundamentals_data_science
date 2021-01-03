from numpy import array

i_hat = array([1, 2])
j_hat = array([-4, -1])

basis = array([i_hat, j_hat]).transpose()

v = array([1,1])

w = basis.dot(v)

print(w)
