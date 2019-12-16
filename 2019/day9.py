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
    return

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import aoc_input as inp

    DAY = 9
    print(part1(inp.read(DAY)))
    print(part2(inp.read(DAY)))
