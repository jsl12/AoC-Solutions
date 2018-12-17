import re
import pandas as pd
import numpy as np

class Garden:
    INPUT_REGEX = re.compile('([\.#]{5}) => ([\.#])')
    STATE_REGEX = re.compile('initial state: ([\.#]+)')

    def __repr__(self):
        if len(self.state) > 30:
            return '{} plants in {} pots'.format(self.state.count('#'), len(self.state))
        else:
            return self.state

    def __str__(self):
        return '\n'.join(['{} ({}) {}'.format(i, pc, s) for i, (z, pc, s) in enumerate(self.history)])

    def __init__(self, input):
        self.state = self.STATE_REGEX.search(input).group(1)
        self.zero = 0
        self.extend()
        self.rules = {m[0]: m[1] for m in self.INPUT_REGEX.findall(input)}
        self.history = []
        self.record()

    def grow(self, n=1):
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

    def stabilize(self, step=100):
        self.grow(step)
        while self.growth.iloc[-step] != self.growth.iloc[-1]:
            self.grow(step)

    def fast_forward(self, steps):
        remaining_steps = steps - len(self.history)
        return self.plant_count + (remaining_steps * self.growth.iloc[-1])

    @property
    def plant_count(self):
        return sum([i - self.zero for i, c in enumerate(self.state) if c != '.'])

    @property
    def plant_counts(self):
        return pd.Series([pc for i, pc, s in self.history], dtype=np.int64)

    @property
    def growth(self):
        return self.plant_counts.diff()[1:]

def part1(input):
    g = Garden(input)
    g.grow(20)
    return g.plant_count

def part2(input):
    g = Garden(input)
    g.stabilize()
    g.fast_forward(50000000000)
    return

if __name__ == '__main__':
    import input as inp
    DAY = 12
    input = inp.read(DAY)
    print(part1(input))
    print(part2(input))