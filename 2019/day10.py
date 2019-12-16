import math
from dataclasses import dataclass
from typing import Tuple

import numpy as np


class Field:
    def __init__(self, input):
        self.input = input
        char_list = list(self.input.replace('\n', ''))
        self.width = len(input.splitlines()[0])
        self.height = int(len(char_list) / self.width)

        bool_list = [True if c == '#' else False for c in char_list]
        self.array = np.array(bool_list).reshape((self.width, self.height))

    def scan_all(self):
        res = [(ast, self.scan_from(*ast.pos)) for ast in self.asteroid_gen()]
        return max(res, key=lambda r: r[1])


    def scan_from(self, y, x):
        """
        Tries to find a direct line of sight back from each asteroid back to the base, which
        is located at the input coordinates and is the location of another asteroid

        :param y: scan start y position
        :param x: scan start x position
        :return:
        """
        count = 0
        for ast in self.asteroid_gen():
            dy, dx = ast.get_trajectory(x, y)
            # skip self
            if not (dx == 0 and dy == 0):
                # position to check
                pos = (ast.y + dy, ast.x + dx)
                while self.inbounds(*pos):
                    if pos == (y, x):
                        # reached the base successfully
                        count += 1
                        break
                    elif self.array[pos]:
                        # hit another asteroid on the way back to the base
                        break
                    pos = (pos[0] + dy, pos[1] + dx)
        return count

    def asteroid_gen(self):
        with self.asteroid_iter as it:
            while not it.finished:
                res = it.multi_index
                val = it[0]
                it.iternext()
                if val:
                    yield Asteroid(res)

    @property
    def asteroid_iter(self):
        return np.nditer(self.array, flags=['multi_index'], op_flags=['readonly'])

    def inbounds(self, y, x):
        return (0 <= x < self.width) and (0 <= y < self.height)


@dataclass
class Asteroid:
    pos: Tuple[int, int]

    @property
    def x(self):
        return self.pos[1]

    @property
    def y(self):
        return self.pos[0]

    def get_trajectory(self, base_x, base_y):
        dx = base_x - self.x
        dy = base_y - self.y
        gcd = math.gcd(dx, dy)
        try:
            dx /= gcd
        except ZeroDivisionError:
            dx = 0

        try:
            dy /= gcd
        except ZeroDivisionError:
            dy = 0

        return int(dy), int(dx)

def part1(input):
    """
    >>> import aoc_input as inp; part1(inp.read(10))
    314
    """
    f = Field(input)
    return f.scan_all()[1]

def part2(input):
    return

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import aoc_input as inp

    DAY = 10
    # print(part1(inp.read(DAY)))
    print(part2(inp.read(DAY)))
