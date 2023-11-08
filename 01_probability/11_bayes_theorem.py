# Flip a conditional probability using Bayes Theorem

p_color_blind = .0425
p_male = .50
p_color_blind_given_male = .08

p_male_given_color_blind = p_color_blind_given_male * p_male / p_color_blind

# 0.9411764705882353
print(p_male_given_color_blind)
