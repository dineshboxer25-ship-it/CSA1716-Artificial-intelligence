# Hyperparameter Tuning using GridSearchCV

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = RandomForestClassifier(random_state=42)

# Define parameters
parameters = {
    'n_estimators': [10, 50, 100],
    'max_depth': [2, 4, 6, None]
}

# Hyperparameter tuning
grid = GridSearchCV(
    model,
    parameters,
    cv=5,
    scoring='accuracy'
)

grid.fit(X_train, y_train)

# Best model
best_model = grid.best_estimator_

# Prediction
y_pred = best_model.predict(X_test)

# Results
print("Best Parameters:", grid.best_params_)

print("Best Cross-Validation Accuracy:",
      grid.best_score_ * 100, "%")

print("Test Accuracy:",
      accuracy_score(y_test, y_pred) * 100, "%")
