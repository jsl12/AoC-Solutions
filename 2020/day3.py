import numpy as np
from typing import Iterable
import aoc_input
from functools import reduce
import operator

class Field:
    def __init__(self, lines, initial_pos: Iterable[int] = (0, 0)):
        self.field = np.array([list(line.strip()) for line in lines])
        self.pos = np.array(initial_pos)
        self.trees = 0

    def __repr__(self):
        return '\n'.join(''.join(row.tolist()) for row in self.field)

    @property
    def current_char(self):
        try:
            row = self.field[self.pos[1]]
        except IndexError:
            return False
        else:
            try:
                return row[self.pos[0]]
            except IndexError:
                self.pos[0] %= self.field.shape[1]
                return row[self.pos[0]]

    def move(self, distance: Iterable[int]):
        self.pos += np.array(distance)
        if self.current_char:
            if self.current_char == '.':
                self.field[self.pos[1], self.pos[0]] = 'O'
            elif self.current_char == '#':
                self.field[self.pos[1], self.pos[0]] = 'X'
                self.trees += 1
            else:
                raise ValueError(f'Invalid char: {self.current_char}')

    def move_continuously(self, distance: Iterable[int]):
        while self.current_char:
            self.move(distance)
        return self


def part1(lines):
    return Field(lines).move_continuously((3, 1)).trees

def part2(lines):
    sets = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    trees = [Field(lines).move_continuously((right, down)).trees for right, down in sets]
    print(reduce(operator.mul, trees))

if __name__ == '__main__':
    DAY = 3
    print(part1(aoc_input.read(DAY)))
    print(part2(aoc_input.read(DAY)))
