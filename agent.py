from field import Field

class Agent:

    directions = ["↑", "↓", "←", "→"]
    delta_x = [-1, 1, 0, 0]
    delta_y = [0, 0, -1, 1]

    def __init__(self, field = Field()) -> None:
        self.position = (0, 0)
        self.goals = field.goals
        self.field = field

    # Move agent to coordinate
    def set_position(self, coordinate) -> None:
        self.position = coordinate
    
    # Get next state without moving agent
    def next_state(self, direction):
        # If terminal state, simply return current position
        if self.position in self.field.terminal:
            return self.position
        x, y = self.position
        return (x + self.delta_x[direction], y + self.delta_y[direction])
    
    def is_terminal(self):
        if self.field.is_terminal(self.position):
            return True
        return False


