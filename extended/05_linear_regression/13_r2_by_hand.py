# Calculating R-square from scratch

slope = 1.73333333
y_intercept = 5.49999999999999

x_test = [9, 3, 6, 7]
y_test = [25, 10, 15, 19]

y_test_avg = sum(y_test) / len(y_test)
# 17.25

y_test_predict = [(slope * x) + y_intercept for x in x_test]
# [21.099999969999992, 10.699999989999991, 15.89999997999999, 17.63333330999999]

sum_sq_regression = sum((y_test[i] - y_test_predict[i])**2 for i in range(0,len(y_test)))
sum_sq_total = sum((y_test[i] - y_test_avg)**2 for i in range(0,len(y_test)))

r_square = 1.0 - sum_sq_regression / sum_sq_total
# 0.8478030805337009

print(r_square)
