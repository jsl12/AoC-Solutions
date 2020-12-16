def part1(lines):
    res = 0
    for line in lines:
        params, password = line.split(': ')
        params, char = params.split(' ')
        min, max = params.split('-')
        valid = int(min) <= password.count(char) <= int(max)
        if valid:
            res += 1
    return res

def part2(lines):
    return

if __name__ == '__main__':
    import aoc_input as inp
    DAY = 2
    print(part1(inp.read(DAY)))
    # print(part2(input_nums))