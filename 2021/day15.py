from dataclasses import dataclass, field
from typing import Tuple, List, Set

import numpy as np
from rich.panel import Panel

from helpers import adjacent
from helpers import array_to_panel


@dataclass
class ArrayPath:
    _pos: Tuple[int, int] = field(default=(0, 0))
    path: List[Tuple[int, int]] = field(default_factory=list)
    visited: Set[Tuple[int, int]] = field(default_factory=set)

    def __post_init__(self):
        self.path = [self.pos]
        self.visited.add(self.pos)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, new):
        self._pos = new
        self.path.append(new)
        if new not in self.visited:
            self.visited.add(new)

    def panel(self, arr: np.ndarray) -> Panel:
        res = arr.astype(np.dtype(('U', 20)))

        for coords in self.visited:
            res[coords] = f'[red bold]{res[coords]}[/]'

        for coords in self.forward(arr):
            res[coords] = f'[green bold]{res[coords]}[/]'

        return array_to_panel(arr=res, delim=' ', title=f'{self.pos} of {arr.shape}')

    def adjacent(self, arr: np.ndarray):
        yield from adjacent(pos=self.pos, size=arr.shape)

    def forward(self, arr: np.ndarray):
        yield from (
            coords
            for coords in self.adjacent(arr)
            if coords not in self.visited
        )

    def forward_vals(self, arr: np.ndarray):
        yield from ((arr[coords], coords) for coords in self.forward(arr))
