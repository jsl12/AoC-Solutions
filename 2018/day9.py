import re
import numpy as np
from itertools import cycle

class Game:
    REGEX = re.compile('(\d+) players; last marble is worth (\d+) points')

    def __repr__(self):
        return 'Circle: {}'.format(' '.join([str(m) for m in self.circle[:self.size]]))

    def __init__(self, input):
        match = self.REGEX.match(input)
        self.player_count = int(match.group(1))
        self.last_marble = int(match.group(2))
        self.players = cycle(range(self.player_count))

        self.scores = np.zeros(self.player_count, dtype=np.int32)
        self.circle = np.zeros(self.last_marble, dtype=np.int32)
        self.circle[0] = 0
        self.marble = 1
        self.size = 1
        self.current_marble = 1

    def take_turn(self):
        self.size += 1
        self.current_marble += 2
        if self.current_marble > (self.size - 1):
            self.current_marble -= self.size
        self.circle[self.current_marble] = self.marble
        self.marble += 1

        next(self.players)

def part1(input):
    g = Game(input)
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