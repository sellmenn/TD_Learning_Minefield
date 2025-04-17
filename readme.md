# Minefield Q-Learning Agent

This project implements a simple Q-learning agent that learns to navigate a 2D grid-based environment (the **Field**) while avoiding mines and reaching a designated goal.

## Overview

The project consists of three main components:

- `field.py`: Defines the environment, including mines, goal, and valid states.
- `agent.py`: Implements the agent's movement and interaction with the field.
- `solver.py`: Contains the Q-learning logic, including policy creation, training, and extraction of optimal policies.

The agent learns through trial and error using a reinforcement learning algorithm to reach a goal with the highest possible reward while avoiding obstacles (e.g., mines).

## Requirements

- Python 3.8+
- NumPy

Install dependencies via pip if needed:

```bash
pip install numpy
