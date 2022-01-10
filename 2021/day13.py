from typing import Iterable, Tuple, List

import numpy as np
from rich import print

from helpers import array_to_panel, convert_array


def array_from_input(input_str):
    dots, folds = input_str.split('\n\n')
    dots = [tuple(int(i) for i in line.split(',')) for line in dots.splitlines()]
    return initialize_array(dots, False, True)


def lines_from_input(input_str):
    axes = {'x': 1, 'y': 0}
    dots, folds = input_str.split('\n\n')
    folds = folds.splitlines()
    folds = (line.split('=') for line in folds)
    folds = ((axes[along[-1]], int(pos)) for along, pos in folds)
    return list(folds)


def initialize_array(points: Iterable[Tuple[int, int]], blank_val=0, point_val=1):
    x, y = zip(*points)
    size = (max(y) + 1, max(x) + 1)
    res = np.full(size, blank_val)
    res[y, x] = point_val
    return res


def split_and_fold(arr: np.ndarray, axis: int, pos: int):
    base, folded = np.split(arr, [pos], axis=axis)
    folded = np.flip(folded, axis=axis)

    idx = [slice(None), slice(None)]
    idx[axis] = slice(None, -1, None)
    return base | folded[tuple(idx)]


def part1(input_str: str):
    arr = array_from_input(input_str)
    lines = lines_from_input(input_str)
    res = split_and_fold(arr, *lines[0])
    return res.sum()


def fold_sequence(arr: np.ndarray, fold_lines: List[Tuple[int, int]]):
    for axis, pos in fold_lines:
        arr = split_and_fold(arr, pos=pos, axis=axis)
    return arr


def part2(input_str: str):
    arr = array_from_input(input_str)
    lines = lines_from_input(input_str)
    res = fold_sequence(arr, lines)
    m = {True: '#', False: '.'}
    convert_and_print = lambda a, **kwargs: print(array_to_panel(convert_array(a, lambda v: m[v]), **kwargs))
    convert_and_print(res, title='Day 13 Part 2')
