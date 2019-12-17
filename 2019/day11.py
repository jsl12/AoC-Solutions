from intcode import Computer, Robot


def part1(input):
    """
    >>> import aoc_input as inp; part1(inp.read(11))
    1564
    """
    r = Robot(input)
    r.run()
    return len(r.painted.keys())

def part2(input):
    return

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    import aoc_input as inp

    DAY = 11
    print(part1(inp.read(DAY)))
    print(part2(inp.read(DAY)))
