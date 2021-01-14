p_rain = .30
p_umbrella_on_time = .40
p_umbrella_on_time_given_rain = .20

# Probability of it raining and umbrella arriving on time 
p_rain_and_umbrella_on_time = p_rain * p_umbrella_on_time_given_rain

print(p_rain_and_umbrella_on_time)
