from intcode import Arcade


def part1(input):
    """
    >>> import aoc_input as inp; part1(inp.read(13))
    277
    """
    a = Arcade(input)
    return a.count_blocks()


def part2(input):
    """
    >>> import aoc_input as inp; part2(inp.read(13))
    12856
    """
    a = Arcade(input)
    a.ic.inputs = [0]
    score = a.play()
    return score


if __name__ == '__main__':
    import doctest
    doctest.testmod()
