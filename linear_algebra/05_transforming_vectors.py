from numpy import array

i_hat = array([-.25, 0])
j_hat = array([0, -1])

basis = array([i_hat, j_hat]).transpose()

v = array([4,2])

w = basis.dot(v)

print(w)
