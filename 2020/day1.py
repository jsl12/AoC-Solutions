import numpy as np
from typing import Iterable

def part1(nums: Iterable):
    for n in nums:
        added = n + nums
        try:
            idx = np.where(added==2020)[0][0]
        except IndexError:
            continue
        else:
            return n * nums[idx]


def part2(input):
    return


if __name__ == '__main__':
    import aoc_input as inp

    DAY = 1
    nums = np.array([n for n in inp.read_nums(DAY)])
    print(part1(nums))
    print(part2(inp.read(DAY)))