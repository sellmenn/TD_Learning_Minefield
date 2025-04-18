from random import randint

class Field:
    def __init__(self, length = 10, mines = 20, goals = [(9, 9)], terminal = [])-> None:
        self.length = length
        self.num_mines = mines
        self.goals = goals
        self.map, self.mines = self.create_field()
        self.states = self.get_states()
        self.terminal = terminal + self.goals + self.mines

    # Return a map of the minefield as a str object
    def __repr__(self):
        field = self.map
        field_str = str()
        length = self.length
        for i in range(length):
            for j in range(length):
                if (i,j) not in self.goals:
                    field_str += f" {str(field[i][j])} "
                else:
                    field_str += " G "
            field_str += "\n"
        return field_str

    # Create and return a tuple of a map of the minefield, with randomly planted mines, as a list, and a list of coordinates of planted mines
    def create_field(self) -> list:
        field = []
        length = self.length
        for i in range(length):
            field.append(list())
            for j in range(length):
                field[i].append(0)
        mines = []
        mine_count = 0
        while mine_count < self.num_mines:
            x, y = randint(0, length - 1), randint(0, length - 1)
            if (x, y) not in mines and (x,y) not in self.goals:
                field[x][y] = "X"
                mines.append((x, y))
            mine_count += 1
        return field, mines
    
    # Returns a list of all states excluding those in exc
    def get_states(self, exc=[]):
        states = []
        for i in range(self.length):
            for j in range(self.length):
                if (i,j) not in exc:
                    states.append((i,j))
        return states