import re

class Garden:
    INPUT_REGEX = re.compile('([\.#]{5}) => ([\.#])')
    STATE_REGEX = re.compile('initial state: ([\.#]+)')

    def __repr__(self):
        return self.state

    def __init__(self, input):
        self.state = self.STATE_REGEX.search(input).group(1)
        self.zero = 0
        self.extend()
        self.rules = {m[0]: m[1] for m in self.INPUT_REGEX.findall(input)}
        self.history = []
        self.record()

    def grow(self, n):
        for i in range(n):
            self.extend()
            res = self.state[:2]
            for i in range(len(self.state)-5):
                block = self.state[i:i+5]
                res += self.rules[block]
            self.state = res
            self.record()

    def replace(self, n, c):
        if self.state[n] != c:
            self.state = self.state[:n] + c + self.state[n+1:]

    def extend(self, n=10):
        ext = '.' * n
        if self.state[:n] != ext:
            self.state = ext + self.state
            self.zero += n
        if self.state[-n:] != ext:
            self.state += ext

    def record(self):
        self.history.append((self.zero, self.plant_count, self.state))

    @property
    def plant_count(self):
        return sum([i - self.zero for i, c in enumerate(self.state) if c != '.'])

    def print(self):
        for i, (z, pc, s) in enumerate(self.history):
            print('{} ({}) {}'.format(i, pc, s))

def part1(input):
    g = Garden(input)
    g.grow(20)
    return g.plant_count

def part2(input):
    g = Garden(input)
    g.grow(50 * (10 ** 6))
    return

if __name__ == '__main__':
    import input as inp
    DAY = 12
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))