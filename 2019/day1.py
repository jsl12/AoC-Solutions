from math import floor


def fuel_needed(mass, fuel_total:int = 0):
    fuel = floor(int(mass) / 3) - 2
    if fuel > 0:
        fuel_total += fuel
        return fuel + fuel_needed(fuel, fuel_total)
    else:
        return 0


def part1(input):
    res = sum([floor(int(line) / 3) - 2 for line in input.splitlines()])
    return res


def part2(input):
    res = sum([fuel_needed(line) for line in input.splitlines()])
    return res


if __name__ == '__main__':
    import aoc_input as inp

    DAY = 1
    print(part1(inp.read(DAY)))
    print(part2(inp.read(DAY)))
