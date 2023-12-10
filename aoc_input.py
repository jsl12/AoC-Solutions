from pathlib import Path

INPUT_DIR = Path(__file__).parents[1] / 'AoC-Inputs'


def find_day(year: int, day: int):
    file = INPUT_DIR / str(year) / f'day{day}.txt'
    if file.exists():
        return file


def read(year: int, day: int):
    file = find_day(year, day)
    with file.open('r') as f:
        return f.read()


def read_lines(year: int, day: int):
    return read(year, day).splitlines()


def read_ints(year: int, day: int):
    return read_factory(year, day, int)


def read_factory(year: int, day: int, factory_func):
    return [factory_func(line) for line in read_lines(year, day)]
