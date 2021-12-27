from typing import List

from aoc_input import read


tokens = {
    '(': ')',
    '<': '>',
    '{': '}',
    '[': ']'
}


class Line:
    def __init__(self, line:str):
        self.chars = list(line)
        self.open = []
    
    def __repr__(self):
        return ''.join(self.chars)
    
    def validate(self):
        for char in self.chars:
            if char in tokens:
                self.open.append(char)
            elif char == tokens[self.open[-1]]:
                self.open.pop(-1)
            else:
                return False
        else:
            return True

    def closers(self):
        return [tokens[char] for char in self.open][::-1]
    
    def score(self):
        scores = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4
        }
        total = 0
        for char in self.closers():
            total *= 5
            total += scores[char]
        return total


def check_line(line: str):
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    open_chars = []
    for char in line:
        if char in tokens:
            open_chars.append(char)
        elif char == tokens[open_chars[-1]]:
            open_chars.pop(-1)
        else:
            points = scores[char]
            return char, points
    else:
        return open_chars

    
def part1(inp: List[str]):
    score = 0
    for line in inp:
        try:
            char, points = check_line(line)
        except:
            continue
        else:
            score += points
    return score


def part2(inp: List[str]):
    lines = [Line(line) for line in inp]
    lines = [line for line in lines if line.validate()]
    totals = sorted([line.score() for line in lines])
    return totals[int(len(totals) / 2)]
