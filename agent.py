from field import Field

class Agent:

    directions = ["↑", "↓", "←", "→"]
    delta_x = [-1, 1, 0, 0]
    delta_y = [0, 0, -1, 1]

    def __init__(self, field = Field()) -> None:
        self.position = (0, 0)
        self.goal = field.goal
        self.field = field

    # Move agent to coordinate
    def set_position(self, coordinate) -> None:
        self.position = coordinate
    
    # Get next state without moving agent
    def next_state(self, direction):
        x, y = self.position
        return (x + self.delta_x[direction], y + self.delta_y[direction])

