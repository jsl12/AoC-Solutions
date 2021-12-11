from pathlib import Path
from typing import List

from rich import print

def part1(nums: List[int]):
    return sum([n > i for n, i in zip(nums[1:], nums)])

def part2(nums: List[int], n):
    sums = map(sum, (nums[i:i+n] for i in range(len(nums))))
    return day1(list(sums))
