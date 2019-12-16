from dataclasses import dataclass
import re
import math
from functools import reduce

import itertools

planet_regex = re.compile('x=([-\d]+).*y=([-\d]+).*z=([-\d]+)')


class PlanetSystem:
    def __init__(self, input):
        self.planets = [Planet(line) for line in input.splitlines()]

    def total_cycle_time(self):
        cycles = [self.dimension_cycle_time(i) for i in range(3)]
        gcd = reduce(math.gcd, cycles)
        return int(reduce(lambda x, y: x * y, cycles) / gcd)

    def dimension_cycle_time(self, dim):
        count = 1
        self.simulate_dimension(dim)
        while not all([p.vel[dim] == 0 for p in self.planets]):
            self.simulate_dimension(dim)
            count += 1
        return count

    def simulate_dimension(self, dim, count:int = 1):
        for i in range(count):
            self.apply_gravity(dim)
            self.apply_vel(dim)

    def apply_gravity(self, dim: int):
        for planet1, planet2 in itertools.combinations(self.planets, 2):
            if planet1.pos[dim] > planet2.pos[dim]:
                planet1.vel[dim] -= 1
                planet2.vel[dim] += 1
            elif planet1.pos[dim] < planet2.pos[dim]:
                planet1.vel[dim] += 1
                planet2.vel[dim] -= 1

    def apply_vel(self, dim: int):
        for p in self.planets:
            p.pos[dim] += p.vel[dim]

    @property
    def total_energy(self):
        return sum([p.potential * p.kinetic for p in self.planets])


@dataclass
class Planet:
    input: str
    def __post_init__(self):
        m = planet_regex.search(self.input)
        self.pos = [
            int(m.group(1)),
            int(m.group(2)),
            int(m.group(3))
        ]
        self.vel = [0, 0, 0]

    @property
    def potential(self):
        return sum([abs(pos) for pos in self.pos])

    @property
    def kinetic(self):
        return sum([abs(vel) for vel in self.vel])

    def __repr__(self):
        pos = f'pos=<x={self.pos[0]:2}, y={self.pos[1]:2}, z={self.pos[2]:2}>'
        vel = f'<x={self.vel[0]:2}, y={self.vel[1]:2}, z={self.vel[2]:2}>'
        return f'pos={pos:25}, vel={vel:25}'


def part1(input):
    """
    >>> import aoc_input as inp; part1(inp.read(12))
    13045
    """
    ps = PlanetSystem(input)
    for i in range(3):
        ps.simulate_dimension(i, 1000)
    return ps.total_energy


def part2(input):
    """
    >>> import aoc_input as inp; part2(inp.read(12))
    344724687853944
    """
    ps = PlanetSystem(input)
    c = ps.total_cycle_time()
    return c


if __name__ == '__main__':
    import doctest
    doctest.testmod()
