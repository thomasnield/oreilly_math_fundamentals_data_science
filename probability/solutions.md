# Solutions - Probability


## Task 1

On line 21, calculate the joint probability by multiplying the two probabilities. 

```
p_rain_and_umbrella_on_time = p_rain * p_umbrella_on_time
```


## Task 2

On line 17, the probability of no rain is calculated by subtracting the probability of rain from 1.0. 

```
p_no_rain = 1.0 - p_rain
```

On line 19, the probability of no rain or umbrella arrives is going to add the two probabilities and then subtract their joint probabilities. 

```
p_no_rain_or_umbrella_on_time = p_no_rain + p_umbrella_on_time - (p_no_rain * p_umbrella_on_time)
```

### Task 3

On line 20, use the conditional probability for your joint probability.  

```
p_rain_and_umbrella_on_time = p_rain * p_umbrella_on_time_given_rain
```


## Task 4

On line 29, use Bayes Theorem to account for population that actually has the disease into your conditonal probability. 

```
p_true_positive_population = p_true_positive * p_at_risk / p_positive
```

## Task 5

On line 18, get the area between .5 and 1.0 for the beta distribution CDF. 

```
p = 1.0 - beta.cdf(.5, heads, tails)
```

## Task 6

On line 21, modify the range so you iterate the 50th to 137th passenger. 

```
for x in range(50,138):
```

On line 22,  provide the `n` and `p` arguments to the binomial distribution. 

```
p_50_or_more_noshows += binom.pmf(x, n, p)
```
