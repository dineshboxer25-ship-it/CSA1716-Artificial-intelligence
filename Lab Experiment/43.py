# Reinforcement Learning using Q-Learning

import numpy as np
import random

# Environment: 4 states and 2 actions
# Action 0 = Left, Action 1 = Right

Q = np.zeros((4, 2))

learning_rate = 0.8
discount_factor = 0.9
episodes = 100

for episode in range(episodes):

    state = 0

    while state != 3:

        # Choose action
        if random.random() < 0.2:
            action = random.randint(0, 1)
        else:
            action = np.argmax(Q[state])

        # Move to next state
        if action == 1:
            next_state = min(state + 1, 3)
        else:
            next_state = max(state - 1, 0)

        # Reward
        if next_state == 3:
            reward = 10
        else:
            reward = -1

        # Update Q-value
        Q[state, action] += learning_rate * (
            reward +
            discount_factor * np.max(Q[next_state])
            - Q[state, action]
        )

        state = next_state

print("Q-Learning Training Completed")

print("\nQ-Table:")
print(Q)

print("\nBest Actions:")

for state in range(3):
    print("State", state, "Action", np.argmax(Q[state]))
