
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the data
df = pd.read_csv('https://bit.ly/2SPJDuX', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.33, random_state=10)

# Perform logistic regression
model = LogisticRegression(solver='liblinear')
model.fit(X, Y)

result = model.score(X_test, Y_test)

print("MODEL SCORE: {}".format(result))

# Interact and test with new employee data
def predict(age, video_gamer, likes_ice_cream, minority):
    prediction = model.predict([[age, video_gamer, likes_ice_cream, minority]])
    if prediction == [[1]]:
        return "IS CRIMINAL: {0}".format(model.predict_proba([[age, video_gamer, likes_ice_cream, minority]])[0][1])
    else:
        return "IS NOT CRIMINAL: {0}".format(model.predict_proba([[age, video_gamer, likes_ice_cream, minority]])[0][1])


# Test a predictions
while True:
    n = input("Predict whether someone is a criminal {age},{video_gamer},{likes_ice_cream},{minority}: ")
    (age, video_gamer, likes_ice_cream, minority) = n.split(",")
    print(predict(int(age), int(video_gamer), int(likes_ice_cream), int(minority)))
