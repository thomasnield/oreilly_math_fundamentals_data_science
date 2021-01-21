from math import sqrt
from scipy.stats import t

def t_test(sample_mean, sample_std, pop_mean, n):
    return (sample_mean - pop_mean) / (sample_std / sqrt(n))

sample_mean = 64.7
sample_std = 3.17
pop_mean = 65.5
n = 25

# -1.7108820799094282
decision_t = t.ppf(.05, df=n-1)

# -1.261829652996841
t_value = t_test(sample_mean,sample_std,pop_mean, n)

print("DECISION T: {}".format(decision_t))
print("TEST T: {}".format(t_value))

# FAILED TO REJECT H0
if decision_t <= t_value:
    print("REJECT H0")
else:
    print("FAILED TO REJECT H0")
