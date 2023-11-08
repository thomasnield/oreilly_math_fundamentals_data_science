"""
Below we have some predicted and actual values. 

Calculate the total loss as the sum of squares by 
completing the code below. 

Then execute the script by typing this command in the terminal:
python3 task1.py 
"""

predicted_vals = [6.67, 8.61, 10.55, 12.49, 14.43, 16.37]
actual_vals = [5, 10, 10, 15, 14, 15]

loss = 0.0

for predicted, actual in zip(actual_vals, predicted_vals):
    loss += ?

print(loss)
