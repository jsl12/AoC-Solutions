from aoc_input import read

import numpy as np

from scipy.signal import argrelmin


def make_array(inp):
    return np.array([[int(i) for i in line] for line in inp.splitlines()])


def find_mins(arr):
    padded = np.pad(arr.astype(float), (1, 1), 'constant', constant_values=np.inf)
    coords = set(zip(*argrelmin(padded)))
    coords = coords.intersection(set(zip(*argrelmin(padded, axis=1))))
    coords = [(y - 1, x - 1) for y, x in coords]
    return coords


def part1(inp):
    arr = make_array(inp)
    coords = find_mins(arr)
    vals = [int(arr[y, x]) for y, x in coords]
    res = sum(vals) + len(vals)
    return res
