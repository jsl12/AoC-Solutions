def part1(input):
    res = 0
    for line in input.splitlines():
        res += int(line)
    return res

if __name__ == '__main__':
    with open('day1_input.txt', 'r') as file:
        res = part1(file.read())
    print(res)