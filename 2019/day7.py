from utils import AmpSystem


def part1(input):
    """
    >>> import aoc_input as inp; part1(inp.read(7))
    262086
    """
    sys = AmpSystem(input)
    return sys.max_thruster_signal()

def part2(input):
    return

if __name__ == '__main__':
    import aoc_input as inp

    DAY = 7
    print(part1(inp.read(DAY)))
    print(part2(inp.read(DAY)))
