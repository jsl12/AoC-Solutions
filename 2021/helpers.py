import itertools
from typing import Callable, Iterable

import numpy as np
import pandas as pd
from rich.panel import Panel


def make_array(s) -> np.ndarray:
    """intended to be used with lines of only integers"""
    lines = s.splitlines()
    width = max(map(len, lines))
    height = len(lines)
    return np.fromiter((char for line in lines for char in line), dtype=int).reshape(width, height)


def array_to_panel(arr: np.ndarray, delim: str = '', width: int = None, **kwargs):
    return Panel(
        '\n'.join(
            delim.join(str(val).rjust(width) if width is not None else val
                       for val in row)
            for row in arr.astype(str)
        ),
        expand=False,
        **kwargs
    )


def convert_array(arr: np.ndarray, func: Callable, *args, **kwargs):
    return pd.DataFrame(arr).applymap(lambda val: func(val, *args, **kwargs)).values


def offsets(diagonal: bool = True, self: bool = True):
    for offset in itertools.product(*(list(range(-1, 2)) for _ in range(2))):
        dist = sum(map(abs, offset))
        if dist == 0:
            if self:
                yield offset
            else:
                continue
        elif dist == 1:
            yield offset
        elif dist == 2 and diagonal:
            yield offset


def adjacent(pos: Iterable[int], size: Iterable[int]):
    for offset in offsets(diagonal=False, self=False):
        y, x = tuple(map(sum, zip(pos, offset)))
        if (0 <= y < size[0]) and (0 <= x < size[1]):
            yield y, x
