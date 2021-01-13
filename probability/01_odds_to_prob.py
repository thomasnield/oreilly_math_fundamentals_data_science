def prob_to_odds(p):
  return p / (1.0 - p)
  
def odds_to_prob(o):
  return o / (1.0 + o)


p_x = .75
o_x = prob_to_odds(p_x)

# prints ODDS: 3.0
print("ODDS: {}".format(o_x))
