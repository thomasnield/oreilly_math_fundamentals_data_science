import pandas as pd

# Don't limit display of rows or columns
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

# Set every variable against every other variable to see its correlation
# A correlation of 1.0 indicates a perfect positive correlation
# A correlation of -1.0 indicates a perfect negative correlation
df = pd.read_csv('https://bit.ly/33iTfS9')
df['PROMOTION_RATE'] = df['YEARS_EMPLOYED'] / df['PROMOTIONS']

correlations = df.corr(method='pearson')

print(correlations)