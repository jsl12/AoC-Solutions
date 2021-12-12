from collections import Counter
from typing import List


def rates(inp):
    counts = [Counter(map(lambda s: s[i], inp)) for i in range(len(inp[0]))]
    gamma = int(''.join(map(lambda c: c.most_common()[0][0], counts)), 2)
    epsilon = int(''.join(map(lambda c: c.most_common()[-1][0], counts)), 2)
    return gamma, epsilon


def part1(lines: List[str]):
    g, e = rates(lines)
    return g * e


def get_rating(inp, default_val: str, idx: int):
    n = len(inp[0])
    get_counts = lambda nums: [Counter(map(lambda s: s[i], nums)) for i in range(n)]
    for i in range(n):
        counts = get_counts(inp)
        pos_counts = counts[i].most_common()

        if pos_counts[0][1] == pos_counts[1][1]:
            target = default_val
        else:
            target = pos_counts[idx][0]

        inp = [num for num in inp if num[i] == target]
        if len(inp) == 1:
            break
    return int(inp[0], 2)


def oxygen_rating(inp):
    return get_rating(inp, '1', 0)


def co2_rating(inp):
    return get_rating(inp, '0', -1)


def part2(inp):
    return oxygen_rating(inp) * co2_rating(inp)
