import re
import matplotlib.pyplot as plt
import pandas as pd

REGEX = re.compile('position=< ?([-\d]+), +([-\d]+)> velocity=< ?([-\d]+), +([-\d]+)>')

class Point:
    def __init__(self, line):
        match = REGEX.match(line)
        self.pos = (int(match.group(2)), int(match.group(3)))
        self.vel = (int(match.group(3)),int(match.group(4)))

    def advance(self, t=1):
        self.pos = (
            self.pos[0] + (self.vel[0] * t),
            self.pos[1] + (self.vel[1] * t)
        )

def visualize(points, step, n):
    df = pd.DataFrame({'x': [pt.pos[0] for pt in points], 'y': [pt.pos[1] for pt in points]}).set_index('x')
    fig, ax = plt.subplots(figsize=(19.2, 10.8))
    ax.plot(df, '.')
    fig.savefig('day10.png')
    plt.close(fig)

def part1(input):
    pts = [Point(line) for line in input.splitlines()]
    [pt.advance(1000) for pt in pts]
    visualize(pts)

    return

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 10
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))