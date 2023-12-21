import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

f = Path(__file__).parents[1]
sys.path.insert(0, str(f))
import aoc_input


def format_line(vals, width: int = 32):
    string = ' '.join(f'{i:<4}' for i in vals)
    string = string.center(width)
    return string


def diff(lst):
    try:
        len(lst)
    except:
        lst = list(lst)

    yield from ((lst[i+1] - lst[i]) for i in range(0, len(lst) - 1))


def check(lst):
    return not all(v == 0 for v in diff(lst))


@dataclass
class Tree:
    first_line: List[int]
    lines: List[List[int]] = field(default_factory=list)
    width: int = field(init=False)

    def __post_init__(self):
        self.lines = [self.first_line]
        self.width = len(format_line(self.first_line))
        while self.check():
            self.lines.append(self.next_line())
        self.lines.append(self.next_line())

    def next_line(self, i: int = -1):
        return list(diff(self.lines[i]))
    
    def check(self, i: int = -1):
        return check(self.lines[i])

    def tree_string(self):
        return '\n'.join(map(lambda line: format_line(line, self.width), self.lines))
    
    def extrapolate(self):
        line: List[int]
        self.lines[-1].append(0)
        for i, line in enumerate(self.lines[-2::-1]):
            line_num = -(i + 2)
            char = len(self.lines[line_num])
            # print(i, line_num, char)
            left = line[-1]
            down = self.lines[line_num + 1][-1]
            # print(left, down)
            line.append(left + down)
        return self.lines[0][-1]


def part1(input: str):
    return sum([
        Tree([int(i) for i in line.split(' ')]).extrapolate()
        for line in input.splitlines()
    ])


def part2(input: str):
    return


if __name__ == '__main__':
    input = aoc_input.read(2023, 9)
    print(part1(input))
    print(part2(input))