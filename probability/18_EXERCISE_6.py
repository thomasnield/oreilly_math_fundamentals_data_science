"""
You have 137 passengers booked on a full flight from Las Vegas to Dallas. 

However it is Las Vegas on a Sunday morning and you estimate each passenger is 40% likely to not show up. 

You are trying to figure out how many seats to overbook so the plane does not fly empty. 

How likely is it 50 or more passengers will not show up? 

Complete the code below.
"""
from scipy.stats import binom

n = 137
p = .40

p_50_or_more_noshows = 0.0

for x in range(?,?):
    p_50_or_more_noshows += binom.pmf(x, ?, ?)

print(p_50_or_more_noshows)
