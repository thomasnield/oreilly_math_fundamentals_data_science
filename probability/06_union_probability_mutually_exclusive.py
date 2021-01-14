# Probability of getting a "heads" or a "six"
# With a coin flip and die roll

p_heads = .50
p_six = 1.0 / 6.0

p_heads_or_six = p_heads + p_six - (p_heads * p_six)

# 0.5833333333333333
print(p_heads_or_six)
