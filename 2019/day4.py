def rule1_check(input):
    res = True
    for i, c in enumerate(input):
        if i > 0:
            if int(input[i]) < int(input[i-1]):
                res = False
                break
    return res

def rule2_check(input):
    for i in range(9):
        if input.count(str(i)) >= 2:
            return True
    return False

def part1(input):
    limits = [line for line in input.split('-')]
    count = 0
    with open('day4_sols.txt', 'w') as file:
        for i in range(int(limits[0]), int(limits[1])):
            i = str(i)
            if rule1_check(i) and rule2_check(i):
                count += 1
                file.write(f'{i}\n')
    return count

def part2(input):
    return

if __name__ == '__main__':
    import aoc_input as inp

    DAY = 4
    print(part1(inp.read(DAY)))
    # print(part2(inp.read(DAY)))
