from dataclasses import dataclass, field

from pathlib import Path
from typing import List


def get_input(day: int):
    return (Path('inputs') / f'day{day}.txt').open('r').read().splitlines()


def get_steps(lines: List[str]):
    return map(lambda step: (step[0], int(step[1])), map(lambda line: line.split(), lines))


@dataclass
class Step:
    direction: str
    n: int


@dataclass
class Position:
    horizontal: int = 0
    depth: int = 0


@dataclass
class Aim:
    n: int = 0


@dataclass
class Submarine:
    pos: Position = field(default_factory=Position)
    aim: Aim = field(default_factory=Aim)

    def move(self, step: Step):
        if step.direction == 'forward':
            self.pos.horizontal += step.n
            self.pos.depth += self.aim.n * step.n
        elif step.direction == 'down':
            self.aim.n += step.n
        elif step.direction == 'up':
            self.aim.n -= step.n

    def moves(self, steps: List[Step]):
        for s in steps:
            self.move(s)
        return self

    def move_lines(self, lines: List[str]):
        return self.moves(map(lambda args: Step(*args), get_steps(lines)))
