# K-Means Clustering

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Dataset
X = [
    [2, 3], [3, 3], [3, 4],
    [8, 8], [9, 8], [8, 9],
    [1, 2], [9, 9]
]

# Create K-Means model
model = KMeans(n_clusters=2, random_state=42, n_init=10)

# Train model
model.fit(X)

# Get cluster labels
labels = model.labels_

print("K-Means Clustering Results")

for i in range(len(X)):
    print("Data:", X[i], "Cluster:", labels[i])

print("\nCluster Centers:")
print(model.cluster_centers_)

# Plot clusters
plt.scatter(
    [p[0] for p in X],
    [p[1] for p in X],
    c=labels
)

plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    marker='X',
    s=200
)

plt.title("K-Means Clustering")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
