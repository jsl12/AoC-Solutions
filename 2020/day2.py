def parse_input_line(line):
    params, password = line.split(': ')
    params, char = params.split(' ')
    param1, param2 = params.split('-')
    return int(param1), int(param2), char, password


def part1(lines):
    res = 0
    for line in lines:
        min, max, char, password = parse_input_line(line)
        valid = min <= password.count(char) <= max
        if valid:
            res += 1
    return res


def part2_check(line):
    pos1, pos2, char, password = parse_input_line(line)
    return bool((password[pos1 - 1] == char)  != (password[pos2 - 1] == char))


def part2(lines):
    res = 0
    for line in lines:
        if part2_check(line):
            res += 1
    return res


if __name__ == '__main__':
    import aoc_input as inp
    DAY = 2
    part2_check('2-9 c: ccccccccc')
    print(part1(inp.read_lines(DAY)))
    print(part2(inp.read_lines(DAY)))