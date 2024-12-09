import re
import sys
from copy import deepcopy
from dataclasses import dataclass, field
from itertools import chain, count
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set

from rich import print
from rich.progress import Progress, track

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
            if line.source <= seed <= (line.source + line.length):
                return line.dest + (seed - line.source)
        else:
            return seed


def process_seed(seed: Iterable[int], sources: Dict[str, Map]):
    source_map = sources['seed']
    new_seed = source_map.eval(seed)
    while source_map.dest != 'location':
        source_map = sources[source_map.dest]
        new_seed = source_map.eval(new_seed)
        # print(source_map.dest)
    return new_seed


def part1(input: str):
    parts = input.split('\n\n')
    seeds = set(map(int, SEED_REGEX.match(parts.pop(0)).group(1).split(' ')))

    maps = Map.from_parts(parts)
    sources = {m.source: m for m in maps}

    locations = {s: process_seed(s, sources) for s in seeds}
    return min(locations.values())


def part2(input: str):
        parts = input.split('\n\n')
        seed_input = list(map(int, SEED_REGEX.match(parts.pop(0)).group(1).split(' ')))
        
        ranges = (seed_input[i:i+2] for i in range(0, len(seed_input), 2))
        print(list(ranges))
        # ranges = (range(start, start+length) for start, length in ranges)
        # seeds = chain(*ranges)

        # maps = Map.from_parts(parts)
        # sources = {m.source: m for m in maps}
        # print(sources)

        # res = {
        #     s: process_seed(s, sources)
        #     for s in track(seeds, description="Processing seeds...")
        # }

        # return min(res.values())
        return seeds


if __name__ == '__main__':
    sample = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    print(part1(aoc_input.read(2023, 5)))
    # print(part2(sample))
    print(part2(aoc_input.read(2023, 5)))