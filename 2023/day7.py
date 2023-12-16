import operator
import re
import sys
from dataclasses import dataclass, field
from functools import reduce
from pathlib import Path
import operator
import sys
from collections import Counter
from dataclasses import dataclass, field
from functools import reduce
from itertools import count
from typing import List, Tuple
from rich import print

f = Path(__file__).parents[1]
sys.path.insert(0, str(f))
import aoc_input


CARD_RANKS = {
    c: v
    for c, v in
    zip(
        ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1],
        count(2)
    )
}


HAND_RANKS = {
    c: v
    for c, v in
    zip(
        [
            'high card',
            'one pair',
            'two pair',
            'three of a kind',
            'full house',
            'four of a kind',
            'five of a kind'
        ],
        count()
    )
}


@dataclass
class Card:
    val: str

    def __post_init__(self):
        assert self.val in CARD_RANKS.keys()

    @property
    def rank(self):
        return CARD_RANKS[self.val]
    
    def __eq__(self, other):
        return self.rank == other.rank

    def __gt__(self, other):
        return self.rank > other.rank
    
    def __lt__(self, other):
        return self.rank < other.rank


@dataclass
class Hand:
    cards: Tuple[Card, Card, Card, Card, Card]

    @classmethod
    def from_str(cls, hand_str: str):
        return cls(tuple(Card(c) for c in hand_str))
    
    def __post_init__(self):
        assert len(self.cards) == 5

    def __repr__(self) -> str:
        return "".join(c.val for c in self.cards)

    def rank(self):
        return HAND_RANKS[self.best_hand()]

    def __eq__(self, other):
        return self.cards == other.cards

    def __gt__(self, other):
        if self.rank() == other.rank():
            for self_card, other_card in zip(self.cards, other.cards):
                if CARD_RANKS[self_card.val] == CARD_RANKS[other_card.val]:
                    continue
                else:
                    return CARD_RANKS[self_card.val] > CARD_RANKS[other_card.val]
        else:
            return self.rank() > other.rank()
    
    def __lt__(self, other):
        if self.rank() == other.rank():
            for self_card, other_card in zip(self.cards, other.cards):
                if CARD_RANKS[self_card.val] == CARD_RANKS[other_card.val]:
                    continue
                else:
                    return CARD_RANKS[self_card.val] < CARD_RANKS[other_card.val]
        else:
            return self.rank() < other.rank()

    def best_hand(self):
        counts = Counter(c.val for c in self.cards)
        most_common = counts.most_common()[0][1]

        if most_common == 5:
            return 'five of a kind'
        elif most_common == 4:
            return 'four of a kind'
        elif most_common == 3 and len(counts) == 2:
            return 'full house'
        elif most_common == 3:
            return 'three of a kind'
        elif most_common == 2 and len(counts) == 3:
            return 'two pair'
        elif most_common == 2 and len(counts) == 4:
            return 'one pair'
        else:
            return 'high card'


def parse_hands(input: str) -> Tuple[Tuple[Hand, int], ...]:
    data = tuple(tuple(line.split(' ')) for line in input.splitlines())
    data = tuple(sorted((Hand.from_str(hand_str), int(bid)) for hand_str, bid in data))
    return data


def part1(input: str):
    return sum([
        rank * bid
        for rank, (hand, bid) in
        enumerate(parse_hands(input), start=1)
    ])