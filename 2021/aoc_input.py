from pathlib import Path


def find_day(day: int):
    base = Path(r'..\..\AoC-Inputs\2021')
    if (res := base / f'day{day}.txt').exists():
        return res


def read(day: int):
    file = find_day(day)
    with file.open('r') as f:
        return f.read()


def read_lines(day: int):
    return read(day).splitlines()


def read_ints(day: int):
    return read_factory(day, int)


def read_factory(day: int, factory_func):
    return [factory_func(line) for line in read_lines(day)]
