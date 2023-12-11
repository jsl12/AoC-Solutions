import re
import sys
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Set

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
    def from_text(cls, text: str) -> Dict[int, Any]:
        return {
            card.id: card
            for card in map(cls.from_line, text.splitlines())
        }

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
        self.winning_count = len(self.winning_nums)
        self.winning_ids = range(self.id + 1, self.id + self.winning_count + 1)
        self.value = 0 if self.winning_count == 0 else 2**(self.winning_count - 1)

    def play(self, cards: Dict):
        if self.value > 0:
            for i in self.winning_ids:
                card = cards[i]
                print(f'Yielding from {card}')
                yield from card.play(cards)


def part1(input: str):
    return sum(
        card.value
        for card in
        map(Card.from_line, input.splitlines())
    )

def part2(input):
    cards = Card.from_text(input)
    deck = deepcopy(list(cards.values()))
    played = 0
    while len(deck) > 0:
        card = deck.pop(0)
        played += 1
        for i in sorted(card.winning_ids):
            deck.insert(0, cards[i])
    return played


if __name__ == '__main__':
    print(part1(aoc_input.read(2023, 4)))
    print(part2(aoc_input.read(2023, 4)))