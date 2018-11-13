from day1_input import input
from itertools import cycle

# Day 1
OFFSET1 = 1

# DAY 2
OFFSET2 = len(input) / 2

#input = '1122'

def solve(input, offset):
    sum = 0
    for i, c in enumerate(input):
        ind = int((i + offset) % len(input))
        if input[ind] == c:
            sum += int(c)
    return sum


if __name__ == '__main__':
    print(solve(input, OFFSET1))
    print(solve(input, OFFSET2))
    