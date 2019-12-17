from intcode import Arcade


def part1(input):
    """
    >>> import aoc_input as inp; part1(inp.read(13))
    277
    """
    a = Arcade(input)
    return a.count_blocks()

def part2(input):
    return

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import aoc_input as inp

    DAY = 13
    # print(part1(inp.read(DAY)))
    print(part2(inp.read(DAY)))
