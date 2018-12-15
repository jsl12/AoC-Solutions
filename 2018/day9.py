import re
import numpy as np
from itertools import cycle

class Game:
    REGEX = re.compile('(\d+) players; last marble is worth (\d+) points')

    def __repr__(self):
        return 'Circle: {}'.format(' '.join([str(m) for m in self.circle]))

    def __init__(self, input):
        match = self.REGEX.match(input)
        self.player_count = int(match.group(1))
        self.last_marble = int(match.group(2))
        self.players = cycle(range(self.player_count))

        self.scores = np.zeros(self.player_count, dtype=np.int32)
        self._circle = np.zeros(self.last_marble, dtype=np.int32)
        self.size = 1
        self.marble = 1
        self.current_marble = 1

    @property
    def circle(self):
        return self._circle[:self.size]

    def insert(self, position, marble_val):
        self.size += 1
        if position >= self.size:
            position = 1
        self.circle[position+1:] = self.circle[position:-1]
        self.circle[position] = marble_val
        return position

    def take_turn(self):
        self.current_marble = self.insert(self.current_marble+2, self.marble)
        self.marble += 1

        next(self.players)

def part1(input):
    g = Game(input)
    # n=10
    # vals = [0, 8, 4, 9, 2, 5, 1, 6, 3, 7]
    # g.size = len(vals)
    # g.circle[:len(vals)] = vals
    # g.current_marble = 3
    # g.insert(5, 10)
    while g.marble < g.last_marble:
        g.take_turn()
    return

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 9
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))