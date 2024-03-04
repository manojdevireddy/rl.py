# -*- coding: utf-8 -*-
"""rl exp9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/123R4s6DaIauI6Ioq8osyn4LUmibFklae
"""

import numpy as np

# Define the grid world
n_rows, n_cols = 6, 4

# Define actions (up, down, left, right)
actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the state values
state_values = np.zeros((n_rows, n_cols))

# Simulated reward function (example)
rewards = np.zeros((n_rows, n_cols))
rewards[5, 3] = 1  # Maximum Reward

# Discount factor
gamma = 0.9

# Q-Learning: Update state values using exploitation
num_iterations = 100

for _ in range(num_iterations):
    new_state_values = np.copy(state_values)
    for i in range(n_rows):
        for j in range(n_cols):
            if rewards[i, j] != 0:
                continue
            q_values = []
            for action in actions:
                next_i, next_j = i + action[0], j + action[1]
                if 0 <= next_i < n_rows and 0 <= next_j < n_cols:
                    q_values.append(state_values[next_i, next_j])
            if q_values:
                new_state_values[i, j] = max(q_values) * gamma
    state_values = new_state_values

# Display the state values with exploitation
print(state_values)