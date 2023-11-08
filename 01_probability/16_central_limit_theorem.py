# Samples of the uniform distribution will average out to a normal distribution.

import random

import plotly.express as px

# Central limit theorem, 1000 samples each with 1000 random numbers between 0.0 and 1.0 
x_values = [(sum([random.uniform(0.0, 1.0) for i in range(1000)]) / 1000.0) for _ in range(1000)]
y_values = [1 for _ in range(1000)]

px.histogram(x=x_values, y = y_values, nbins=20).show()
