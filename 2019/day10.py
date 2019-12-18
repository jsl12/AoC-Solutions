import math
from dataclasses import dataclass
from itertools import combinations
from math import atan2, degrees
from typing import Tuple, Iterator, Type, Mapping, List


@dataclass
class Asteroid:
    pos: Tuple[int, int]

    def __post_init__(self):
        self.visible = []

    def __hash__(self):
        return self.pos.__hash__()

    def __eq__(self, other):
        if isinstance(other, Asteroid):
            return self.pos == other.pos
        elif isinstance(other, Tuple):
            return self.pos == other

    @property
    def visible_count(self):
        return len(self.visible)

    @property
    def x(self):
        return self.pos[1]

    @property
    def y(self):
        return self.pos[0]

    def get_trajectory(self, base_y, base_x):
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

    def angle(self, y, x):
        dy = self.y - y
        dx = self.x - x
        angle = degrees(atan2(dx, -dy))
        if angle < 0:
            angle += 360
        return angle


def scan(input:str, ast_char:str = '#') -> Iterator[Type[Asteroid]]:
    for y, line in enumerate(input.splitlines()):
        for x, c in enumerate(line):
            if c == ast_char:
                yield Asteroid((y, x))


def get_asteroids(input:str, ast_char: str = '#') -> List[Type[Asteroid]]:
    return {a.pos: a for a in [ast for ast in scan(input, ast_char)]}

def compute_sightlines(asteroids):
    for ast1, ast2 in combinations(asteroids.values(), 2):
        dy, dx = ast1.get_trajectory(*ast2.pos)
        y, x = (ast1.pos[0] + dy, ast1.pos[1] + dx)
        while (y, x) != ast2.pos:
            if (y, x) in asteroids:
                break
            y += dy
            x += dx
        else:
            ast1.visible.append(ast2)
            ast2.visible.append(ast1)
    return asteroids


def part1(input):
    """
    >>> import aoc_input as inp; part1(inp.read(10))
    314
    """
    ast = compute_sightlines(get_asteroids(input))
    return max(ast.values(), key=lambda a: a.visible_count).visible_count


def part2(input):
    """
    >>> import aoc_input as inp; part2(inp.read(10))
    1513
    """
    ast = compute_sightlines(get_asteroids(input))
    base = max(ast.values(), key=lambda a: a.visible_count)
    visible_ast = sorted(base.visible, key=lambda a: a.angle(*base.pos))
    y, x = visible_ast[199].pos
    return (x * 100) + y


if __name__ == '__main__':
    import doctest
    doctest.testmod()
