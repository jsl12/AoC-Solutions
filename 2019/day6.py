def gen_dict(input):
    input = [line.split(')') for line in input.splitlines()]
    return {line[1]: line[0] for line in input}


def count(key, dict):
    count = 0
    while key in dict:
        key = dict[key]
        count += 1
    return count


def trace_back(start, dict):
    path = []
    key = dict[start]
    while key in dict:
        path.append(key)
        key = dict[key]
    return path[::-1]


def distance(start, end, dict):
    start_path = trace_back(start, dict)
    end_path = trace_back(end, dict)

    for i, p in enumerate(start_path):
        if p == end_path[i]:
            joint = p
        else:
            break
    start_length = len(start_path[start_path.index(joint):-1])
    end_length = len(end_path[end_path.index(joint)+1:])
    return (start_length + end_length)


def part1(input):
    input = gen_dict(input)
    total = sum([count(planet, input) for planet in input])
    return total


def part2(input):
    input = gen_dict(input)
    res = distance('YOU', 'SAN', input)
    return res


if __name__ == '__main__':
    import aoc_input as inp

    DAY = 6
    # print(part1('COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L'))
    # print(part2('COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN'))

    print(part1(inp.read(DAY)))
    print(part2(inp.read(DAY)))
