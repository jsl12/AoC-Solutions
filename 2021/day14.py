import itertools
from collections import Counter
from typing import Dict, Tuple


def process_input(s) -> Tuple[str, Dict[str, str]]:
    template, lines = s.split('\n\n')
    rules = {}
    for line in lines.splitlines():
        src, dst = line.split(' -> ')
        rules[src] = dst
    return template, rules


def part1(input_str: str) -> int:
    template, rules = process_input(input_str)
    for _ in range(10):
        template = cycle(template, rules)
    counts = Counter(template).most_common()
    return counts[0][1] - counts[-1][1]


def cycle(template: str, rules: Dict[str, str]) -> str:
    res = template[:]
    pairs = itertools.pairwise(template)
    insertions = ((i, ''.join(chars)) for i, chars in enumerate(pairs))
    insertions = ((i + 1, rules[token]) for i, token in insertions if token in rules)
    for pos, char in sorted(insertions, reverse=True):
        res = res[:pos] + char + res[pos:]
    return res
