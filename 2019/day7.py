from utils import AmpSystem


def part1(input):
    """
    >>> import aoc_input as inp; part1(inp.read(7))
    262086
    """
    sys = AmpSystem(input)
    return sys.max_thruster_signal([i for i in range(5)])

def part2(input):
    """
    >>> import aoc_input as inp; part2(inp.read(7))
    5371621
    """
    sys = AmpSystem(input)
    return sys.max_thruster_signal([i for i in range(5, 10)])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
