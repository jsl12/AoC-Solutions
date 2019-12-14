from intcode import Computer


def part1(input):
    """
    >>> import aoc_input as inp; part1(inp.read(5))
    12896948
    """
    ic = Computer(input, [1])
    ic.run()
    return ic.outputs[-1]

def part2(input):
    """
    >>> import aoc_input as inp; part2(inp.read(5))
    7704130
    """
    ic = Computer(input, [5])
    return ic.run()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
