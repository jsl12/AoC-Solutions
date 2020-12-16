from pathlib import Path


def find_day(day: int):
    base = Path(r'C:\Users\lanca\OneDrive\Documents\Software\Advent of Code\AoC-Inputs\2020')
    if (res := base / f'day{day}.txt').exists():
        return res


def read(day: int):
    file = find_day(day)
    with file.open('r') as f:
        yield from f.readlines()

def read_nums(day: int):
    yield from (int(line) for line in read(day))