def solve(input, offset):
    sum = 0
    for i, c in enumerate(input):
        ind = int((i + offset) % len(input))
        if input[ind] == c:
            sum += int(c)
    return sum

def part1(input):
    return solve(input, 1)

def part2(input):
    return solve(input, len(input) / 2)

if __name__ == '__main__':
    from pathlib import Path
    import os

    with open(Path(os.getcwd()) / 'day1.txt', 'r') as file:
        input = file.read()
    print(part1(input))
    print(part2(input))
