from dataclasses import dataclass, field

from pathlib import Path
from typing import List

from rich import print

from submarine import Submarine, get_steps


def part1(lines: List[str]):
    pos = [0, 0]
    for direction, n in get_steps(lines):
        if direction == 'forward':
            pos[0] += n
        elif direction == 'down':
            pos[1] += n
        elif direction == 'up':
            pos[1] -= n
        else:
            print(direction)
    return pos[0] * pos[1]


def part2(lines: List[str]):
    sub = Submarine().move_lines(lines)
    return sub.pos.horizontal * sub.pos.depth
