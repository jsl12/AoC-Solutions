import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Set

from rich import print

f = Path(__file__).parents[1]
sys.path.insert(0, str(f))


import aoc_input

card_regex = re.compile(r'Card\s+(?P<id>\d+): (?P<winning>[\d ]+) \| (?P<have>[\d ]+)$')
num_regex = re.compile(r'\d+')

def parse_nums(line: str):
    return set(map(int, num_regex.findall(line)))


@dataclass
class Card:
    id: int
    winning: Set[int]
    have: Set[int]

    @classmethod
    def from_line(cls, line: str):
        m = card_regex.match(line)
        self = cls(
            id=int(m.group('id')),
            winning=parse_nums(m.group('winning')),
            have=parse_nums(m.group('have'))
        )
        return self
    
    def __post_init__(self):
        self.winning_nums = set(num for num in self.have if num in self.winning)
        self.value = 0 if len(self.winning_nums) == 0 else 2**(len(self.winning_nums) - 1)

def part1(input: str):
    return sum(
        card.value
        for card in
        map(Card.from_line, input.splitlines())
    )


if __name__ == '__main__':
    print(part1(aoc_input.read(2023, 4)))