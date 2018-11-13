from profile import profile_by_day

# # Part 1
# OFFSET1 = 1
#
# # Part 2
# OFFSET2 = len(input) / 2

#input = '1122'
def solve(input, offset):
    sum = 0
    for i, c in enumerate(input):
        ind = int((i + offset) % len(input))
        if input[ind] == c:
            sum += int(c)
    return sum

@profile_by_day(day=1)
def part1(input):
    return solve(input, 1)

@profile_by_day(day=1)
def part2(input):
    return solve(input, len(input) / 2)

if __name__ == '__main__':
    from pathlib import Path
    import os

    part1()
    part2()
    