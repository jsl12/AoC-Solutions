import re
import numpy as np

class Claim:
    REGEX = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text

    def __init__(self, claim_str):
        self.text = claim_str
        match = self.REGEX.match(claim_str)
        self.num = int(match.group(1))
        self.x = int(match.group(2))
        self.y = int(match.group(3))
        self.w = int(match.group(4))
        self.h = int(match.group(5))

class Space:
    def __repr__(self):
        return '{} x {} grid with {} claims'.format(
            self.space.shape[0],
            self.space.shape[1],
            len(self.claims)
        )

    def __init__(self, input):
        self.claims = [Claim(line) for line in input.splitlines()]
        mx = np.array([c.x for c in self.claims]).max() + np.array([c.w for c in self.claims]).max()
        my = np.array([c.y for c in self.claims]).max() + np.array([c.h for c in self.claims]).max()
        self.space = np.zeros((mx, my), dtype=np.int32)

    def _place(self, claim):
        self.space[sorted(list(range(claim.y, claim.y+claim.h)) * claim.w), list(range(claim.x, claim.x+claim.w)) * claim.h] += 1

    def place_claims(self):
        for c in self.claims:
            self._place(c)

    def multiple_owners(self):
        return self.space[self.space > 1].size

    def _check(self, claim):
        return self.space[sorted(list(range(claim.y, claim.y + claim.h)) * claim.w), list(range(claim.x, claim.x + claim.w)) * claim.h] == 1

    def find_complete(self):
        for c in self.claims:
            if self._check(c).all():
                return c

def part1(input):
    sp = Space(input)
    sp.place_claims()
    return sp.multiple_owners()

def part2(input):
    sp = Space(input)
    sp.place_claims()
    return sp.find_complete().num

if __name__ == '__main__':
    import input as inp
    DAY = 3
    input = inp.read(DAY)
    print(part1(input))
    print(part2(input))