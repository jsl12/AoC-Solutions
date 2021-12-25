from aoc_input import read

tokens = {
    '(': ')',
    '<': '>',
    '{': '}',
    '[': ']'
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def part1(inp):
    line_length = max(map(len, inp))
    score = 0
    for line in inp:
        open_chars = []
        for char in line:
            if char in tokens:
                open_chars.append(char)
            elif char == tokens[open_chars[-1]]:
                open_chars.pop(-1)
            else:
                points = scores[char]
                # print(f'{line.ljust(line_length)} - Expected {tokens[open_chars[-1]]}, but found {char} instead, {points}')
                score += points
                break
    return score
