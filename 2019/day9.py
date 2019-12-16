from intcode import Computer


def part1(input):
    """
    >>> import aoc_input as inp; part1(inp.read(9))
    3780860499
    """
    ic = Computer(input, [1])
    res = ic.run()
    return res


def part2(input):
    """
    >>> import aoc_input as inp; part2(inp.read(9))
    33343
    """
    ic = Computer(input, [2])
    coords = ic.run()
    return coords


if __name__ == '__main__':
    import doctest
    doctest.testmod()
