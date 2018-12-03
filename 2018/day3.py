import re
import itertools

class Claim:
    REGEX = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    def __str__(self):
        return self.text

    def __init__(self, claim):
        self.text = claim
        match = self.REGEX.match(self.text)
        self.num = int(match.group(1))
        self.coords = (int(match.group(2)), int(match.group(3)))
        self.size = (int(match.group(4)), int(match.group(5)))

        self.iter_pos = list(self.coords)
        # Moves the pointer back a position so that next() returns the first value
        self.iter_pos[0] -= 1

    def check_corners(self, claim):
    #     Check 4 corners of comparison claim to see if any of them are inside
        for i, corner in enumerate(claim.corners()):
            if self.check(corner[0], corner[1]):
                # Corners are numbered starting with the origin and going clockwise
                return i

    def overlap(self, claim):
        c = self.check_corners(claim)
        if c is not None:
            if c == 0:
                origin = claim.coords
                size = (
                    self.x_end() - origin[0],
                    self.y_end() - origin[1]
                )
            elif c == 1:
                origin = (self.coords[0], claim.coords[1])
                size = (
                    claim.x_end() - origin[0],
                    self.y_end() - origin[1]
                )
            elif c == 2:
              origin = self.coords
              size = (
                  claim.x_end() - origin[0],
                  claim.y_end() - origin[1]
              )
            elif c == 3:
                origin = (claim.coords[0], self.coords[1])
                size = (
                    self.x_end() - origin[0],
                    claim.y_end() - origin[1]
                )

            ol = Claim('#{} @ {},{}: {}x{}'.format(
                0,
                origin[0],
                origin[1],
                size[0] + 1,
                size[1] + 1
            ))
            return ol
        else:
            return None

    def corners(self):
        res = [
            (self.coords[0], self.coords[1]),
            (self.x_end(), self.coords[1]),
            (self.x_end(), self.y_end()),
            (self.coords[0], self.y_end())
        ]
        return res

    def x_end(self):
        return self.coords[0] + self.size[0] - 1

    def x_check(self, x=None):
        if x is None:
            x = self.iter_pos[0]
        return self.coords[0] <= x <= self.x_end()

    def y_end(self):
        return self.coords[1] + self.size[1] - 1

    def y_check(self, y=None):
        if y is None:
            y = self.iter_pos[1]
        return self.coords[1] <= y <= self.y_end()

    def check(self, x=None, y=None):
        hor = self.x_check(x)
        ver = self.y_check(y)
        return hor and ver

    def __iter__(self):
        return self

    def __next__(self):
        if self.increment_pointer():
            return self.iter_pos
        else:
            raise StopIteration

    def increment_pointer(self):
        # Move to the right once
        self.iter_pos[0] += 1

        # Determine if out of bounds
        if not self.check():
            # Determine if at end of row
            if self.y_check() and not self.x_check():
                # Reset column
                self.iter_pos[0] = self.coords[0]
                # Increment row
                self.iter_pos[1] += 1

            # Check to make sure still in bounds, only necessary to check y
            if not self.y_check():
                return False
            else:
                return True
        else:
            return True


def part1(input):
    hits = 0
    input = [Claim(line) for line in input.splitlines()]
    for a, b in itertools.combinations(input, 2):
        overlap = a.overlap(b)
        if overlap is not None:
            print(''.center(50, '='))
            # # print('Overlapping corner between:\n{}\n{}'.format(a, b))
            print('Corner of {} is inside {}'.format(a.num, b.num))
            hits += 1
            print(overlap)
    return hits

def part2(input):
    return

if __name__ == '__main__':
    # from pathlib import Path
    # p = Path(r'C:\Users\lanca_000\Documents\Software\Python\AoC Benchmark\AoC-Inputs\2018')
    # with open(p / 'day3.txt', 'r') as file:
    #     input = file.read()
    # print(part1(input))
    # print(part2(input))
    # print(part1('#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2'))
    print(part1('#0 @ 0,0: 4x3\n#1 @ 4,0: 4x3\n#2 @ 2,2: 4x4\n#3 @ 0,5: 3x2\n#4 @ 5,5: 4x2\n'))