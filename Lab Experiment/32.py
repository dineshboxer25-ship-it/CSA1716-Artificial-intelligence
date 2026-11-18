import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create Dataset
data = {
    'Study_Hours': [1, 2, 3, 4, 5, 6, 7, 8],
    'Marks': [20, 30, 40, 50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)

# Separate Input and Output
X = df[['Study_Hours']]
y = df['Marks']

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Training Completed")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Prediction
y_pred = model.predict(X_test)

print("\nActual Marks:", list(y_test))
print("Predicted Marks:", y_pred)

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error:", mse)
print("R2 Score:", r2)

# Visualization
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red',
         label='Regression Line')

plt.xlabel('Study Hours')
plt.ylabel('Student Marks')
plt.title('Linear Regression')
plt.legend()
plt.grid()
plt.show()

# New Prediction
hours = pd.DataFrame({'Study_Hours': [9]})
prediction = model.predict(hours)

print("\nPredicted Marks for 9 Hours:",
      prediction[0])
