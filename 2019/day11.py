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
    """
    >>> import aoc_input as inp; part2(inp.read(11))
    .###..####.####.###...##..####.####.###.
    .#..#.#....#....#..#.#..#.#....#....#..#
    .#..#.###..###..#..#.#....###..###..###.
    .###..#....#....###..#....#....#....#..#
    .#.#..#....#....#....#..#.#....#....#..#
    .#..#.#....####.#.....##..#....####.###.
    """
    r = Robot(input)
    r.painted[(0, 0)] = 1
    r.run()
    r.visualize()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
