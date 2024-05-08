# Solutions - Statistics and Hypothesis Testing

## Task 1 

Correct line 18 to subtract 1 from the denominator. 

```
var = sum((v - mean) ** 2 for v in values) / (len(values) - 1)
```

## Task 2

Correct line 22 to subtract the area up to 20 from the area up to 30 in the normal CDF 

```
x = norm.cdf(30, mean, std_dev) - norm.cdf(20, mean, std_dev) 
```

## Task 3 

Correct line 19 to calculate the z-score for a given x-value. 

```
return (x - mean) /  std
```

Use the corrected function to calculate the pug's z-score on line 25. 

```
my_pug_zscore = x_to_z(my_pug_weight, mean, stdev)
```

## Task 4

On line 23, `dof` is `13 - 1 = 12`.  

```
t_dist = t(df=12)
```

On line 26, return the bounds for the lower and upper bounds of our critical Z range. 

```
return t_dist.ppf(left_area), t_dist.ppf(right_area)
```

On line 35, return the lower and upper confidence interval by adding to the sample mean. 

```
return sample_mean + lower_ci, sample_mean + upper_ci
```

## Task 5

On line 21, calculate the probability of achieving $10,345 or less

```
p1 = norm.cdf(10345, mean, std_dev)
```

on line 22, we can simply take advantage of symmetry to find the other p-value. 

```
p2 = p1
```

On line 25, the two-tailed p-value is the sum of both tails. 

```
p_value = p1 + p2
```
