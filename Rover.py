DIRECTIONS = "NESW"
SHIFTS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
TURNS = "LR"


class Rover(object):
    def __init__(self, x, y, direction, planet):
        """
        Initialize a rover
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.planet = planet

    def forward(self):
        self.x += SHIFTS[DIRECTIONS.index(self.direction)][0]
        self.y += SHIFTS[DIRECTIONS.index(self.direction)][1]

    def turn(self, turn):
        if turn == 'L':
            self.direction = DIRECTIONS[(
                DIRECTIONS.index(self.direction) - 1 + 4) % 4]
        if turn == 'R':
            self.direction = DIRECTIONS[(
                DIRECTIONS.index(self.direction) + 1) % 4]

    def execute(self, commands):
        for command in commands:
            if command in TURNS:
                self.turn(command)
            else:
                self.forward()
        self.lost = self.x > self.planet.x or self.y > self.planet.y
        print(self.x, self.y, self.direction, "Lost" if self.lost else "")

    def get_position(self):
        return (self.x, self.y)
