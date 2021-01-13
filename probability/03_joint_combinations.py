# Declare possible outcomes for coin and die
coin_outcomes = ["H", "T"]
die_outcomes = [1, 2, 3, 4, 5, 6]

# Combine each outcome between coin and die 
all_combinations = [(c,d) for c in coin_outcomes for d in die_outcomes]

# Find only outcomes for Heads and 6 (should only be one)
head_and_6 = [t for t in all_combinations if t[0] == "H" and t[1] == 6]

# 1/12 = .083333
print(float(len(head_and_6)) / float(len(all_combinations)))
