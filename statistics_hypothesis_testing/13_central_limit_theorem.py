# Samples of the uniform distribution will average out to a normal distribution.

import random

import plotly.express as px

sample_size = 30
sample_count = 1000

# Central limit theorem, 1000 samples each with 30 random numbers between 0.0 and 1.0 
x_values = [(sum([random.uniform(0.0, 1.0) for i in range(sample_size)]) / sample_size) for _ in range(sample_count)]
y_values = [1 for _ in range(sample_count)]

px.histogram(x=x_values, y = y_values, nbins=20).show()
