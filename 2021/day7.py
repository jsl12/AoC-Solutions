def part1(inp):
    crabs = list(map(int, inp.split(',')))
    rng = min(crabs), max(crabs) + 1
    return min([sum(map(lambda x: abs(i - x), crabs)) for i in range(*rng)])
