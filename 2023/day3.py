import operator
import re
import sys
from dataclasses import dataclass, field, fields
from functools import reduce
from pathlib import Path
from typing import Generator, Iterable, List, Tuple

from rich import print

f = Path(__file__).parents[1]
sys.path.insert(0, str(f))
import aoc_input


def coerce_zero(num: int):
    return num if num >= 0 else 0


def coerce_max(num: int, max: int):
    return num if num < max else max - 1


SYMBOL_REGEX = re.compile(r'[^\d\.\s]')
GEAR_REGEX = re.compile(r'\*')


def matches_with_lines(text: str, regex: re.Pattern):
    for i, line in enumerate(text.splitlines()):
        for m in regex.finditer(line):
            yield i, m


def slice_text(text: str, slices: Iterable[Iterable[int]]):
    return '\n'.join(
        line[slice(*slices[1])]
        for line in
        text.splitlines()[slice(*slices[0])]
    )


@dataclass
class Thingy:
    line: int
    start: int
    text: str

    @classmethod
    def from_str(cls, text: str, regex: re.Pattern):
        selfs = [cls(line, match.start(), match.group()) for line, match in matches_with_lines(text, regex)]
        for instance in selfs:
            instance.surr = Surrounding.from_thingy(text, instance)
        return selfs

    @property
    def end(self):
        return self.start + len(self.text)


@dataclass
class Gear(Thingy):
    @classmethod
    def from_str(cls, text: str):
        gears = super().from_str(text, GEAR_REGEX)
        for gear in gears:
            gear.valid = len(list(re.finditer(r'\d+', gear.surr.text))) >= 2
        return gears

    def __post_init__(self):
        assert self.text == '*'


@dataclass
class PartNumber(Thingy):
    num: int = field(init=False)

    @classmethod
    def from_str(cls, text: str):
        part_numbers = super().from_str(text, re.compile(r'\d+'))
        for part_number in part_numbers:
            part_number.valid = re.search(r'[^\d\.\s]', part_number.surr.text) is not None
        return part_numbers

    def __post_init__(self):
        self.num = int(self.text)


@dataclass
class Surrounding:
    text: str
    thing: Thingy
    extents: List[Tuple[int, int]]

    @classmethod
    def from_thingy(cls, body: str, thing: Thingy):
        lines = body.splitlines()
        extents = [
            (
                coerce_zero(thing.line - 1),
                coerce_max(thing.line + 2, len(lines) + 1)
            ),
            (
                coerce_zero(thing.start - 1),
                coerce_max(thing.end + 1, len(lines[thing.line]) + 1)
            )
        ]
        return cls(thing=thing, extents=extents, text=slice_text(body, extents))
    
    def is_inside(self, line: int, pos: int) -> bool:
        return all(
            lower <= num < upper
            for num, (lower, upper) in
            zip((line, pos), self.extents)
        )


@dataclass
class Schematic:
    text: str
    lines: List[str] = field(init=False)
    part_numbers: List[PartNumber] = field(init=False)
    gears: List[Gear] = field(init=False)

    def __post_init__(self):
        self.lines = self.text.splitlines()
        self.part_numbers = PartNumber.from_str(self.text)
        self.gears = Gear.from_str(self.text)

    def valid_part_numbers(self) -> Generator[PartNumber, None, None]:
        yield from (
            pn
            for pn in self.part_numbers
            if pn.valid
        )

    def total(self) -> int:
        return sum(pn.num for pn in self.valid_part_numbers())
    
    def parts_from_gear(self, gear: Gear):
        for pn in self.valid_part_numbers():
            if pn.surr.is_inside(gear.line, gear.start):
                yield pn

    def gear_ratio(self, gear: Gear):
        return reduce(
            operator.mul,
            (
                pn.num
                for pn in
                self.parts_from_gear(gear)
            )
        )

def part1(input: str):
    return Schematic(input).total()


def part2(input: str):
    s = Schematic(input)
    return sum(s.gear_ratio(g) for g in s.gears if g.valid)

if __name__ == '__main__':
    print(part1(aoc_input.read(2023, 3)))
    print(part2(aoc_input.read(2023, 3)))