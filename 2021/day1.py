from typing import List


def part1(nums: List[int]):
    return sum([n > i for n, i in zip(nums[1:], nums)])


def part2(nums: List[int], n: int = 3):
    sums = map(sum, (nums[i:i+n] for i in range(len(nums))))
    return part1(list(sums))
