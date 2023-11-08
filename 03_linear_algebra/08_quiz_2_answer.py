from numpy import array

i_hat = array([-2, 1])
j_hat = array([1, -2])

basis = array([i_hat, j_hat]).transpose()

v = array([1,2])

w = basis.dot(v)

print(w)
