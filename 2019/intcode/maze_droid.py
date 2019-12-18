from dataclasses import dataclass
from typing import List

from .computer import Computer


class MazeDroid:
    def __init__(self, seq):
        self.ic = Computer(seq)

