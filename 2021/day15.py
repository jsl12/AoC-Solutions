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
        if len(self.path) == 0:
            self.path = [self.pos]
            self.visited.add(self.pos)
        else:
            self.path.append(self.pos)
            self.visited = set(self.path)

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

        return array_to_panel(arr=res, delim=' ', title=f'{self.pos} of {self.calc_risk(arr)}')

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

    def traverse(self, arr: np.ndarray, current_min: int = None):
        pot = sorted(self.forward_vals(arr), key=lambda val: val[0])
        for val, new_yx in pot:
            new = self.spawn_subpath(pos=new_yx)

            if current_min is not None and new.calc_risk(arr) > current_min:
                continue
            elif len(self.path) > sum(arr.shape):
                continue
            elif self.check_termination(arr, pos=new_yx):
                yield new
            else:
                yield from new.traverse(arr, current_min=current_min)

    def check_termination(self, arr: np.ndarray, pos: Tuple[int, int]):
        return (pos[0] == arr.shape[0] - 1) and (pos[1] == arr.shape[1] - 1)

    def spawn_subpath(self, pos: Tuple[int, int]):
        return ArrayPath(pos, self.path.copy())

    def calc_risk(self, arr: np.ndarray):
        return arr[tuple(zip(*self.visited))].flatten().sum()
