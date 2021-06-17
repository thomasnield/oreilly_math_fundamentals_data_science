import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load the data
df = pd.read_csv('https://bit.ly/30ngND7', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)\
Y = df.values[:, -1]

model = LogisticRegression(solver='liblinear')
model.fit(X, Y)

# Interact and test with new employee data
def predict_light_dark_font(red, green, blue):

    # We are only testing one sample, so we just grab the first row and the second element (the true probability)
    probability_of_dark = model.predict_proba(np.array([red, green, blue]).reshape(1, -1))[0][1]
    if probability_of_dark >= .5:
        return "DARK FONT RECOMMENDED, {0}% probability of dark".format(round(probability_of_dark * 100.0, 2))
    else:
        return "LIGHT FONT RECOMMENDED, {0}% probability of dark".format(round(probability_of_dark * 100.0, 2))


while True:
    n = input("Predict light or dark font for a given background color: {red},{green},{blue}: ")
    (red, green, blue) = n.split(",")
    print(predict_light_dark_font(int(red), int(green), int(blue)))
