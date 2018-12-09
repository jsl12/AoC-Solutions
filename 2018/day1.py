def part1(input):
    res = 0
    for line in input.splitlines():
        res += int(line)
    return res

def part2(input):
    # TODO refactor to use sets
    input = [int(line) for line in input.splitlines()]
    # input = [int(line) for line in input.splitlines()][:10]
    new_f = 0
    prev = [0]

    # for c in input:
    # while new_f not in prev:
    while True:
        new_f = prev[-1] + input[0]
        if new_f in prev:
            return new_f
        else:
            prev.append(new_f)
            input = rotate(input)
            if len(prev) > 10000:
                return 'Failed'

def rotate(input, n=1):
    return input[n:] + input[:n]

if __name__ == '__main__':
    import input as inp
    DAY = 1
    input = inp.read(DAY)
    print(part1(input))
    print(part2(input))
    # print(part2('+1\n-1'))
    # print(part2('+3\n+3\n+4\n-2\n-4\n'))
    # print(part2('-6\n+3\n+8\n+5\n-6'))
    # print(part2('+7\n+7\n-2\n-7\n-4'))