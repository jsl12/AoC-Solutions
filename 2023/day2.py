import re
import sys
from dataclasses import asdict, dataclass, fields
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


if __name__ == '__main__':
    res = part1(aoc_input.read(2023, 2))
    print(res)
