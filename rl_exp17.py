# -*- coding: utf-8 -*-
"""rl exp17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10V8FRGHNnLJJ-Bnon82jk3ba46udmCgW
"""

import numpy as np

# Define environment
num_states = 10
num_actions = 2
reward_matrix = np.random.rand(num_states, num_actions)

# Define parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Epsilon-greedy exploration parameter
num_episodes = 1000

class Train:
    def __init__(self, name, algorithm):
        self.name = name
        self.algorithm = algorithm
        self.Q = np.zeros((num_states, num_actions))
        self.total_reward = 0

    def choose_action(self, state):
        if np.random.rand() < epsilon:
            return np.random.choice(num_actions)
        else:
            return np.argmax(self.Q[state])

    def update_Q(self, state, action, reward, next_state=None, next_action=None):
        if self.algorithm == 'TD(0)':
            self.Q[state, action] += alpha * (reward + gamma * np.max(self.Q[next_state]) - self.Q[state, action])
        elif self.algorithm == 'SARSA':
            self.Q[state, action] += alpha * (reward + gamma * self.Q[next_state, next_action] - self.Q[state, action])
        elif self.algorithm == 'Q-Learning':
            self.Q[state, action] += alpha * (reward + gamma * np.max(self.Q[next_state]) - self.Q[state, action])

    def train(self):
        state = 0
        for _ in range(num_episodes):
            action = self.choose_action(state)
            next_state = np.random.choice(num_states)
            next_action = self.choose_action(next_state)
            reward = reward_matrix[state, action]
            self.update_Q(state, action, reward, next_state, next_action)
            self.total_reward += reward
            state = next_state

# Run simulations
trains = [
    Train('Train A', 'TD(0)'),
    Train('Train B', 'SARSA'),
    Train('Train C', 'Q-Learning')
]

for train in trains:
    train.train()
    print(f"{train.name} total reward: {train.total_reward}")