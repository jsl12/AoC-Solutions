import numpy as np
from typing import Iterable
from itertools import combinations
from functools import reduce

def part1(nums, num_items=2, target=2020):
    for combo in combinations(nums, num_items):
        if sum(combo) == target:
            break
    return reduce(lambda x,y: x*y, combo)


def part2(nums):
    return part1(nums, num_items=3)


if __name__ == '__main__':
    import aoc_input as inp
    DAY = 1
    input_nums = np.array([n for n in inp.read_nums(DAY)])
    print(part1(input_nums))
    print(part2(input_nums))
