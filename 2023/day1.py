import re
import sys
from pathlib import Path
from typing import List

from rich import print

f = Path(__file__).parents[1]
sys.path.insert(0, str(f))
import aoc_input


NUM_TEXTS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}

NUM_TEXT_REGEX = re.compile(f"(({'|'.join(NUM_TEXTS.keys())})|\d)")
# NUM_TEXT_REGEX = re.compile(f"({'|'.join(NUM_TEXTS.keys())})")


def convert_num(val: str):
    try:
        return int(val)
    except Exception:
        return int(NUM_TEXTS[val])
    

def get_digits(line: str):
    return [int(d) for d in re.findall('\d', line)]


def make_num(digits: List[int]):
    return int(f'{digits[0]}{digits[-1]}')


def part1(input: str):
    # lines = input.splitlines()
    # lines = map(get_digits, lines)
    # lines = map(make_num, lines)
    nums = [
        make_num(
            [
                convert_num(val.group())
                for val in re.finditer(r'\d', line)
            ]
        )
        for line in input.splitlines()
    ]
    return sum(nums)


def part2(input: str):
    nums = [
        make_num(
            [
                convert_num(val.group())
                for val in NUM_TEXT_REGEX.finditer(line)
            ]
        )
        for line in input.splitlines()
    ]
    return nums

if __name__ == '__main__':
    res = part1(aoc_input.read(2023, 1))
    print(res)

    print(part2(aoc_input.read(2023, 1)))
