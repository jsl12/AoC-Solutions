from aoc_input import read_lines

from dataclasses import dataclass
from typing import List
from rich import print
from rich.panel import Panel

import re

import numpy as np


def make_array(input_lines: List[str]):
    return np.array([[int(i) for i in line] for line in read_lines(11)])


@dataclass
class PanelArray:
    arr: np.array
    title: str = None
    
    @property
    def width(self):
        # return max(len(str(c)) for row in self.arr for c in row)
        return 2
    
    def __str__(self):
        return '\n'.join(' '.join(str(c).rjust(self.width) for c in line) for line in self.arr)
    
    def colorize(self):
        return str(self)
    
    def __rich__(self):
        kwargs = {
            'title': getattr(self, 'title', None),
            'expand': False
        }
        return Panel(self.colorize(), **kwargs)

    
@dataclass
class Octopi(PanelArray):
    step: int = 0
    
    def __post_init__(self):
        self.arr = make_array(self.arr)
    
    @property
    def title(self):
        return f'Octopi, Step {self.step}'
    
    @title.setter
    def title(self, _):
        return
    
    def colorize(self):
        colors = {
            0: 'green bold',
            9: 'red bold'
        }
        res = str(self)
        for i, fmt in colors.items():
            res = re.sub(f' {i}', f' [{fmt}]{i}[/{fmt}]', res)
        return res
    
    def increase_energy(self):
        self.step += 1
        self.arr += 1
        self.flashed = []

    def increase_coords(self, coords):
        self.arr[tuple(np.array(idx) for idx in zip(*coords))] += 1
        
    def flash(self):
        coords = list(zip(*np.where(self.arr >= 9)))
        coords = [idx for idx in coords if idx not in self.flashed]
        self.flashed.extend(coords)
        
        below = [(y + 1, x) for y, x in coords if (y + 1) < self.arr.shape[0]]
        self.increase_coords(below)
        
        above = [(y - 1, x) for y, x in coords if (y - 1) >= 0]
        self.increase_coords(above)
        
        right = [(y, x + 1) for y, x in coords if (x + 1) < self.arr.shape[1]]
        self.increase_coords(right)
        
        left = [(y, x - 1) for y, x in coords if (x - 1) >= 0]
        self.increase_coords(left)
        
        # self.arr[tuple(zip(*self.flashed))] = 0
        self.arr[tuple(zip(*coords))] = 0
        