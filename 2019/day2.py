from utils import IntcodeComputer

def part1(input):
    """
    >>> import aoc_input as inp; part1(inp.read(2))
    4138687
    """
    ic = IntcodeComputer(input)
    ic.seq[1] = 12
    ic.seq[2] = 2
    ic.run()
    return ic.seq[0]


def part2(input):
    """
    >>> import aoc_input as inp; part2(inp.read(2))
    6635
    """
    ic = IntcodeComputer(input)
    target_val = 19690720
    for noun in range(99):
        for verb in range(99):
            ic.reset()
            ic.seq[1] = noun
            ic.seq[2] = verb
            ic.run()
            if ic.seq[0] == target_val:
                break
        if ic.seq[0] == target_val:
            break
    return 100 * noun + verb


if __name__ == '__main__':
    import doctest
    doctest.testmod()
