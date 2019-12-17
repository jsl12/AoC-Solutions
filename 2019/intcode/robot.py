import numpy as np

from . import Computer


class Robot:
    def __init__(self, input):
        self.brain = Computer(input)
        self.pos = [0, 0] # [y, x]
        self.dir = 0
        self.painted = {}

    def turn(self, dir):
        if dir == 0:
            self.dir -= 1
        elif dir == 1:
            self.dir += 1

        if self.dir >= 4:
            self.dir =0
        elif self.dir < 0:
            self.dir += 4

    def move(self):
        if self.dir == 0:
            self.pos[0] -= 1
        elif self.dir == 1:
            self.pos[1] += 1
        elif self.dir == 2:
            self.pos[0] += 1
        elif self.dir == 3:
            self.pos[1] -= 1

    def step(self):
        current_color = self.painted.get(tuple(self.pos), 0)
        self.brain.inputs.append(current_color)
        self.brain.run(output_stop=2)
        if self.brain.op != 99:
            new_color = self.brain.outputs.pop(0)
            turn_dir = self.brain.outputs.pop(0)

            if new_color != current_color:
                self.painted[tuple(self.pos)] = new_color

            self.turn(turn_dir)
            self.move()

    def run(self):
        while self.brain.op != 99:
            self.step()

    def visualize(self):
        x_vals = [val[1] for val in self.painted.keys()]
        y_vals = [val[0] for val in self.painted.keys()]
        min_x = min(x_vals)
        max_x = max(x_vals)
        min_y = min(y_vals)
        max_y = max(y_vals)

        transform = (0 - min_y, 0 - min_x)
        width = max_x - min_x + 1
        height = max_y - min_y + 1

        array = np.array(['.' for i in range(width*height)]).reshape((height, width))
        for pos in self.painted:
            if self.painted[pos] == 1:
                pos = tuple(sum(x) for x in zip(pos, transform))
                array[pos] = '#'
        for row in array:
            print(''.join(list(row)))
