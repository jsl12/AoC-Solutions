
import sys
from dataclasses import dataclass, field
from functools import reduce
from pathlib import Path

from rich import print

f = Path(__file__).parents[1]
sys.path.insert(0, str(f))
import aoc_input


def part1(input: str):
    return

def part2(input: str):
    return

if __name__ == '__main__':
    input = aoc_input.read(2023, 9)
    print(part1(input))
    print(part2(input))