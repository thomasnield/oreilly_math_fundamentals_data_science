from numpy import array

i_hat = array([2, 0])
j_hat = array([0, 1.5])

basis = array([i_hat, j_hat]).transpose()

v = array([1,2])

w = basis.dot(v)

print(w)
