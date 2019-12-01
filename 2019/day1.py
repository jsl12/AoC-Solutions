from math import floor

def part1(input):
    res = sum([floor(int(line) / 3) - 2 for line in input.splitlines()])
    return res

if __name__ == '__main__':
    import input as inp
    DAY = 1
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))