from dataclasses import dataclass, field
from typing import Tuple, List, Set

import numpy as np
from rich.panel import Panel

from helpers import adjacent
from helpers import array_to_panel


@dataclass
class ArrayPath:
    pos: Tuple[int, int] = (0, 0)
    path: List[Tuple[int, int]] = field(default_factory=list)
    visited: Set[Tuple[int, int]] = field(default_factory=set)
    _pos: Tuple[int, int] = field(default=None)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key == 'pos' and hasattr(self, 'path') and hasattr(self, 'visited'):
            if value not in self.visited:
                self.path.append(value)
            else:
                self.visited.add(value)

    def __post_init__(self):
        self.path = [self.pos]
        self.visited.add(self.pos)

    def panel(self, arr: np.ndarray) -> Panel:
        res = arr.astype(np.dtype(('U', 20)))

        for coords in self.path:
            print(coords)
            res[coords] = f'[red bold]{res[coords]}[/]'

        for coords in self.forward(arr):
            res[coords] = f'[green bold]{res[coords]}[/]'

        return array_to_panel(arr=res, delim=' ', title=f'{self.pos} of {arr.shape}')

    def adjacent(self, arr: np.ndarray):
        yield from adjacent(pos=self.pos, size=arr.shape)

    def forward(self, arr: np.ndarray):
        for coords in self.adjacent(arr):
            if len(self.path) >= 2:
                if self.path[-2] == coords:
                    continue
            yield coords
