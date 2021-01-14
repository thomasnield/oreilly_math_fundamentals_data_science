# Probability of being male and colorblind
# Use conditonal probability if it is available and applies to condition

p_male = .50
p_colorblind = .0425
p_colorblind_given_male = .08

p_male_and_colorblind = p_male * p_colorblind_given_male

print(p_male_and_colorblind)
