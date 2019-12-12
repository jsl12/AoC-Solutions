def gen_dict(input):
    input = [line.split(')') for line in input.splitlines()]
    return {line[1]: line[0] for line in input}

def count(key, dict):
    count = 0
    while key in dict:
        key = dict[key]
        count += 1
    return count

def part1(input):
    input = gen_dict(input)
    total = sum([count(planet, input) for planet in input])
    return total

def part2(input):
    return

if __name__ == '__main__':
    import aoc_input as inp

    DAY = 6
    # print(part1('COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L'))

    print(part1(inp.read(DAY)))
    # print(part2(inp.read(DAY)))
