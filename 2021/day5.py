from dataclasses import dataclass
from typing import List

import numpy as np
from rich import print


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    start: Point
    end: Point

    @classmethod
    def from_str(cls, input_str):
        return cls(*[Point(*map(int, pt.split(','))) for pt in input_str.split(' -> ')])

    def __post_init__(self):
        self.start, self.end = sorted((self.start, self.end), key=lambda p: p.x)

    def __rich__(self):
        fmt_point = lambda coords: '[black], '.join(map(lambda v: f'[red]{v:>3}', coords))
        pt1 = fmt_point((self.start.x, self.y1))
        pt2 = fmt_point((self.end.x, self.y2))
        res = f'[black]({pt1}[black]) -> [black]({pt2}[black])'
        if self.horizontal:
            res += ' [blue]horizontal'
        elif self.vertical:
            res += ' [green]vertical'
        elif self.diagonal:
            res += ' [green]diagonal'
        return res

    def slope(self):
        try:
            return int((self.end.y - self.start.y) / (self.end.x - self.start.x))
        except:
            return

    @property
    def horizontal(self):
        return self.start.y == self.end.y

    @property
    def vertical(self):
        return self.start.x == self.end.x

    def x_points(self):
        yield from range(self.start.x, self.end.x + 1)

    def points(self):
        m = self.slope()
        if m is not None:
            for i, x in enumerate(self.x_points()):
                yield Point(x, self.start.y + m * i)
        else:
            lims = sorted([self.start.y, self.end.y])
            lims[-1] += 1
            yield from (Point(self.start.x, y) for y in range(*lims))


@dataclass
class Field:
    lines: List[Line]

    def __post_init__(self):
        self.shape = [
            max((max((line.start.x, line.end.x)) for line in self.lines)) + 5,
            max((max((line.start.y, line.end.y)) for line in self.lines)) + 5
        ]
        self.shape = max(self.shape), max(self.shape)
        self.array = np.full(self.shape, 0)

    def __rich__(self):
        return '\n'.join(
            [
                ''.join(
                    str(val) if val != 0 else '.'
                    for val in row
                )[:100]
                for row in self.array
            ][:100]
        )

    def draw_line(self, line: Line):
        for pt in line.points():
            self.array[pt.y, pt.x] += 1

    def draw_all(self, diagonal: bool = False):
        for line in self.lines:
            if diagonal:
                self.draw_line(line)
            else:
                if line.vertical or line.horizontal:
                    self.draw_line(line)


def part1(inp):
    f = Field([Line.from_str(s) for s in inp])
    f.draw_all()
    return len([
        val
        for row in f.array
        for val in row
        if val >= 2
    ])


def part2(inp):
    f = Field([Line.from_str(s) for s in inp])
    f.draw_all(diagonal=True)
    return len([
        val for row in f.array
        for val in row
        if val >= 2
    ])


if __name__ == '__main__':
    from aoc_input import read_lines

    print(part1(read_lines(5)))
    print(part2(read_lines(5)))
