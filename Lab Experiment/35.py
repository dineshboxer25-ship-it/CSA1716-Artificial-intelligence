# Decision Tree Classification

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Display results
print("Decision Tree Classification")
print("Actual Values:", y_test)
print("Predicted Values:", y_pred)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy * 100, "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred,
                            target_names=iris.target_names))

# Predict new sample
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)

print("New Sample Prediction:",
      iris.target_names[prediction[0]])
