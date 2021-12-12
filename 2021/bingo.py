import re
from dataclasses import dataclass
from typing import List

from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel

console = Console()


@dataclass
class BingoBoard:
    board: List[List[int]]

    def __post_init__(self):
        self.height, self.width = len(self.board), len(self.board[0])
        self.called = [[False for _ in range(self.width)] for _ in range(self.width)]

    def __rich__(self):
        return Panel(
            '\n'.join(
                ' '.join(
                    f"[{'red' if call else 'green'}]{val:>3}"
                    for val, call in zip(val_row, call_row)
                )
                for val_row, call_row in zip(self.board, self.called)
            ),
            title='BingoBoard',
            expand=False
        )

    @classmethod
    def from_str(cls, input_str):
        return cls([[int(m) for m in re.findall('\d+', row)] for row in input_str.split('\n')])

    @property
    def values(self):
        yield from (
            (val, called)
            for val_row, call_row in zip(self.board, self.called)
            for val, called in zip(val_row, call_row)
        )

    def total(self):
        return sum(val for val, called in self.values if not called)

    def register_value(self, target: int):
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                if val == target:
                    self.called[i][j] = True
                    return True

    def check_winning(self):
        return any(all(row) for row in self.called) or \
               any(all(row[i] for row in self.called) for i in range(self.width))


@dataclass
class BingoGame:
    seq: List[int]
    boards: List[BingoBoard]

    @classmethod
    def from_str(cls, input_str):
        input_str = input_str.split('\n\n')
        return cls(
            list(map(int, input_str[0].split(','))),
            list(map(BingoBoard.from_str, input_str[1:]))
        )

    def call_number(self, number):
        for b in self.boards:
            b.register_value(number)
        for i, b in enumerate(self.boards):
            if b.check_winning():
                # print(b)
                return self.boards.pop(i)

    def play_game(self):
        for num in self.seq:
            res = self.call_number(num)
            # print(self)
            if isinstance(res, BingoBoard):
                yield num, res

    def __rich__(self):
        return Columns([b.__rich__() for b in self.boards])
