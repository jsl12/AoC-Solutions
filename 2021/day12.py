from collections import Counter
from typing import Iterable, Tuple

import numpy as np

check_upper = lambda s: s == s.upper()
check_lower = lambda s: s == s.lower()


class CaveSystem:
    def __init__(self, input_str):
        self.caves = np.unique([
            cave
            for line in input_str.splitlines()
            for cave in line.split('-')
        ])

        self.paths = {cave: list() for cave in self.caves}

        for line in input_str.splitlines():
            start, end = line.split('-')
            self.paths[start].append(end)
            self.paths[end].append(start)

    def traverse(self,
                 node: str = 'start',
                 path: Tuple[str] = None,
                 limit: int = 0) -> Iterable[Tuple[str]]:
        path = (node,) if path is None else path
        connected_paths = (path + (connected,) for connected in self.paths[node])

        for connected, connected_path in zip(self.paths[node], connected_paths):
            if connected == 'start':
                continue
            elif not validate_path(connected_path, limit=limit):
                continue
            elif connected_path[-1] == 'end':
                yield connected_path
            else:
                yield from self.traverse(node=connected, path=connected_path, limit=limit)


def validate_path(path, limit: int = 0):
    multiple = [
        (key, count)
        for key, count in Counter(
            key for key in path if key == key.lower()
        ).most_common()
        if count > 1
    ]
    try:
        valid_count = multiple[0][1] <= 2
    except:
        valid_count = True

    return len(multiple) <= limit and valid_count


def part1(input_str):
    return len(list(CaveSystem(input_str).traverse(limit=0)))


def part2(input_str):
    return len(list(CaveSystem(input_str).traverse(limit=1)))
