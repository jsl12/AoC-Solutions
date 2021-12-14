from dataclasses import dataclass
from typing import List

from rich import print


@dataclass
class LanternFish:
    lifespan: int = 8

    def live(self):
        self.lifespan -= 1
        if self.lifespan < 0:
            self.lifespan = 6
            return LanternFish()


@dataclass
class School:
    fish: List[LanternFish]
    days: int = 0

    @classmethod
    def from_str(cls, input_str):
        return cls([LanternFish(int(i)) for i in input_str.split(',')])

    def live(self, days: int = 1, verbose: bool = False):
        for _ in range(days):
            self.days += 1
            new = 0
            for fish in self.fish:
                if (spawn := fish.live()) is not None:
                    new += 1
            self.fish.extend([LanternFish() for _ in range(new)])

            if verbose:
                print(str(self))
        return self

    def __str__(self):
        seq = ','.join((str(fish.lifespan) for fish in self.fish))
        return f'After {self.days:<2} days: {seq}'


def part1(inp):
    s = School.from_str(inp)
    s.live(80)
    return len(s.fish)


def part2(inp):
    s = School.from_str(inp)
    s.live(256)
    return len(s.fish)
