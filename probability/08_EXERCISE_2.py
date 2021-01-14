# Probability of no rain or umbrella arrives on time 
p_rain = .30
p_no_rain = 1.0 - p_rain
p_umbrella_on_time = .40

p_no_rain_or_umbrella_on_time = p_no_rain + p_umbrella_on_time - (p_no_rain * p_umbrella_on_time)

# 0.82
print(p_no_rain_or_umbrella_on_time)
