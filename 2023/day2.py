import operator
import re
import sys
from dataclasses import asdict, dataclass, fields
from functools import reduce
from pathlib import Path
from typing import List

f = Path(__file__).parents[1]
sys.path.insert(0, str(f))
import aoc_input

ID_REGEX = re.compile(r'^Game (\d+)')


@dataclass
class Revealed:
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    def from_line(cls, line: str):
        self = cls()
        for color in line.split(','):
            n, color = color.strip().split(' ')
            setattr(self, color, int(n))
        return self

    def compare(self, game_set):
        return any(
            amount > getattr(game_set, color)
            for color, amount in asdict(self).items()
        )
    
    def power(self):
        return reduce(operator.mul, (getattr(self, field.name) for field in fields(self)))
    

@dataclass
class Game:
    id: int
    rev: List[Revealed]

    @classmethod
    def from_line(cls, line: str):
        self = cls(
            id=int(ID_REGEX.match(line).group(1)),
            rev=[
                Revealed.from_line(part)
                for part in 
                line.split(':')[1].split(';')
            ]
        )
        return self
    
    def compare(self, game_set: Revealed) -> bool:
        """True if impossible"""
        return any(rev.compare(game_set) for rev in self.rev)
    
    def max_each_color(self) -> Revealed:
        maxs = {
            field.name: max(getattr(rev, field.name) for rev in self.rev)
            for field in fields(Revealed)
        }
        return Revealed(**maxs)


def filter_max(games: List[Game], game_set: Revealed) -> List[Revealed]:
    return [
        game
        for game in
        games
        if not game.compare(game_set)
    ]


def part1(input: str):
    games = [
        Game.from_line(line)
        for line in
        input.splitlines()
    ]
    return sum(game.id for game in filter_max(games, Revealed(red=12, green=13, blue=14)))


def part2(input: str):
    games = [
        Game.from_line(line)
        for line in input.splitlines()
    ]

    powers = {
        game.id: game.max_each_color().power()
        for game in games
    }

    return sum(powers.values())

if __name__ == '__main__':
    print(part1(aoc_input.read(2023, 2)))
    print(part2(aoc_input.read(2023, 2)))
