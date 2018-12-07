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


def part1(input):
    hits = 0
    input = [Claim(line) for line in input.splitlines()]
    for a, b in itertools.combinations(input, 2):
        overlap = a.overlap(b)
        if overlap is not None:
            print(''.center(50, '='))
            print('Corner of {} is inside {}'.format(a.num, b.num))
            print(overlap)
            hits += 1
    return hits

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 3
    input = inp.read(DAY)
    print(part1(input))
    print(part2(input))
    # print(part1('#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2'))
    # print(part1('#0 @ 0,0: 4x3\n#1 @ 4,0: 4x3\n#2 @ 2,2: 4x4\n#3 @ 0,5: 3x2\n#4 @ 5,5: 4x2\n'))
    # test_boxes = [
    #     '#1 @ 2,2: 4x4',
    #     '#2 @ 5,5: 3x2'
    # ]
    # ol = Claim(test_boxes[0]).overlap(Claim(test_boxes[1]))
    # print(ol)
