from pathlib import Path

from aoc_input import find_day


def elf_gen(lines):
    elf_total = 0
    for line in lines:
        try:
            elf_total += int(line)
        except:
            yield elf_total
            elf_total = 0

if __name__ == '__main__':
    this_file = Path(__file__)
    path = this_file.parents[2] / f'inputs/2022/{this_file.stem}.txt'
    lines = path.read_text().splitlines()

    elves = sorted(elf_gen(lines))

    print(max(elves))
    print(sum(elves[-3:]))
