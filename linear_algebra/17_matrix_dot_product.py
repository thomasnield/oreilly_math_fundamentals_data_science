from numpy import array, dot

i_hat = array([-1, 2])
j_hat = array([3, 1])

basis = array([i_hat, j_hat]).transpose()

v = array([1, 1])

dot_product = basis.dot(v)

print(dot_product) # prints [2, 3]
