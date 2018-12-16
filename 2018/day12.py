import numpy as np
import re

class Garden:
    INPUT_REGEX = re.compile('([\.#]{5}) => ([\.#])')
    STATE_REGEX = re.compile('initial state: ([\.#]+)')

    def __repr__(self):
        return self.state

    def __init__(self, input):
        self.state = self.STATE_REGEX.search(input).group(1)
        self.regex = {
            re.compile('(?=({}))'.format(m[0].replace('.', '\.'))): m[1]
            for m in self.INPUT_REGEX.findall(input)}

    def grow(self, n):
        for i in range(n):
            for reg in self.regex:
                for m in re.finditer(reg, self.state):
                    start = m.span(1)[0]
                    self.state =  self.state[:start+2] + self.regex[reg] + self.state[start+3:]
                    continue

def part1(input):
    g = Garden(input)
    g.grow(20)
    return

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 12
    input = inp.read(DAY)
#     input = '''initial state: #..#.#..##......###...###
#
# ...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #
#     '''
    print(part1(input))
    # print(part2(input))