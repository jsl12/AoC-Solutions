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
        self.x = int(match.group(2))
        self.y = int(match.group(3))
        self.w = int(match.group(4))
        self.h = int(match.group(5))

def part1(input):
    input = [Claim(line) for line in input.splitlines()]
    mx = np.array([c.x for c in input])
    mx = max(mx) + input[mx.argmax()].w

    my = np.array([c.y for c in input])
    my = max(my) + input[my.argmax()].h
    space = np.zeros((mx, my), dtype=np.int32)
    return

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
