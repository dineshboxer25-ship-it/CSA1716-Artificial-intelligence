# Genetic Algorithm for Neural Network XOR

import numpy as np
import random

# XOR dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 0])

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -50, 50)))

# Neural network prediction
def predict(weights, inputs):

    W1 = weights[:6].reshape(2, 3)
    b1 = weights[6:9]

    W2 = weights[9:12].reshape(3, 1)
    b2 = weights[12]

    hidden = sigmoid(inputs @ W1 + b1)

    output = sigmoid(hidden @ W2 + b2)

    return output.flatten()

# Fitness function
def fitness(weights):

    predictions = predict(weights, X)

    error = np.mean((predictions - y) ** 2)

    return 1 / (1 + error)

# Initial population
population = [
    np.random.uniform(-2, 2, 13)
    for i in range(20)
]

# Genetic algorithm
for generation in range(100):

    population.sort(
        key=fitness,
        reverse=True
    )

    new_population = population[:2]

    while len(new_population) < 20:

        parent1 = random.choice(population[:10])
        parent2 = random.choice(population[:10])

        # Crossover
        child = (parent1 + parent2) / 2

        # Mutation
        child += np.random.normal(0, 0.1, 13)

        new_population.append(child)

    population = new_population

# Best neural network
best = max(population, key=fitness)

predictions = predict(best, X)

print("Genetic Algorithm Training Completed")

print("\nXOR Predictions:")

for i in range(len(X)):
    print(
        X[i],
        "Predicted:",
        round(predictions[i], 3),
        "Actual:",
        y[i]
    )

print("\nBest Fitness:", fitness(best))
