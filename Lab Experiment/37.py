# Genetic Algorithm for Function Optimization

import random

# Fitness function
def fitness(x):
    return x * x

# Initial population
population = [
    random.randint(0, 31) for i in range(6)
]

# Genetic Algorithm
for generation in range(20):

    # Sort population based on fitness
    population.sort(key=fitness, reverse=True)

    # Select best individuals
    parents = population[:3]

    # Create new population
    new_population = parents.copy()

    while len(new_population) < 6:

        parent1 = random.choice(parents)
        parent2 = random.choice(parents)

        # Crossover
        child = (parent1 + parent2) // 2

        # Mutation
        if random.random() < 0.2:
            child = random.randint(0, 31)

        new_population.append(child)

    population = new_population

    best = max(population, key=fitness)

    print("Generation:", generation + 1,
          "Best Solution:", best,
          "Fitness:", fitness(best))

# Final result
best_solution = max(population, key=fitness)

print("\nOptimal Solution:", best_solution)
print("Maximum Fitness:", fitness(best_solution))
