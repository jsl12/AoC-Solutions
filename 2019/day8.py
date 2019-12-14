import textwrap
from dataclasses import dataclass
from typing import Tuple


@dataclass
class Image:
    input: str
    dims: Tuple[int, int]

    @property
    def size(self):
        return self.dims[0] * self.dims[1]

    def __post_init__(self):
        self.layers = [Layer(input, self.dims) for input in textwrap.wrap(self.input, self.size)]

    def counts(self, char):
        return [layer.count(char) for layer in self.layers]

    def fewest_layer(self, char):
        counts = self.counts(char)
        return self.layers[counts.index(min(counts))]

    @property
    def rendered(self):
        return [[layer.input[i] for layer in self.layers if layer.input[i] != '2'][0] for i in range(len(self.layers[0].input))]

    def __str__(self):
        return '\n'.join([line for line in textwrap.wrap(''.join(self.rendered), self.dims[1])]).replace('0', ' ')


@dataclass
class Layer:
    input: str
    dims: Tuple[int, int]

    def count(self, char):
        return self.input.count(char)


def part1(input):
    """
    >>> import aoc_input as inp; part1(inp.read(8))
    1215
    """
    img = Image(input, (6, 25))
    layer = img.fewest_layer('0')
    return layer.count('1') * layer.count('2')


def part2(input):
    img = Image(input, (6, 25))
    return str(img)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import aoc_input as inp

    DAY = 8
    print(part1(inp.read(DAY)))
    print(part2(inp.read(DAY)))
