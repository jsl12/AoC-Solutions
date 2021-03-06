import pandas as pd
import matplotlib.pyplot as plt


def segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    # http: // www.cs.swan.ac.uk / ~cssimon / line_intersection.html
    denom = (x4 - x3) * (y1 - y2) - (x1 - x2) * (y4 - y3)
    r = ((y3 - y4) * (x1 - x3) + (x4 - x3) * (y1 - y3)) / denom
    s = ((y1 - y2) * (x1 - x3) + (x2 - x1) * (y1 - y3)) / denom

    if 0 < r < 1 and 0 < s < 1:
        x_cross = x1 + (x2 - x1) * r
        y_cross = y1 + (y2 - y1) * r
        return round(x_cross), round(y_cross)


class Wire:
    def __init__(self, input:str):
        self.input = input
        self.segments = [Segment(i) for i in input.split(',')]
        self.vertical_segments = [seg for seg in self.segments if seg.vertical]
        self.horizontal_segments = [seg for seg in self.segments if not seg.vertical]
        self.draw_all()

    def __repr__(self):
        return self.input

    def draw_all(self):
        for i, wire in enumerate(self.segments):
            try:
                wire.draw(*self.segments[i-1].end)
            except (IndexError, AttributeError):
                wire.draw(0, 0)
        return self

    @property
    def series(self):
        return pd.Series(
            data=[0] + [w.end[1] for w in self.segments],
            index=pd.Index(
                data=[0] + [w.end[0] for w in self.segments]
            )
        )

    def closest_intersection(self, other_wire):
        res = [min_dist(seg, other_wire) for seg in self.segments]
        return min([r for r in res if r is not None])

    def intersections(self, other_wire):
        res = []
        [res.extend(seg.wire_intersection(other_wire)) for seg in self.segments]
        return res

    def distance_to_intersection(self, x, y):
        res = 0
        for seg in self.segments:
            if seg.check_point(x, y):
                res += abs(x - seg.start[0]) + abs(y - seg.start[1])
                break
            else:
                res += seg.len
        return res

def min_dist(seg, wire):
    intersections = seg.wire_intersection(wire)
    try:
        return min([abs(c[0]) + abs(c[1]) for c in intersections if c])
    except ValueError:
        return


class Segment:
    def __init__(self, input):
        self.input = input
        self.dir = input[0]
        self.len = int(input[1:])

    def __repr__(self):
        return self.input

    def draw(self, start_x, start_y):
        self.start = (start_x, start_y)
        if self.dir == 'U':
            self.end = (start_x, start_y + self.len)
        elif self.dir == 'D':
            self.end = (start_x, start_y - self.len)
        elif self.dir == 'R':
            self.end = (start_x + self.len, start_y)
        elif self.dir == 'L':
            self.end = (start_x - self.len, start_y)
        return self.end

    @property
    def vertical(self):
        return self.dir == 'U' or self.dir == 'D'

    def wire_intersection(self, wire: Wire):
        if self.vertical:
            segments_to_check = wire.horizontal_segments
        else:
            segments_to_check = wire.vertical_segments

        intersections = [self.check_segment(seg) for seg in segments_to_check]
        return [cross for cross in intersections if cross is not None]

    def check_segment(self, seg):
        return segment_intersection(
            x1=self.start[0],
            y1=self.start[1],
            x2 = self.end[0],
            y2 = self.end[1],
            x3 = seg.start[0],
            y3 = seg.start[1],
            x4 = seg.end[0],
            y4 = seg.end[1],
        )

    def check_point(self, x, y):
        min_x = min([self.start[0], self.end[0]])
        max_x = max([self.start[0], self.end[0]])
        min_y = min([self.start[1], self.end[1]])
        max_y = max([self.start[1], self.end[1]])
        return (min_x <= x <= max_x) and (min_y <= y <= max_y)


def part1(input):
    wires = [Wire(line) for line in input.splitlines()]
    return wires[0].closest_intersection(wires[1])


def part2(input):
    wires = [Wire(line) for line in input.splitlines()]
    crosses = wires[0].intersections(wires[1])
    res = [wires[0].distance_to_intersection(*c) + wires[1].distance_to_intersection(*c) for c in crosses]
    return min(res)


def visualize(input):
    wires = [Wire(line) for line in input.splitlines()]
    fig, ax = plt.subplots()
    for w in wires:
        ax.plot(w.series)
    ax.grid(True)
    fig.savefig('day3.png')


if __name__ == '__main__':
    import aoc_input as inp
    DAY = 3
    sample1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83'
    sample2 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
    print(part2(sample1))
    print(part2(sample2))
    # visualize(sample2)
    print(part1(inp.read(DAY)))
    print(part2(inp.read(DAY)))
