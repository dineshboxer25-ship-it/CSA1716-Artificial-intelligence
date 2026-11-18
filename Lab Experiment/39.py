# Principal Component Analysis (PCA)

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

print("Original Dataset Shape:", X.shape)

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

print("Reduced Dataset Shape:", X_pca.shape)

# Explained variance
print("Explained Variance Ratio:",
      pca.explained_variance_ratio_)

# Plot PCA result
plt.figure(figsize=(8, 6))

for i in range(3):
    plt.scatter(
        X_pca[y == i, 0],
        X_pca[y == i, 1],
        label=iris.target_names[i]
    )

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA - Dimensionality Reduction")
plt.legend()
plt.grid()
plt.show()
