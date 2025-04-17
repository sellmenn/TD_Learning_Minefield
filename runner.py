import numpy as np
from field import Field
from agent import Agent
from random import choice, choices, randint

LENGTH = 10 # Length of board
MINES = 20 # Number of mines to be randomly planted
GOAL = (9, 9) # Coordinate of goal state
REWARD = 10 # Reward for reaching goal state
PENALTY = -10 # Penalty for encountering mine
STEP_PENALTY = -1 # Penalty awarded at each step to encourage shorter paths
EXPLORATION_RATE = 0.2 # Probability of selecting random next-action
LEARNING_RATE = 0.3 # Rate of updating Q-value
DISCOUNT = 0.9 # Weight associated with future rewards
EPOCHS = 100000 # Training cycles

def main():
    # Create field with mines
    field = Field(length=LENGTH, mines=MINES, goal=GOAL)
    # Create agent object
    agent = Agent(field)
    # Create Utility Table
    q_table = create_Q_table(field, len(Agent.directions))
    # Print Actual Minefield
    print("\nHidden Minefield:")
    print(field)
    # Print expected utilities
    print("\nExpected Utilities:")
    print(flatten_q_table(q_table))
    # Print policy
    print("\nPolicy:")
    print(extract_policy(q_table, field))
    
def create_Q_table(field, num_actions):
    Q_table = np.zeros([field.length, field.length, num_actions]) # Initialise zeroed Q-table
    states = field.get_states() # Get all possible states
    agent = Agent(field) # Initialise agent
    for _ in range(EPOCHS):
        state = choice(states) # Randomly select a state
        agent.set_position(state) # Position agent at state
        new_state = (-1, -1) # Initialise with invalid state
        attempts = 0
        # Repeat until a valid new state is obtained, or attempt limit is reached
        while new_state not in field.states and attempts < 10:
            if choices([True, False], [EXPLORATION_RATE, 1-EXPLORATION_RATE])[0]: # Explore or exploit
                action = randint(0, len(Agent.directions)-1) # Select random action
            else:
                action = np.argmax(Q_table[state[0], state[1], :]) # Select action with greatest utility
            new_state = agent.next_state(action) # Get the new state associated with performing the action
            attempts += 1 
        if attempts > 9: 
            continue # Skip this iteration if unable to select a legal action
        new_q = max(Q_table[new_state[0], new_state[1], :]) # Obtain maximum possible utility from new state
        current_q = Q_table[state[0], state[1], action] 
        Q_table[state[0], state[1], action] += LEARNING_RATE * (get_reward(field, new_state) + DISCOUNT * new_q - current_q) # Temporal difference equation
    return Q_table

def extract_policy(Q_table, field):
    directions = Agent.directions
    for x in range(np.size(Q_table, 0)):
        for y in range(np.size(Q_table, 1)):
            if field.map[x][y] == 0:
                field.map[x][y] = directions[int(np.argmax(Q_table[x, y, :]))] # Replace all '0's with reccomended direction based on policy
    return field

def flatten_q_table(Q_table):
    np.set_printoptions(1) # Set np to 1 d.p.
    expected_utility = np.zeros([np.size(Q_table, 0), np.size(Q_table, 1)]) # Initialise zeroed 2D array
    for x in range(np.size(Q_table, 0)):
        for y in range(np.size(Q_table, 1)):
            expected_utility[x][y] = np.max(Q_table[x, y, :]) # Store maximimum utility
    return expected_utility
            
def get_reward(field, coordinate):
    if coordinate in field.mines:
        return PENALTY
    elif coordinate == GOAL:
        return REWARD
    else:
        return STEP_PENALTY

if __name__ == "__main__":
    main()