import re
import sys
from copy import deepcopy
from dataclasses import dataclass, field
from itertools import count
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set

from rich import print

f = Path(__file__).parents[1]
sys.path.insert(0, str(f))
import aoc_input

SEED_REGEX = re.compile(r'seeds:\s+(.*?)$')
TITLE_REGEX = re.compile(r'^(?P<source>\w+)-to-(?P<dest>\w+)')

@dataclass
class MapLine:
    dest: int
    source: int
    length: int


@dataclass
class Map:
    type: str
    lines: List[MapLine] = field(repr=False)
    source: str = field(init=False, repr=False)
    dest: str = field(init=False, repr=False)

    @classmethod
    def from_parts(cls, parts: List[str]):
        return [
            Map(
                TITLE_REGEX.match(part).group(),
                [
                    MapLine(*(int(i) for i in line.split(' ')))
                    for line in
                    part.splitlines()[1:]
                ]
            )
            for part in parts
        ]
    
    def __post_init__(self):
        self.source, self.dest = self.type.split('-to-')

    def eval(self, seed: int):
        for line in self.lines:
            # print(line)
            if line.source <= seed <= (line.source + line.length):
                # print(f'Modifying value: {seed}')
                return line.dest + (seed - line.source)
        else:
            # print(f'Not affected by modifiations: {seed}')
            return seed


def process_seed(seed: Iterable[int], sources: Dict[str, Map]):
    source_map = sources['seed']
    seed = source_map.eval(seed)
    while source_map.dest != 'location':
        source_map = sources[source_map.dest]
        seed = source_map.eval(seed)
    return seed

def part1(input: str):
    parts = input.split('\n\n')
    seeds = set(map(int, SEED_REGEX.match(parts.pop(0)).group(1).split(' ')))
    # print(seeds)

    maps = Map.from_parts(parts)
    sources = {m.source: m for m in maps}

    locations = {s: process_seed(s, sources) for s in seeds}
    return min(locations.values())


if __name__ == '__main__':
    print(part1(aoc_input.read(2023, 5)))
    # print(part2(aoc_input.read(2023, 5)))