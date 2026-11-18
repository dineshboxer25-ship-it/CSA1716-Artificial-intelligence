# Markov Chain Model

import numpy as np

# States
states = ["Sunny", "Rainy"]

# Transition probability matrix
transition_matrix = np.array([
    [0.8, 0.2],
    [0.4, 0.6]
])

# Initial state
current_state = 0

print("Markov Chain Prediction")
print("Initial State:", states[current_state])

# Predict next 10 events
for i in range(10):

    current_state = np.random.choice(
        [0, 1],
        p=transition_matrix[current_state]
    )

    print("Step", i + 1, ":", states[current_state])
