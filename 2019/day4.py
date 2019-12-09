def rule1_check(input):
    res = True
    for i, c in enumerate(input):
        if i > 0:
            if int(input[i]) < int(input[i-1]):
                res = False
                break
    return res


def rule2_check(input, count_threshold = 2):
    count = 1
    max_count = 0
    for i, c in enumerate(input):
        try:
            if input[i+1] == c:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 1
        except IndexError:
            pass
    return max_count >= count_threshold

def part1(input):
    limits = [line for line in input.split('-')]
    res = [i for i in range(int(limits[0]), int(limits[1])) if rule1_check(str(i)) and rule2_check(str(i), 2)]
    return len(res)

def part2(input):
    return

if __name__ == '__main__':
    import aoc_input as inp

    DAY = 4
    print(part1(inp.read(DAY)))
    # print(part2(inp.read(DAY)))
