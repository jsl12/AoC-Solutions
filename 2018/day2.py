def part1(input):
    twos = 0
    threes = 0

    for line in input.splitlines():
        letters = {}
        for c in line:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1

        if [letters[c] for c in letters if letters[c] == 2]:
            twos += 1
        if [letters[c] for c in letters if letters[c] == 3]:
            threes += 1

    checksum = twos * threes
    return checksum

def part2(input):
    return

if __name__ == '__main__':
    from pathlib import Path
    p = Path(r'C:\Users\lanca_000\Documents\Software\Python\AoC Benchmark\AoC-Inputs\2018')
    with open(p / 'day2.txt', 'r') as file:
        input = file.read()
    print(part1(input))
    print(part2(input))