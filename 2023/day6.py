import operator
import re
import sys
from dataclasses import dataclass, field
from functools import reduce
from pathlib import Path

from rich import print

f = Path(__file__).parents[1]
sys.path.insert(0, str(f))
import aoc_input


@dataclass
class Game:
    time: int
    distance: int

    @classmethod
    def from_input(cls, input: str):
        NUM_REGEX = re.compile(r'\d+')
        data = map(lambda line: map(int, NUM_REGEX.findall(line)), input.splitlines())
        games = [cls(*g) for g in zip(*data)]
        return games
    
    def race(self, charge_time: int):
        speed = charge_time
        race_time = self.time - charge_time
        distance_traveled = speed * race_time
        return distance_traveled

    def race_all(self):
        dist = [self.race(i) for i in range(self.time)]
        winning = [d for d in dist if d > self.distance]
        return winning
    
    
def part1(input: str):
    return reduce(operator.mul, [len(g.race_all()) for g in Game.from_input(input)])
