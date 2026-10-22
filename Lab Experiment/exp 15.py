
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the decision tree
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Calculate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", round(accuracy, 4))

# Display decision tree rules
print("\nDecision tree rules:")
print(export_text(model, feature_names=list(iris.feature_names)))

# Predict a sample
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)[0]

print("\nPrediction for", sample[0], "->", iris.target_names[prediction])

