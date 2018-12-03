import re

class Claim:
    REGEX = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    def __init__(self, claim):
        self.text = claim
        match = self.REGEX.match(self.text)
        self.num = int(match.group(1))
        self.coords = (int(match.group(2)), int(match.group(3)))
        self.size = (int(match.group(4)), int(match.group(5)))

        self.iter_pos = list(self.coords)
        # Moves the pointer back a position so that next() returns the first value
        self.iter_pos[0] -= 1

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
    scanned = []
    hits = []
    for line in input.splitlines():
        c = Claim(line)
        print(c.num)

        # For each coordinate in the claim
        for x, y in c:
            # print(x, y)
            # For each claim already scanned
            for prev in scanned:
                # If the coordinate is a hit
                if prev.check(x, y):
                    # Append the coordinates to the list of hits
                    hits.append((x, y))
        scanned.append(c)
    return len(hits)

def part2(input):
    return

if __name__ == '__main__':
    from pathlib import Path
    p = Path(r'C:\Users\lanca_000\Documents\Software\Python\AoC Benchmark\AoC-Inputs\2018')
    with open(p / 'day3.txt', 'r') as file:
        input = file.read()
    print(part1(input))
    # print(part2(input))
    # print(part1('#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2'))