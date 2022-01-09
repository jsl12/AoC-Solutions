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

    def traverse(self, node: str = 'start', path: Tuple[str] = None) -> Iterable[Tuple[str]]:
        path = (node,) if path is None else path
        connected_paths = (path + (connected,) for connected in self.paths[node])
        for connected, connected_path in zip(self.paths[node], connected_paths):
            if connected_path[-1] == 'start':
                continue
            elif connected in path and check_lower(connected):
                continue
            elif connected_path[-1] == 'end':
                yield connected_path
            else:
                yield from self.traverse(node=connected, path=connected_path)

def part1(input_str):
    return len(list(CaveSystem(input_str).traverse()))
