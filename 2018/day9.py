import re
import numpy as np
from itertools import cycle

class Game:
    REGEX = re.compile('(\d+) players; last marble is worth (\d+) points')

    def __repr__(self):
        s = [str(m) for m in self.circle]
        s[self.current_marble] = '({})'.format(s[self.current_marble])
        return ' '.join(s)

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

    def play(self):
        while self.marble <= self.last_marble:
            self.take_turn()
        return self.scores.max()

    def take_turn(self):
        if self.marble % 23 == 0:
            self.score()
        else:
            self.insert()
        self.marble += 1
        self.player = next(self.players)

    def insert(self):
        self.size += 1
        self.current_marble += 2
        if self.current_marble >= self.size:
            self.current_marble = 1
        self.circle[self.current_marble + 1:] = self.circle[self.current_marble:-1]
        self.circle[self.current_marble] = self.marble

    def score(self):
        self.scores[self.player] += self.marble
        self.current_marble -= 7
        if self.current_marble < 0:
            self.current_marble += self.size
        self.scores[self.player] += self.circle[self.current_marble]
        self.circle[self.current_marble:-1] = self.circle[self.current_marble + 1:]
        self.size -= 1

def part1(input):
    g = Game(input)
    return g.play()

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 9
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))
    # print(part1('10 players; last marble is worth 1618 points'))
    # print(part1('13 players; last marble is worth 7999 points'))
    # print(part1('17 players; last marble is worth 1104 points'))
    # print(part1('21 players; last marble is worth 6111 points'))
    # print(part1('30 players; last marble is worth 5807 points'))
