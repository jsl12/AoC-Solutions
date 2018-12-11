import re
import numpy as np

REGEX = re.compile('position=< ?([-\d]+), +([-\d]+)> velocity=< ?([-\d]+), +([-\d]+)>')

def parse(line):
    match = REGEX.match(line)
    traj = {
        'pos': (match.group(2), match.group(3)),
        'vel': (match.group(3), match.group(4))
    }
    return traj

def part1(input):
    input = [parse(line) for line in input.splitlines()]

    return

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 10
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))