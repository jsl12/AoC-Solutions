import re
import sys
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Generator, List

from rich import print

f = Path(__file__).parents[1]
sys.path.insert(0, str(f))
import aoc_input


def coerce_zero(num: int):
    return num if num >= 0 else 0


def coerce_max(num: int, max: int):
    return num if num < max else max - 1


SYMBOL_REGEX = re.compile(r'[^\d\.\s]')


@dataclass
class PartNumber:
    line: int
    start: int
    num: int

    @property
    def end(self):
        return self.start + len(str(self.num))


@dataclass
class Surrounding:
    part_num: PartNumber
    preceding_line: str
    line: str
    following_line: str
    valid: bool = field(init=False)

    def __post_init__(self):
        self.valid = SYMBOL_REGEX.search(str(self)) is not None

    def __str__(self):
        return '\n'.join(
            getattr(self, field.name)
            for field in fields(self)
            if field.name.endswith('line')
        ).strip()


@dataclass
class Schematic:
    text: str
    lines: List[str] = field(init=False)
    part_numbers: List[PartNumber] = field(init=False)

    def __post_init__(self):
        self.lines = self.text.splitlines()
        self.part_numbers = [
            PartNumber(line=i, start=m.start(), num=int(m.group()))
            for i, line in enumerate(self.lines)
            for m in re.finditer(r'\d+', line)
        ]

    def surrounding(self, part_num: PartNumber) -> Surrounding:
        line = self.lines[part_num.line]
        line_length = len(line)
        start = coerce_zero(part_num.start - 1)
        end = coerce_max(part_num.end + 1, line_length)
        
        if (i := part_num.line - 1) >= 0:
            preceding_line = self.lines[i][start:end]
        else:
            preceding_line = ''

        if (i := part_num.line + 1) < len(self.lines):
            following_line = self.lines[i][start:end]
        else:
            following_line = ''
        
        return Surrounding(
            part_num=part_num,
            preceding_line=preceding_line,
            line=self.lines[part_num.line][start:end],
            following_line=following_line
        )

    def valid_part_numbers(self) -> Generator[PartNumber, None, None]:
        for pn in self.part_numbers:
            surr = self.surrounding(pn)
            if surr.valid:
                yield pn

    def total(self) -> int:
        return sum(pn.num for pn in self.valid_part_numbers())


def part1(input: str):
    return Schematic(input).total()

if __name__ == '__main__':
    print(part1(aoc_input.read(2023, 3)))