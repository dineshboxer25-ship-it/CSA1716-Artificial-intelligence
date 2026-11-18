# Recommendation System using Collaborative Filtering

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# User-Item Rating Dataset
data = {
    'Movie1': [5, 4, 0, 1],
    'Movie2': [4, 5, 0, 2],
    'Movie3': [1, 0, 5, 4],
    'Movie4': [0, 1, 4, 5]
}

users = ['User1', 'User2', 'User3', 'User4']

# Create DataFrame
df = pd.DataFrame(data, index=users)

print("User-Item Rating Matrix:")
print(df)

# Calculate user similarity
similarity = cosine_similarity(df)

similarity_df = pd.DataFrame(
    similarity,
    index=users,
    columns=users
)

print("\nUser Similarity Matrix:")
print(similarity_df.round(2))

# Select user
target_user = 'User1'

# Find most similar user
similar_users = similarity_df[target_user].drop(target_user)

best_user = similar_users.idxmax()

print("\nSelected User:", target_user)
print("Most Similar User:", best_user)

# Recommend movies not rated by target user
recommendations = df.loc[best_user][df.loc[target_user] == 0]

print("\nRecommended Movies:")

if len(recommendations) > 0:
    for movie in recommendations.index:
        print(movie)
else:
    print("No new recommendations available.")
