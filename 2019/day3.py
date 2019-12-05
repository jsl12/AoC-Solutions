import pandas as pd

class Wire:
    def __init__(self, input:str):
        self.input = input
        self.segments = [Segment(i) for i in input.split(',')]
        self.vertical_segments = [seg for seg in self.segments if seg.vertical]
        self.horizontal_segments = [seg for seg in self.segments if not seg.vertical]

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
        distances = [seg.check_wire(other_wire) for seg in self.segments]
        return min([d for d in distances if d is not None])


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

    @property
    def x(self):
        return self.start[0], self.end[0]

    @property
    def y(self):
        return self.start[1], self.end[1]

    def check_wire(self, wire: Wire) -> bool:
        if self.vertical:
            segments_to_check = wire.horizontal_segments
        else:
            segments_to_check = wire.vertical_segments


        intersections = [self.check_segment(seg) for seg in segments_to_check]
        distances = [abs(cross[0]) + abs(cross[1]) for cross in intersections if cross is not None]
        if distances:
            return min(distances)


    def check_segment(self, seg) -> bool:
        """
        http://www.cs.swan.ac.uk/~cssimon/line_intersection.html
        """
        x1 = self.start[0]
        y1 = self.start[1]
        x2 = self.end[0]
        y2 = self.end[1]

        x3 = seg.start[0]
        y3 = seg.start[1]
        x4 = seg.end[0]
        y4 = seg.end[1]

        denom = (x4 - x3) * (y1 - y2) - (x1 - x2) * (y4 - y3)
        r = ((y3 - y4)*(x1 - x3) + (x4 - x3)*(y1 - y3)) / denom
        s = ((y1 - y2)*(x1 - x3) + (x2 - x1)*(y1 - y3)) / denom

        if 0 < r < 1 and 0 < s < 1:
            x_cross = x1 + (x2 - x1) * r
            y_cross = y1 + (y2 - y1) * r
            return int(x_cross), int(y_cross)

def part1(input):
    wires = [Wire(line).draw_all() for line in input.splitlines()]
    return wires[0].closest_intersection(wires[1])


def part2(input):
    return


if __name__ == '__main__':
    import aoc_input as inp
    DAY = 3
    print(part1('R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83'))
    print(part1(inp.read(DAY)))
    # print(part2(inp.read(DAY)))